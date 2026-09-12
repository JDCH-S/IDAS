# Top 20 opportunities (scoring v1, after competitive/existence checks)

Date: 2026-09-11. Inputs: `opportunity-universe.md` (102 unique opportunities, 40 investigated), `_raw/ci-batch-1..4.md` (existence checks), `_raw/stream-A..E.md` (discovery evidence). Scores are computed by `score.py` from 23 criteria; the master data is `opportunity-database.json` and the flat export `opportunity-database.csv`. All facts are from WebSearch result summaries (pages could not be opened); VERIFIED means VERIFIED (search-summary).

## Scoring model and weights

Every criterion is 0-10, higher is better for this founder (so "competition" 10 = uncrowded, "initial capital" 10 = almost none needed, "barrier to entry" 10 = easy for this founder to enter). Weights sum to 100 and encode the goal "high upside + realistic entry + strong founder fit + future resilience":

| Group | Criteria (weight) | Group weight | Why |
|---|---|---|---|
| Entry realism | part-time feasibility (7), distribution feasibility (6), time to first revenue (5), initial capital (4), regulatory feasibility (4), barrier to entry (3) | 29 | The founder keeps a full-time job and has little capital; anything that cannot start in 30 days part-time is worthless however large |
| Founder and interest fit | founder fit (10), interest fit (7) | 17 | Asymmetric advantage and five-year stamina |
| Pain, willingness to pay, market | willingness to pay (7), customer pain (5), market size (3), market growth (2) | 17 | WTP weighted above pain: loud pain with no budget killed several ideas |
| Competition, gap, defensibility | competitive gap (5), defensibility (5), competition (3) | 13 | Competition alone is not fatal; absence of a wedge is |
| Future resilience | AI leverage (4), AI commoditisation resistance (4), AGI resilience (2), ASI resilience (1) | 11 | Prefer businesses AI strengthens; discount thin wrappers |
| Upside and geography | recurring revenue (4), Belgium launchability (3), EU expansion (3), large-company potential (3) | 13 | Belgium is the launchpad; recurring revenue is the path off founder labour |

Not a simple average: entry realism and fit together carry 46 points because the brief's binding constraints are time and capital, not market size. Market size is deliberately light (3) because every bottom-up size here is an estimate with missing Belgian counts.

## Ranking

| Rank | ID | Opportunity | Score | CI verdict |
|---|---|---|---|---|
| 1 | U-031 | AI-native fractional controlling / HQ reporting for BE-LU subsidiaries and holdings | 72.1 | PROMISING |
| 2 | U-021 | Done-for-you group consolidation and intercompany clean-up for Belgian holdings on Odoo/Exact, productised later | 69.9 | PROMISING |
| 3 | U-002 | Peppol portfolio operations for accounting firms (exception triage, master-data hygiene) | 63.9 | POSSIBLE |
| 4 | U-064 | Productised QoE-light financial analysis for small Belgian acquisitions | 62.5 | POSSIBLE |
| 5 | U-011 | AI-assisted reporting/automation capacity partner for accounting firms with client stops | 61.2 | POSSIBLE |
| 6 | U-004 | 2028 e-reporting readiness and reported-vs-booked reconciliation | 60.3 | POSSIBLE |
| 7 | U-046 | DORA vendor pack for small ICT suppliers to financial entities | 58.3 | POSSIBLE |
| 8 | U-089 | Independent finance-automation ROI review for SME CFOs | 58.3 | POSSIBLE |
| 9 | U-023 | Variance-commentary / management-reporting agent | 57.9 | WEAK |
| 10 | U-068 | Brussels co-ownership renovation financing packs | 57.7 | POSSIBLE |
| 11 | U-027 | Month-end close orchestration for EU SME/lower mid-market | 56.6 | WEAK |
| 12 | U-043 | Supplier compliance passport (VSME + NIS2 + DORA) | 56.1 | POSSIBLE |
| 13 | U-042 | Belgian public-tender bid-ops pack | 54.6 | POSSIBLE |
| 14 | U-024 | Reporting-pack tie-out agent | 53.7 | WEAK |
| 15 | U-012 | Vendor-neutral data/MCP/portability layer | 53.3 | WEAK |
| 16 | U-092 | Odoo Belgian-localisation setup/QA service | 52.0 | WEAK |
| 17 | U-022 | ERP data-extraction / reporting layer | 51.9 | WEAK |
| 18 | U-009 | Client document-chasing agent for firms | 51.1 | WEAK |
| 19 | U-072 | Architect project profitability tool | 50.9 | WEAK |
| 20 | U-044 | Finance-grade VSME data via accountants | 50.7 | WEAK |

