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

## Phase 5 notes (deep research)
- OPP-D (U-068 co-ownership packs): WEAKENED. Renolution primes suspended Aug 2024 and not returning (replacement 0% loan scheme 2027, rules unpublished); ECORENO not open to ACPs; Bruxelles Environnement Facilitateur Copropriété and Federia Syndic Reno Support (430+ syndics, 120+ projects) occupy the free channel; CoBrACE PEB provisions pushed to Jul 2028 by 19 Feb 2026 order. Strengths: 42,388 Brussels apartment buildings, ACP co-liability for unit fines, financing is #1 brake. TAM ~EUR 1.3-2M/yr; EUR 100k/month unreachable. Decision: keep as niche, likely drops out of top 5 on upside.
- OPP-A (U-031+U-021): CONFIRMED with caveats. Odoo consolidation gap real (app removed v18, replacement deprecated in v19 docs, 5 forum threads Mar-May 2026). Demand: group controller avg EUR 64.9k, live vacancies, interim EUR 600-800/day, Big-4/top-10 sell consolidation as service. Population: ~5,500 groups (Statbel old basis), 30,552 holdings, 80,210 management companies, ~11-13k foreign-controlled firms (ESTIMATE). Price corridor EUR 1.5-4k/month between tools (EUR 400-900) and 2 controller days (EUR 1,200-1,600). WEAKNESSES: ITAA law reserves bookkeeping, closing, annual accounts AND "analysis by accounting techniques of situation/performance/risk" (criminal if illegal practice); Cassation 28 Nov 2022 allows non-member subcontracting under ITAA firm engagement; monthly management-consolidation WTP not evidenced (all outsourced prices are statutory/annual); close-week collision with founder's own job; Flemish-language segment; Odoo platform risk; AI tests: labour revenue AGI-destroyed. Ceiling solo ~EUR 200k/yr.
- CROSS-CUTTING: the ITAA reserved-activity finding also hits OPP-C (QoE = analysis of a target's performance) and U-011. Must be checked with ITAA/lawyer; subcontracting under an ITAA firm is the legal route.
- OPP-B (U-002+U-004): WEAKENED. Free bulk checkers exist (e-invoice.be Peppol Radar CSV, peppolcheck.be, Peppol Practical, Nymus, Finplex); Peppol Directory REST API free; portfolio-level status views exist in OkiOki, Billit accountant portal, Yuki; Peliqan Billit MCP already persists acknowledgements and pitches rejected-invoice agents at EUR 150/mo; Belgian PSP Forum saw ~1% problematic exchanges and expects improvement; 1.06M businesses (89%) registered; no fine enforcement evidence found. Practitioner pain is "where is my invoice"/workload, not rejection triage. Reserved activity: "checking and correcting bookkeeping documents" is ITAA-reserved; service must stay at identifier/transport layer. AI angle thin. 2028 e-reporting dataset only in early-2027 Royal Decree -> revenue gap. SAM EUR 1-5M/yr; solo SOM EUR 35-250k. Verdict: service wedge only, OEM/pivot plan needed.
- OPP-C (U-064): WEAKENED. ITAA law art. 3 reserves 4° verification/correction of accounting documents and 5° "analysis by accounting techniques of situation and functioning of enterprises (creditworthiness, profitability, risks)" -> core of QoE; ITAA prosecutes (Kortrijk Dec 2024: suspended prison + fine; end-2025 request to prosecutors). Competitors exist: Analyzediz (Flanders, small-deal DD), Syno M&A pre-audit, Bol Adviseurs "verkort boekenonderzoek" (NL, Apr 2026). Demand strong: ~20,000 businesses/yr facing succession, Wallonia Cheque-Transmission covers 75% of DD up to EUR 15k (labelled providers only, 3 yrs experience). SAM EUR 2.8-3.9M; solo SOM EUR 80-140k gross, EUR 50-90k after signatory share. Verdict: only co-branded with an ITAA/IBR signatory, or as tooling for advisers.
- Emerging pattern after wave 1: every pure-founder service in Belgian SME finance hits the ITAA reserved-activity wall or platform absorption; OPP-A survives best because management reporting/controlling for a group is arguably non-reserved and the buyer is not an accounting firm.

## Phase 6 notes (red team)
- RED OPP-B: FATAL for phase 1 (Belgian Peppol Authority + FPS Finance "Network Data Scanner" cut identifier error rate 2.41% -> 0.31% Dec 2025-Apr 2026 on 2.06M records; forum voted to globalise it) and FATAL for product moat (22 Peppol MCP repos; Peliqan/Chift sell cross-ledger layer; MLS v1.1.0 makes undelivered status visible in every AP). SERIOUS: no firm pays for Peppol audits; FPS FAQ assigns delivery investigation to software supplier; Wallonia = integrator-managed on-prem stacks; 2028 decree early 2027. Over-kill: KVABB Jan 2026 letter and FPS credit-note trail create documentation work; Luxembourg 2028 is a real FR-language second market. Steelman residual: FR-language fixed-fee "Peppol incident documentation and clean-up" engagement (EUR 1-2k) for on-prem fiduciaires; nothing survives as a product. Decision: OPP-B drops out of the top 3; keep as a reserve service wedge.
