# Research worklog

Date: 2026-09-11. Repo: jdch-s/idas, branch claude/amazing-darwin-udo71p.

## Environment constraints
- WebSearch available (returns titles, URLs, content summaries).
- WebFetch/curl blocked for all domains except github.com. Primary pages cannot be opened.
- Evidence labels used everywhere: VERIFIED FACT (search-summary) / ESTIMATE / INFERENCE / HYPOTHESIS / Evidence not found.

## Task graph
0 Setup -> 1 Discovery (5 parallel streams A-E) -> 2 Universe consolidation (>=100 -> 40)
-> 3 Competitive/existence check (4 batches) -> 4 Scoring v1 -> Top 20
-> 5 Deep research (top ~8, parallel) -> 6 Red team (parallel, independent)
-> 7 Rescore -> Top 5 -> 8 Final reviewer challenge -> decision -> 9 Deliverables, commit, push

## Decisions & contradictions log
- (Phase 0) Founder languages unknown; scoring assumes EN + working FR, NL flagged where material.
- (Phase 0) OpenAccountants MCP unusable (account wall); tax facts via search only.
- (Phase 0) Time budget assumed 10-15 h/week. Employer/sector unknown -> non-compete flagged as check item.

## Status
- [x] 0 Setup
- [ ] 1 Discovery streams A-E
- [ ] 2 Universe consolidation
- [ ] 3 Competitive intelligence
- [ ] 4 Scoring v1 / Top 20
- [ ] 5 Deep research
- [ ] 6 Red team
- [ ] 7 Top 5
- [ ] 8 Final review + decision
- [ ] 9 Deliverables committed and pushed

## Phase 1 notes
- Stream E: reddit.com blocked for search agents; 200-query budget per agent hit after 32 queries (budget appears per-agent, orchestrator search still works). Reddit-based pain evidence therefore thin; substitute HN/IH/review sites.
- Stream A: 44 queries, 30 opportunities. Strong signals: SME-group consolidation on Odoo/Exact/Yuki (A-09); accounting-firm capacity crunch (A-04/06); BE 2028 e-reporting (A-03); ITAA "digital dependency"/vendor concentration (A-16); Peppol clean-up (A-01); ERP data extraction (A-10); month-end close lower mid-market (A-07). Caveat: many hour/cost figures are vendor-blog sourced.
- Stream B: 40 queries, 32 opportunities. Key: regulation SOFTENED (CSRD >1,000 employees & >€450m; CSDDD 2029; AI Act high-risk deployer duties deferred to Dec 2027/Aug 2028; EUDR delayed to Dec 2026; GDPR omnibus RoPA exemption proposed <750 employees) -> avoid mandatory-CSRD, high-risk-AI-Act, EUDR tooling. Promising: multi-country e-invoicing/e-reporting control layer for small groups (B-26); BE 2028 dual-sided e-reporting reconciliation (B-02); DORA cascade onto small ICT vendors (B-09); CBAM as finance/provisioning problem (B-14); NIS2 evidence packs via MSP/accountant channel (B-07/08); 30bis withholding check at AP run (B-30, BE-specific small TAM). VSME value-chain cap binding (Jul 2026) -> supplier-side channel play, not standalone.
- Stream C: 36 queries, 30 opportunities. Key: accounting-firm capacity crunch again (C-24; 56% refuse clients, expert-comptable shortage profession in all 3 regions); 30bis subcontractor withholding check (C-01) confirms B-30; co-ownership energy-renovation capex/financing on syndics (C-12; >90,000 co-ownerships vs ~500-560 exclusive syndics C-11); SME access to public procurement (C-26; thresholds raised to €75k); pharmacy pricing after APB dropped suggested prices (C-10); micro-contractor cash-flow (C-02). Surprises: Flanders kmo-portefeuille advice now cybersecurity-only; energy sharing dead (fee structure); CBAM not an SME market (50t threshold exempts ~90%). Contradiction to resolve: stream B ranked CBAM finance angle #4, stream C says CBAM SME market is tiny -> resolve in phase 2 (likely downgrade to mid-market importers only).