Reading the ranking: the pattern across all 40 checks is that pure-software plays in Belgian SME finance are already crowded or being absorbed by platforms (Microsoft, Odoo, Xero, Exact, Visma), while the gaps that survive are service-shaped work that a controller can start now and that AI makes unusually cheap to deliver. Ranks 1, 2, 5, 9 and 14 are one business seen from different angles (see `top-5-deep-dives.md`). Ranks 9, 11, 14, 15, 17 are kept in the Top 20 as assets or features of higher-ranked opportunities, not as companies.

## The 20 opportunities

### 1. U-031 AI-native fractional controlling / HQ reporting for BE-LU subsidiaries and holdings
- One sentence: A monthly retainer that delivers HQ-format reporting packs, variance commentary, consolidation and pack QA for Belgian/Luxembourg subsidiaries of foreign groups and small Belgian holdings, delivered by one senior controller leveraged by agents, priced below two controller-days a month.
- Exact customer: finance manager or managing director of a BE/LU subsidiary (20-300 FTE) reporting to a foreign HQ; owner-CFO of a 3-15 entity Belgian holding.
- Exact problem: small local finance teams must produce group-format packs every month; interim controllers cost EUR 600-800/day and Big-4 managed services are people-priced (VERIFIED, Apex League / EY / KPMG pages).
- Current solution: in-house controller, interim/freelance controller, Big-4 managed services, Excel.
- Existing competitors: interim agencies (Apex League, Michael Page, Robert Half), Finvision, FinForces, Flow Partners, EY/KPMG managed services; Neno (NL, EUR 6.6M, bookkeeping) and Skalar (DE, EUR 12M, tax) are the agent-first services analogues, not FP&A.
- Why customers pay: they already pay day rates; a fixed retainer with faster turnaround and fewer errors is a like-for-like substitution.
- Why now: agent leverage lets one senior person serve many subsidiaries; interim rates were reported as rising by a recruitment blog citing a "Dosign" ruling, which the final review identified as the Dutch WAADI judgment (not applicable in Belgium): no verified Belgian rate-rise; incumbents are day-rate models with no incentive to compress.
- Why still open: services niche, not a category; nobody has productised it; Big-4 ignore sub-EUR-50M subsidiaries' price point.
- Belgium entry: Brussels has a dense population of foreign-owned subsidiaries and holdings (count: Evidence not found); founder's own network is the first channel.
- Founder fit 10/10: exactly the founder's job, done for several companies instead of one.
- Interest fit 8/10: customer conversations with finance peers, building agent tooling, business strategy; less product novelty.
- Barrier to entry: LOW overall; regulatory feasibility 8 (management reporting is not obviously ITAA-reserved; to confirm), employment-contract side-activity clause is the real check.
- Capital: EUR 0-500. Time to first revenue: 1-3 months.
- AI leverage: high; connectors, mapping, commentary drafting, tie-out can be agentic; the human stays for judgement and sign-off.
- AI commoditisation risk: moderate (Copilot Finance Agents, Syft commentary); resilience comes from the relationship, the HQ-format know-how and the Odoo/Exact data plumbing Microsoft does not cover.
- AGI resilience: weakened as labour, strengthened as a productised service with proprietary templates and client data. ASI: weak; only relationships and trust remain.
- Defensibility 4/10 today (labour); rises with tooling, templates and references.
- Overall: 72.1.

