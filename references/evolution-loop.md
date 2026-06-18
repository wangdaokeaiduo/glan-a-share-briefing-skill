# Evolution Loop

Use this reference whenever a prior outlook is tested by later trading, especially 午盘观察 and 收盘复盘.

## Purpose

Improve future briefings by turning failed calls into explicit rules. The goal is not to defend the previous article. The goal is to learn why the market disagreed.

## Falsification Review

For every prior thesis, classify it:

- **Validated**: sector and named leader stocks moved as expected, or the stated trigger happened.
- **Partially validated**: direction was right but leader selection, timing, or breadth was weak.
- **Falsified**: stated trigger failed, leaders moved opposite, or market chose another main line.
- **Not yet testable**: event needs more time or no market session has occurred.

Use this table:

| 上一期判断 | 触发条件 | 实际盘面 | 结论 | 错因/经验 |
| --- | --- | --- | --- | --- |
| thesis | exact trigger | what happened | validated/partial/falsified/not testable | lesson |

## Error Taxonomy

When a call is wrong, identify the main error type:

1. **新闻权重过高**: the news was real, but funds did not treat it as tradable.
2. **忽略盘口位置**: the sector was too crowded/high, so good news became sell-the-news.
3. **龙头选择错误**: named stocks were not the actual market leaders.
4. **市场风格错判**: market preferred defense/high dividend/low valuation instead of growth.
5. **资金强度不足**: turnover, breadth, or follow-through did not support the thesis.
6. **外部冲击覆盖**: macro/geopolitical/commodity event overwhelmed sector logic.
7. **产业链映射太远**: A-share names were indirect beneficiaries, not direct pricing targets.

## Optimization Rule

After the error analysis, write one rule beginning with:

> 下一次优化：

Examples:

- “下一次优化：周末利好如果只刺激弹性小票，核心龙头不跟，不能把它升级为主线。”
- “下一次优化：高位科技方向出现放量长阴后，必须先看核心票是否缩量止跌，再谈修复。”
- “下一次优化：同一新闻同时利好多个环节时，优先选择订单、涨价、产能最直接的环节。”

## Memory Log (新闻与复盘台账)

When finishing an analysis, you MUST update the `A股每日新闻与复盘台账.md` in the current workspace with the current session's newly discovered news, thesis, and evolutionary lessons.

Use this format to append:

```markdown
## YYYY-MM-DD [模式: 开盘前/午盘/收盘]

- **核心催化/新闻**：(List key news identified, e.g., AI PC, 钠电池量产)
- **核心判断/主线推导**：(Your thesis for this session)
- **上一期验证结果**：(验证 / 部分验证 / 证伪 / 待验证)
- **错因分类与下一次优化**：(If falsified, log the lesson here)
```

**Cleanup Rule:** 
Before saving, ensure the log only contains entries from the last 5 days. Delete any entries older than 5 days from the file to keep it concise and relevant.
Do not fabricate historical entries. Only log what was actually observed and analyzed.

## The Sleep Cycle (深度进化触发器)

The daily reporting process logs the "Training Data" (your mistakes and lessons). True structural evolution happens offline.
If you notice that a prior falsified thesis reveals a fundamental gap in your current `reasoning-framework.md` (e.g., a completely new market pattern you didn't know how to handle), you MUST suggest to the user at the end of your report:
> 💡 **系统建议**：本期复盘发现严重的逻辑误判，建议您运行 `glan-sleep-optimizer` 技能进行深度反思，更新底层推理框架补丁库。

## Article Placement

Put self-evolution after “上一期判断复盘” and before the new market thesis when a prior call failed. If the call was validated, include a shorter note:

> 这条判断暂时被盘面验证，后续继续看是否有成交和龙头跟进。
