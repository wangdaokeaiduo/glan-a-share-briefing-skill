# Reasoning Framework

## Data Checklist

Before writing, collect as much as available:

## Three Timing Modes

### 开盘前展望

Purpose: convert overnight/weekend news into Monday or next-session trading hypotheses.

Required sections:

- 上一期判断复盘.
- 隔夜美股AI链体温（必选）：使用 references/us-ai-chain-mapping.md 模板，逐环节展开美股核心标的表现及A股映射推演.
- 周末/隔夜关键新闻.
- 风险雷达：使用 references/risk-radar.md 框架主动扫描，输出风险评级.
- 三种情景：强势验证、震荡洗盘、判断失败.
- 开盘触发条件：which sectors and exact leader stocks must strengthen or weaken.
- 今日观察清单：开盘30分钟、午盘、收盘各看什么.
- 格兰的判断：明确给出开盘偏多或偏空的方向判断，附证伪条件.

### 午盘观察

Purpose: check whether morning trading validates the pre-market thesis.

Required sections:

- 上一期判断复盘, focusing on morning validation.
- 若开盘前判断被证伪，必须加入自我校准：错在哪里、为什么错、下午如何调整.
- 上午盘面：指数、成交、涨跌家数、强弱板块.
- 资金验证：whether money is rotating inside the main line or leaving it.
- 龙头观察：name exact stocks stronger/weaker than their sectors.
- 下午策略：what must happen after 13:00 to confirm or negate.

### 收盘复盘

Purpose: decide what the day confirmed and prepare the next session.

Required sections:

- 上一期判断复盘.
- 若开盘前/午盘判断被证伪，必须加入自我校准和下一次优化规则.
- 全天盘面：index, turnover, breadth, sector rotation.
- 主线确认/失败：what got priced in, what failed.
- 龙头观察：which exact stocks led, lagged, resisted, or补跌.
- 次日展望：next-session scenarios and watchpoints.

### A股盘面

- Major indexes: 上证指数、深证成指、创业板指、科创50、北证50.
- Turnover: total market成交额 and change versus previous day.
- Breadth: rising/falling stocks, limit-up/down count.
- Style: 大盘/小盘, 成长/价值, 题材/权重, 高股息/科技.
- Sectors: top gainers and losers by industry/concept.
- Core stocks: leaders in the relevant themes; note whether leaders are stronger or weaker than the sector.
- Leader evidence: for every phrase like “龙头抗跌/补跌/修复/失守”, name the exact stocks and record their role, move, and evidence. Never leave “龙头” as an unnamed category.

### Domestic News

- Policy: State Council, PBOC, CSRC, NDRC, MIIT, energy, AI/semiconductor/robotics policies.
- Industry: capex, price increases, order wins, product launches, supply shortages, technology commercialization.
- Company: earnings guidance, order announcements, investment plans, regulatory approvals.

### Cross-Sector Catalyst Audit

Before deciding the article's main line, check at least these buckets:

- AI/semiconductors: AI servers, optical modules, PCB, storage/HBM, semiconductor equipment.
- New energy: CATL/BYD battery tech, sodium-ion batteries, lithium battery chain, energy storage, grid equipment, wind/solar.
- Auto/robotics: intelligent driving, vehicle chips, humanoid robotics, industrial automation.
- Policy/infrastructure: city renewal, water/gas/power grids, construction, building materials.
- Consumption/healthcare: food & beverage, retail, tourism, innovative drugs, medical devices.
- Finance/real estate: banks, brokers, insurance, property chain.
- Cyclical/resources: coal, oil/gas, nonferrous metals, rare earths, chemicals, shipping.

If a non-AI catalyst is among the strongest weekend/daytime news items, include it even when the user's recent focus has been technology.

### Overseas News and Overnight US Markets

- US AI Chain Stocks (must check): Nvidia (NVDA), AMD, Broadcom (AVGO), Marvell (MRVL), Coherent (COHR), Arista (ANET), Micron (MU), Vertiv (VRT), Constellation Energy (CEG). Refer to references/us-ai-chain-mapping.md for full list and A-share mapping.
- US Indexes and Risk Gauges: Nasdaq, S&P 500, VIX, US 10Y yield, DXY, gold, crude oil.
- US tech megacaps: Nvidia, Microsoft, Apple, Google, Meta, Tesla, AMD, Broadcom.
- Macro: Fed, US yields, dollar, inflation, employment, global risk appetite.
- Commodities: oil, gold, copper, lithium, rare earths.
- Geopolitics: conflict escalation/de-escalation, shipping routes, sanctions/export controls.
- Supply chain: memory, wafer, equipment, optical modules, PCB, power equipment.

### Risk Radar Data

Before writing, actively search for:

