---
name: glan-sleep-optimizer
description: An offline self-evolution skill inspired by SkillOpt. Use this skill when the user asks to "执行睡眠进化", "Run the sleep cycle", or "优化格兰的规则". It harvests past A-share market predictions, compares them against actual market outcomes, reflects on failures, and proposes permanent edits to Glan's reasoning framework to prevent future mistakes.
---

# Glan Sleep Optimizer (格兰睡眠进化引擎)

## Purpose

This skill acts as the offline "Optimizer" for the `a-share-glan-style-briefing` skill. 
It implements a "Sleep Cycle" that turns short-term mistakes (logged in the daily memory log) into long-term structural competence (by patching the core `reasoning-framework.md` rules).

**The Core Philosophy (SkillOpt inspired):**
Treat the natural language instructions of an agent as its trainable parameters. Evolve the agent by reflecting on failed rollouts and applying bounded text edits to the instructions, gated by human validation.

## Workflow (The Sleep Cycle)

### 1. Harvest & Recall (数据收割)
- Read the `A股每日新闻与复盘台账.md` workspace log.
- Extract any entries from the last 5 days where the "上一期验证结果" is marked as **证伪 (Falsified)** or **部分验证 (Partially Validated)**.
- If there are no falsified entries, report to the user: "当前短期记忆库中无严重误判记录，暂不需启动进化周期。" and exit gracefully.

### 2. Reality Check & Reflection (核对与反思)
For each falsified thesis found:
1. Identify the exact date the prediction was made and the target date it was predicting.
2. **[MANDATORY]** Use the `run_command` tool to run `python {BRIEFING_SKILL_DIR}/scripts/fetch_market_snapshot.py` or use other search tools to fetch the *actual* historical market data for the target date.
> **{BRIEFING_SKILL_DIR}** refers to the `a-share-glan-style-briefing` skill directory. If installed as a subdirectory of this repo, it's the parent directory of `glan-sleep-optimizer/`. If installed as a sibling skill, it's `../a-share-glan-style-briefing/`.
3. Compare the prediction (e.g., "Washout, expect rebound tomorrow") with the reality (e.g., "Market crashed further").
4. Formulate an answer: **Why did the existing `reasoning-framework.md` lead to this mistake?** What edge case or new market regime was missed?

### 3. Bounded Edit Proposal (生成进化补丁)
Draft a concrete, actionable rule that would prevent this specific mistake in the future.
- The rule must be specific (e.g., "If turnover drops below 1.5T while breaking the 5-day MA, do not classify as a washout").
- It must not break existing good logic.
- Target destination: The **"Evolutionary Patches (自我进化补丁库)"** section at the bottom of `{BRIEFING_SKILL_DIR}/references/reasoning-framework.md`.

### 4. Validation Gate (人工验证门 - Human-in-the-loop)
**Do NOT directly edit the `reasoning-framework.md` file.**
Financial analysis is subjective, and an automated edit might cause "mode collapse" (learning a wrong rule).

You MUST output your reflection and proposed edit into a new Artifact named `proposed_skill_edits.md`.
Use the following format for the artifact:

```markdown
# Sleep Cycle Evolution Proposal

## 🛑 Failed Prediction (被证伪的推演)
[Describe the past mistake from the log]

## 📊 Reality (真实盘面)
[Describe what actually happened based on fetched data]

## 🧠 Reflection (错因深究)
[Explain why the current framework failed to catch this]

## 🔧 Proposed Patch (拟新增底层规则)
[The exact text you propose to append to the Evolutionary Patches section]

> [!WARNING]
> Please review this rule. If it makes logical sense and aligns with the Glan trading style, approve this artifact to apply the patch permanently to the `reasoning-framework.md` gene pool.
```

Present this artifact to the user and ask for their approval. 

### 5. Commit (写入基因库)
**Only AFTER the user explicitly approves** the `proposed_skill_edits.md`, you must:
1. **[MANDATORY] Backup the file**: Run the backup script to save the current state:
   `python3 {SLEEP_SKILL_DIR}/scripts/backup_framework.py {BRIEFING_SKILL_DIR}/references/reasoning-framework.md`
   > **{SLEEP_SKILL_DIR}** = this `glan-sleep-optimizer` skill directory.
2. **Apply Edit**: Use the `replace_file_content` tool to append the new rule into the `Evolutionary Patches (自我进化补丁库)` section of the `reasoning-framework.md` file.
3. **Clean Log**: Clear the corresponding error entry from the `A股每日新闻与复盘台账.md` to indicate it has been digested.
