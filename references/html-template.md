# HTML Output Template (Markdown 直出方案 - 极简极净阅读版)

## 核心原理

AI **不需要手动转换 HTML 标签**。只需要：
1. 把完整的 Markdown 分析报告作为字符串嵌入 HTML 模板的 `MARKDOWN_CONTENT` 位置
2. 浏览器端 `marked.js` 自动将 Markdown 渲染为精美 HTML
3. 本模板采用顶级投研机构极简排版，无浮夸动画，专注文字与表格的阅读体验。

## 输出规则

1. **文件名格式**：`格兰_{模式}_{YYYY-MM-DD_HHmm}.html` 和 `格兰_{模式}_{YYYY-MM-DD_HHmm}.md`
2. **保存路径**：统一保存到工作区根目录下的 `jiedu/` 文件夹
3. **MD 文件**：先保存完整 Markdown 原文到 `jiedu/` 文件夹，用于验证和复盘对照
4. **生成后自动弹出**：`open /path/to/jiedu/格兰_xxx.html`

## 操作步骤（仅3步）

### Step 1: 正常写完 Markdown 分析报告

按照 SKILL.md 中的 Output Shape 正常生成完整的 Markdown 分析内容。**必须包含标题作为 Markdown 的 `# 一级标题`**，并且正文必须写出 `<p>模式：...</p>` 和 `<p>数据时间：...</p>`。**不需要做任何手动 HTML 转换。**

### Step 2: 把 Markdown 内容嵌入模板

把下方完整 HTML 模板复制出来，将分析报告的 Markdown 文本替换 `__MARKDOWN_CONTENT__` 占位符。

注意事项：
- Markdown 内容中的反引号 `` ` `` 需要保持原样，模板用 `__MARKDOWN_CONTENT__` 占位，不是 JS 模板字符串
- Markdown 内容放在 `<textarea id="md-source">` 标签内，会被浏览器当做纯文本，所有特殊字符自动转义
- 此版本没有 `__TITLE__` 等分离变量，**全部内容都在 Markdown 里写死**。只需替换 `__MARKDOWN_CONTENT__`。

### Step 3: 保存 MD + HTML 文件到 jiedu/ 并 open 弹出

先将 Markdown 原文保存为 `jiedu/格兰_{模式}_{YYYY-MM-DD_HHmm}.md`，然后保存 HTML 到同一文件夹并 open 弹出。

## 完整 HTML 模板

```html
<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>格兰投研复盘</title>
<style>
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;line-height:1.75;max-width:1080px;margin:40px auto;padding:0 22px;color:#172033;background:#fbfbf8}
h1,h2,h3{line-height:1.35;color:#111827}
h1{font-size:30px}
h2{margin-top:34px;border-bottom:1px solid #d9dde7;padding-bottom:6px}
table{border-collapse:collapse;width:100%;display:block;overflow-x:auto;background:white;margin:16px 0}
th,td{border:1px solid #d7dce5;padding:8px 10px;vertical-align:top;white-space:nowrap}
td:nth-child(2),td:nth-child(3),td:nth-child(4),td:nth-child(5){white-space:normal}
th{background:#eef2f7;font-weight:600;text-align:left}
code{background:#eef2f7;padding:2px 4px;border-radius:4px;color:#d946ef;font-size:14px}
blockquote{border-left:4px solid #9aa4b2;padding-left:14px;color:#475569;background:#f3f5f7;margin:16px 0;padding:12px 14px}
p{margin-bottom:14px}
</style>
</head>
<body>

<textarea id="md-source" style="display:none">
__MARKDOWN_CONTENT__
</textarea>

<div id="report"></div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  const md = document.getElementById('md-source').value;
  document.getElementById('report').innerHTML = marked.parse(md);
</script>
</body>
</html>
```

## AI 操作流程（极简3步）

### Step 1：正常生成 Markdown 分析

按 SKILL.md 的 Output Shape 正常写 Markdown。开头必须是 `# 标题`，紧跟模式和时间。

```markdown
# 美股泼冷水，A股上午接住了吗？
<p>模式：午盘观察</p>
<p>数据时间：2026-06-17 11:35 CST</p>

## 上一期判断复盘
...
```

### Step 2：嵌入模板并保存

直接把整段 Markdown 原封不动地替换到 `<textarea id="md-source">__MARKDOWN_CONTENT__</textarea>` 中。

### Step 3：保存 MD + HTML 到 jiedu/ 并 open 弹出

```bash
# 先保存 MD 原文
write jiedu/格兰_开盘前展望_2026-06-03_0900.md
# 再保存 HTML
write jiedu/格兰_开盘前展望_2026-06-03_0900.html
# 最后弹出
open /path/to/jiedu/格兰_开盘前展望_2026-06-03_0900.html
```