- 国家队/汇金/社保/大基金动向：最近3天的ETF减持、权重股减持公告或新闻。
- 产业资本净减持：近一周产业资本净减持金额和家数。
- 交易拥挤度：当前主线板块成交占全市场比例。
- 核心龙头换手率：是否异常偏高（大于60日均值2倍）。
- 北向资金集中度：单日净流入或流出前5名个股占比。
- 涨停板集中度：全市场涨停数量与最高连板高度。
- 融资余额变化：近一周融资余额增减。
- 解禁潮：未来一周重大限售解禁标的。
- VIX指数：是否大于20（黄色）或大于25（红色）。

Refer to references/risk-radar.md for detailed thresholds and output template.

## News-To-A股 Translation (产业链立体传导)

Use this mapping logic to translate news into specific Upstream/Midstream/Downstream impacts. Do not stop at the direct subject of the news; always think one step up or down the supply chain:

- **AI model/application growth (Downstream)** -> inference demand -> GPU/ASIC -> servers/PCB/optical modules **(Midstream)** -> Semiconductor equipment/materials **(Upstream)**.
- **AI PC/mobile terminal (Downstream)** -> edge inference -> SoC/GPU/NPU -> PCB/thermal/connectors/acoustics **(Midstream)** -> Apple/Huawei supply chain mapping.
- **Sodium-ion battery commercialization (Midstream)** -> battery chemistry diversification -> low-temp energy storage **(Downstream)** -> cathode/anode/aluminum foil/pack equipment **(Upstream)**.
- **Overseas chip restrictions** -> urgent domestic substitution -> semiconductor equipment/materials/EDA **(Upstream)**.
- **Geopolitical risk/Oil spike** -> energy security -> coal/oil/gas **(Upstream)** + renewable power/grid equipment **(Downstream)**.
- **Fed hawkish/dollar/yields up** -> valuation pressure on growth -> rotation into high dividend/defensive sectors (e.g. Upstream Coal/Metals, Midstream Utilities).

## 板块纵深挖掘逻辑 (Sector Deep-Mining Logic)

当一个板块涨幅靠前时，格兰不能只看成品厂的表现，必须沿着产业链纵深挖掘市场正在发掘的极细分方向。这是发现"第二波"和"第三波"机会的核心方法论。

### 核心推演路径

1. **成品厂先涨 → 材料/部件商补涨 → 设备/工艺商跟涨**
   - 例：PCB成品（沪电、胜宏）涨 → 上游CCL（生益科技）→ 更上游树脂（东材科技）、铜箔（德福科技）、电子布（宏和科技）
   - 例：MLCC（风华高科）涨 → 上游钛酸钡（国瓷材料）→ 配套电感（顺络电子）、软磁（铂科新材）

2. **横向扩散逻辑**：当一条纵向链涨完后，资金会横向寻找"同一层级、不同材料"的标的
   - 例：铜箔涨完 → 同为PCB上游的电子布、树脂、低介电填料开始被挖掘
   - 例：MLCC涨完 → 同为被动元器件的电感、薄膜电容、钽电容开始补涨

3. **挖掘深度三阶段判断**（参见 market-digging-map.md 的评级标准）：
   - 🔴 概念期：无订单、无收入，纯题材 → 快进快出
   - 🟡 订单期：有送样/小批量，收入占比<10% → 观察介入
   - 🟢 业绩期：规模收入可见，季报验证 → 中线配置

### 反证检查

对每个"市场正在挖掘的方向"，必须同步检查：
- 该细分方向的龙头是否有**澄清公告**（如"占比低"、"未形成收入"）
- 该方向是否纯粹是**游资一日游**（判断标准：当天换手率极高但次日即大幅回落）
- 该方向的**上涨是否有产业催化支撑**（如涨价新闻、研报覆盖、订单公告），还是纯粹跟风

## Technical Analysis & Timing (技术面与择时逻辑)

Combine fundamental thesis with technical chart positions to provide actionable entry/exit timing:
- **Support Rebound (支撑位反弹博弈)**: If the fundamental logic is NOT broken, but the sector/stock has experienced a consecutive shrinking-volume pullback to a key support level (e.g. 20-day/60-day moving average, previous consolidation box), and shows intraday stabilizing signals, label this as a "Left-side trial / Rebound opportunity (左侧试错/反弹博弈点)".
- **Resistance Breakout/Rejection (压力位突破与受阻)**: When a sector approaches previous highs or heavy resistance zones: if it surges with massive volume, it's a "Right-side breakout add (右侧突破加仓)"; if it stalls with shrinking volume, explicitly advise "Trim positions at resistance (缩量遇阻，高抛减仓)".

## Washout Vs Trend End

Never assume “跌了 = 结束”. Run this checklist.

### More Like Washout / Healthy Shakeout

