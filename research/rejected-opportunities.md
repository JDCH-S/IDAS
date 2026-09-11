# Rejected opportunities database

Every idea dropped at any stage is recorded here with the reason categories from the brief (competitor, barrier, capital, regulatory, AI risk, founder fit, interest fit, other). "Stage" says where it died: SCREEN (universe -> 40), CI (competitive/existence check -> 20), DEEP (deep research -> top 10), RED (red team -> top 5), FINAL. Evidence for each item lives in `opportunity-universe.md` and `_raw/`.

Column key for the problem flags: C = competitor problem, B = barrier problem, K = capital problem, R = regulatory problem, A = AI-commoditisation risk, F = founder-fit problem, I = interest-fit problem, O = other. A dash means not the reason.

## Stage SCREEN (52 rejected at consolidation)

| ID | Idea | Market | Why it was investigated | Why rejected | C | B | K | R | A | F | I | O |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| U-001 | Peppol laggard onboarding / send-receive tooling | BE micro-SMEs | 660k enterprises still to onboard late 2025; fines | Send/receive layer commoditised: dozens of access points, OSS (phax, recommand), every package ships it | Y | - | - | - | Y | - | - | - |
| U-003 | UBL-without-PDF viewer | Bookkeepers | Practitioners complain about machine-only invoices | Free viewers exist; a feature, not a company | Y | - | - | - | Y | - | - | - |
| U-006 | Cross-border e-invoice format router API | Exporting SMEs, integrators | Patchwork of CIUS formats | Crowded (Storecove, Banqup, Vertex, Qvalia); OSS libraries make formats free | Y | - | - | - | Y | - | - | - |
| U-016 | Odoo statutory outputs (NBB XBRL/Biztax) | BE SMEs on Odoo | Odoo forum confirms gaps | Folded into U-021; Odoo can close the gap itself (platform risk) | Y | - | - | - | - | - | - | platform risk |
| U-018 | Human-in-the-loop validator marketplace | AI-accounting vendors, freelance accountants | Agent-native firms need licensed local review | Marketplace cold start on both sides; ITAA professional rules; no buyer found | - | Y | Y | Y | - | - | - | network effect required |
| U-019 | BE/LU agent-native bookkeeping firm | Micro-SMEs, freelancers | Neno (NL EUR 6.6M), Dougs, Pennylane show the model | Requires ITAA-licensed practice or partner; capital-heavy; Neno/Pennylane expanding; Botkeeper/Bench failure pattern | Y | Y | Y | Y | - | - | - | - |
| U-025 | Reporting-pack maintenance when structures change | FP&A | Lucanet/Datarails reviews | Feature of U-021/U-023 | - | - | - | - | - | - | - | feature not company |
| U-026 | ERP-to-BI consistency monitor | Controllers | Single Lucanet review | Thin evidence; feature | - | - | - | - | - | - | - | evidence too thin |
| U-029 | SME cash-flow forecasting | SME owners | 65% cite cash flow as top challenge | Agicap heavily funded; Xero JAX ships free payment-timing predictions; those priced out at EUR 99/mo unlikely to pay | Y | - | - | - | Y | - | - | - |
| U-030 | Management reporting as advisory product for firms | Firms | Advisory push | Merged into U-011/U-021; Emasphere, Silverfin, Yuki dashboards crowd it; evidence vendor-only | Y | - | - | - | - | - | - | - |
| U-032 | Anomaly/duplicate detection, non-Odoo ERPs | Controllers | Odoo 20 ships it | Every ERP will ship it; feature | Y | - | - | - | Y | - | - | - |
| U-033 | Audit-prep PBC automation | Audited BE companies | 60-120 hours per engagement (vendor) | Small Belgian audit universe; figures vendor-sourced; auditor portals exist | Y | - | - | - | - | - | - | small TAM in BE |
| U-034 | Audit-evidence automation for small audit firms | Small audit practices | DataSnipper USD 1B+ exit | Needs audit credentials and network; regulated; WK/Basis/Accrual funded | Y | Y | - | Y | - | Y | - | - |
| U-035 | Integration-health monitor | Bookkeepers | Connector failures across 4 vendors | Unclear buyer (vendor or firm); feature | - | - | - | - | - | - | - | no clear buyer |
| U-036 | Payroll-to-GL reconciliation | SME bookkeepers | SD Worx sells a training on it | Weak evidence; bundled in packages (Billit, Octopus, AFAS) | Y | - | - | - | - | - | - | evidence thin |
| U-039 | Generic contractor quoting software | Micro contractors | Excel quoting | Robaws, Buildbase, Billit, AFAS, Exact Bouw well established | Y | - | - | - | - | - | Y | - |
| U-041 | CheckInAtWork registration | Contractors on large sites | Daily obligation | Geodynamics and social secretariats serve it; hardware | Y | Y | - | - | - | Y | Y | - |
| U-049 | Mandatory CSRD tooling for mid-caps | 250-1,000 FTE firms | Big 2024-25 market | Directive (EU) 2026/470 removed them from scope; shrinking market | - | - | - | Y | - | - | - | demand removed by regulation |
| U-050 | EUDR due-diligence tooling | Wood/cocoa/coffee importers | Belgian chocolate exposure | Delayed twice (Dec 2026 / Jun 2027), simplification pending; IntegrityNext/osapiens exist | Y | - | - | Y | - | - | - | regulatory instability |
| U-051 | AI Act literacy / inventory / governance kit | SME deployers | Art. 4 in force, Art. 50 Aug 2026 | Real SME cost <EUR 2k/yr; high-risk deferred to Dec 2027/Aug 2028; free templates; 10+ startups | Y | - | - | Y | Y | - | - | low WTP |
| U-052 | DAC8 CASP reporting | EU crypto providers | Live Jan 2026 | Few hundred customers EU-wide; Taxdo/CoinTracking/Sovos exist | Y | - | - | Y | - | - | - | tiny TAM |
| U-053 | DAC7 platform reporting | Small marketplaces | Enforcement letters 2026 | Annual, vendors exist (Tipalti, Signicat), small BE TAM | Y | - | - | - | - | - | - | tiny TAM |
| U-055 | Whistleblowing channel SaaS | 50-249 FTE firms | Mandatory since 2023 | Commoditised from EUR 190/yr; social secretariats bundle | Y | - | - | - | Y | - | Y | - |
| U-056 | Outsourced DPO / GDPR docs | SMEs | APD priorities | Mature market; Digital Omnibus reduces burden | Y | - | - | Y | - | - | Y | - |
| U-057 | Digital product passport | Battery/textile makers | 2027 battery passport | Too early; engineering-heavy; Circularise-type vendors | Y | Y | - | - | - | Y | - | timing |
| U-058 | European Accessibility Act | E-commerce SMEs | Fines EUR 25-150k | Web/UX domain; Recite Me, Level Access, agencies | Y | - | - | - | - | Y | Y | - |
| U-059 | Mobility-budget TCO simulator | HR of 15-250 FTE employers | Mandatory 2027/2028 | Pluxee, Monizze, MoveMove, Skipr; feature | Y | - | - | - | - | - | - | feature |
| U-060 | Owner remuneration / dividend simulator | Accountants of owner-managers | Budget 2026-29 changes | One-off re-optimisation; small product; folded into U-014 | - | - | - | - | - | - | - | too small |
| U-061 | VAT provision-account monitoring | ITAA firms | May 2026 chaos | Transient government bug; folded into U-014 | - | - | - | - | - | - | - | transient |
| U-063 | Grant/subsidy financial reporting | Funded innovation SMEs | Horizon/VLAIO compliance | Thin evidence; PNO-type consultants entrenched | Y | - | - | - | - | - | - | evidence thin |
| U-065 | SME FX / treasury | Exporting SMEs | 89% do not stress-test FX | Regulated, capital-heavy, crowded (Alpha, iBanFirst, Trezy) | Y | Y | Y | Y | - | - | - | - |
| U-066 | Expense management / card-agnostic spend agents | SMEs 20-200 staff | Manual expense checks | Rydoo, Pleo, Payhawk, Spendesk, Sage/Fyle; card economics | Y | - | Y | - | Y | - | Y | - |
| U-069 | Flemish renovation-obligation tracker | Home buyers | 6-year deadline | Consumer, low WTP, first deadlines 2029 | - | - | - | - | - | - | Y | low WTP |
| U-070 | Rental management for landlords | Private landlords | Indexation, deposits | Rentio, Kotmaster, Rent Expert, Korfine | Y | - | - | - | - | - | Y | - |
| U-074 | GP-practice finance dashboard | GP group practices | New Deal, e-invoicing to insurers | eHealth-certified vendors (Corilus) gate the data; no founder access | Y | Y | - | Y | - | Y | - | - |
| U-075 | Care-home staffing-norm forecasting | Woonzorgcentra | Record inspections | Bottleneck is people not software; small wedge | - | - | - | - | - | Y | Y | wrong bottleneck |
| U-076 | Horeca margin visibility | Independent restaurants | Bankruptcies | Cash-poor customers; POS analytics crowded | Y | - | - | - | - | - | Y | low WTP |
| U-077 | Retail vacancy | Retailers, municipalities | Record vacancy | Macro problem, no software wedge | - | - | - | - | - | Y | Y | no wedge |
| U-078 | Energy-sharing settlement layer | Solar owners | 0.8% adoption | Blocker is supplier fee structure, not tooling; needs regulatory change | - | Y | - | Y | - | - | - | wrong bottleneck |
| U-079 | Solar/battery ROI simulator | Installers | Subsidies ended | Easily copied; feature of lead-gen | - | - | - | - | Y | - | - | no defensibility |
| U-080 | Heat-pump premium dossier automation | RESCert installers | Rejected files | Small niche; Fluvius may simplify portal | - | - | - | Y | - | - | Y | tiny |
| U-081 | EV charge-point compliance/billing | SMEs with parkings | >20 spaces rule | Saturated CPO/installer market | Y | Y | - | - | - | Y | - | - |
| U-082 | Small law-firm billing | 1-5 lawyer firms | 10-20% unbilled hours | Kleos, LEAP, Septeo, MV Office, Hammock | Y | - | - | - | - | - | - | - |
| U-083 | Micro non-profit accounts and UBO | Volunteer treasurers | Sloppy filings | Near-zero WTP; free filing | - | - | - | - | - | - | - | no WTP |
| U-084 | Farmer admin (MAP7, e-invoicing) | Flemish farmers | New obligations | Captive Boerenbond/SBB ecosystem; no sector ties from Brussels | Y | Y | - | - | - | Y | Y | - |
| U-085 | Wholesale/distribution ERP | Trading SMEs | Excel stock | Odoo (Belgian) dominant | Y | - | - | - | - | - | - | - |
| U-086 | Notarial-office tooling | Notaries | 1,200 offices | Closed Fednot ecosystem | - | Y | - | Y | - | - | - | closed ecosystem |
| U-087 | SME customs / forwarder admin | Exporters to UK | Broker fees | Thin Belgian evidence; port authority and brokers strong | Y | - | - | - | - | - | - | evidence thin |
| U-091 | Generic AI/automation agency | SMEs | Dozens exist in BE | Fails the brief's quality bar (generic agency, prompt-only moat) | Y | - | - | - | Y | - | Y | quality bar |
| U-093 | Cross-vendor finance-ops support concierge | SMEs | "Can't reach a human" | Low-margin service; fix is plan upgrade | - | - | - | - | - | - | Y | no scalable model |
| U-094 | Switching/migration assistant off Exact/Yuki | NL/BE SMEs | Price creep complaints | One-off, accountant-mediated, nobody pays | - | - | - | - | - | - | - | no WTP |
| U-095 | EU VAT/OSS for digital sellers | SaaS founders | Perennial HN pain | Solved by merchants of record (Paddle, Lemon Squeezy, Stripe Tax) | Y | - | - | - | - | - | - | - |
| U-096 | Cross-border freelancer invoicing | Freelancers | Country formats | Crowded, price-sensitive | Y | - | - | - | Y | - | Y | - |
| U-097 | Spend-card export reconciliation checker | Bookkeepers | Card-tool 1-star reviews | Hypothesis only; no evidence of the specific pain | - | - | - | - | - | - | - | no evidence |
| U-099 | Vendor-continuity ledger escrow | AI-bookkeeping customers | Bench/Botkeeper shutdowns | Feature; folded into U-012 | - | - | - | - | - | - | - | feature |

## Stage CI (to be appended after competitive/existence checks)

## Stage DEEP / RED / FINAL (to be appended)
