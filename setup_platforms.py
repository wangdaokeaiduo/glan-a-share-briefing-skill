#!/usr/bin/env python3
"""
格兰 Skill 多平台适配器 (Glan Multi-Platform Adapter)
=====================================================
一键生成全平台兼容配置文件。

支持平台：
  国际: Gemini CLI, Claude Code, Cursor, Windsurf, GitHub Copilot, Cline, Aider
  国内: CodeBuddy (腾讯), Trae (字节/豆包), 通义灵码 (阿里)

用法:
  python3 setup_platforms.py              # 交互式选择平台
  python3 setup_platforms.py --all        # 生成所有平台配置
  python3 setup_platforms.py --list       # 列出支持的平台
  python3 setup_platforms.py cursor trae  # 只生成指定平台
"""

import os
import sys
import shutil
import textwrap

# ── 路径检测 ──────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = SCRIPT_DIR  # setup_platforms.py 放在 skill 根目录
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")
PROJECT_ROOT = None  # 将在运行时检测

def find_project_root():
    """向上查找项目根目录（含 .git 或 package.json 的目录）"""
    path = SKILL_DIR
    for _ in range(10):
        parent = os.path.dirname(path)
        if parent == path:
            break
        # 如果是 .agents/skills/xxx 结构，项目根在 .agents 的上三级
        if os.path.basename(os.path.dirname(os.path.dirname(path))) == '.agents':
            return os.path.dirname(os.path.dirname(os.path.dirname(path)))
        if os.path.exists(os.path.join(parent, '.git')) or os.path.exists(os.path.join(parent, 'package.json')):
            return parent
        path = parent
    # 默认返回 skill 目录的上三级（假设 .agents/skills/xxx 结构）
    return os.path.dirname(os.path.dirname(os.path.dirname(SKILL_DIR)))


def read_skill_md():
    """读取 SKILL.md 内容"""
    with open(SKILL_MD, 'r', encoding='utf-8') as f:
        return f.read()


def get_core_instructions():
    """提取核心指令（去掉 YAML frontmatter，适配各平台）"""
    content = read_skill_md()
    # 去掉 YAML frontmatter
    if content.startswith('---'):
        end = content.find('---', 3)
        if end != -1:
            content = content[end + 3:].strip()
    return content


def get_compact_instructions():
    """生成精简版指令（适用于有字符限制的平台）"""
    return textwrap.dedent("""\
    # 格兰 A股实战投研分析师 (Glan A-Share Analyst)
    
    ## 角色
    你是"格兰"——一个带着仓位思维和焦虑感的A股实战派投研分析师。
    不做中立观察者，必须给出明确的多空判断。
    
    ## 三种模式
    - 开盘前展望：基于隔夜美股+亚太市场+新闻，给出今日A股预判
    - 午盘观察：上午收盘后分析盘面，给出下午策略
    - 收盘复盘：全天复盘，总结主线并预判次日
    
    ## 数据规则
    - 必须通过脚本获取实时行情数据，禁止幻觉编造
    - 行情脚本: {SKILL_DIR}/scripts/fetch_market_snapshot.py
    - 新闻脚本: {SKILL_DIR}/scripts/fetch_news.py
    - 必须联网搜索当日新闻和小作文
    
    ## 核心分析框架
    1. 上一期判断复盘（对照验证）
    2. 隔夜催化独立拆解（每条催化做迷你研报）
    3. 美股→A股映射（参考 references/us-ai-chain-mapping.md）
    4. 主线推导 + 硬科技拆链
    5. 龙头逐只盘口分析（禁止笼统概括）
    6. 风险雷达（8大类风险扫描）
    7. 操作建议（含仓位、触发/失效条件）
    
    ## 风格要求
    - 立场先行，先判断再解释
    - 每个判断附带证伪条件
    - 用格兰黑话：骨架、体温、子弹、换血、假摔、真刀子
    - 禁止"综上所述""需要注意风险"等废话
    
    ## 参考文件
    - references/core-stock-pool.md — 核心股池
    - references/style-playbook.md — 风格指南
    - references/risk-radar.md — 风险扫描框架
    - references/reasoning-framework.md — 推理框架
    """)


# ── 平台生成器 ──────────────────────────────────────────────

PLATFORMS = {}

def platform(name, display, path_hint):
    """装饰器：注册平台生成器"""
    def wrapper(func):
        PLATFORMS[name] = {
            'func': func,
            'display': display,
            'path_hint': path_hint,
        }
        return func
    return wrapper