### 2. U-021 Done-for-you group consolidation and intercompany clean-up for Belgian holdings on Odoo/Exact
- One sentence: Monthly group closing and consolidation (with intercompany matching and eliminations) for 3-15 entity Belgian holdings, sold as a retainer and turned into an Odoo/Exact-native consolidation product.
- Exact customer: group controller or owner-CFO of a Belgian holding with 3-15 entities, often on Odoo 18/19 (consolidation app removed in v18, forum confusion in 2026, VERIFIED) or Exact; below the statutory consolidation threshold.
- Exact problem: Excel consolidation every month, intercompany balances that do not reconcile, no bank/board-grade group numbers; Lucanet-class tools priced for >EUR 50M groups.
- Current solution: Excel, hiring a consolidation controller (live Belgian vacancies, VERIFIED), NL tools (Speedbooks EUR 69/mo, Finstack from EUR 39/mo, Liquid, Easyclose EUR 705-905/mo), PwC "consolidation as a service".
- Existing competitors: Easyclose, Finstack, Speedbooks, Liquid, BrightAnalytics, EMAsphere, Exact Consolidatie, Silverfin (firm channel), Prophix/Sigma Conso, Lucanet, Odoo partners (Gravitai), PwC CaaS.
- Why customers pay: banks, boards and buyers demand group numbers; a controller hire costs more than a retainer.
- Why now: Odoo removed its consolidation app; PE/holding roll-ups multiply entities; MCP connectors make ledger access cheap; PwC now sells the service to SMEs (validation).
- Why still open: tool layer is crowded in NL and Exact-first; none surfaced with a Belgian-GAAP + Odoo-native + done-for-you position.
- Belgium entry: Odoo is Belgian and heavily installed; Belgian holdings/management companies are common; Odoo integrators (OBS, Odive, Agile-Minds) as channel.
- Founder fit 10/10; interest fit 9/10 (modelling, data, product).
- Barrier: LOW-MODERATE, GOOD barrier (domain templates and Odoo know-how become the moat).
- Capital: EUR 0-500 for service; EUR 2-5k for product. Time to first revenue: 1-3 months.
- AI leverage: high (LLM chart-of-accounts mapping, IC matching, elimination proposals).
- AI commoditisation risk: moderate; Odoo could re-ship consolidation; Exact has a module.
- AGI: neutral-to-strengthened if the product owns the Odoo niche; ASI: weak.
- Defensibility 5/10.
- Overall: 69.9.