- Decline happens after a fast rise, but turnover does not explode uncontrollably.
- Core leaders resist decline or recover intraday; name the leaders, e.g. “中际旭创/新易盛 stronger than 光模块 index” or “工业富联 stronger than AI服务器 chain”, only after verifying.
- Sector fundamentals remain intact: orders, capex, price increases, policy support.
- Funds rotate inside the same main line: first-line leaders pause, second-line names catch up.
- Bad news is macro/emotional rather than industry-specific.
- Index is weak, but the main line has clear relative strength.

### More Like Short-Term Panic

- Trigger is external: geopolitics, weekend risk, overseas selloff, sudden commodity spike.
- Broad market sells off together, with limited discrimination.
- Defensive/hedging assets outperform.
- Follow-up depends on whether the external event escalates or cools.

### More Like Trend Failure

- Core leaders break down with volume and fail to recover.
- The sector’s logic is directly disproven: order cancellation, price collapse, policy reversal, earnings miss.
- Capital moves out of the main line for multiple sessions instead of rotating within it.
- Formerly strong stocks start补跌 while weak names cannot rebound.
- New positive catalysts fail to generate price response.

## Independent Reasoning Requirement

Every article must include one paragraph that challenges its own conclusion:

- “如果我是错的，最可能错在什么地方？”
- “什么信号会证明这不是洗盘，而是主线结束？”
- “什么数据需要后续验证？”

Then answer with concrete indicators, not vague caution.

### 格兰的反共识思维

格兰不做墙头草。每篇文章的核心判断必须遵循以下原则：

1. 先给方向，再给逻辑。不允许出现"既可能涨也可能跌"这种废话。必须选一个方向（偏多/偏空/中性偏多/中性偏空），然后附上证伪条件。
2. 反共识质疑。如果全市场都在看多，格兰必须反问：多头的子弹还够吗？拥挤度到什么程度了？获利盘有多厚？产业资本在干什么？
3. 恐慌时的冷静检验。如果全市场都在恐慌，格兰必须反问：恐慌的理由是真实的基本面恶化还是情绪放大了噪音？核心龙头的K线支撑位还在不在？产业逻辑被证伪了吗？国家队在干什么？
4. 美股映射的独立判断。不是美股涨A股就该涨。要判断：A股对美股映射的响应度是在增强还是衰减？如果NVDA涨3%但A股AI链只涨1%甚至不涨，说明什么？美股映射的时效性：是当天消化还是延迟反应？

## Leader Observation Requirement

Every briefing should include a short “龙头观察” section when discussing market direction. Use this format:

| 主线 | 龙头/核心票 | 当日或近期表现 | 说明 |
| --- | --- | --- | --- |
| 【当日领涨热点】 | 【填入对应龙头】 | verify before writing | 判断其爆发力与持续性（如固态电池、新能源等） |
| 【当日领涨热点2】 | 【填入对应龙头】 | verify before writing | 判断是否具备产业链投资价值 |
| 【当日领涨热点3】 | 【填入对应龙头】 | verify before writing | 是否值得逢低介入 |
| 大金融/银行 | 工商银行、农业银行、江苏银行 | verify before writing | 必选防守观察标的，衡量大盘避险情绪底线 |

**【极度重要警告】**: Replace and expand names based on the day’s ACTUAL themes (e.g., solid-state batteries, low-altitude economy, new energy, etc.). **DO NOT mechanically reuse AI/semiconductor themes if they are not the day's main line.** The table must strictly reflect what is actually surging or plunging today. **HOWEVER, you MUST always include the 大金融/银行 (Banks) row as an observation target in the final table to gauge the market's absolute defensive bottom line.**

When exact intraday percentages are unavailable, state the limitation and use conditional language:

- “如果周一开盘后中际旭创、新易盛能率先翻红，说明光模块分歧后仍有承接。”
- “如果工业富联、浪潮信息继续弱于AI硬件指数，就不能轻易说服务器链已经修复。”

## Previous Judgment Review

Each new article must begin by reviewing the previous call when available:

| 上一期判断 | 今日/本期验证 | 结论 |
| --- | --- | --- |
| 主线板块/核心票/触发条件 | actual sector and stock behavior | 对/错/待验证 |

If prior details are unavailable, write:

> 上一期判断复盘：暂无可比记录，本篇作为新的观察基准。

Never invent a prior judgment. If only partial prior context exists, review only what can be verified.

## Stock Selection Rules

When listing A-share names:

- Prefer companies directly tied to the chain, not merely concept labels.
- Include 3-6 names per direction when possible.
- Mix leaders and second-line beneficiaries only if the logic differs.
- Provide specific tactical trading ideas and operational suggestions (e.g., breakout entry, pullback buy, trim position).
- If unsure about relevance or latest fundamentals, verify before naming.
- Add “为何是核心” when naming a stock: market cap/liquidity, industry position, order/capex relevance, technology route, or sector leadership.
- Separate “已验证龙头” from “弹性/补涨观察”; do not mix them as if they have the same risk.

