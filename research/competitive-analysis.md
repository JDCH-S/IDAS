# Competitive analysis

Date: 2026-09-11. Existence checks were run on the 40 investigated opportunities in four batches (`_raw/ci-batch-1..4.md`, ~190 searches, EN/NL/FR/DE). This file summarises what was found; full per-competitor tables with URLs are in the batch files. All facts are VERIFIED (search-summary) unless labelled ESTIMATE / INFERENCE; ENF = Evidence not found.

## 1. Cross-cutting findings

1. **Software layers in Belgian SME finance are crowded or platform-absorbed.** Of 40 opportunities, 12 were rejected outright because an incumbent already ships the feature (Odoo 19/20 bank matching and AI audit agent; Exact Purchase Agent; Corilus pharmacy margins; official 30bis REST API; Easy Cyber Protection NIS2 packs; CBAM tools' forecasting; Superfisc/Silverfin/Sofisk tax filing; Clearnox/Chaser dunning). 16 more are WEAK because the tool layer is cheap and contested (consolidation tools from EUR 39/month; Peliqan EUR 150/month connectors; Microsoft Finance Agents GA April 2026; OkiOki EUR 8-11/month document chasing).
2. **What survives is service-shaped work that AI makes cheap to deliver** and that incumbents are structurally unwilling to price down: fractional controlling/HQ reporting (day-rate incumbents), done-for-you consolidation (PwC now sells it to SMEs), QoE-light (mid-tier hourly models), DORA vendor packs (law firms hourly), co-ownership financing packs (nobody), Peppol portfolio operations (unowned across access points).
3. **Ghent is the Belgian "AI for accountants" cluster**: Silverfin (Visma, EUR 300M exit), Ravical (EUR 7.3M, 100+ practices), Dytto (EUR 1.5M), Cashfeed (EUR 1.3M, 350 clients), Eagl (EUR 825k), TenderWolf, plus Peliqan and Chift (Brussels, EUR 2.3M) on the data layer. A Brussels founder should not compete for the same Flemish accounting-firm buyer with a generic AI pitch.
4. **Regulation created fewer gaps than expected.** CSRD, CSDDD, EU AI Act high-risk, EUDR were softened or delayed; CBAM's 50-tonne threshold exempts ~90% of importers; Belgium missed pay-transparency transposition. Only the Peppol/e-reporting wave (BE 2026/2028, FR 2026/27, DE 2027/28, LU 2028) and DORA/NIS2 supply-chain cascades hold up.
5. **Price anchors matter.** Access points EUR 5-10/month per company; consolidation tools EUR 39-905/month; AI commentary USD 39-79/entity; NIS2 packs from EUR 25/client/month. Any product idea must be sold per firm or per group, not per SME, to clear these anchors.

## 2. Landscape by theme (major competitors)

### 2.1 Fractional controlling, FP&A and consolidation (U-031, U-021, U-023, U-024)
| Player | Product | Customer | Pricing | Funding/size | Geography | Strengths | Weaknesses | Positioning |
|---|---|---|---|---|---|---|---|---|
| Interim/freelance controllers (Apex League, Michael Page, Robert Half, HeadFirst) | Day-rate capacity | BE SMEs, subsidiaries | Controller EUR 600-800/day; CFO EUR 900-1,400/day | n/a | BE | Trusted, flexible | People-priced, no leverage; Dosign ruling pushes rates up | The price ceiling |
| EY FAAS / KPMG managed services | Outsourced reporting/consolidation | Subsidiaries, groups | ENF (Big-4) | Big-4 | BE | Brand, scale | Expensive for sub-EUR-50M | Top of market |
| Finvision, FinForces, Flow Partners, Fractional-csuite | CFO-as-a-service | SMEs, scale-ups | Flow: EUR 1,000-1,800/day | Small | BE | Local | Day-rate, no tooling story | Direct substitutes |
| Neno (NL), Skalar (DE) | Agent-first accounting/tax services | SMEs | Neno from EUR 80/mo | EUR 6.6M / EUR 12M | NL/DE; Neno to BE H2 2027 | Capital, AI-native | Bookkeeping/tax layer, not FP&A | Validate the model, adjacent layer |
| Easyclose, Finstack, Speedbooks, Liquid | SME consolidation/close SaaS | NL SMEs, firms | EUR 39-905/mo | Finstack $1.39M | NL | Cheap, transparent | Exact/Twinfield/AFAS-first; NL | Tool-layer price floor |
| BrightAnalytics, EMAsphere | Management reporting + consolidation | BE/NL SMEs | Quote | Private | BE | Belgian, Odoo/Exact connectors | Quote-only, no service | Belgian tool incumbents |
| Exact Consolidatie; Silverfin; Prophix/Sigma Conso; Lucanet | Incumbent consolidation | Exact users; firms; mid/large | Lucanet ~$1,200/user/yr + $5k+ impl. | Visma/PE | BE/EU | Installed base | Heavy or firm-channel | Top and channel |
| Odoo (native) | Consolidation app removed in v18; multi-ledger filtering | Odoo groups | Included | Odoo | BE | Installed base | Regression created a gap; partners fill with services | The wedge |
| PwC Belgium CaaS | Consolidation as a service | BE SMEs | ENF | Big-4 | BE | Validates demand | Big-4 pricing | Service validation |
| Microsoft Finance Agents, Copilot Excel Skills | Reconciliation + variance agents (GA 2026) | M365 users | ~GBP 360/user/yr on top | Microsoft | Global | Platform | D365/SAP connectors, not Odoo/Exact (INFERENCE) | Commoditises U-023 |
| Syft (Xero), Fathom, Datarails, Cube, Jirav, Abacum, Pigment, Endex | Reporting/FP&A/AI commentary | SMEs to enterprise | $39/entity to $150k/yr | VC | Global | Feature-complete | Priced for US/mid-market; Excel-connected | Floor and ceiling |

Entry point: none as software. As a service, the founder enters where nobody sells "done-for-you consolidation and HQ packs on Odoo/Exact at a fixed retainer below two controller days", then productises the Odoo-specific consolidation logic.

### 2.2 Peppol and e-reporting operations (U-002, U-004, U-005, U-012)
| Player | Product | Customer | Pricing | Size | Geography | Strengths | Weaknesses | Positioning |
|---|---|---|---|---|---|---|---|---|
| Billit | Access point + invoicing; per-invoice evidence files; per-account audit logs | SMEs, firms, vendors | ENF | 120k+ businesses, 2M+ invoices/mo (third-party) | BE | Dominant AP | Per account, not per portfolio | Most likely to add a portfolio view |
| Peppol Box | Cheap reception/sending; identifier-issue support | Micro-SMEs, firms | EUR 5-7/mo | 1,500+ companies | BE | Cheap, content on "problems 2026" | Small | Price anchor |
| Banqup (Unifiedpost), Yuki, Exact, Octopus, Teamleader | Peppol inside ledger | SMEs, firms | Bundled | Banqup 85k SMEs | BE/EU | Bundled | Single-vendor view | Incumbents |
| Cashfeed | AI AP agent incl. Peppol intake | SMEs, firms | Volume-based | EUR 1.3M, 350 clients | Ghent | Funded, fast | AP side, not exceptions | Adjacent |
| Codabox (Wolters Kluwer) | CODA/SODA/VOILA data pipes | Firms | Tiered per client | WK | BE | De-facto standard | Pipes, not analytics | Potential partner |
| Peliqan, Chift, Apideck/CData/Zapier, OSS MCP servers | Connectors/MCP for Benelux ledgers | Firms, SaaS, devs | Peliqan EUR 150/mo; Chift ENF | Chift EUR 2.3M | BE | Commoditised access | No pricing power | Enabling layer, not a business |
| Fonoa, Storecove, EDICOM, Comarch, Sovos, Vertex, DDD Invoices, A-Cube | Transmission / multi-country CTC | Mid-market to enterprise | Storecove ~EUR 495/mo per entity; Sovos USD 15k-250k | Funded | EU | Pipes for 2028 | Ignore firms' portfolio problem | Kill U-005 |
| Italian SIAC FTEL ADRI; Avalara SII content | Reported-vs-booked reconciliation abroad | IT/ES firms | ENF | n/a | IT/ES | Proves U-004 category | 2-4 years after mandate, by incumbents | Timing analogue |

Entry point: cross-access-point, per-client-portfolio exception and master-data dashboard for firms, service first; U-004 reconciliation engine from 2027.

### 2.3 Accounting-firm tooling and capacity (U-009, U-010, U-011, U-013, U-014, U-015)
| Player | Product | Pricing | Size | Notes |
|---|---|---|---|---|
| Ravical | AI "virtual employees" for expert firms, outcome-priced | ENF | EUR 7.3M, 100+ practices BE/NL/UK | Owns "capacity as software" |
| Dytto | AI assistant in firm email/docs | ENF | EUR 1.5M | Ghent |
| Silverfin (Visma) | Working papers, Assistant flags missing transactions; consolidation | Per file, 50-file minimum | 850 firms | Firm channel owned |
| OkiOki (Xerius) | Intake + client follow-up | EUR 8-11/mo | Social-secretariat channel | Kills U-009 localisation gap |
| Octopus, Fid-Manager, AdminPulse, COMAX UBO | Cheap practice/compliance tools | Free files; EUR 92/mo; EUR 290/mo | Belgian | Kill U-013, U-014 |
| Superfisc, Sofisk, Adsolut, Wally, WK monKEY AI, GenIA-L | Tax filing/AI assistance | ENF | Superfisc >40% of ISOC returns | Kill U-015 |
| Eastvantage, Aviaan, 2Max | Offshore capacity | USD 10-30/h; USD 200-750/client/mo | n/a | Price ceiling for U-011 |
| Clearnox, Twikey | Dunning, direct debit | EUR 100-549/mo | n/a | Kill U-010/U-037 |

Regulatory finding: ITAA registration is a legal requirement to perform accountancy for third parties; freelance dossier roles require an ITAA title (VERIFIED). Only non-reserved reporting/automation work is open to the founder.

### 2.4 Compliance cascades (U-043, U-044, U-045, U-046, U-047, U-048, U-054, U-062)
| Player | Product | Pricing | Notes |
|---|---|---|---|
| Vanta, Drata, Secfix | Security compliance automation, trust centres | USD 7.5-12k/yr; Secfix USD 12M Series A | Tech-firm persona |
| Easy Cyber Protection (BE) | CyFun-native NIS2 audit readiness via MSPs | EUR 25-9,075/client/mo | Kills U-045 |
| EcoVadis; IntegrityNext; 3rdRisk | Supplier ratings / buyer-side TPRM | On request | Buyer side |
| Hybridity (SE) | AI contract review vs DORA/NIS2/GDPR/CSRD; RoI builder | EUR 5M total | Buyer side; could extend |
| RegReportingDesk, DORApp | DORA RoI tooling for financial entities | ENF | Buyer side |
| Law firms (Norton Rose, DLA, penrose.law) | Bespoke DORA addenda | Hourly | Vendor-side substitute |
| VSME Reporter, VSME Ready, ExecutESG, Eevery, Coolset, Sunhat | VSME reporting | EUR 199/yr to EUR 99/mo | Eevery runs an accountant channel |
| CBAMBOO, Coolset, SAP, IntegrityNext | CBAM incl. cost forecasting | ENF | Kill U-047 |
| Lizenzero, Cleo Labs, Asuene | EPR/PPWR | <EUR 25/mo or GBP 200/registration | Kill U-048 |
| Figures, PayAnalytics, Syndio, Ravio; SD Worx/Acerta/Securex | Pay-gap analytics; payroll channel | Figures EUR 2,500/yr | Belgium not transposed |
| TPGenie, Reptune, Aibidia, Exactera, Coperitas | TP documentation | Quote | Adviser-guarded |

Entry point: vendor-side DORA pack (unowned, small); supplier bundle (unowned, credibility gap). Everything else rejected.

### 2.5 Verticals and services (U-038, U-042, U-064, U-067, U-068, U-071, U-072, U-073, U-089, U-092)
| Player | Product | Pricing | Notes |
|---|---|---|---|
| Robaws, Vertuoza, Trezy | Construction ERP / cash forecast with retention | Trezy EUR 7.50-32.50/mo; Vertuoza EUR 11.2M | Kill U-038 |
| TenderWolf, Tender Experts, GPC Gov | Tender discovery + AI analysis | EUR 79-149/mo | Discovery taken; bid-ops ENF |
| Baker Tilly, Moore, VGD, BDO, Vandelanotte; Rapid Diligence (US), Scalemetrics (CH) | DD / QoE | US from USD 8,900; CH CHF 8-60k; BE ENF | No Belgian productised QoE |
| Syndic24, TheSyndic, FMT, Konvivio (free tier) | Syndic software | EUR 2-4/lot/mo | Kill U-067 |
| Homegrade, Renolution, Fonds du Logement (ECORENO), KBC VME loan, Look&Fin; Flanders public VME financing tool (announced); French PPT software | Co-ownership financing/advice | Free / bank | No Belgian commercial planner |
| Corilus CareConnect | Pharmacy pricing/margin | Bundled | Kill U-071 |
| B-abel, PlanMolder; NAV member tools | Architect practice tools | ENF | Kill U-072 |
| TLV/ITLB cost tool | Free haulier cost-price tool | Free | Kill U-073 |
| WDC, Flowful, Aives, LTC, ClickForest; Crux Digits (NL) | AI audits/agencies | Crux EUR 2,500 audit, EUR 20k PoC | U-089 is a cash engine only |
| ~130 official Odoo BE partners | Odoo implementation | EUR 5-30k | U-092 skills bridge only |

## 3. Where this founder can realistically enter
1. Service-led controlling/consolidation for Belgian holdings and subsidiaries (2.1): the only place where the incumbents are people-priced and AI leverage is not yet productised.
2. Peppol portfolio operations for firms (2.2): unowned cross-access-point niche with a 2028 second act; low price anchor is the risk.
3. Productised analysis services with no Belgian productised competitor: QoE-light (2.5), DORA vendor pack (2.4), co-ownership financing packs (2.5). Each is one-off or low-recurrence.

## 4. Where not to enter (and why)
- Any "AI for accounting firms" generic pitch (Ravical, Dytto, Silverfin own it).
- Bank reconciliation, AP coding, dunning, cash forecasting, close checklists, document chasing (platform-absorbed or channel-owned).
- Regulation categories softened in 2025-26 (CSRD mid-caps, AI Act high-risk deployers, EUDR, SME CBAM) and anything gated by closed ecosystems (eHealth, Fednot, Boerenbond).
