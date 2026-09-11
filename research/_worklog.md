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