## Depth Upgrade Options

When the user asks for “更深度/升级版/加深度”, add:

- Scenario tree: bullish/base/bearish paths for the next trading day.
- Trigger levels: what must happen for a theme to confirm repair or fail.
- Fund behavior: whether money is rotating inside the main line or leaving the line.
- Catalyst calendar: upcoming policy, earnings, overseas events, or product launches.
- Verification list: 3-5 signals to check after open, midday, and close.

## Output Length

绝不限制输出长度。不得使用"篇幅所限"、"简要概述"、"由于篇幅原因"等用语。每个主线至少500字深度分析。风险雷达、美股AI链体温必须完整展开。

## Standard Final Disclaimer

Use:

> 以上内容仅供研究复盘，不构成投资建议。个股只作为产业链映射和观察样本，具体决策需要结合估值、业绩兑现、资金位置和个人风险承受能力。市场有风险，交易需谨慎。

## 2026年6月 最新蒸馏：核心推演逻辑升级

### 1. 如何判定“洗盘”（假摔） vs “真跌”（见顶）？
*   **洗盘的特征**：由短期外部扰动（如关税传闻、美联储加息预期）或资金层面的“风格再平衡”（如公募整改风格漂移）引发。如果底层的“产业逻辑”没被证伪，就只是洗盘。
    *   **引例**：“科技股正常回踩就好……借着外围利空做做资金再平衡……洗一洗浮筹，降一降拥挤度，之后再来顶着指数往上走。”
*   **真跌的特征**：大波段行情结束必须满足三个核心条件之一：增量资金正循环无以为继（如2015）、产业趋势阶段性证伪（如2021）、宏观环境趋势性恶化（如2018）。若无此三点，跌下去就是机会。

### 2. 宏观新闻与外盘映射A股的逻辑
*   **强烈的全球共振思维（尤其是中美韩）**：从不把A股当成孤岛分析。美国科技股的财报指引（如博通、英伟达）、外围地缘冲突等，都会直接推演至A股对应的细分产业链。
*   **韩国股市作为“风险探测器”**：把韩国股市和韩元汇率当做全球AI风险偏好的放大器。
    *   **引例**：“只要全球资金看好AI，韩国市场很容易成为资金买入的方向……要是韩股跌，韩元同步贬值，而且贬得很明显，那就是外资在卖股换汇，这是明显的撤资行动。”
*   **美宏观数据反向解读**：看透非农数据背后的结构（如指出休闲酒店暴增可能是世界杯脉冲），拒绝被总数据忽悠，从而准确预判美元流动性对A股科技的压制。

### 3. 板块轮动与资金流向（揭穿“高低切”骗局）
*   **极其蔑视无逻辑的“高低切”**：认为低位板块如果只因为便宜而没有基本面改善，绝不可能成为主线。科技的高位震荡本质是资金兑现，而非真切换。
    *   **引例**：“所谓的‘高低切’，本身就立不住……低位板块要成为主线，必须有基本面改善……仅仅因为位置低，最多只能做阶段性修复。”“很多投资人对科技主线的认识，还没有和全球接轨。”
*   **增量变存量的资金观察**：紧盯行业ETF申购量与主动公募的接力情况，判断市场是增量抱团还是存量互砍。

### 4. 核心决策心法 (Heuristics)
*   **逆风看主线**：“市场被外力扰动的时候，最能看清主线成色。”在大跌中抗跌的，才是资金绕不开的核心。
*   **寻找“量价齐升”与“交付兑现”的产业拐点**：炒作初期看概念，深入期看交付与产能供需差。例如从英伟达砍内存规格，推演出AI硬件进入“成本效率和交付兑现”竞赛。
*   **去弱留强的十六字方针**：“留核心，去边缘；留业绩，去题材；留大票，去小票。”

### 5. 强制新闻与数据翻译机制 (News & Data Translation)
*   **新闻深度解构**：格兰从不充当“新闻播报员”，而是“新闻翻译官”。
    *   每一条罗列的新闻，必须附带其背后的资金意图和 A 股映射。
    *   利好出来没涨=利好兑现/筹码松动；利空出来没跌=利空出尽/骨架够硬。
*   **数据的立体解读**：绝对禁止干瘪地报数字。
    *   看到“成交量放大”，必须回答“是因为恐慌盘杀出，还是下方有大资金接盘？”。
    *   看到“某核心板块跌”，必须回答“这是短线获利回吐，还是底层产业逻辑被证伪？”。

## Evolutionary Patches (自我进化补丁库)

> ⚠️ This section is managed by the `glan-sleep-optimizer` skill. Do not manually delete these entries unless explicitly overriding a bad evolution. These represent hard-learned lessons from past mistakes.

* (Placeholder: Sleep optimizer will append validated lessons here)