@platform('gemini', 'Gemini CLI (Google)', '.agents/skills/a-share-glan-style-briefing/')
def gen_gemini(root):
    """Gemini CLI — 原生 SKILL.md 格式，直接复制整个目录"""
    target = os.path.join(root, '.agents', 'skills', 'a-share-glan-style-briefing')
    if os.path.abspath(target) == os.path.abspath(SKILL_DIR):
        print("  ⏭  当前已在 Gemini CLI 标准位置，跳过")
        return
    os.makedirs(target, exist_ok=True)
    # 复制所有文件（排除 .git 和 setup 脚本自身的输出）
    for item in os.listdir(SKILL_DIR):
        if item.startswith('.') or item == 'glan-sleep-optimizer':
            continue
        src = os.path.join(SKILL_DIR, item)
        dst = os.path.join(target, item)
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    print(f"  ✅ 已复制到 {target}")


@platform('claude', 'Claude Code (Anthropic)', 'CLAUDE.md + .claude/commands/')
def gen_claude(root):
    """Claude Code — CLAUDE.md + .claude/commands/"""
    # 1. CLAUDE.md (精简版，因为 Claude 建议 <300 行)
    claude_md = os.path.join(root, 'CLAUDE.md')
    content = get_compact_instructions()
    # 检查是否已存在 CLAUDE.md，如果存在则追加
    if os.path.exists(claude_md):
        with open(claude_md, 'r', encoding='utf-8') as f:
            existing = f.read()
        if '格兰' not in existing:
            content = existing.rstrip() + '\n\n---\n\n' + content
        else:
            print("  ⏭  CLAUDE.md 已包含格兰指令，跳过")
            content = None
    if content:
        with open(claude_md, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ 已生成 {claude_md}")
    
    # 2. 自定义命令
    cmd_dir = os.path.join(root, '.claude', 'commands')
    os.makedirs(cmd_dir, exist_ok=True)
    for mode, trigger in [('morning', '开盘前展望'), ('noon', '午盘观察'), ('evening', '收盘复盘')]:
        cmd_file = os.path.join(cmd_dir, f'glan-{mode}.md')
        with open(cmd_file, 'w', encoding='utf-8') as f:
            f.write(f"请以格兰的风格执行「{trigger}」模式分析。\n\n"
                    f"参考 CLAUDE.md 中的格兰指令，以及项目中的 references/ 参考文件。\n"
                    f"必须先运行行情脚本获取实时数据，禁止幻觉编造任何数据。\n")
        print(f"  ✅ 已生成命令 /glan-{mode}")


@platform('cursor', 'Cursor', '.cursor/rules/*.mdc')
def gen_cursor(root):
    """Cursor — .cursor/rules/*.mdc 格式"""
    rules_dir = os.path.join(root, '.cursor', 'rules')
    os.makedirs(rules_dir, exist_ok=True)
    
    content = textwrap.dedent("""\
    ---
    description: 格兰A股实战投研分析师 - 午盘/收盘/开盘前展望复盘分析
    globs: "**/*.md"
    alwaysApply: false
    ---
    
    """) + get_compact_instructions()
    
    rule_file = os.path.join(rules_dir, 'glan-a-share-briefing.mdc')
    with open(rule_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {rule_file}")


@platform('windsurf', 'Windsurf (Codeium)', '.windsurfrules')
def gen_windsurf(root):
    """Windsurf — .windsurfrules 文件"""
    rules_file = os.path.join(root, '.windsurfrules')
    content = get_compact_instructions()
    if os.path.exists(rules_file):
        with open(rules_file, 'r', encoding='utf-8') as f:
            existing = f.read()
        if '格兰' not in existing:
            content = existing.rstrip() + '\n\n---\n\n' + content
        else:
            print("  ⏭  .windsurfrules 已包含格兰指令，跳过")
            return
    with open(rules_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {rules_file}")


@platform('copilot', 'GitHub Copilot', '.github/copilot-instructions.md')
def gen_copilot(root):
    """GitHub Copilot — .github/copilot-instructions.md"""
    gh_dir = os.path.join(root, '.github')
    os.makedirs(gh_dir, exist_ok=True)
    instructions_file = os.path.join(gh_dir, 'copilot-instructions.md')
    content = get_compact_instructions()
    if os.path.exists(instructions_file):
        with open(instructions_file, 'r', encoding='utf-8') as f:
            existing = f.read()
        if '格兰' not in existing:
            content = existing.rstrip() + '\n\n---\n\n' + content
        else:
            print("  ⏭  copilot-instructions.md 已包含格兰指令，跳过")
            return
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {instructions_file}")


@platform('cline', 'Cline', '.clinerules')
def gen_cline(root):
    """Cline — .clinerules 文件"""
    rules_file = os.path.join(root, '.clinerules')
    content = get_compact_instructions()
    with open(rules_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {rules_file}")


@platform('aider', 'Aider', 'CONVENTIONS.md')
def gen_aider(root):
    """Aider — CONVENTIONS.md"""
    conv_file = os.path.join(root, 'CONVENTIONS.md')
    content = get_compact_instructions()
    if os.path.exists(conv_file):
        with open(conv_file, 'r', encoding='utf-8') as f:
            existing = f.read()
        if '格兰' not in existing:
            content = existing.rstrip() + '\n\n---\n\n' + content
        else:
            print("  ⏭  CONVENTIONS.md 已包含格兰指令，跳过")
            return
    with open(conv_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {conv_file}")


@platform('codebuddy', 'CodeBuddy (腾讯)', '.codebuddy/rules/ + .codebuddy/skills/')
def gen_codebuddy(root):
    """CodeBuddy (腾讯) — .codebuddy/rules/*.md + .codebuddy/skills/"""
    # 1. 规则文件
    rules_dir = os.path.join(root, '.codebuddy', 'rules')
    os.makedirs(rules_dir, exist_ok=True)
    
    content = textwrap.dedent("""\
    ---
    name: glan-a-share-briefing
    description: 格兰A股实战投研分析师 - 午盘/收盘/开盘前展望复盘分析。当用户提及"午盘复盘""收盘复盘""开盘展望""格兰"时触发。
    ---
    
    """) + get_compact_instructions()
    
    rule_file = os.path.join(rules_dir, 'glan-a-share-briefing.md')
    with open(rule_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成规则 {rule_file}")
    
    # 2. Skill 目录（CodeBuddy 也支持 SKILL.md 格式）
    skill_dir = os.path.join(root, '.codebuddy', 'skills', 'a-share-glan-style-briefing')
    os.makedirs(skill_dir, exist_ok=True)
    for item in ['SKILL.md', 'references', 'scripts']:
        src = os.path.join(SKILL_DIR, item)
        dst = os.path.join(skill_dir, item)
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)
    print(f"  ✅ 已复制 Skill 到 {skill_dir}")


@platform('trae', 'Trae (字节/豆包)', '.trae/rules/')
def gen_trae(root):
    """Trae (字节跳动) — .trae/rules/*.md"""
    rules_dir = os.path.join(root, '.trae', 'rules')
    os.makedirs(rules_dir, exist_ok=True)
    
    content = textwrap.dedent("""\
    ---
    alwaysApply: false
    ---
    
    """) + get_compact_instructions()
    
    rule_file = os.path.join(rules_dir, 'glan-a-share-briefing.md')
    with open(rule_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {rule_file}")


@platform('lingma', '通义灵码 (阿里)', '.lingma/rules/')
def gen_lingma(root):
    """通义灵码 (阿里) — .lingma/rules/*.md"""
    rules_dir = os.path.join(root, '.lingma', 'rules')
    os.makedirs(rules_dir, exist_ok=True)
    
    content = get_compact_instructions()
    rule_file = os.path.join(rules_dir, 'glan-a-share-briefing.md')
    with open(rule_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ 已生成 {rule_file}")


# ── 主逻辑 ──────────────────────────────────────────────

def print_banner():
    print("""
╔══════════════════════════════════════════════════╗
║   🧠 格兰 Skill 多平台适配器                       ║
║   Glan A-Share Briefing — Multi-Platform Setup   ║
╚══════════════════════════════════════════════════╝
""")

def print_platform_list():
    print("支持的平台：\n")
    print(f"  {'ID':<12} {'平台名称':<30} {'配置路径'}")
    print(f"  {'—'*12} {'—'*30} {'—'*40}")
    for key, info in PLATFORMS.items():
        print(f"  {key:<12} {info['display']:<30} {info['path_hint']}")
    print()

def main():
    print_banner()
    
    if '--list' in sys.argv:
        print_platform_list()
        return
    
    # 确定项目根目录
    root = find_project_root()
    print(f"📂 项目根目录: {root}\n")
    
    # 确定要生成的平台
    if '--all' in sys.argv:
        selected = list(PLATFORMS.keys())
    elif len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        selected = [arg for arg in sys.argv[1:] if arg in PLATFORMS]
        unknown = [arg for arg in sys.argv[1:] if arg not in PLATFORMS and not arg.startswith('-')]
        if unknown:
            print(f"⚠️  未知平台: {', '.join(unknown)}")
            print_platform_list()
            return
    else:
        # 交互式选择
        print_platform_list()
        print("请输入平台 ID（多个用空格分隔，或输入 all）：")
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n已取消")
            return
        if user_input.lower() == 'all':
            selected = list(PLATFORMS.keys())
        else:
            selected = user_input.split()
            unknown = [s for s in selected if s not in PLATFORMS]
            if unknown:
                print(f"\n⚠️  未知平台: {', '.join(unknown)}")
                return
    
    if not selected:
        print("未选择任何平台，退出。")
        return
    
    print(f"\n🚀 即将生成 {len(selected)} 个平台的配置...\n")
    
    for name in selected:
        info = PLATFORMS[name]
        print(f"━━ {info['display']} ━━")
        try:
            info['func'](root)
        except Exception as e:
            print(f"  ❌ 错误: {e}")
        print()
    
    print("═" * 50)
    print("✅ 全部完成！重启你的 IDE/Agent 即可生效。")
    print("═" * 50)


if __name__ == '__main__':
    main()
