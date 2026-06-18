# News Source Matrix

Use this source router before writing A股复盘/展望. The goal is broad, current, cross-verified coverage, not simply collecting the most links.

## Source Tiers

### Tier 0: Official / Primary Sources

Use first when available.

- China policy/regulators: 中国政府网、新华社、央视新闻、央行、证监会、发改委、工信部、财政部、商务部、国家能源局、交易所公告.
- Company primary sources: 上市公司公告、互动易/上证e互动、公司官网、业绩说明会、新闻稿.
- Overseas primary sources: Fed, Treasury, SEC filings, company IR pages, Nvidia/Microsoft/Apple/Tesla/CATL/BYD official releases.

### Tier 1: Market Data / A股盘面

Use for market breadth, sector ranking, turnover, and individual stock moves.

- 东方财富、同花顺、Wind/Choice if available, 新浪财经、证券时报行情、交易所行情 pages.
- For sector strength: 东方财富板块、同花顺概念、财联社电报/盘面直播 if accessible.

### Tier 2: Chinese Financial News

Use for speed and domestic market interpretation; cross-check important items.

- 财联社：快讯、盘面异动、题材催化、机构解读.
- 证券时报、上海证券报、中国证券报、经济观察报、21世纪经济报道、每经网、界面财联社.
- 腾讯新闻/腾讯财经、新浪财经、澎湃财讯、第一财经.

### Tier 3: International News

Use for overnight risk appetite, US tech, macro, commodities, and geopolitics.

- Reuters, AP, CNBC, Bloomberg public pages, Financial Times public pages, Wall Street Journal public pages, MarketWatch, Investing.com.
- Nikkei Asia, The Information, Semafor, TechCrunch for tech/supply-chain clues.
- For commodities: ICE/CME/LME pages when accessible, Investing.com, CNBC commodities.

### Tier 4: Investment Bank / Asset Manager Views

Use for high-level framing, not as trading truth. Do not claim access to paywalled reports unless public.

- Public insights pages: Goldman Sachs, Morgan Stanley, JPMorgan, UBS, Citi, Bank of America, BlackRock, PIMCO, Bridgewater, Apollo, KKR.
- Search terms: `site:goldmansachs.com insights AI capex`, `site:morganstanley.com ideas China market`, `JPMorgan market outlook`, `UBS CIO`, `BlackRock weekly commentary`.
- Treat broker/IB views as “外资/机构视角”, then verify with market data and primary facts.

### Tier 5: Social / Rumor / Market Chatter

Use only as weak signals, never as standalone facts.

- X/Twitter, Xueqiu, Weibo, Telegram summaries, forum posts.
- If useful, write “市场传闻/情绪线索，尚需公告或权威媒体验证.”

## Collection Workflow

1. Start with market data: index, turnover, breadth, sectors, leaders.
2. Scan Tier 0 official and company sources for hard catalysts.
3. Scan Tier 2 Chinese financial media for domestic speed.
4. Scan Tier 3 international media for overnight macro, US tech, commodities, geopolitics.
5. Scan Tier 4 public IB/asset manager views when the topic is macro allocation, AI capex, China assets, commodities, or rates.
6. De-duplicate repeated news. Prefer the earliest primary source or the most authoritative confirmation.

## Scoring Rules

Score each candidate news item from 1-5 on:

- **Importance**: significance among all news items scanned for this briefing.
- **Impact**: likely effect on market direction or a major sector.
- **Credibility**: official/primary > reputable media > rumor.
- **Tradability**: clear A-share mapping and identifiable stocks.
- **Novelty**: new information, not already priced.
- **Verification**: supported by data, company news, or multiple sources.

Only promote an item into the article if it scores high on at least three dimensions. Mention lower-score items only as risks or pending verification.

## Required Source Output Module

Every briefing must end with a “采用新闻源与评分” module after the investment directions and before/after the risk disclaimer. Include the sources actually used, not every source scanned.

Use this format:

| 来源/链接 | 信息类型 | 采用原因 | 重要度 | 影响力 | 可信度 | 可交易性 | 新鲜度 | 验证度 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Source name + link | policy/data/company/international/IB view | why it mattered | 1-5 | 1-5 | 1-5 | 1-5 | 1-5 | 1-5 |

Then add 2-4 bullet notes:

- “未采用但关注”：important rumors or unverified items not used as core logic.
- “交叉验证”：which facts were confirmed by multiple sources.
- “缺口”：which data remains missing, such as intraday breadth, exact northbound flow, or company announcement confirmation.

Scoring guidance:

- Importance 5: top market-moving item; 3: useful background; 1: minor.
- Impact 5: broad market or major sector effect; 3: subsector only; 1: weak mapping.
- Credibility 5: official/primary; 4: reputable wire/major financial media; 3: single reputable secondary source; 1-2: rumor/social.
- Tradability 5: clear A-share sector and stock mapping; 3: indirect; 1: hard to trade.
- Novelty 5: newly released and underpriced; 3: continuation; 1: stale.
- Verification 5: primary + cross-confirmed; 3: reputable single-source; 1: unverified.

## Mandatory Cross-Sector Check

For each briefing, check at least one source or query for every bucket:

- AI/semiconductor
- New energy/battery/sodium-ion/storage
- Auto/intelligent driving/robotics
- Policy/infrastructure/city renewal
- Consumption/healthcare
- Finance/real estate
- Resources/commodities/shipping/geopolitics

If a bucket has no meaningful new catalyst, say nothing. Do not force a theme.

## Constraints

- Do not bypass paywalls or reproduce copyrighted articles.
- Quote only short excerpts when necessary; prefer paraphrase and cite links.
- If a source is unavailable, use a reputable alternative and state uncertainty.
- Do not let one familiar source dominate. The article should reflect source diversity.
