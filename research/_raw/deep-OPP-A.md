# Deep-dive OPP-A: AI-native fractional controlling for Belgian SME groups and foreign-owned subsidiaries (consolidation + HQ reporting as the wedge)

Date: 2026-09-11. Method: 43 WebSearch queries (EN/NL/FR) on top of the universe rows U-021, U-031, U-023, U-024, U-022, U-011, the CI batches 1-2, stream items A-09, A-11, D-13, D-16, E-03 and belgium-founder-facts.md. Pages could not be opened; every "VERIFIED" below means VERIFIED (search-summary). Labels: VERIFIED (search-summary) / ESTIMATE / INFERENCE / HYPOTHESIS / "Evidence not found" (ENF). Figures never invented; where a search summary looked internally inconsistent it is flagged.

Founder frame applied throughout: Brussels, full-time employed, 10-15 h/week, limited capital, MSc corporate finance, controlling/FP&A/reporting background, learning Python/SQL/agents, EN + working FR, NL flagged where it matters.

---

## 1. Exact problem and exact customer

### 1.1 The problem, stated precisely
Two customer groups share one monthly job that nobody inside them owns well:

(a) **Belgian SME groups (3-15 legal entities)**: a holding/management company on top of 2-14 operating companies, each with its own ledger (Odoo, Exact Online, Yuki, sometimes WinBooks/Horus at the accountant), often with different charts of accounts, intercompany loans/management fees/recharges that do not reconcile, and a bank, a board, a family council or a buyer asking for group numbers every month or quarter. They are legally exempt from statutory consolidation (a "group of limited scope" does not exceed more than one of: EUR 42.5M turnover, EUR 21.25M balance sheet, 250 FTE on a consolidated basis, for financial years from 1 Jan 2024 — VERIFIED, https://vanhavermaet.be/artikels/vennootschappen-in-groep/ ; https://insights.hlb.be/nl/actua/belgi%C3%AB-volgt-europa-nieuwe-groottecriteria-voor-ondernemingen-vanaf-2024). Consequence: they never bought a consolidation tool and never hired a consolidation specialist; the work is done in Excel by the CFO/owner, by an overloaded financial controller, or by the external accountant once a year (A-09, E-03, U-021). Note that the 2024 uplift of the exemption thresholds *enlarged* the population that is exempt — i.e. the population that does management-only consolidation without tooling.

(b) **Belgian (and Luxembourg) subsidiaries of foreign groups**: a local finance manager or a 1-3 person team must deliver a monthly reporting package in the HQ's format (group chart of accounts, IFRS/US-GAAP/HQ-GAAP adjustments on top of Belgian GAAP, intercompany confirmations, variance commentary vs budget/forecast, headcount and KPI schedules) on HQ's close calendar (typically WD3-WD5), from a local ledger (Odoo/Exact/Yuki, or a Belgian instance of the group ERP). Search surfaced Belgian finance-manager vacancies describing exactly "delivering structured reporting and financial insights to local management and HQ" (VERIFIED, https://www.glassdoor.com/Job/belgium-finance-manager-jobs-SRCH_IL.0,7_IN25_KO8,23.htm). The pain is peaks (close week), staff turnover in a 1-3 person team, and the mismatch between what the local accountant produces (statutory, annual) and what HQ wants (management, monthly).

The thesis is a **service-first** business: monthly group consolidation, intercompany clean-up, HQ-format packs and variance commentary, delivered by the founder with his own agent tooling (ledger connectors, LLM chart-of-accounts mapping, IC matching, pack QA), evolving into an Odoo/Exact-native product.

### 1.2 Exact customer
| | Segment (a) Belgian SME group | Segment (b) foreign-owned subsidiary |
|---|---|---|
| Size | 3-15 entities; group revenue EUR 5-60M (below the EUR 42.5M consolidated-turnover exemption for most; the EUR 42.5-60M band is where statutory consolidation kicks in and the accountant/auditor takes over) — ESTIMATE | 20-250 FTE locally; local revenue EUR 5-100M — ESTIMATE |
| Systems | Odoo (Belgian-heavy installed base; Odoo is a Belgian company), Exact Online ("most complete for larger SMEs, with intercompany functions" — VERIFIED, https://www.boekhoudvergelijker.be/vergelijkingen/beste-boekhoudsoftware-belgie/), Yuki (136,000+ Belgian companies — VERIFIED, https://leadservice.be/top-11-boekhoudsoftware-gebruikt-door-belgische-boekhouders/), WinBooks/Horus at the accountant | Local Odoo/Exact/Yuki, or a satellite of the group ERP (SAP/D365/NetSuite); HQ consolidation tool (Lucanet, Tagetik, OneStream, HFM) upstream |
| Who signs | Owner-CEO or family CFO of the holding; sometimes the external accountant recommends | Local Managing Director or local Finance Manager; budget often needs HQ CFO/Group Controller nod |
| Who uses | CFO/controller of the holding, the bank, the board | Local finance manager (day-to-day), HQ group controller (receives the pack) |
| Trigger events | Bank covenant reporting, new acquisition/entity, family-office professionalisation, preparing a sale, controller resignation, Odoo migration (18/19 removed the consolidation app) | Finance manager leaves/maternity leave, HQ changes reporting tool/format, audit findings on IC, new HQ close calendar, ERP migration |
| Budget line | "External accountant / advisory" or "interim" | "Interim finance" / "professional fees" |

### 1.3 What is delivered monthly (the offer)
1. Ledger pull from each entity (API/MCP, or trial-balance export where no API).
2. Mapping to a group chart of accounts (LLM-proposed, human-approved, versioned).
3. Intercompany matching and reconciliation; proposed elimination entries; open-item list to the entities.
4. Consolidated P&L, balance sheet, cash-flow (management basis; BE GAAP or HQ GAAP adjustments as agreed).
5. Reporting pack in the client's/HQ's format (Excel/PowerPoint/Google Sheets/HQ upload template) with variance commentary vs budget/prior period.
6. Pack QA: tie-out between pack, workbook and ledgers (the U-024 asset).
7. A 30-60 minute review call; ad-hoc questions during the month within a fair-use cap.

---

## 2. Evidence of demand

### 2.1 Belgian job postings for group controllers / consolidation
- StepStone.be shows ~1,636 vacancies matching "Group Controller" in Belgium (broad keyword match; not all are group-consolidation roles) and an average Group Controller salary of EUR 64,900 (range EUR 55,300-75,400) — VERIFIED (search-summary), https://www.stepstone.be/salaris/Groeps-controller.html
- Glassdoor: 15 "group financial controller" jobs in Brussels (Sept 2026) and 372 "finance manager" jobs in Belgium (Apr 2026) — VERIFIED, https://www.glassdoor.com/Job/brussels-group-financial-controller-jobs-SRCH_IL.0,8_IC2302160_KO9,35.htm ; https://www.glassdoor.com/Job/belgium-finance-manager-jobs-SRCH_IL.0,7_IN25_KO8,23.htm
- A "Financial Controller (Consolidation)" vacancy in Deerlijk (West Flanders family group) at EUR 2,500-4,500 gross/month — VERIFIED, https://ctrl-f.be/en/vacancy/financial-controller-consolidation-a1wp800000ao5gtmaz/ ; the same Waregem/Deerlijk cluster appeared in A-09 via Michael Page (https://jobs.accaglobal.com/job/13914949/financial-controller-and-consolidatie-waregem-/?TrackID=9). Azuro: "Group Controller — rapportering en consolidatie" (https://azuro.be/en/).
- Robert Half (NL page — Netherlands, not Belgium, flagged): Group/Concern Controller EUR 6,500-9,500+ gross/month — VERIFIED for NL, https://www.roberthalf.com/nl/nl/baan-details/group-controller
- FR: "contrôleur de gestion" average EUR 3,765/month; 2,500-3,800 junior, 4,000-6,000 with 3-6 years — VERIFIED, https://fr.glassdoor.be/Salaires/controleur-de-gestion-salaire-SRCH_KO0,21.htm ; https://www.robertwalters.be/fr/eclairages/conseils-carriere/blog/combien-gagnez-vous-en-tant-que-controleur.html ; FED Finance grid https://www.fed-group.be/fed-finance/recruter-finance/grille-salaire-finance-comptabilite
- Total employer cost of one Belgian group controller at EUR 65k gross ≈ EUR 90-100k/yr incl. ~30% employer social charges, car, bonus (ESTIMATE from the StepStone figure). This is the number a 3-15-entity group compares against.

Reading: the hiring signal is real and recurring, but the posts are for permanent, full-time people at mid-size groups (the Deerlijk range EUR 2,500-4,500/month suggests a junior/medior profile — i.e. SME groups try to solve consolidation with one cheap hire). The service must be positioned against "one medior hire we cannot find" (shortage: controllers listed as a shortage profession, C-24), not against a Big-4 engagement.

### 2.2 Interim / freelance controller rates (what the alternative costs)
- Financial controller EUR 75-100/h or EUR 600-800/day; interim CFO EUR 120-175/h or EUR 900-1,400/day; Dosign ruling (1 Jan 2026) pushes interim rates up — VERIFIED, https://www.apexleague.be/insights/hoe-bepaal-je-jouw-freelance-finance-tarief-in-belgie ; https://www.apexleague.be/insights/interim-cfo-uurtarief-in-belgie ; https://www.apexleague.be/insights/tarieven-en-kosten-van-een-finance-consultant-in-belgie
- Belgian fractional executives on 2-3 days/week: monthly retainers EUR 2,600-8,000 — VERIFIED (aggregator, fractional-csuite), https://fractional-csuite.com/tools/rates/
- US benchmark (context only): fractional controller USD 100-225/h, retainers USD 3,000-10,000/month — VERIFIED, https://www.ridgewayfs.com/controller-compensation-saas-fintech-crypto/
- UK (expansion context): fractional FD GBP 600-1,200/day; SME engagements GBP 850-1,300/day; 1-4 days/month retainers GBP 1,500-5,000 — VERIFIED, https://leadership-services.co.uk/rate-report-2026/ ; https://lanop.co.uk/part-time-finance-director-uk-guide/

### 2.3 "Consolidation as a service" offers in Belgium
- PwC Belgium CaaS for SMEs (from CI batch 2), https://www.pwc.be/en/services/small-medium-or-family-business-for-the-future/sme-accounting-and-advice/CAAS.html — price ENF.
- EY FAAS managed services and KPMG managed services sell outsourced consolidation/reporting to subsidiaries and groups (CI batch 2) — price ENF.
- Vandelanotte (top-10 Belgian firm, 580 staff, 17 offices, large SME segment) markets a consolidation team incl. GAAP conversions and international consolidation — VERIFIED, https://www.vandelanotte.be/en/our-offer/consolidation
- VGD (mid-tier firm) blog "Consolidatie: cruciaal voor de kracht van je groep" — consolidation marketed to SME groups as a service — VERIFIED, https://vgd.eu/blog/consolidatie-cruciaal-voor-de-kracht-van-je-groep
- No Belgian boutique offering "monthly management consolidation as a subscription" surfaced (NL: Easyclose "built by a controller"; FR: MELVAN, Primexis, BM&A sell outsourced consolidation to mid-size groups; LU: Fiducia Management sells "consolidation comptable" at fixed fees) — VERIFIED that these exist, https://easyclose.nl/beste-consolidatiesoftware ; https://www.melvan.fr/consolidation-et-reporting-financier/externalisation-de-la-consolidation/ ; https://bma-groupe.com/conseil-et-supports-operationnels/externalisation-de-consolidation-chez-les-groupes-de-taille-moyenne/ ; https://www.fiduciamanagement.lu/services/consolidation-comptable/
- BM&A's framing is the demand thesis in one sentence: consolidation is "ponctuelle dans l'année", so the "coût significatif d'un consolideur est difficile à optimiser pour un groupe de petite ou moyenne taille" — VERIFIED (FR source), same URL. Caveat: that is about *statutory* annual consolidation; the monthly *management* version is the founder's bet and is less evidenced.

### 2.4 Odoo consolidation gap 2025-2026
- The Consolidation app was removed in Odoo 18 and replaced by "shared accounts"; the Odoo 19 documentation lists shared accounts as deprecated and moves to a multi-ledger + account-mapping approach; in 18 subsidiaries had to share the same account list (same account ID), which users called "very rigid" — VERIFIED, https://www.odoo.com/forum/help-1/why-was-the-consolidation-module-removed-in-odoo-18-267924 ; https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/consolidation.html
- Live 2026 forum threads: "Does Odoo 19 still support Elimination Entities?" (https://www.odoo.com/forum/help-1/does-odoo-19-still-support-elimination-entities-to-consolidate-financial-data-in-a-group-of-companies-298432), "How does Odoo support inter company eliminations in Europe?" (https://www.odoo.com/forum/help-1/how-does-odoo-support-inter-company-eliminations-in-europe-299551), "How comprehensive are Odoo's multi-company consolidation capabilities?" (https://www.odoo.com/forum/help-1/consolidation-in-odoo-303609), "Consolidation set up" (https://www.odoo.com/forum/help-1/consolidation-set-up-300474), "[Odoo 19] Consolidation for multi-currency and multi companies" (https://www.odoo.com/forum/help-1/odoo-19accounting-consolidation-for-multi-currency-and-multi-companies-300195) — VERIFIED, dated Mar-May 2026.
- Odoo 19.2 release notes: "journals are now included instead of excluded in multi-ledger consolidation" — Odoo is iterating on consolidation inside the core (VERIFIED, https://www.odoo.com/odoo-19-2-release-notes). Platform risk: Odoo may close the gap in 19.x/20 (see section 16).
- Conflict flagged: an Odoo partner blog (ECOSIRE) claims "Odoo 19 Enterprise includes a Consolidation module ... automates most eliminations if intercompany accounts are consistently coded" (https://ecosire.com/blog/odoo-multi-company-setup-guide). This contradicts the official docs and forum; treat as partner marketing. Working position: Odoo 19 offers *aggregation with manual adjustment journals via multi-ledger*, not a consolidation engine with IC detection/elimination.

### 2.5 Belgian holding / group statistics
- Statbel/Federal Planning Bureau enterprise-group database: ~5,500 groups active in Belgium controlling >15,000 Belgian subsidiary companies; ~2,100 domestic groups, ~1,800 Belgian-controlled multinational groups, ~1,600 foreign-controlled multinational groups — VERIFIED (search-summary), but the FPB report analyses 2015 data (published 2022); Statbel says coverage grew ~10% 2020-2023 and 2023 is the latest complete year, https://statbelpr.belgium.be/nl/themas/datalab/multinationale-groepen-belgie ; https://www.plan.be/publications/publication-2249-nl-multinationale_groepen_in_belgie_structuur_en_economische_activiteit ; https://statbel.fgov.be/nl/themas/datalab/multinationale-groepen-belgie
  Caveat: this database is built from the European Group Register and likely under-counts small purely domestic holding structures (INFERENCE) — 2,100 domestic groups is far below what the holding counts below suggest.
- Holdings: 30,552 "holdings" in Belgium (KBO/Statbel-derived commercial database, 2026) — VERIFIED (search-summary, commercial source), https://companydata.com/nl/bedrijven/belgie/holdings-belgie/
- Management companies: 80,210 Belgians hold a management company in 2024, up from 41,510 in 2019 (Statbel via KennisWest) — VERIFIED, https://www.kenniswest.be/artikel/al-meer-dan-80000-belgen-hebben-managementvennootschap-blijkt-uit-cijfers-van-de-statistiekdienst-statbel/253258 . Most are single-person vehicles, not groups (INFERENCE), but the doubling shows Belgian structuring appetite.
- Enterprise size classes: 27,754 enterprises with 10-49 employees and 4,221 with 50-249 (Statbel-derived; year not labelled in the summary) — VERIFIED (search-summary), https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?view=e4bcf725-1708-4bb2-aa27-df1c69b010bb ; https://economie.fgov.be/nl/themas/ondernemingen/kmos-en-zelfstandigen-cijfers/statistieken-over-kmos-belgie/kmos-grootteklasse
- Number of companies filing consolidated accounts at the NBB: ENF (the NBB "in figures" page tracks filings incl. consolidated accounts; ~500,000 sets of annual accounts filed per year in total) — https://www.nbb.be/en/central-balance-sheet-office/about-central-balance-sheet-office/central-balance-sheet-office-figur-0 . Relevant because the *target* segment is the exempt one, so a low statutory count would not weaken the thesis.

### 2.6 Foreign-owned subsidiaries in Belgium
- Flanders: 7,288 enterprises under foreign control (2023 data, 2025 publication; earlier figure 6,554), <1% of Flemish enterprises, EUR 72.7bn gross value added, ~460,000 jobs, 30% of private-sector wage employment; 56.9% have an EU-27 parent — VERIFIED, https://www.ewi-vlaanderen.be/nieuws/buitenlands-zeggenschap-vlaanderen-anno-2023 ; https://www.ecoom.be/downloads/publications/790 ; https://publicaties.vlaanderen.be/view-file/57006
- Belgium total: Eurostat inward-FATS summary reported Belgium's foreign-controlled share of enterprises as "0.1%" / "<1%" — the 0.1% looks like a summary error (Flanders alone reports 7,288 firms) and is NOT used; https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Foreign-controlled_enterprises_statistics_-_inward_FATS . ESTIMATE: Belgium ≈ 11,000-13,000 foreign-controlled enterprises (Flanders 7,288 scaled by Flanders' ~58-60% share of the Belgian economy; Brussels has a high density of regional HQs which may push this up). Statbel's 1,600 foreign-controlled *groups* (2015 basis) is consistent with ~10-15k legal entities.
- Luxembourg: >168,000 legal entities on the RCS (Dec 2025), disproportionately funds, SOPARFIs and SPVs; no clean count of active operating subsidiaries or SOPARFIs found — VERIFIED / ENF, https://kyckr.com/guides-and-reports/luxembourg-registry-guide-2025 ; https://zephira.ai/luxembourg-company-registry-data-how-to-search-the-rcs-2026/ . Luxembourg consolidation exemption: EUR 25M balance sheet / EUR 50M turnover / 250 FTE (Grand-Ducal regulation 25 Oct 2024, applicable from FY2023) — VERIFIED, https://www.cssf.lu/en/2023/02/qa-cnc-22-028-regarding-the-implementation-of-the-consolidation-exemption-for-small-groups-article-1711-4-lsc/ ; https://www.dsm.legal/en/the-new-framework-for-size-criteria-of-companies-and-groups/ . Luxembourg fiduciary fees: holding/patrimonial structures EUR 5,000-20,000/yr for simple structures; mid-size SME EUR 8,000-25,000/yr all-in; group consolidation billed separately at a pre-agreed fee — VERIFIED, https://ilicompta.lu/guides/cout-expert-comptable-luxembourg ; https://www.financialservices.lu/en/accounting-pricing-luxembourg ; https://www.fiduciamanagement.lu/services/consolidation-comptable/ . Luxembourg SOPARFI reporting needs are dominated by domiciliation agents/fiduciaries (a licensed, regulated market: expert-comptable OEC and PSF-domiciliation rules) — INFERENCE; the founder's entry there is as a subcontractor to a fiduciary or as HQ-pack producer for an operating subsidiary, not as a domiciliation provider.

### 2.7 Demand verdict
Recurring, evidenced pain (Odoo gap live in 2026; hiring signal; interim rates rising; firms and Big-4 selling the service). What is NOT evidenced: any Belgian SME group publicly saying "we pay X per month for outsourced monthly consolidation". Willingness to pay for *monthly management* consolidation (vs annual statutory) remains a HYPOTHESIS to test in interviews (section 17).

---

## 3. Willingness to pay

| Reference price | Amount | Label | Source |
|---|---|---|---|
| Freelance financial controller | EUR 600-800/day (EUR 75-100/h) | VERIFIED | https://www.apexleague.be/insights/hoe-bepaal-je-jouw-freelance-finance-tarief-in-belgie |
| Interim CFO | EUR 900-1,400/day | VERIFIED | https://www.apexleague.be/insights/interim-cfo-uurtarief-in-belgie |
| **A 2-day/month controller** | **EUR 1,200-1,600/month** (2 x 600-800), EUR 14-19k/yr; a 2-day/week controller EUR 5-7k/month | INFERENCE from verified day rates | as above |
| Belgian fractional exec retainers (2-3 d/week) | EUR 2,600-8,000/month | VERIFIED (aggregator) | https://fractional-csuite.com/tools/rates/ |
| Employed group controller (BE) | EUR 64,900 gross avg → ~EUR 90-100k employer cost | VERIFIED salary / ESTIMATE cost | https://www.stepstone.be/salaris/Groeps-controller.html |
| Easyclose (NL, close+consolidation, 10 entities) | EUR 705/month, ~EUR 905 with add-ons | VERIFIED | https://easyclose.nl/beste-consolidatiesoftware |
| Finstack | from EUR 39/month per entity (10 entities ≈ EUR 390/month before add-ons) | VERIFIED | https://finstack.io/pricing-single-entity ; https://finstack.io/solutions/financial-consolidation |
| Speedbooks Ultimate (NL) | EUR 69/month for 10 administrations incl. consolidation | VERIFIED | https://www.speedbooks.nl/tarieven |
| Syft Analytics | USD 39-79/entity/month; USD 399/month unlimited | VERIFIED | https://claryx.ai/blog/syft-analytics-review/ |
| Lucanet | ~USD 1,200/user/yr; implementation from ~USD 5k (third-party) | VERIFIED (third-party) | https://www.itqlick.com/lucanet-consolidation-planning-and-reporting/pricing |
| EMAsphere | "Standard 0 EUR/month", Pro/Enterprise/Premium custom; BNP Paribas distributes an annual-subscription version | VERIFIED (Capterra/BNP listing) | https://www.capterra.com/p/156656/EMAsphere/ ; https://banqueentreprise.bnpparibas/post/gestion-au-quotidien/offre/reporting-pilotez-votre-entreprise-avec-emasphere-cl96wfxg900be012i48te08jx |
| BrightAnalytics (Gits, BE) | quote only (demo) | VERIFIED | https://www.capterra.com/p/218509/BrightAnalytics/ |
| Silverfin consolidation | per-file annual pricing, minimum file count, quote only | VERIFIED | https://silverfin.com/en-gb/silverfin-pricing/ |
| Peliqan (connectors + MCP, BE) | from ~USD 199/month | VERIFIED (CI batch 2) | https://peliqan.io/ |
| PwC/EY/KPMG Belgium CaaS / managed services | ENF | — | https://www.pwc.be/en/services/small-medium-or-family-business-for-the-future/sme-accounting-and-advice/CAAS.html |
| French outsourced accounting (context) | EUR 900-1,800/month median for a PME; up to EUR 3,500+/month for 150+ FTE | VERIFIED (FR) | https://www.iteradvisors.com/ressources/blog/cout-externalisation-comptable-2026 |
| Luxembourg fiduciary, holding structure | EUR 5,000-20,000/yr; consolidation extra | VERIFIED | https://ilicompta.lu/guides/cout-expert-comptable-luxembourg |
| Microsoft Copilot for Finance | ~GBP 360/user/yr on top of M365 | VERIFIED (CI batch 2) | https://learn.microsoft.com/en-us/copilot/release-plan/2026wave1/finance-agents/ |

Pricing corridor that follows (INFERENCE): the software floor is EUR 400-900/month (Finstack/Easyclose) *plus the client's own labour*; the labour alternative is EUR 1,200-1,600/month for two controller days; the employed alternative is EUR 7.5-8.5k/month. A done-for-you monthly consolidation + pack at **EUR 1,500-3,500/month** (segment a) and **EUR 2,000-4,000/month** (segment b, HQ-format packs with commentary) sits below "hire" and below "two interim days", and above the tool floor. Big-4 CaaS is quote-only; INFERENCE that it starts well above EUR 5k/month given Big-4 rate cards.

---

## 4. Bottom-up TAM / SAM / SOM

All inputs labelled. Annual contract value (ACV) assumptions: segment (a) EUR 24k (EUR 2k/month), segment (b) EUR 30k (EUR 2.5k/month) — ESTIMATE anchored on section 3.

### Belgium
| Step | Segment (a) SME groups | Segment (b) foreign-owned subsidiaries |
|---|---|---|
| Population | 5,500 groups in EGR-based database (VERIFIED, 2015 basis) + domestic holding structures not in EGR; 30,552 "holdings" (VERIFIED, commercial); working figure **6,000-10,000 Belgian groups with ≥3 entities** — ESTIMATE | **11,000-13,000 foreign-controlled enterprises** (ESTIMATE from Flanders 7,288 VERIFIED) |
| Relevant size | 3-15 entities and revenue EUR 5-60M: ~50% → **3,000-5,000** — HYPOTHESIS | 20-250 FTE, lean local finance, HQ pack required: ~30% → **3,300-3,900** — HYPOTHESIS |
| TAM (spend addressable) | 4,000 x EUR 24k = **EUR ~96M/yr** — ESTIMATE | 3,600 x EUR 30k = **EUR ~108M/yr** — ESTIMATE |
| SAM (Odoo/Exact/Yuki or trial-balance-accessible; no full-time group controller; buys external help; reachable in FR/EN or English-working Flemish) | ~35% of TAM population → ~1,400 groups → **EUR ~34M/yr** — ESTIMATE | ~25% → ~900 subsidiaries → **EUR ~27M/yr** — ESTIMATE |
| SOM (solo, part-time, 3 years) | 6-10 clients | 4-8 clients |
| SOM revenue | **EUR 250-450k/yr combined at 10-18 clients** — ESTIMATE; capped by founder hours (section 12), not by market |

### Benelux
- Netherlands: larger economy, more groups, but the tool layer is the most crowded in Europe (Speedbooks EUR 69, Finstack EUR 39/entity, Liquid, Easyclose, Visionplanner, Exact Consolidatie) and Dutch-language delivery is expected — INFERENCE; NL TAM (a)+(b) ≈ 1.5-2x Belgium → EUR ~300-400M (ESTIMATE); SAM for this founder small unless a Dutch-speaking partner joins.
- Luxembourg: ~168k RCS entities (VERIFIED) but dominated by funds/SPVs served by regulated fiduciaries; operating subsidiaries needing HQ packs number in the low thousands (HYPOTHESIS); TAM (b) EUR ~30-60M (ESTIMATE); accessible via Brussels proximity and French.
- Benelux TAM ≈ EUR 550-650M/yr (ESTIMATE); SAM for this founder ≈ EUR 80-100M (ESTIMATE).

### EU (NL, FR, DE, LU, UK)
- EU foreign-controlled enterprises and SME groups are ~10-15x Belgium (INFERENCE from GDP share); EU TAM order of magnitude EUR 2-3bn/yr for outsourced group/HQ reporting for small groups — ESTIMATE; irrelevant for a solo founder's decision, relevant only for the product phase (section 15).

### Sanity check
The market is far bigger than the founder's capacity. The decision does not hinge on TAM; it hinges on (i) whether monthly management consolidation is a budgeted recurring purchase for small groups (unproven), (ii) regulatory scope (section 7), (iii) hours.

---

## 5. Competitive landscape

| Category | Player | What they sell | Strengths | Weaknesses vs this thesis | Positioning relative to founder |
|---|---|---|---|---|---|
| Direct service (BE) | PwC Belgium CaaS; EY FAAS managed services; KPMG managed services | Outsourced consolidation/reporting, full or partial | Brand, liability cover, IFRS depth, HQ trust | People-priced; quote-only; INFERENCE >EUR 5k/month; not Odoo-native | Founder undercuts on price and speed for <EUR 60M groups; loses on brand |
| Direct service (BE firms) | Vandelanotte, VGD, Crowe, BDO/Moore-type mid-tier | Statutory consolidation, GAAP conversion | ITAA-licensed, existing client relationship | Annual/statutory mindset; capacity crunch (56% of firms refuse clients, C-24); monthly management packs not their product | Partner/referral source, not just competitor |
| Direct service (NL/FR/LU) | Easyclose (NL, "built by a controller"), MELVAN/Primexis/BM&A (FR), Fiducia Management (LU) | Outsourced consolidation | Prove the service model exists and prices | Not in Belgium; not Odoo-native; FR ones target mid-size statutory | Template for the offer; possible LU partner |
| Interim/fractional supply | Apex League, Michael Page, Robert Half, HeadFirst, Finvision, FinForces, Flow Partners | Day-rate controllers/CFOs | Abundant, trusted model | EUR 600-1,400/day; rates rising (Dosign); no tooling leverage; person-bound | Founder's price anchor and the incumbent "solution" |
| SME consolidation software (cheap) | Finstack (EUR 39/entity), Speedbooks (EUR 69), Liquid, Easyclose SaaS, Syft (USD 399), Fathom (GBP 175/10 cos) | Self-serve consolidation/reporting | Cheap, fast, IC detection built in | Client still needs a person to run it; Exact/Twinfield/AFAS/Xero-first; Belgian GAAP and Odoo coverage thin | Founder can *use* one as delivery tooling (buy vs build, section 10) |
| Belgian mid-market reporting | BrightAnalytics (Gits), EMAsphere (Mont-Saint-Guibert), Bizzcontrol | Management reporting + consolidation, IC eliminations, Odoo/Exact connectors | Belgian, Odoo connector, firm channel, BNP distribution (EMAsphere) | Quote-based; software not service; implementation still needs a controller | Could be partner (founder as implementation/operations partner) or competitor in product phase |
| Enterprise CPM | Lucanet, Prophix/Sigma Conso (Brussels heritage), CCH Tagetik, OneStream, Talentia | Statutory + management consolidation | Full-featured, audited | >EUR 50M groups; consultant-dependent (E-03) | Irrelevant below EUR 60M; HQ tools in segment (b) define the *format* the founder must feed |
| Firm platforms | Silverfin (Visma), Exact Consolidatie | Consolidated files with IC eliminations for firms / Exact groups | Owned channel (90% of Flemish accountants use Silverfin per one claim, https://www.b2btax.be/digitale-boekhoudsoftware-kmo/) | Per-file, firm-only, annual cadence; Exact-only | Not accessible to founder directly; reinforce "accountant does year-end, founder does monthly" split |
| Platform owner | Odoo (multi-ledger consolidation, 19.x iterating; AI agents in 19) | Aggregation in core | Free to Odoo Enterprise users; Belgian vendor | No IC detection/eliminations engine; docs/forum confusion | Biggest product-phase risk; service-phase tailwind |
| Horizontal AI | Microsoft Copilot Finance Agents (reconciliation, variance analysis, Excel Skills) | Variance/reconciliation inside Excel | Bundled, GA 2026 | Native to D365/SAP, not Odoo/Exact/Yuki; needs a human who knows the numbers | Commoditises the commentary *tool*, not the accountable service |
| AI-native services (adjacent) | Neno (NL, EUR 6.6M, Belgium H2 2027), Skalar (DE), Ravical (Ghent, firms), LAC/Balance (YC) | AI-native bookkeeping/tax; agents for firms | Capital, engineering | Bookkeeping/tax layer, not group controlling; not yet in BE | Prove investors fund "agent-first services"; could move up-stack later |
| Data/connectors | Peliqan (BE, USD 199/month, MCP), Chift (BE unified API: Odoo/Exact/Yuki, 50+ connectors; pricing ENF), CData, Odoo App Store MCP modules, OSS ivnvxd/mcp-server-odoo (384 stars) | Ledger access | Commoditised, cheap | Not a business | Founder buys/uses; does not compete |
| Manual substitutes | Excel by CFO/owner; the external accountant once a year; the local finance manager's overtime | Status quo | Free (visibly), familiar | Errors, no IC discipline, key-person risk, late | The real competitor for segment (a) |
| Open source | none usable for consolidation (GitHub: 4 zero-star repos, CI batch 2) | — | — | — | No OSS threat; small OSS opportunity (Belgian-GAAP mapping library) |

**Where this founder enters**: the empty cell is "monthly, done-for-you, Odoo/Exact/Yuki-native management consolidation + HQ pack for sub-EUR-60M groups and subsidiaries, at EUR 1.5-4k/month, delivered by an ex-corporate controller with agent tooling". Nobody in Belgium surfaced in that cell. The nearest are Easyclose (NL, software+method), Big-4 CaaS (too expensive) and interim controllers (person-priced).

---

## 6. Why now; why incumbents have not solved it; why customers would switch

**Why now**
1. Ledger access became cheap: Odoo App Store MCP servers for 19.0 (https://apps.odoo.com/apps/modules/19.0/ai_mcp_server ; https://apps.odoo.com/apps/modules/19.0/mcp_server_odoo), OSS Odoo MCP (https://github.com/ivnvxd/mcp-server-odoo), Peliqan MCP incl. an open-source Exact Online connector (https://peliqan.io/blog/mcp-rate-limits-guide/), Chift unified API (https://www.chift.eu/) — VERIFIED.
2. LLM chart-of-accounts mapping is now studied and works: "Exploring the efficiency of GPT models in automating trial balance mapping" (Soft Computing, 2025/26, https://link.springer.com/article/10.1007/s00500-025-10983-4); accounting-reasoning benchmarks show strong but imperfect performance (https://arxiv.org/html/2512.22443v2 ; https://www.dualentry.com/accounting-ai-benchmark) — VERIFIED that the literature exists; accuracy figures ENF in summaries. This removes the setup cost that made consolidation tools consultant-dependent (E-03).
3. Odoo removed its consolidation app (18) and deprecated the replacement (19) — a live, dated gap with 2026 forum traffic (section 2.4).
4. Interim rates are under upward pressure (Dosign 2026), controllers are a shortage profession, firms refuse clients — the labour alternative gets dearer and scarcer (VERIFIED, sections 2-3).
5. Capital is flowing to agent-first finance services (Neno EUR 6.6M Aug 2026, Skalar EUR 12M, Ravical EUR 7.3M) — the model is being validated one layer below (VERIFIED, CI batches 1-2).
6. 2024 threshold uplift widened the statutory-exempt population that still needs group numbers for banks/boards (VERIFIED thresholds; INFERENCE on effect).

**Why incumbents have not solved it**
- Software vendors sell tools and assume a controller exists on the client side; the SME group's problem is that the controller does not exist (or is the owner).
- Accounting firms are capacity-constrained and organised around the annual statutory cycle; monthly management consolidation is low-margin for them without tooling and sits outside their engagement-letter habits (INFERENCE from C-24 and firm positioning).
- Big-4 are people-priced; compressing price would cannibalise their staff-hour model.
- Interim agencies sell days; an agent-leveraged fixed fee would break their revenue model.
- Odoo prioritises breadth; consolidation for small groups is a niche for them (INFERENCE from removal/deprecation cycle).

**Why customers would switch**
- Segment (a): from "owner's Excel / accountant once a year" to a monthly pack for less than two controller days — the trigger is usually a bank, a board, a buyer or a new entity; without a trigger they do not switch (HYPOTHESIS; must test).
- Segment (b): from "local finance manager overtime + interim in peaks" to a fixed-fee pack on HQ's calendar with IC pre-reconciled — switch triggers are turnover, HQ tool/format change, audit findings (INFERENCE from vacancy texts).
- Objections to expect: "our accountant does this", "HQ will not let an outsider into the ERP", "we need someone on-site", "what if you are hit by a bus", "who is liable" (section 13).

---

## 7. Barrier-to-entry analysis

### 7.1 Capital
Bracket **EUR 500-2,000** to start (service phase): sole-proprietor registration ~EUR 109 + VAT activation EUR 60-80 (belgium-founder-facts.md), professional liability insurance from ~EUR 270/yr for consultants (VERIFIED, https://www.verzekeringen.be/ondernemen/beroepsaansprakelijkheidsverzekering-consultant ; https://hellosafe.be/nl/beroepsaansprakelijkheidsverzekering), LLM API budget EUR 50-200/month, one connector subscription (Peliqan ~USD 199/month, optional), a Finstack/Easyclose-type tool as delivery aid EUR 40-400/month (optional), domain/M365. Product phase later: EUR 5-20k+ (contract engineer for an Odoo module or Exact app, security review, Odoo partner fees) — ESTIMATE. Capital is a **low** barrier for everyone, including copycats.

### 7.2 Technical
- Founder builds (in reach with Python/SQL + agent frameworks): trial-balance/GL extraction scripts (Odoo XML-RPC/JSON-2, Exact Online REST with OAuth and the 5,000 requests/day limit — VERIFIED, https://peliqan.io/blog/mcp-rate-limits-guide/), Yuki API, a group chart-of-accounts mapping table with LLM proposals, IC matching by counterparty/amount/reference, elimination journal generator, Excel/PowerPoint pack generation (openpyxl/python-pptx), pack tie-out checks, prompts for commentary.
- AI (Claude Code/Copilot) builds: most glue code, tests, the MCP server wrappers, dashboards.
- Needs an engineer: a multi-tenant SaaS with auth, secrets, audit logs, SOC2-style controls; a certified Odoo Enterprise module or Exact App Store listing; anything HQ IT security will review (INFERENCE). Not needed in year 1.
- Barrier for competitors: **low-medium**. Any controller with Claude Code can replicate the tooling in months; the moat is not the code.

### 7.3 Regulatory (the decision-critical barrier)
- Law of 17 March 2019 (ITAA): reserved activities under art. 3 include organisation of accounting services; opening, keeping, centralising and closing of books; determination of results and drawing up of annual accounts; verification/correction of accounting documents; and "analysis, by means of accounting techniques, of the situation and functioning of undertakings from the point of view of their credit, performance and risks". Performing reserved activities for third parties as a self-employed person without ITAA registration is a criminal offence (art. 117); ITAA runs an illegal-practice hotline and pursues "pseudo-professionals" — VERIFIED, https://www.ejustice.just.fgov.be/eli/wet/2019/03/17/2019040805/justel ; https://www.itaa.be/nl/instituut/meldpunten/illegale-uitoefening/ ; https://www.blogitaa.be/fr/2026/06/29/protection-du-titre-et-de-la-profession-comment-litaa-agit-contre-lexercice-illegal/ ; https://www.itaa.be/wp-content/uploads/ITAA-zine_05-2022_Juni_NL.pdf
- Not reserved: "anyone in Belgium can provide financial advice, prepare financial declarations or assist companies financially"; not all financial services are reserved — VERIFIED (search-summary of ITAA/ATTA sources), https://www.atta-ai.com/glossaire/itaa ; https://itaa-servicedesk.freshdesk.com/fr/support/solutions/articles/80001017133-pourriez-vous-clarifier-quelque-peu-les-nouveaux-titres-
- Subcontracting: Court of Cassation 28 Nov 2022 held that reserved activities are only "for third parties" when performed for a client; a subcontractor executing part of an ITAA firm's engagement letter is not acting for a third party and need not be registered; ITAA has a "sous-traitance comptable" page — VERIFIED, https://blog.forumforthefuture.be/fr/article/itaa-et-sous-traitants-non-agrees-le-probleme-semble-regle-/17549 ; https://academiefiscale.eu/profession/en-belgique-un-sous-traitant-independant-peut-valablement-tenir-la-comptabilite-des-clients-dun-cabinet-dexpertise-comptable/ ; https://www.itaa.be/fr/sous-traitance-comptable/ . An older ITAA-zine (2022) said non-members may not perform reserved activities "even as subcontractor" — the Cassation ruling post-dates it; treat the ruling as controlling but confirm the ITAA's current guidance on its sous-traitance page.
- **Application to OPP-A (INFERENCE, needs a lawyer/ITAA confirmation)**:
  - Management consolidation, HQ reporting packs, variance commentary, KPI reporting, IC *matching lists* delivered to the client's own bookkeepers: most likely *not* reserved (management reporting/controlling/financial analysis for management purposes), provided the founder does not keep books, post entries, or draw up statutory (consolidated) annual accounts. Risk point: the art. 3 "analysis by accounting techniques of situation/functioning ... credit, performance, risk" wording could be read to cover management analysis; ITAA guidance/case law on whether internal management reporting by an external controller falls under it: ENF.
  - Posting elimination entries into the client's Odoo, "cleaning up" intercompany in the ledgers, or producing *statutory* consolidated accounts filed at the NBB: **likely reserved** (keeping/closing books; drawing up annual accounts). Mitigation: founder *proposes* entries; client's bookkeeper or ITAA accountant posts them; statutory consolidation stays with the ITAA firm/auditor.
  - Safe structures: (1) contract as "financial reporting/controlling services" with explicit exclusion of bookkeeping and statutory accounts; (2) subcontract to an ITAA firm under its engagement letter for anything ledger-touching (Cassation route); (3) longer term, ITAA traineeship (3 years) — heavy for a part-time founder.
  - Foreign HQ as client (segment b): the Belgian subsidiary is still the "third party"; same analysis.
- Professional liability: not legally mandatory for a non-regulated consultant but standard; EUR 270-1,000/yr (VERIFIED range). Clients (especially HQs) will ask for it.
- GDPR: ledgers contain personal data (employee payroll lines, sole-trader suppliers/customers). Belgian guidance says "economic professionals" (accountants) act as controllers, not processors; a consultant strictly following client instructions is a processor and needs an art. 28 processor agreement — VERIFIED, https://blog.be.accountants/nl/article/gdpr-1-in-welke-hoedanigheid-verwerk-ik-gegevens-van-mijn-clienten/4586 ; https://privacypolicygenerator.be/kennisbank/verwerkersovereenkomst/ . INFERENCE: for OPP-A the founder is a processor for reporting data; sign a DPA, keep data in EU regions, use LLM providers with zero-retention/enterprise terms, minimise personal data sent to LLMs (aggregate at account level; pseudonymise counterparties).
- HQ data/NDA: HQ groups will require NDA, sometimes IT-security questionnaires, and will resist third-party API tokens into the group ERP; expect "export-only" access (trial balance files) in segment (b) — INFERENCE.
- Belgian VAT/legal form for the founder: start as sole proprietor under the VAT franchise (<EUR 25k, no VAT on invoices; B2B clients cannot recover anything anyway so neutral), incorporate (BV/SRL, EUR 1.5-2.5k) around EUR 80k turnover or when liability exposure grows (belgium-founder-facts.md). Note: B2B e-invoicing mandate (Peppol) from Jan 2026 applies to VAT-registered businesses; a franchise business is commonly reported as out of scope for issuing (to confirm).
- Barrier assessment: **medium** and *asymmetric*: it blocks nothing in the controlling scope, but blocks the most valuable "we also fix your books" scope. For competitors it is the same: it keeps ITAA firms as the only ones who can do the whole chain — which is why partnering with one is strategic.

### 7.4 Distribution
Reaching owner-CEOs of Belgian holdings and local finance managers of subsidiaries is relationship-driven (accountants, Odoo integrators, bankers, ex-colleagues). No public marketplace. Barrier **medium** for a founder with corporate network; **high** for a foreign copycat.

### 7.5 Sales cycle
Segment (a): 1-3 months from intro to signed retainer once a trigger exists; without trigger, indefinite (INFERENCE). Segment (b): 2-6 months (local MD + HQ CFO approval; procurement/NDA) — INFERENCE.

### 7.6 Operational
Monthly deadlines on the client's calendar collide with a full-time job: WD1-WD5 close weeks are also the founder's employer's close weeks (he works in FP&A). This is the single biggest *operational* barrier — **high** for this founder specifically, low for a full-time competitor. Mitigation: choose clients with WD10+ deadlines (segment a boards; HQs with monthly-but-not-fast cadence), automate extraction to run overnight, keep a backup freelancer.

### 7.7 Data
Each onboarding creates a mapped chart of accounts, IC counterparty matrix and pack template — a **switching cost** for the client and a growing library for the founder. Barrier low at entry, grows with clients (GOOD barrier).

### 7.8 Partnership
Odoo integrators (Belgian partner ecosystem, e.g. lists at https://www.bayforward.be/top-10-odoo-implementation-partners-in-belgium/), ITAA firms with client stops, Peliqan/Chift, EMAsphere/BrightAnalytics implementation. Barrier **medium**: partners want references first.

### 7.9 Trust
Clients hand over the group's numbers to one person. Trust is built by credentials (MSc, corporate controlling track record), insurance, references and a visible QA process. **High** barrier for an unknown; the founder's employer brand (unnamed) and Brussels network lower it.

### 7.10 Network effects
None in the service. Weak data-network effect in the product (Belgian-GAAP-to-group mapping library; IC pattern library) — HYPOTHESIS.

### 7.11 Overall classification
Barriers to *entry* are **low-medium** (capital, tech) — anyone can start. Barriers to *scale and trust* are **medium-high** (regulation, close-week operations, trust, distribution). **GOOD vs BAD**: the regulatory and trust barriers are GOOD barriers *if the founder partners with an ITAA firm* (they then protect him from copycat controllers without a firm relationship); the operational barrier (close-week conflict with employment) is a BAD barrier — it hurts the founder more than competitors. Net: a defensible-enough services niche, not a defensible software category.

---

## 8. Belgium analysis

| Factor | Assessment | Evidence / reasoning |
|---|---|---|
| Density of holding/group structures | **Advantage** | 30,552 holdings (VERIFIED, commercial); management companies doubled to 80,210 by 2024 (VERIFIED); 5,500+ groups in the EGR-based database (VERIFIED, old basis) |
| Foreign-subsidiary density | **Advantage** | Flanders alone 7,288 foreign-controlled firms employing ~460k (VERIFIED); Brussels hosts EU/regional HQs (INFERENCE); Luxembourg 2 h away |
| Odoo is Belgian; Odoo gap is live | **Advantage** | Sections 2.4, 6 |
| Controller shortage + rising interim rates | **Advantage** | C-24, Apex League (VERIFIED) |
| Accounting-firm capacity crunch | **Advantage** (channel) | 56% of firms refuse clients; firms cannot deliver advisory (C-24) |
| Regional subsidies for the *client* | **Neutral-to-advantage** | Flanders KMO-portefeuille: consulting subsidy limited to digitalisation-cybersecurity since Feb 2026, training still open (VERIFIED, belgium-founder-facts); Wallonia chèques-entreprises digital-maturity voucher 50% up to EUR 50k over 3 years, reform May 2026 (VERIFIED); Brussels consultancy subsidy 60% but suspended from 12 Aug 2026 (VERIFIED). INFERENCE: a "reporting automation / digital maturity" framing of onboarding could be subsidised in Wallonia; monthly retainers are not subsidisable |
| Languages | **Disadvantage in Flanders, neutral in Brussels/Wallonia, advantage for segment (b)** | Segment (a) groups are disproportionately Flemish family groups (the consolidation vacancies found are in Waregem/Deerlijk; the holding/management-company boom is reported by Flemish media) — Dutch matters for owner-CEO sales and for reading Flemish ledgers/notes; deliverables in EN/FR are acceptable in Brussels and Wallonia and for most HQ packs (HQ language is English). Practical: start with Brussels/Walloon-Brabant groups and foreign subsidiaries (EN), add a Dutch-speaking partner or improve NL for Flanders |
| Brussels-specific | **Advantage** | Concentration of foreign subsidiaries/regional HQs, Big-4 alumni network, international finance managers who work in English; hub.brussels free start-up guidance; Brussels consultancy subsidy currently suspended (VERIFIED) |
| Legal form / VAT for founder | **Neutral** | Sole proprietor + VAT franchise to start; BV/SRL later (belgium-founder-facts). Side-activity social contributions minimal (EUR 98.51/quarter minimum, exemption below EUR 1,922 income) |
| Employment constraints | **Disadvantage** | Non-compete only post-termination and only above salary thresholds, but loyalty/unfair-competition duty during employment; contract/work rules must be checked; if the employer is itself a foreign-owned subsidiary the overlap is sensitive (belgium-founder-facts; INFERENCE) |
| Regulatory (ITAA) | **Disadvantage vs NL/UK** | Belgium reserves more accounting activities than NL/UK; controlling is open but ledger-touching is not (section 7.3) |
| Overall | **Advantage** for a service business; **neutral** for a product (NL has more tools and a bigger self-serve market) |

---

## 9. EU expansion (NL, FR, DE, LU, UK): what changes

| | Language | GAAP / thresholds | Tools / ledgers | Sales / regulation |
|---|---|---|---|---|
| NL | Dutch mandatory for SME groups; English OK for subsidiaries | Dutch GAAP (RJ); EU-uplifted size thresholds (Delegated Directive 2023/2775, +25%, from FY2024 — VERIFIED, https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202302775) | Exact Online, Twinfield, AFAS dominant; crowded cheap consolidation SaaS (Speedbooks, Finstack, Liquid, Easyclose, Visionplanner) | No reserved-activity regime like ITAA for bookkeeping/reporting (INFERENCE); fractional finance market mature; hardest market to differentiate on tooling |
| FR | French | French GAAP (PCG), CRC 99-02 for consolidation; outsourced consolidation ("externalisation de la consolidation") is an established category (MELVAN, Primexis, BM&A — VERIFIED) | Sage, Cegid, Pennylane; Odoo strong in France (top-concentration country — VERIFIED, https://insightfulerp.com/odoo-statistics-2026-market-share-growth-and-why-businesses-are-switching/) | Expert-comptable monopoly (Ordre) on bookkeeping is stricter than Belgium; management reporting open (INFERENCE); big market for Odoo groups; founder's French usable |
| DE | German mandatory | HGB, § 290 ff. consolidation; thresholds uplifted 2024 | DATEV dominates; Odoo growing; Lucanet home market | Steuerberater monopoly on bookkeeping; Skalar shows AI-first firm model (VERIFIED); language is the barrier |
| LU | French/English (German) | Lux GAAP; exemption EUR 25M/50M/250 (VERIFIED) | Fiduciaries' own tools (BOB/Sage), group HQ tools | OEC-regulated profession; domiciliation licensed; entry only as subcontractor to fiduciaries or via operating subsidiaries; small, high-value, Brussels-adjacent |
| UK | English | FRS 102; group exemption for small groups; consolidation less common for SMEs | Xero/QuickBooks/Sage + Syft/Fathom (cheap consolidation with AI commentary — VERIFIED) | No reserved activities for management accounts; extremely mature fractional FD market at GBP 600-1,200/day (VERIFIED); crowded; useful only as product market |

Sequence that follows (INFERENCE): Belgium (a)+(b) → Luxembourg (b) → France (Odoo groups, French) → NL only with a Dutch partner → UK/DE only as product.

---

## 10. AI architecture

### 10.1 Service phase (months 0-12): "founder + agents" stack
Principle: deterministic where the answer must be exact (sums, eliminations, tie-outs); LLM where the task is mapping, classification, drafting or QA reading; human-in-the-loop at every point where a number leaves the system.

Connectors (read-only by default):
- Odoo: External API (XML-RPC ≤18, JSON-2 for 19) via OSS MCP (ivnvxd/mcp-server-odoo, 384 stars) or an App Store MCP module; pull account.move.line aggregates by account/partner/period, analytic tags, currencies.
- Exact Online: REST + OAuth; 5,000 requests/day cap (VERIFIED) → pull trial balances and GL transactions per division nightly, cache in the founder's DB; Peliqan's OSS Exact MCP connector as fallback.
- Yuki: API (Chift lists it); or monthly export.
- No-API entities (WinBooks at the accountant, HQ ERP): CSV/XLSX trial-balance drop folder with a schema validator.
- Optional managed layer: Peliqan (~USD 199/month, 250+ connectors, MCP) or Chift (unified API, pricing ENF) if maintaining connectors eats founder hours.

Data model (Postgres/DuckDB, one schema per client):
- entity, period, local_account, group_account, mapping(local_account→group_account, version, approved_by, approved_at), tb_line(entity, period, local_account, debit, credit, currency, partner_id), ic_pair(entity_a, account_a, entity_b, account_b, amount_a, amount_b, diff, status, explanation), elimination_entry(period, lines, rationale, approved), fx_rate, pack_template(client, cells→queries), commentary(period, section, draft, final, author), qa_check(period, rule, result, delta).

LLM tasks (Claude/GPT class; enterprise/zero-retention terms; account-level aggregates only):
- Propose local→group chart-of-accounts mapping with confidence and rationale (few-shot from prior clients' mapping library; Belgian PCMN/MAR codes as anchors).
- Classify unmatched IC items (timing, FX, missing invoice, wrong counterparty) and draft the open-item email to the entity bookkeeper.
- Draft variance commentary from a computed bridge (numbers come from code, never from the model).
- Read the produced pack and flag inconsistencies (tie-out narrative, U-024 asset).
- Summarise client questions and prior-period notes for the review call.

Deterministic tasks (Python): FX translation, aggregation, IC matching rules (exact amount, tolerance, reference, partner), elimination journal generation, roll-forward, bridge calculation, Excel/PowerPoint rendering (openpyxl/python-pptx), rule-based QA (BS balances, CF ties, pack=workbook=DB), audit log.

Human-in-the-loop: founder approves every mapping change, every elimination, and signs the pack; client bookkeeper posts entries (ITAA safety); review call closes the month.

Build effort for this founder (ESTIMATE): connector + TB store 40-60 h; mapping engine with LLM proposals 30-40 h; IC matching + eliminations 40-60 h; pack renderer for one template 30-40 h; QA rules 20 h; commentary prompts 10-20 h. Total ~170-240 h ≈ 4-6 months at 10 h/week — i.e. the first client must be served *manually* (Excel + one tool) while this is built.

### 10.2 Product phase (months 12-36): Odoo/Exact-native consolidation and reporting product
- Packaging options: (i) Odoo module (Enterprise) adding IC detection, mapping and elimination-proposal views; (ii) standalone web app with Odoo/Exact/Yuki connectors (Chift/Peliqan or own); (iii) Exact App Store listing. Option (ii) is most realistic for a non-elite engineer with an AI coding assistant; (i) has the best distribution (Odoo partners) but requires Odoo development skills and partner status.
- Multi-tenancy, SSO, audit trail, role-based approvals, EU hosting, DPA, pen-test: needs a contract engineer (EUR 5-20k+) — ESTIMATE.
- Differentiators that survive commoditisation: Belgian-GAAP-aware mapping library, IC pattern library, HQ-format templates, and the *service* wrapped around it (the accountable human).

---

## 11. AI leverage and the three tests

**AI leverage now (service phase)**: of the monthly hours in a consolidation + pack cycle, ESTIMATE 40-60% can be executed by LLM/agents/software today (extraction, mapping proposals, IC first-pass, bridge computation, first-draft commentary, QA reading, rendering); 40-60% remains human (judgement on mappings/eliminations, client conversation, HQ nuances, sign-off, exception handling). **In 3 years**: 75-90% by software/agents; the human share shrinks to sign-off, relationship, judgement on unusual transactions (ESTIMATE).

**AI commoditisation test** — will general AI (Copilot Finance Agents, Odoo AI, Excel Skills, cheap SaaS with AI commentary) do this for the customer directly?
- Tool layer: already commoditised (Finstack EUR 39/entity, Syft/Fathom AI commentary, Copilot variance agent GA 2026, Odoo 19 AI agents) — the *software* value of OPP-A is **WEAKENED**.
- Service layer: the customer still lacks the person who knows which mapping is right, who chases the sister company, who signs. Commoditisation lowers delivery cost for the founder as much as for competitors. Classification: **NEUTRAL-to-WEAKENED** overall; STRENGTHENED for margins in the service phase, WEAKENED for the product ambition.

**AGI test** (a system that can do any cognitive job a competent controller can, at low cost): the accountable-human role survives only where regulation, liability or HQ policy requires a named responsible person; the labour component disappears. Classification: **DESTROYED** for the labour-based revenue; **WEAKENED** rather than destroyed only if the founder has by then become the ITAA-partnered, insured signatory for a client base (trust/liability position) — HYPOTHESIS.

**ASI test**: **DESTROYED** (as for every knowledge service); the only residual is legal-accountability positions, which regulation could also reassign.

Reasoning summary: OPP-A is an *AI-leverage* business (AI makes a solo controller 3-5x more productive), not an *AI-defensibility* business. Its window is the 3-7 years in which agents are good enough to leverage but customers still need a named human who owns the numbers.

---

## 12. Business model and unit economics

### 12.1 Pricing options
1. Fixed monthly retainer per group/subsidiary: EUR 1,500-3,500 (a), EUR 2,000-4,000 (b); onboarding fee EUR 2,500-7,500 (mapping, IC baseline, template) — ESTIMATE anchored on section 3.
2. Per-entity pricing: EUR 250-400/entity/month with a EUR 1,500 floor — mirrors Finstack's logic at a service price.
3. Onboarding-only project (EUR 5-15k) + "run" retainer; or onboarding + hand-over to a client tool (Finstack/Easyclose/BrightAnalytics) with a light QA retainer (EUR 500-900/month).
4. Subsidiary "close-week" package: fixed fee per pack + hourly for ad-hoc.

### 12.2 Gross margin per retainer at founder hours
Steady-state hours per client per month (ESTIMATE): 4-6 h with tooling (10-14 h in the first three months). At EUR 2,000/month and 5 h: EUR 400/h effective. Direct costs: LLM EUR 20-60/client/month; connector/tool share EUR 50-150; insurance/admin share EUR 30. Gross margin ~85-92% (ESTIMATE). Onboarding at 25-40 h is where fixed-fee risk sits — price it separately.

### 12.3 Capacity ceiling
10-15 h/week ≈ 45-65 h/month. Reserve 15 h for building/sales → 30-50 delivery hours → **6-10 clients** at steady state (fewer during onboarding waves). Revenue ceiling at 8 clients x EUR 2,250 = **EUR ~18k/month (EUR ~215k/yr)** — ESTIMATE. Close-week bunching may cap it lower (section 7.6).

### 12.4 Paths
- **EUR 1k/month**: 1 segment-(a) client at EUR 1,000-1,500 done largely manually with one cheap tool; reachable within 3-6 months via network. Purpose: learn the mapping/IC problems, build templates.
- **EUR 10k/month**: 4-6 clients; requires the tooling of section 10.1 to keep hours within 10-15 h/week; 12-24 months; probably requires choosing clients with WD10+ deadlines. This is also the point where the employment question must be resolved (go 4/5 or leave).
- **EUR 100k/month**: not reachable as a solo service. Requires either (i) a firm of 6-10 controllers using the founder's tooling (a Neno/Skalar-style agent-first firm; needs capital and ITAA partnership) or (ii) product revenue: ~400 groups at EUR 250/month or 100 firms/integrators at EUR 1k/month — INFERENCE; only if the Odoo/Exact-native product finds a channel (integrators, EMAsphere/BrightAnalytics-type partnership) and Odoo does not close the gap.

### 12.5 Four capital scenarios
- **EUR 0**: sole-proprietor registration deferred until first invoice (it costs ~EUR 109 anyway — so EUR 0 means "friends-and-family pilot unpaid"); tools = Excel + free tiers (Invantive free connector, OSS Odoo MCP, free LLM tiers); one unpaid/discounted pilot to build the case study. Viable but slow; weak signal on WTP.
- **EUR 500**: registration + VAT activation (~EUR 190), liability insurance (~EUR 270), LLM API credits; first paying pilot at EUR 1,000-1,500/month. Recommended starting bracket.
- **EUR 2,000**: adds a Peliqan or Finstack/Easyclose subscription for 6 months (EUR 600-1,200) to avoid building connectors first, a proper DPA/contract template from a lawyer (EUR 300-600), a professional website/LinkedIn assets. Allows 2-3 clients within the hour budget.
- **EUR 5,000**: adds a BV/SRL when turnover justifies (EUR 1.5-2.5k), a 2-3 day Odoo-development bootcamp or a contract developer for an MCP/ETL layer (EUR 1.5-2.5k), a Dutch-language sales asset/translator for Flanders. Does not change the ceiling (hours do).

---

## 13. Customer acquisition

- **First customer**: warm network — an ex-colleague who is now finance manager of a foreign-owned subsidiary in Brussels, or a family group the founder knows through his employer's ecosystem; or the founder's own accountant's client with a holding. Offer: 3-month pilot at EUR 1,000-1,500/month, onboarding free, in exchange for a reference and a testimonial. Deliver the first two months largely by hand.
- **Customers 2-10**: (1) two or three Odoo integrators in Brussels/Wallonia (the CI named OBS, Odive, Agile-Minds; Odive already blogs on "meerdere vennootschappen in Odoo") who see multi-company clients struggling post-18/19 — offer them a white-label "consolidation onboarding" service; (2) small ITAA firms with client stops that refuse advisory (C-24) — offer a referral fee or a subcontracting arrangement (Cassation route) so they keep the statutory work and the founder takes the monthly pack; (3) LinkedIn content in EN/FR on "Odoo 19 consolidation without the app", "IC reconciliation checklist for Belgian groups", "HQ pack from Exact in 3 days" — the Odoo forum threads show the search intent; (4) Luxembourg fiduciaries as subcontract clients for HQ packs.
- **Scaling channels**: Odoo partner network (co-marketing at Odoo Experience, Belgian partner events), EMAsphere/BrightAnalytics implementation partnership, bank relationship managers (EMAsphere is distributed by BNP Paribas in France — the bank channel exists), Big-4 alumni networks in Brussels, HQ-finance communities (group controllers who want a reliable Belgian pack producer).
- **Objections and answers**: "our accountant does it" (they do it annually; we do monthly and hand them a clean IC position); "HQ will not open the ERP" (we work from exports; read-only; DPA/NDA; EU-hosted); "one person risk" (documented process, backup freelancer, tooling the client keeps); "liability" (insurance; you post, we propose; statutory stays with ITAA/auditor); "price" (below two interim days; below the tool + your own time).
- **Price sensitivity**: segment (a) owners compare with "my accountant charges EUR X per year" and are highly price-sensitive without a trigger; segment (b) budgets are held by HQ, less price-sensitive but slower — INFERENCE.

---

## 14. MVP

- **Manual at first**: extraction (client exports or founder's read-only login), mapping in Excel, IC matching in Excel with a simple matching macro/Python script, pack in the client's template, commentary written by the founder with an LLM as drafting aid, review call.
- **Automate first (in this order)**: (1) trial-balance ingestion + validation for Odoo/Exact/CSV; (2) mapping table with LLM proposals and version control; (3) IC matching and open-item list generation; (4) pack rendering from the DB; (5) QA tie-out rules; (6) commentary drafting from computed bridges.
- **Do NOT build (year 1)**: a multi-tenant SaaS, an Odoo module, statutory consolidation (CONSO NBB filings), IFRS conversion engines, budgeting/forecasting modules, dashboards (BrightAnalytics/Power BI exist), connectors for ledgers you have no client on, anything that touches posting into client ledgers.

---

## 15. Service → product → platform trajectory

- **Year 1 (service)**: 2-4 clients, EUR 3-8k/month by month 12 (ESTIMATE); internal tooling built around real clients; ITAA-firm partnership signed; case studies; decision point on employment.
- **Year 2 (productised service)**: 6-10 clients, EUR 12-20k/month at the hour ceiling; onboarding standardised (fixed-fee); first white-label deliveries through 1-2 Odoo integrators; maybe one freelance controller subcontracted for close weeks; tooling packaged as an internal app.
- **Year 3 (product beta)**: web app with Odoo/Exact/Yuki connectors offered to (i) the founder's clients as self-serve between review calls, (ii) 3-5 accounting firms/integrators; pricing EUR 250-400/entity/month or EUR 1k/month per firm seat; service revenue still >70%.
- **Year 5 (platform, conditional)**: only if Odoo has not shipped a real consolidation engine and a channel (integrators/firms/EMAsphere-type partner) has adopted the product: 100-300 groups on the product, a small team of controllers delivering the service on it — EUR 1-3M/yr revenue (HYPOTHESIS). If Odoo closes the gap, the business stays a EUR 200-400k/yr specialist service or exits to a firm/integrator (Vandelanotte-type firms buy capabilities; Finstack-type vendors buy customer bases).
- **Can it escape founder labour?** Partially. The service cannot without hiring controllers (which reintroduces the ITAA and management questions). The product can, but its defensibility is weak (section 11). The realistic escape is a small agent-first controlling firm (3-8 people) with high margins, or a sale.

---

## 16. Main risks and reasons NOT to pursue; evidence that would change the recommendation

1. **Close-week collision with employment** (highest, operational): monthly deadlines fall in the founder's own busiest week. Kill signal: two consecutive months where a client pack is late because of the day job. Changer: clients accept WD10+ or quarterly cadence; employer agrees to 4/5.
2. **ITAA scope** (regulatory): if ITAA guidance or a lawyer concludes that management consolidation/IC analysis for third parties is a reserved activity, the offer must become a subcontract to an ITAA firm (lower margin, dependent) or stop. Changer: written confirmation that controlling/management reporting without bookkeeping is open; or a firm partnership.
3. **Monthly-management WTP is unproven** for segment (a): all outsourced-consolidation evidence is statutory/annual (FR/LU/BE firms). Kill signal: 10 interviews in which owners say "quarterly with the accountant is enough". Changer: 3 signed retainers at ≥EUR 1,500/month within 6 months.
4. **Odoo platform risk**: Odoo iterates on consolidation every 19.x release (19.2 changed journal inclusion); if Odoo 20 ships IC detection and eliminations, the Odoo-native product wedge disappears (service survives). Changer: Odoo roadmap statements; partner intel.
5. **Employer conflict**: if the employer is a foreign-owned subsidiary, serving competitors' subsidiaries may breach loyalty duties; contract check required (belgium-founder-facts).
6. **Language**: Flemish family groups (where the consolidation vacancies are) expect Dutch; the founder's SAM in segment (a) shrinks to Brussels/Wallonia unless NL improves or a partner joins.
7. **Ceiling**: solo, part-time, the business tops out at ~EUR 200k/yr; it is a high-margin lifestyle/second-income business unless it becomes a firm or a product. If the founder's goal is a venture-scale company, OPP-A is a funding engine, not the destination.
8. **Commoditisation**: cheap SaaS + Copilot agents keep lowering the price the customer expects for "the numbers"; the founder must sell accountability and IC discipline, not reports.
9. **Key-person/trust**: one sick month can lose a client; HQs may refuse a solo provider.
10. **Data/security**: HQ security reviews may block API access; working from exports reduces automation gains in segment (b).

Evidence that would flip to "pursue strongly": (i) ITAA/legal confirmation of scope; (ii) 2 paying pilots from the founder's network within 90 days; (iii) an Odoo integrator agreeing to refer multi-company clients; (iv) a written statement from 3+ finance managers of subsidiaries that HQ packs are outsourced or interim-staffed today at ≥EUR 2k/month. Evidence that would flip to "drop": (i) reserved-activity confirmation with no firm willing to partner; (ii) employer prohibition; (iii) Odoo 20 shipping full consolidation with IC eliminations; (iv) interviews showing quarterly/annual cadence is all that is wanted.

---

## 17. Open questions requiring direct customer interviews

Segment (a) — owners/CFOs of 3-15-entity Belgian groups (target 8-10 interviews, half Flemish):
1. Who produces group numbers today, how often, in what tool, and how many hours does it take?
2. Which external party asks for them (bank, board, family, buyer) and at what cadence and deadline?
3. What happened the last time intercompany did not reconcile? Who fixed it and what did it cost?
4. What do you pay your accountant per year and what does it include (consolidation? management reporting?)
5. Would you pay EUR 1,500-2,500/month for a monthly pack + IC clean-up? What would make you say no? Who signs?
6. Which ledgers per entity (Odoo version, Exact, Yuki, other) and who administers API access?
7. Language expectations for deliverables and calls (NL/FR/EN).

Segment (b) — local finance managers/MDs of foreign-owned Belgian/Lux subsidiaries (target 8-10):
8. Describe the HQ pack: format, tool, deadline (WDx), GAAP adjustments, IC confirmations, commentary requirements.
9. How many people produce it; what happens during leave/turnover; do you use interims (rate, days)?
10. Would HQ allow an external provider read-only API access, or exports only? Which security/DPA requirements?
11. Is the budget local or HQ; what approval is needed for a EUR 2-4k/month retainer?
12. Has HQ ever asked you to use a group consolidation tool locally; which one; pain points?

Channel interviews (3 Odoo integrators, 3 ITAA firms, 1 Luxembourg fiduciary):
13. How many multi-company clients lost consolidation functionality in Odoo 18/19; what do you tell them?
14. Would you refer or white-label a monthly consolidation service; under what commercial terms; who carries liability?
15. ITAA firms: is management consolidation/IC analysis by a non-member for your client acceptable as subcontracting under your engagement letter? What would you require?

Regulatory/legal (not customers, but blocking): written ITAA guidance or a lawyer's opinion on art. 3 scope for management reporting/IC analysis by a non-member; employer contract review.

---

## Evidence index (new URLs from this deep-dive; CI/stream URLs are in their own files)
https://statbelpr.belgium.be/nl/themas/datalab/multinationale-groepen-belgie ; https://www.plan.be/publications/publication-2249-nl-multinationale_groepen_in_belgie_structuur_en_economische_activiteit ; https://statbel.fgov.be/nl/themas/datalab/multinationale-groepen-belgie ; https://www.ewi-vlaanderen.be/nieuws/buitenlands-zeggenschap-vlaanderen-anno-2023 ; https://www.ecoom.be/downloads/publications/790 ; https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Foreign-controlled_enterprises_statistics_-_inward_FATS ; https://www.kenniswest.be/artikel/al-meer-dan-80000-belgen-hebben-managementvennootschap-blijkt-uit-cijfers-van-de-statistiekdienst-statbel/253258 ; https://companydata.com/nl/bedrijven/belgie/holdings-belgie/ ; https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?view=e4bcf725-1708-4bb2-aa27-df1c69b010bb ; https://www.nbb.be/en/central-balance-sheet-office/about-central-balance-sheet-office/central-balance-sheet-office-figur-0 ; https://vanhavermaet.be/artikels/vennootschappen-in-groep/ ; https://insights.hlb.be/nl/actua/belgi%C3%AB-volgt-europa-nieuwe-groottecriteria-voor-ondernemingen-vanaf-2024 ; https://www.cssf.lu/en/2023/02/qa-cnc-22-028-regarding-the-implementation-of-the-consolidation-exemption-for-small-groups-article-1711-4-lsc/ ; https://www.dsm.legal/en/the-new-framework-for-size-criteria-of-companies-and-groups/ ; https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202302775 ; https://kyckr.com/guides-and-reports/luxembourg-registry-guide-2025 ; https://ilicompta.lu/guides/cout-expert-comptable-luxembourg ; https://www.financialservices.lu/en/accounting-pricing-luxembourg ; https://www.fiduciamanagement.lu/services/consolidation-comptable/ ; https://www.stepstone.be/salaris/Groeps-controller.html ; https://ctrl-f.be/en/vacancy/financial-controller-consolidation-a1wp800000ao5gtmaz/ ; https://www.roberthalf.com/nl/nl/baan-details/group-controller ; https://fr.glassdoor.be/Salaires/controleur-de-gestion-salaire-SRCH_KO0,21.htm ; https://www.robertwalters.be/fr/eclairages/conseils-carriere/blog/combien-gagnez-vous-en-tant-que-controleur.html ; https://www.fed-group.be/fed-finance/recruter-finance/grille-salaire-finance-comptabilite ; https://www.glassdoor.com/Job/brussels-group-financial-controller-jobs-SRCH_IL.0,8_IC2302160_KO9,35.htm ; https://www.glassdoor.com/Job/belgium-finance-manager-jobs-SRCH_IL.0,7_IN25_KO8,23.htm ; https://www.apexleague.be/insights/tarieven-en-kosten-van-een-finance-consultant-in-belgie ; https://fractional-csuite.com/tools/rates/ ; https://www.ridgewayfs.com/controller-compensation-saas-fintech-crypto/ ; https://leadership-services.co.uk/rate-report-2026/ ; https://lanop.co.uk/part-time-finance-director-uk-guide/ ; https://www.vandelanotte.be/en/our-offer/consolidation ; https://vgd.eu/blog/consolidatie-cruciaal-voor-de-kracht-van-je-groep ; https://www.melvan.fr/consolidation-et-reporting-financier/externalisation-de-la-consolidation/ ; https://bma-groupe.com/conseil-et-supports-operationnels/externalisation-de-consolidation-chez-les-groupes-de-taille-moyenne/ ; https://www.iteradvisors.com/ressources/blog/cout-externalisation-comptable-2026 ; https://www.odoo.com/forum/help-1/how-does-odoo-support-inter-company-eliminations-in-europe-299551 ; https://www.odoo.com/forum/help-1/consolidation-in-odoo-303609 ; https://www.odoo.com/forum/help-1/consolidation-set-up-300474 ; https://www.odoo.com/forum/help-1/odoo-19accounting-consolidation-for-multi-currency-and-multi-companies-300195 ; https://www.odoo.com/odoo-19-2-release-notes ; https://ecosire.com/blog/odoo-multi-company-setup-guide ; https://apps.odoo.com/apps/modules/19.0/ai_mcp_server ; https://apps.odoo.com/apps/modules/19.0/mcp_server_odoo ; https://peliqan.io/blog/mcp-rate-limits-guide/ ; https://www.chift.eu/ ; https://www.chift.eu/tools/odoo ; https://link.springer.com/article/10.1007/s00500-025-10983-4 ; https://arxiv.org/html/2512.22443v2 ; https://www.dualentry.com/accounting-ai-benchmark ; https://www.ejustice.just.fgov.be/eli/wet/2019/03/17/2019040805/justel ; https://www.itaa.be/nl/instituut/meldpunten/illegale-uitoefening/ ; https://www.blogitaa.be/fr/2026/06/29/protection-du-titre-et-de-la-profession-comment-litaa-agit-contre-lexercice-illegal/ ; https://www.itaa.be/fr/sous-traitance-comptable/ ; https://blog.forumforthefuture.be/fr/article/itaa-et-sous-traitants-non-agrees-le-probleme-semble-regle-/17549 ; https://academiefiscale.eu/profession/en-belgique-un-sous-traitant-independant-peut-valablement-tenir-la-comptabilite-des-clients-dun-cabinet-dexpertise-comptable/ ; https://www.atta-ai.com/glossaire/itaa ; https://www.verzekeringen.be/ondernemen/beroepsaansprakelijkheidsverzekering-consultant ; https://hellosafe.be/nl/beroepsaansprakelijkheidsverzekering ; https://blog.be.accountants/nl/article/gdpr-1-in-welke-hoedanigheid-verwerk-ik-gegevens-van-mijn-clienten/4586 ; https://privacypolicygenerator.be/kennisbank/verwerkersovereenkomst/ ; https://www.capterra.com/p/156656/EMAsphere/ ; https://banqueentreprise.bnpparibas/post/gestion-au-quotidien/offre/reporting-pilotez-votre-entreprise-avec-emasphere-cl96wfxg900be012i48te08jx ; https://www.capterra.com/p/218509/BrightAnalytics/ ; https://finstack.io/pricing-single-entity ; https://silverfin.com/en-gb/silverfin-pricing/ ; https://leadservice.be/top-11-boekhoudsoftware-gebruikt-door-belgische-boekhouders/ ; https://www.boekhoudvergelijker.be/vergelijkingen/beste-boekhoudsoftware-belgie/ ; https://www.b2btax.be/digitale-boekhoudsoftware-kmo/ ; https://insightfulerp.com/odoo-statistics-2026-market-share-growth-and-why-businesses-are-switching/ ; https://www.bayforward.be/top-10-odoo-implementation-partners-in-belgium/
