# 🧠 格兰 A股复盘/展望 Skill (Glan A-Share Briefing)

> 一套面向 AI Agent 的 A股实战投研分析系统，受微软 SkillOpt 论文启发，具备自我进化能力。

![模式](https://img.shields.io/badge/模式-开盘前展望%20|%20午盘观察%20|%20收盘复盘-blue)
![语言](https://img.shields.io/badge/语言-中文-red)
![平台](https://img.shields.io/badge/平台-Gemini%20CLI%20|%20Jules%20|%20任何支持%20Skills%20的%20Agent-green)

---

## 🎯 这是什么？

这是一个专为 **Gemini CLI** 等 AI Agent 设计的 Skill（技能包），让 AI 变身成一个有血有肉的 **A股实战投研分析师——"格兰"**。

格兰不是一个中立的市场播报员，他是一个带着仓位思维、带着"如果我错了怎么办"的焦虑感在做判断的实战派老炮。

### 核心能力

- 🔄 **三种分析模式**：开盘前展望、午盘观察、收盘复盘
- 📊 **实时数据抓取**：内置 Python 脚本自动拉取 A股行情快照 + 7×24 财经新闻
- 🇺🇸 **美股→A股映射**：完整的美股 AI 产业链→A股对应标的映射表
- ⚠️ **风险雷达系统**：自动扫描拥挤度、减持、地缘冲突等 8 大类风险
- 📈 **核心股池**：覆盖 60+ 只 A股核心标的，按产业链上中下游分层
- 🧬 **自我进化引擎**：受微软 SkillOpt 启发，通过"睡眠进化"自动从错误中学习

---

## 📁 目录结构

```
├── SKILL.md                          # 🧠 主指令文件（Agent 读取此文件执行分析）
├── README.md                         # 📖 本说明文件
│
├── references/                       # 📚 参考知识库
│   ├── core-stock-pool.md            #   核心股池（60+ 只标的，产业链分层）
│   ├── us-ai-chain-mapping.md        #   美股 AI 链 → A股映射表
│   ├── risk-radar.md                 #   风险雷达扫描框架
│   ├── style-playbook.md             #   格兰人格画像 & 语言风格指南
│   ├── reasoning-framework.md        #   推理框架 & 反证逻辑 & 进化补丁库
│   ├── news-source-matrix.md         #   新闻源评分矩阵
│   ├── evolution-loop.md             #   自我进化循环规则
│   ├── html-template.md              #   HTML 输出模板（浏览器渲染）
│   └── codex-exemplar-2026-06-18.html#   Codex 生成的范本级报告
│
├── scripts/                          # 🔧 数据抓取脚本
│   ├── fetch_market_snapshot.py      #   A股实时行情快照（指数 + 个股 + 板块）
│   └── fetch_news.py                 #   7×24 财经新闻流
│
├── examples/                         # 📄 输出范本
│   ├── 格兰_午盘观察_范本.md           #   Markdown 原始报告
│   └── 格兰_午盘观察_范本.html         #   浏览器渲染版（直接双击打开）
│
├── agents/                           # 🤖 子代理配置
│   └── openai.yaml
│
└── glan-sleep-optimizer/             # 🧬 自我进化引擎（SkillOpt 启发）
    ├── SKILL.md                      #   进化引擎指令
    ├── scripts/backup_framework.py   #   框架文件备份脚本
    └── backups/                      #   历史备份存档
```

---

## 🚀 安装方法

### 前置要求

- [Gemini CLI](https://github.com/google-gemini/gemini-cli) 或其他支持 Skills 的 AI Agent
- Python 3.8+
- `requests` 库

### 安装步骤

```bash
# 1. 安装 Python 依赖
pip install requests

# 2. 克隆到你的项目 .agents/skills/ 目录
cd /你的项目路径/.agents/skills/
git clone https://github.com/wangdaokeaiduo/glan-a-share-briefing-skill.git a-share-glan-style-briefing

# 3. (可选) 将睡眠进化引擎拆分为独立 skill
cp -r a-share-glan-style-briefing/glan-sleep-optimizer ./glan-sleep-optimizer

# 4. 完成！Gemini CLI 会自动发现这两个 skill
```

### 验证安装

启动 Gemini CLI，输入以下任意指令：

```
午盘复盘 格兰
开盘前展望 格兰
收盘复盘 格兰
```

---

## 💬 使用方法

### 触发词

| 触发词 | 说明 |
| --- | --- |
| `开盘前展望` / `开盘展望` | A股开盘前分析（含隔夜美股、亚太市场） |
| `午盘复盘` / `午盘观察` | 午间休市时分析上午盘面 |
| `收盘复盘` / `盘后复盘` | 收盘后全天复盘 |
| `执行睡眠进化` | 触发自我进化引擎（从错误中学习） |

### 自动输出

每次运行后，格兰会自动：

1. 📝 生成 **Markdown 报告**（存入 `jiedu/` 文件夹）
2. 🌐 生成 **HTML 报告**（浏览器自动弹出，极简投研排版）
3. 📋 更新 **复盘台账**（`A股每日新闻与复盘台账.md`）

---

## 📄 输出范本

> 👉 查看 [`examples/`](examples/) 文件夹中的完整范本

### 范本截取（午盘观察模式）

```markdown
# 寒武纪炸裂！银行崩塌！这是A股有史以来最极端的"去防守、all in进攻"吗？

模式：午盘观察
数据时间：2026-06-18 11:35 CST

## 开篇判断

王导，今天上午最重要的不是创业板又涨了1.39%，也不是科创50暴涨3.6%
——最重要的，是这个市场正在进行一场极度凶残的"结构性大屠杀"：
科技矛刺穿天花板的同时，高股息防守盘正在被踩在脚下。

...（完整报告包含 20+ 个模块、50+ 只个股实时分析）
```

### 报告结构（20个核心模块）

| # | 模块 | 说明 |
| --- | --- | --- |
| 1 | 上一期判断复盘 | 对照上次预测 vs 实际盘面 |
| 2 | 开篇判断 | 一句话定调，必须带立场 |
| 3 | 隔夜/盘前核心催化 | 每条催化独立拆成"迷你研报" |
| 4 | 国内外催化归纳 | 浓缩为核心矛盾 |
| 5 | 盘面与资金验证 | 指数+龙头分时走势还原 |
| 6 | 隔夜美股映射 | 美股→A股映射验证表 |
| 7 | 日韩股市传导 | 含韩元/日元汇率联动分析 |
| 8 | 主线推导 | 资金为什么选这条线 |
| 9 | 硬科技拆链 | 产业链矩阵表 |
| 10 | 龙头观察 | 逐只拆解盘口含义 |
| 11 | 股票池雷达 | 分层推荐+投资逻辑+预期差 |
| 12 | 涨价概念观察 | 四道门审核 |
| 13 | 板块可交易性分层 | 景气度+催化+盘口确认 |
| 14 | 风险雷达 | 8大类风险扫描 |
| 15 | 下一波轮动预测 | 资金高低切前瞻 |
| 16 | 企稳关注方向 | 超跌反弹候选 |
| 17 | 操作建议 | 仓位+触发/失效条件 |
| 18 | 反证与风险 | 整体逻辑证伪条件 |
| 19 | 板块和个股跟踪表 | 最终汇总 |
| 20 | 采用新闻源与评分 | 信息溯源+可信度评分 |

---

## 🧬 自我进化引擎 (Sleep Optimizer)

受 [微软 SkillOpt 论文](https://arxiv.org/abs/2405.19056) 启发，格兰具备离线自我进化能力：

```
预测错误 → 数据回收 → 反思错因 → 生成规则补丁 → 人工审核 → 写入基因库
```

**工作流程：**

1. **收割**：从复盘台账中提取被证伪的预测
2. **核对**：拉取真实历史数据对比
3. **反思**：定位推理框架中的缺陷
4. **提案**：生成具体的规则补丁
5. **验证**：人工审核（Human-in-the-loop，防止 mode collapse）
6. **写入**：追加到 `reasoning-framework.md` 的进化补丁库

触发方式：

```
执行睡眠进化
```

---

## ⚙️ 路径说明

SKILL.md 中的脚本路径使用 `{SKILL_DIR}` 占位符：

```bash
python {SKILL_DIR}/scripts/fetch_market_snapshot.py
```

Agent 运行时会自动从 SKILL.md 的文件路径推算出 `{SKILL_DIR}`（即 SKILL.md 所在的目录）。无需手动配置。

---

## 🤝 适用场景

- ✅ 个人投研复盘提效
- ✅ 搭建 AI 投研助手
- ✅ 学习 Agent Skill 的设计范式
- ✅ 研究 LLM 自我进化（SkillOpt）的落地实践

---

## ⚠️ 免责声明

> 本项目仅供研究学习和个人复盘使用，**不构成任何投资建议**。  
> 市场有风险，交易需谨慎。AI 生成的分析可能存在误差，请独立判断。

---

## 📜 License

MIT License

---

## 🙏 致谢

- [微软 SkillOpt](https://arxiv.org/abs/2405.19056) — 自我进化引擎的理论基础
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Agent 运行平台
- 格兰的每一次错误判断 — 让进化引擎有事可做 😄