### 3. U-002 Peppol portfolio operations for accounting firms
- One sentence: A "Peppol portfolio health check" service, then a monitoring agent, that shows an accounting firm every rejected, undelivered or mis-addressed e-invoice and every bad identifier across all its clients and access points.
- Exact customer: Belgian accounting firms with 5-50 staff whose clients sit on several access points (Billit, Yuki, Exact, Octopus, Odoo, Peppol Box).
- Exact problem: since 1 Jan 2026 wrong VAT numbers, missing fields and unregistered recipients cause rejections that delay cash; fines EUR 1,500/3,000/5,000 since April 2026 (VERIFIED); no single vendor sees the whole portfolio.
- Current solution: access-point support tickets, Excel lists, per-account audit logs, advisory blog posts.
- Existing competitors: none named at portfolio level (VERIFIED absence across 8 queries); Billit evidence files and Peppol Box identifier support are building blocks; Cashfeed on the AP side; Peppolcheck.be free single lookups.
- Why customers pay: support time and fines; firms spend 6-10% of revenue on software (VERIFIED).
- Why now: rejection wave is 8 months old; Peppol Invoice Response exists but is not adopted; 2028 e-reporting will turn master-data errors into tax-authority-visible mismatches.
- Why still open: fragmentation (firms' clients spread over many access points) and the layer is unglamorous; any access point can add a per-account view but not a cross-AP one.
- Belgium entry: Belgium is the first big-bang mandate in the region; every firm is affected.
- Founder fit 7/10 (Python + data-quality work, licence-free); interest fit 7/10.
- Barrier: LOW; BAD barrier unless multi-AP data becomes an asset. Price anchor EUR 5-10/mo per company is a headwind.
- Capital: EUR 0-500. Time to first revenue: 1-3 months (paid audit).
- AI leverage: moderate; mostly deterministic validation, LLM for explaining rejections and drafting client fix lists.
- AI commoditisation risk: moderate. AGI: neutral (compliance data work persists). ASI: weak.
- Defensibility 4/10.
- Overall: 63.9.

### 4. U-064 Productised QoE-light for small Belgian acquisitions
- One sentence: A fixed-price, two-week "quality of earnings light" (normalised EBITDA, working capital, cash conversion, red flags) for buyers of EUR 0.5-5M businesses, sold through accountants, brokers and succession programmes.
- Exact customer: individual acquirers, family successors, small PE and corporates buying tuck-ins; advised by accountants at capacity or brokers.
- Exact problem: below EUR 10M diligence is skipped or minimal (VERIFIED, stream A-20); mid-tier fees uneconomic; buyers overpay.
- Current solution: buyer's accountant "has a look", lawyer checklists, skip.
- Existing competitors: none productised in Belgium (VERIFIED absence, 7 queries); Baker Tilly, Moore, VGD, BDO, Vandelanotte bespoke; Rapid Diligence (US, from USD 8,900), Guardian, Scalemetrics (CH); AI QoE tooling for advisers.
- Why customers pay: US sub-USD-5M deals pay USD 7-30k; CH CHF 8-60k (VERIFIED); Belgian small-deal fee: Evidence not found.
- Why now: succession wave; AI cuts analyst hours on ledger ingestion and normalisation.
- Why still open: market too small for mid-tier hourly models; US productisation came with the searcher wave.
- Belgium entry: Brussels accountants refusing DD work, brokers, notaries, hub.brussels/SOWACCESS succession programmes.
- Founder fit 9/10; interest fit 8/10.
- Barrier: LOW; GOOD (method, references), BAD (one-off revenue). Cannot sign as ITAA/IBR mission; position as buyer-side analysis.
- Capital: EUR 0-500. Time to first revenue: 1-3 months.
- AI leverage: moderate-high (ingestion, normalisation, report drafting); judgement stays human.
- AI commoditisation risk: moderate (a buyer could run books through an LLM); resilience from liability, references and channel.
- AGI: weakened (analysis becomes cheap; trust and signature remain). ASI: weak.
- Defensibility 4/10. Recurring revenue 3/10.
- Overall: 62.5.

### 5. U-011 AI-assisted reporting/automation capacity partner for accounting firms
- One sentence: Sell controller-grade management reporting and automation capacity to firms that have client stops, explicitly excluding ITAA-reserved bookkeeping and tax work.
- Exact customer: Belgian firms with 5-30 staff; 56% have client stops (VERIFIED).
- Exact problem: cannot hire (30% of dossier-manager vacancies unfilled), cannot deliver advisory, cannot build automations.
- Current solution: client stops, offshoring at USD 10-30/h, Ravical/Dytto software, price increases.
- Existing competitors: Ravical (EUR 7.3M, 100+ practices, outcome pricing), Dytto, Eastvantage, Aviaan/2Max white-label, Fidushare.
- Why customers pay: firms pay offshore USD 200-750/client/month and charge EUR 50-150/h (VERIFIED).
- Why now: shortage profession in all three regions (July 2026); 2028 e-reporting adds work.
- Why still open: the "AI for firms" space is contested (Ghent); the on-shore controller-grade reporting/automation niche is not a category anyone owns.
- Belgium entry: Brussels/Walloon Brabant FR-speaking firms less served by Ghent startups (INFERENCE).
- Founder fit 8/10; interest fit 6/10 (firm work is less strategic than group controlling).
- Barrier: MODERATE; the regulatory barrier is BAD: ITAA registration is legally required to perform accountancy for third parties (VERIFIED); subcontracting rules: Evidence not found.
- Capital: EUR 0-500. Time to first revenue: 1-3 months.
- AI leverage high; commoditisation risk moderate (Silverfin Assistant, Ravical); AGI weakened; ASI weak.
- Defensibility 3/10.
- Overall: 61.2. Treated in deep dives as the accounting-firm channel variant of U-031.

### 6. U-004 2028 e-reporting readiness and reported-vs-booked reconciliation
- One sentence: The 2027-28 second act of U-002: a per-client pre-check of what FPS Finance will see under dual-sided near-real-time reporting versus what is in the ledger.
- Customer, problem, competitors: as U-002; category proven abroad (SIAC FTEL ADRI in Italy, Avalara SII content in Spain, VERIFIED); nothing in Belgium.
- Why now: law approved 22-23 July 2026, effective 1 Jan 2028 (VERIFIED); ITAA already telling firms to prepare.
- Why still open: the problem does not exist until 2028; vendors sell pipes.
- Belgium entry: same firms as U-002.
- Founder fit 7; interest fit 7. Barrier LOW; timing barrier (zero revenue before 2027). Capital EUR 0-500; time to first revenue 18+ months.
- AI leverage moderate; commoditisation risk moderate (ledger vendors will bundle); AGI neutral; ASI weak. Defensibility 5.
- Overall: 60.3.

### 7. U-046 DORA vendor pack for small ICT suppliers to financial entities
- One sentence: A fixed-fee pack (Article 30 addendum, Register-of-Information data sheet with LEI and subcontractor chain, evidence index) plus annual refresh for SaaS/IT SMEs selling to banks, insurers and funds in BE/LU/NL.
- Exact customer: 10-100 FTE software/IT-services vendors with financial-sector clients.
- Exact problem: every client sends a different addendum and data request; "negotiating the same clauses thirty times" (VERIFIED, dorapp); CSSF reported only 40% of Luxembourg RoI submissions by mid-March 2026 (VERIFIED).
- Current solution: own templates, law firms by the hour, ISO 27001 as proxy.
- Existing competitors: none vendor-side (VERIFIED absence); buyer-side Hybridity (EUR 5M), RegReportingDesk, DORApp, 3rdRisk; law firms.
- Why customers pay: law-firm hourly cost; lost deals when the bank's procurement stalls.
- Why now: DORA live since Jan 2025; annual RoI cycles.
- Why still open: one-off, low recurrence; unattractive for SaaS, suited to productised service.
- Belgium entry: Brussels/Luxembourg financial-sector density.
- Founder fit 6 (finance-literate, speaks the bank's language; no security background); interest fit 5.
- Barrier LOW; BAD (low recurrence). Capital EUR 0-500; time to first revenue 1-3 months.
- AI leverage moderate (agent assembles pack from documents); commoditisation risk moderate-high; AGI weakened; ASI weak. Defensibility 3.
- Overall: 58.3.

### 8. U-089 Independent finance-automation ROI review for SME CFOs
- One sentence: A fixed-price (EUR 1,500-3,000) neutral review of an SME's finance-automation pilots and plans, sold by a controller rather than an agency.
- Exact customer: SME CFOs/CEOs (10-250 FTE) who bought agency PoCs or plan AI spend.
- Exact problem: 95% of pilots fail (MIT), 84% of CFOs see no ROI (Gartner), 51% of Belgian SMEs do not know how to deploy AI (VERIFIED); agency "audits" are conflicted lead magnets.
- Current solution: agency audit (free to EUR 2,500), fractional CFO EUR 1,000-1,800/day, abandon.
- Existing competitors: WDC, Flowful, Aives, LTC, ClickForest, Crux Digits (NL, EUR 2,500 audit).
- Why customers pay: Crux's price point proves it; Belgian independent-review pricing: Evidence not found.
- Why now: AI budgets rising while ROI absent.
- Why still open: no follow-on revenue for a neutral reviewer; agencies give it away.
- Founder fit 7; interest fit 6. Barrier VERY LOW and BAD (no moat). Capital EUR 0; time to first revenue under a month.
- AI leverage moderate; commoditisation risk high; AGI destroyed; ASI destroyed. Defensibility 2.
- Overall: 58.3. Kept as a cash engine, not a company.

### 9. U-023 Variance-commentary / management-reporting agent
- One sentence: Excel-native agent that drafts variance commentary and management packs; ranked here only as a delivery asset for U-031.
- Existing competitors: Microsoft Finance Reconciliation Agent (GA April 2026) and Variance Analysis Agent, Copilot in Excel Skills (25 June 2026), Syft $39-79/entity, Fathom GBP 33, Datarails $24k+, Endex $14M (all VERIFIED).
- Why still open: it is not; Microsoft moved first. Residual: Belgian-GAAP/HQ-format packs with driver data in Odoo/Exact (Microsoft agents connect to D365/SAP, INFERENCE).
- Founder fit 9; interest fit 8; commoditisation risk very high (2); defensibility 2.
- Overall: 57.9. Verdict: fold into U-031.

### 10. U-068 Brussels co-ownership renovation financing packs
- One sentence: Per-building financing packs (per-lot capex allocation, reserve fund vs collective loan vs individual loans, prime/ECORENO stacking, cash-call schedule) that syndics can put in front of a general assembly before the 2030/2033 PEB deadlines.
- Exact customer: professional syndics in Brussels (~500-560 exclusive syndics nationally, VERIFIED), PEB experts and renovation facilitators; the AG decides.
- Exact problem: Brussels co-ownerships need a valid PEB by end-2030 and <=275 kWh/m2 by 2033 (VERIFIED); AGs defer because financing is unclear; syndics are overloaded.
- Current solution: Excel, PEB experts, Homegrade free advice, deferral.
- Existing competitors: none commercial in Belgium (VERIFIED absence); French PPT software exists because PPT is mandatory there; Flanders is building a free public VME financing tool (VERIFIED); KBC VME loan, Look&Fin.
- Why customers pay: Evidence not found for any paid planning tool; INFERENCE from PEB-study and French PPPT fees.
- Why now: deadlines; policy push; financing layer unresolved even in France.
- Why still open: public bodies give advice for free; AG decides once a year; syndic is gatekeeper.
- Belgium entry: Brussels-only wedge; very local.
- Founder fit 7; interest fit 6. Barrier LOW-MODERATE, BAD (free public tool risk, annual cycle). Capital EUR 0-500; time to first revenue 3-6 months.
- AI leverage moderate; commoditisation resistance 6; AGI 5; ASI 4 (physical assets, regulation, local trust). Defensibility 5. Recurring revenue 3.
- Overall: 57.7.

### 11. U-027 Month-end close orchestration for EU SME/lower mid-market
- One sentence: Close-management layer for Exact/Odoo/BC shops; kept as a reference point, not a target.
- Existing competitors: Eagl (Ghent, EUR 825k), Stacks ($35M), Easyclose/FinClose, Numeric ($51M), FloQast, Odoo 20 native accounting agent (all VERIFIED).
- Why not: Ghent contested; ERP-specific angle already taken; needs capital (EUR 5-20k) and 6-12 months to revenue; part-time feasibility 4.
- Founder fit 8; interest fit 8; defensibility 4. Overall: 56.6.

### 12. U-043 Supplier compliance passport (VSME + NIS2 + DORA)
- One sentence: One evidence library and AI answering service for non-tech 50-250 FTE suppliers who receive sustainability, security and DORA questionnaires from large customers.
- Exact customer: manufacturing/logistics/facility suppliers; office manager or controller answers.
- Exact problem: 5-20 questionnaires in different formats (VERIFIED, Socialsuite); three demand waves coincide in 2026-27.
- Existing competitors: per pillar crowded (Vanta/Drata USD 7.5-12k/yr, Secfix USD 12M, EcoVadis, Easy Cyber Protection EUR 25-825/client/mo via MSPs, VSME tools EUR 199/yr-99/mo); no bundler found (VERIFIED absence).
- Why still open: each vendor grew from one regulation and one persona; the non-tech supplier has no persona and low per-account WTP.
- Founder fit 5 (no security background); interest fit 5. Barrier MODERATE, mixed. Capital EUR 500-2k; time to first revenue 3-6 months.
- AI leverage high; commoditisation resistance 5; AGI 4; ASI 4. Defensibility 6; recurring 8; large-company potential 6.
- Overall: 56.1. Highest upside of the compliance ideas, weakest founder fit.

### 13. U-042 Belgian public-tender bid-ops pack
- One sentence: Productised bid-readiness (attests, erkenning eligibility, UEA pre-fill, financial-ratio proofs) for construction/services SMEs, riding on TenderWolf/BOSA feeds.
- Existing competitors: TenderWolf EUR 79-149/mo with AI Quickscan, Tender Experts (Tender Chat), GPC Gov, UK drafting tools GBP 15-EUR 99/mo (VERIFIED). Bid-ops layer: Evidence not found that anyone automates it.
- Why customers pay: 80% report barriers; 31% win rate vs 58% EU (VERIFIED); bid-ops WTP: Evidence not found.
- Founder fit 5; interest fit 5. Barrier LOW, BAD (incumbents adding AI). Capital EUR 0-500; time to first revenue 3-6 months. Defensibility 4.
- Overall: 54.6.

### 14. U-024 Reporting-pack tie-out agent
- Feature, not company: Endex ($14M, OpenAI-backed) ties schedules to source; Copilot Skills cover workbooks; linking add-ins prevent the problem for $200-360/user/yr (VERIFIED). Kept as a QA asset inside U-031. Overall: 53.7.

### 15. U-012 Vendor-neutral data/MCP/portability layer
- Positioning wedge only: connectors commoditised within 12 months (Peliqan EUR 150/mo, Chift EUR 2.3M, Apideck/CData/Zapier, OSS MCP servers for Yuki/Billit/Exact, VERIFIED). ITAA's "digital dependency" framing is real; an OSS portability/exceptions tool can earn visibility for U-002/U-011. Overall: 53.3.

### 16. U-092 Odoo Belgian-localisation setup/QA service
- Skills bridge: ~130 official BE partners, implementations EUR 5-30k (VERIFIED); Odoo ships l10n_be and Peppol natively. Useful to learn Odoo internals for U-021; not a business. Overall: 52.0.

### 17. U-022 ERP data-extraction / reporting layer
- Enabling asset: 8+ Exact-to-Power BI vendors incl. free Invantive, Peliqan $199/mo, 384-star OSS Odoo MCP (VERIFIED). Micro-gap: no popular OSS Exact Online MCP server. Overall: 51.9.

### 18. U-009 Client document-chasing agent for firms
- Gap closed: OkiOki (Xerius, EUR 8-11/mo, "follows up with your clients"), Dytto, Silverfin Assistant, Ravical (VERIFIED). Overall: 51.1.

### 19. U-072 Architect project profitability tool
- Real FP&A-shaped pain (1 in 5 consider quitting; fair rate EUR 65-95/h, VERIFIED) but B-abel and PlanMolder exist, NAV builds member tools, tiny WTP. Overall: 50.9.

### 20. U-044 Finance-grade VSME data via accountants
- Crowded and cheap: 10+ tools free to EUR 99/mo, VSME Ready EUR 199/yr, Eevery already runs an accountant channel (VERIFIED). Service layer for 2-3 firms at best. Overall: 50.7.

## Promoted to deep research (top ~8, with related items folded in)
- OPP-A = U-031 + U-021 (+ U-023, U-024, U-022, U-011 as assets/variants): AI-native fractional controlling with consolidation as wedge.
- OPP-B = U-002 + U-004 (+ U-012 as positioning): Peppol portfolio operations for accounting firms.
- OPP-C = U-064: QoE-light for small Belgian acquisitions.
- OPP-D = U-068: Brussels co-ownership renovation financing packs.
- OPP-E = U-046: DORA vendor pack.
- OPP-F = U-043: Supplier compliance passport.
- OPP-G = U-089: finance-automation ROI review (cash engine).
- OPP-H = U-042: tender bid-ops pack.

## Contradictions resolved at this stage
- U-021 "best founder fit" (universe) vs "software layer crowded" (CI): both true; ranked as service-led.
- U-024 "no competitor found" (stream D) vs Endex/Copilot (CI): CI wins; demoted to feature.
- U-040, U-045, U-047 "gaps" (streams B/C) vs official API / Easy Cyber Protection / CBAM tool features (CI): CI wins; rejected.
- U-009 "localisation gap" (universe) vs OkiOki (CI): CI wins; demoted.


## Status after deep research and red teams (2026-09-12)
- OPP-A (U-031 + U-021): rank 1 confirmed as a services-only steelman; product leg killed by Odoo 19/20 and cheap SaaS.
- OPP-B (U-002 + U-004): product killed (authority scanner, vendor views, Peliqan); reserve service wedge only.
- OPP-C (U-064): only with an ITAA/IBR signatory; natural second product once an ITAA relationship exists.
- OPP-D (U-068): demoted (primes gone, free channel occupied, calendar slipped).
- OPP-E (U-046) and OPP-F (U-043): see `top-5-deep-dives.md` and `final-recommendation.md`.
- U-011, U-023, U-024, U-022, U-012: folded into OPP-A as routes or delivery assets.
