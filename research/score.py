#!/usr/bin/env python3
"""Scoring model for the 40 investigated opportunities.

Weights reflect the founder's goal: realistic part-time entry + strong founder fit
+ future resilience + upside. Each criterion is scored 0-10; higher is always
better for the founder (so 'competition' = 10 means uncrowded, 'initial_capital'
= 10 means almost none needed, 'barrier_to_entry' = 10 means easy for THIS founder).
Run: python3 research/score.py  -> writes opportunity-database.json and prints ranking.
"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent

CRITERIA = [  # (key, weight)
    ("customer_pain", 5), ("willingness_to_pay", 7), ("market_size", 3), ("market_growth", 2),
    ("ai_leverage", 4), ("ai_commoditization_resistance", 4), ("agi_resilience", 2), ("asi_resilience", 1),
    ("competition", 3), ("competitive_gap", 5), ("barrier_to_entry", 3), ("defensibility", 5),
    ("distribution_feasibility", 6), ("regulatory_feasibility", 4), ("belgium_launchability", 3),
    ("eu_expansion", 3), ("initial_capital", 4), ("time_to_first_revenue", 5), ("part_time_feasibility", 7),
    ("founder_fit", 10), ("interest_fit", 7), ("recurring_revenue", 4), ("large_company_potential", 3),
]
assert sum(w for _, w in CRITERIA) == 100

# id: (name, scores[23], status_after_CI, text fields dict)
S = {}
def add(id_, name, scores, status, **t):
    assert len(scores) == 23, id_
    S[id_] = dict(name=name, scores=scores, status=status, text=t)

add("U-031", "AI-native fractional controlling / HQ reporting for BE-LU subsidiaries and holdings",
    [7,8,5,6,7,6,4,3,6,7,8,4,7,8,8,6,10,9,6,10,8,8,4], "PROMISING",
    customer="Finance manager of a BE/LU subsidiary of a foreign group, or owner/CFO of a 3-15 entity Belgian holding",
    problem="Small local finance teams must produce HQ-format monthly packs, consolidation and commentary; interim controllers cost EUR 600-800/day",
    existing_solution="In-house controller, interim/freelance controller, Big-4 managed services, Excel",
    direct="Interim agencies (Apex League, Michael Page, Robert Half), Finvision, FinForces, Flow Partners, EY/KPMG managed services",
    indirect="Neno (NL, bookkeeping), Skalar (DE, tax), Datarails/Copilot used in-house",
    pricing="Controller EUR 600-800/day; CFO EUR 900-1,400/day (VERIFIED); retainer ESTIMATE EUR 1,000-3,000/month",
    market="Belgian foreign-owned subsidiaries count: Evidence not found; solo ceiling ~10 retainers = EUR 240k/yr (ESTIMATE)",
    barrier_type="LOW; GOOD once tooling and references accumulate, BAD while purely labour",
    capital="EUR 0-500", ttr="1-3 months", regulatory="Employment-contract side-activity clause; management reporting not ITAA-reserved (to confirm)",
    technical="Low for service; moderate for product (connectors + mapping)", distribution="Own network, Odoo integrators, firms refusing advisory")
add("U-021", "Done-for-you group consolidation and intercompany clean-up for Belgian holdings on Odoo/Exact, productised later",
    [7,7,5,6,7,6,4,3,4,6,7,5,6,7,8,7,9,8,6,10,9,8,5], "PROMISING",
    customer="Group controller / owner-CFO of 3-15 entity Belgian holding, often on Odoo 18/19 (consolidation app removed) or Exact",
    problem="Monthly Excel consolidation, unreconciled intercompany, no bank/board-grade group numbers; Lucanet too heavy",
    existing_solution="Excel, hiring a consolidation controller, Speedbooks/Finstack/Liquid (NL, Exact-first), PwC CaaS",
    direct="Easyclose EUR 705-905/mo (10 entities), Finstack from EUR 39/mo, Speedbooks EUR 69/mo, BrightAnalytics, EMAsphere, Exact Consolidatie, Silverfin, Prophix/Sigma Conso, Lucanet",
    indirect="Odoo partners (Gravitai), PwC consolidation-as-a-service, Power BI boutiques",
    pricing="Tool layer EUR 39-905/mo (VERIFIED); Lucanet ~$1,200/user/yr + implementation; freelance controller EUR 600-800/day",
    market="Belgian groups with 3+ entities: Evidence not found (ESTIMATE 5-10k); service SOM EUR 0.6-2.4M/yr",
    barrier_type="LOW-MODERATE; GOOD (domain templates, Odoo know-how, references)",
    capital="EUR 0-500 service; EUR 2-5k product", ttr="1-3 months", regulatory="Not statutory consolidation; ITAA scope to confirm; DPA for ledger data",
    technical="Moderate: LLM CoA mapping + IC matching + Odoo/Exact connectors", distribution="Odoo integrators, accounting firms, LinkedIn, hiring signal")
add("U-002", "Peppol portfolio operations for accounting firms (exception triage, master-data hygiene)",
    [6,5,4,8,5,5,4,3,5,6,8,4,6,8,9,7,10,7,8,7,7,7,4], "POSSIBLE",
    customer="Belgian accounting firms 5-50 staff whose clients sit on several access points and ledgers",
    problem="Rejected/undelivered e-invoices and bad identifiers delay cash and create fines; nobody sees the whole portfolio",
    existing_solution="Access-point support tickets, Excel lists, per-account audit logs (Billit), advisory content",
    direct="None named at portfolio level; Billit evidence files, Peppol Box identifier support, Cashfeed (AP side)",
    indirect="Peppolcheck.be (free), peppolvalidator.com, Taxilla middleware, ERP integrators bundling clean-up",
    pricing="Access points EUR 5-10/mo per company (VERIFIED); firm-level tool WTP: Evidence not found (INFERENCE EUR 50-150/mo)",
    market="5-7k firms x EUR 600-1,800/yr = EUR 3-13M/yr BE (ESTIMATE); SOM 30-100 firms",
    barrier_type="LOW; BAD (easy for Billit/Peppol Box to absorb) unless multi-AP data becomes an asset",
    capital="EUR 0-500", ttr="1-3 months (audit service)", regulatory="Data-quality work, not ITAA-reserved (INFERENCE); DPA needed",
    technical="Low-moderate: Python + OSS MCP servers + directory lookups", distribution="ITAA/AccountancyVandaag, OSS lead magnet, direct outreach")
add("U-004", "2028 e-reporting readiness and reported-vs-booked reconciliation", [5,3,5,9,5,5,4,3,5,7,7,5,6,8,9,7,9,2,7,7,7,8,5], "POSSIBLE",
    customer="Same firms as U-002 plus SMEs with POS/multiple invoicing systems", problem="Dual-sided near-real-time reporting from 2028 will expose mismatches between what FPS Finance sees and the ledger",
    existing_solution="Nothing yet; periodic VAT returns", direct="None in Belgium; Italian SIAC FTEL ADRI and Spanish SII reconciliation tools prove the category",
    indirect="Transmission vendors (Fonoa, Storecove, EDICOM), ledger vendors, Silverfin Assistant", pricing="Storecove ~EUR 495/mo per entity (VERIFIED); reconciliation WTP: Evidence not found",
    market="EUR 3-8M/yr BE ceiling from 2028 (ESTIMATE)", barrier_type="LOW; timing barrier (BAD: zero revenue before 2027)", capital="EUR 0-500", ttr="18+ months",
    regulatory="Same as U-002", technical="Moderate", distribution="Same as U-002")
add("U-011", "AI-assisted reporting/automation capacity partner for accounting firms with client stops", [8,6,5,7,7,5,4,3,4,5,6,3,6,4,8,5,10,8,6,8,6,7,3], "POSSIBLE",
    customer="Belgian firms 5-30 staff with client stops (56% of firms)", problem="Cannot hire; cannot deliver advisory/management reporting or build automations",
    existing_solution="Client stops, offshoring (USD 10-30/h), Ravical/Dytto software, price increases", direct="Ravical (EUR 7.3M, 100+ practices), Dytto, Eastvantage, Aviaan/2Max white-label",
    indirect="Silverfin Assistant, Exact Purchase Agent, Bizzcontrol", pricing="Offshore USD 200-750/client/mo (VERIFIED); firm rates EUR 50-150/h; on-shore reporting capacity: Evidence not found",
    market="~3,400 firms with client stops (VERIFIED share x INFERENCE base); solo cap 3-5 retainers", barrier_type="MODERATE; regulatory barrier is BAD (ITAA reserves accountancy for third parties)",
    capital="EUR 0-500", ttr="1-3 months", regulatory="ITAA registration legally required for accountancy for third parties; only non-reserved reporting/automation open; subcontracting rules: Evidence not found",
    technical="Low-moderate", distribution="Direct outreach, ITAA events, Fidushare")
add("U-064", "Productised QoE-light financial analysis for small Belgian acquisitions", [6,7,3,5,6,5,3,3,7,7,7,4,5,6,7,6,10,7,6,9,8,3,3], "POSSIBLE",
    customer="Buyers of EUR 0.5-5M businesses (individual acquirers, successions, small PE) and their accountants/brokers",
    problem="Below EUR 10M diligence is skipped or minimal; mid-tier fees uneconomic; buyers overpay or miss issues",
    existing_solution="Buyer's accountant 'has a look', lawyer checklists, skip DD", direct="None productised in BE; Baker Tilly/Moore/VGD/BDO/Vandelanotte bespoke; Rapid Diligence (US from USD 8,900), Scalemetrics (CH)",
    indirect="AI QoE tools for advisers (Finsider, Keye, Termina), brokers' light DD", pricing="US sub-5M USD 7-30k; CH CHF 8-60k; BE accountant EUR 80-150/h (VERIFIED); BE small-deal QoE: Evidence not found",
    market="850-950 announced BE deals/yr skew mid-market; addressable small deals: Evidence not found; solo 20 reports/yr = EUR 120k", barrier_type="LOW; GOOD (references, method), BAD (one-off)",
    capital="EUR 0-500", ttr="1-3 months", regulatory="Cannot sign as ITAA/IBR mission; position as buyer-side analysis; liability insurance", technical="Low-moderate (NBB XBRL, bank statements, normalisation)",
    distribution="Accountants with client stops, brokers, notaries, succession programmes")
add("U-068", "Brussels co-ownership renovation financing packs for syndics and facilitators", [6,3,4,7,5,6,5,4,8,7,6,5,4,6,9,5,10,5,7,7,6,3,4], "POSSIBLE",
    customer="Professional syndics and PEB experts/renovation facilitators in Brussels; the AG of co-owners decides",
    problem="Multi-year capex, per-lot allocation, prime/ECORENO stacking and loan vs reserve choices ahead of 2030/2033 PEB deadlines; AGs defer",
    existing_solution="Excel, PEB experts, free public advice (Homegrade), deferral", direct="None commercial in BE; French PPT tools (AnalysImmo, Bureau Veritas) exist because PPT is mandatory there",
    indirect="Homegrade/Renolution (free), Flemish public VME financing tool (announced), KBC VME loan desk, Look&Fin", pricing="Any paid planning tool: Evidence not found; pack ESTIMATE EUR 300-800",
    market="~22k Brussels buildings (ESTIMATE) x EUR 500 = EUR 11M one-off over 7 years", barrier_type="LOW-MODERATE; BAD (public free-tool risk, annual AG cycle)",
    capital="EUR 0-500", ttr="3-6 months (AG season)", regulatory="Credit-intermediary rules if recommending loans (to check); IPI rules", technical="Low (financial model + document extraction)",
    distribution="Syndics, Homegrade, PEB experts; slow annual decision cycle")
add("U-046", "DORA vendor pack for small ICT suppliers to financial entities (BE/LU/NL)", [5,6,3,4,6,5,3,3,7,7,8,3,5,7,8,7,10,7,8,6,5,4,2], "POSSIBLE",
    customer="SaaS/IT-services SMEs selling to banks, insurers, funds in BE/LU", problem="Bespoke Art. 30 addenda and Register-of-Information data requests from every client; negotiated 30 times",
    existing_solution="Own templates, law firms hourly, ISO 27001 as substitute", direct="No vendor-side product; Hybridity, RegReportingDesk, DORApp, 3rdRisk are buyer-side",
    indirect="Law firms, free regulation-dora.eu tools, Vanta/Drata trust centres", pricing="Pack price: Evidence not found; INFERENCE EUR 2-5k one-off + EUR 1k/yr refresh",
    market="1-3k relevant SMEs x EUR 2-3k = EUR 2-9M one-off pool (ESTIMATE); CSSF: 40% RoI filed by Mar 2026", barrier_type="LOW; BAD (low recurrence)",
    capital="EUR 0-500", ttr="1-3 months", regulatory="No licence; partner law firm for addendum", technical="Low (agent assembles pack from vendor documents)", distribution="LU/BE fintech networks, law-firm partnership")
add("U-043", "Supplier compliance passport (VSME + NIS2 + DORA) for non-tech Benelux SME suppliers", [6,5,5,7,7,5,4,4,4,6,5,6,4,6,8,7,8,5,5,5,5,8,6], "POSSIBLE",
    customer="50-250 FTE manufacturing/logistics/facility suppliers to large customers, banks", problem="5-20 questionnaires/yr in different formats answered by one office manager",
    existing_solution="Excel, prior answers, consultants, EcoVadis", direct="No bundler found; Vanta/Drata (USD 7.5-12k/yr, tech), Secfix, EcoVadis, Easy Cyber Protection (BE, MSP channel), VSME tools EUR 199/yr-99/mo",
    indirect="ISO 27001, CyFun Basic, buyer-side platforms (IntegrityNext, 3rdRisk)", pricing="Per pillar VERIFIED above; bundle WTP INFERENCE EUR 150-500/mo",
    market="3-6k BE firms x EUR 3k = EUR 9-18M/yr (ESTIMATE)", barrier_type="MODERATE; GOOD if evidence library becomes the asset; BAD credibility gap (no security background)",
    capital="EUR 500-2k", ttr="3-6 months", regulatory="None for founder; clients' obligations", technical="Moderate (evidence library + agent answering)", distribution="Accountants (VSME data) and MSPs (security)")
add("U-089", "Independent finance-automation ROI review for SME CFOs", [6,5,4,8,6,3,2,2,3,4,9,2,6,9,8,5,10,9,8,7,6,3,2], "POSSIBLE",
    customer="SME CFOs/CEOs who bought agency PoCs or plan AI spend", problem="95% of pilots fail; agencies' audits are conflicted lead magnets",
    existing_solution="Agency audit (free-EUR 2.5k), fractional CFO, abandon", direct="WDC, Flowful, Aives, LTC, ClickForest (BE agencies); Crux Digits (NL EUR 2.5k audit)",
    indirect="Big-4/Gartner, accountant, free AI Act checker", pricing="Crux EUR 2,500 audit; BE fractional CFO EUR 1,000-1,800/day (VERIFIED)",
    market="~11k AI-using BE firms >=10 staff; 2% x EUR 2.5k = EUR 0.55M/yr (ESTIMATE)", barrier_type="VERY LOW; BAD (no moat)", capital="EUR 0", ttr="<1 month",
    regulatory="None", technical="None", distribution="Accountants, CFO networks, LinkedIn")
add("U-042", "Belgian public-tender bid-ops pack (attests, erkenning, UEA, financial proofs)", [7,5,4,6,6,4,3,3,4,4,7,4,5,8,8,5,9,6,6,5,5,6,4], "POSSIBLE",
    customer="Construction/services SMEs bidding on Belgian public work", problem="80% report barriers; certificates, UEA, financial-ratio proofs unglamorous and Belgium-specific",
    existing_solution="Consultants, skip tenders, TenderWolf discovery", direct="TenderWolf EUR 79-149/mo (AI Quickscan), Tender Experts (Tender Chat), GPC Gov, UK drafting tools GBP 15-EUR 99/mo",
    indirect="BOSA e-Procurement (free), EBP training, ChatGPT", pricing="TenderWolf EUR 79-149/mo; Lucius EUR 99/mo (VERIFIED); bid-ops WTP: Evidence not found",
    market="Low thousands of paying SMEs x EUR 1-1.8k/yr = EUR 2-5M/yr (ESTIMATE)", barrier_type="LOW; BAD (incumbents adding AI fast)", capital="EUR 0-500", ttr="3-6 months",
    regulatory="None", technical="Low-moderate", distribution="Embuild/UNIZO, accounting firms")
add("U-012", "Vendor-neutral data/MCP/portability layer for Benelux accounting stacks", [4,3,4,6,7,3,3,2,2,3,7,2,5,9,8,6,9,4,7,7,8,5,3], "WEAK",
    customer="Firms, agencies, SMEs on Exact/Yuki/Silverfin/Billit/Odoo", problem="Lock-in fear (ITAA survey), vendor failure risk", existing_solution="Custom wrappers, Peliqan, Chift",
    direct="Peliqan EUR 150/mo, Chift (EUR 2.3M), Apideck/CData/Zapier MCP, OSS MCP servers for Yuki/Billit/Exact", indirect="Codabox, vendors' own agents", pricing="Peliqan EUR 1,800/yr (VERIFIED)",
    market="5-7k firms x EUR 1.8k = EUR 9-13M/yr already contested", barrier_type="VERY LOW; BAD (price to zero)", capital="EUR 0-500", ttr="6+ months", regulatory="None", technical="Moderate", distribution="OSS")
add("U-023", "Variance-commentary / management-reporting agent (Excel-native)", [6,4,5,7,8,2,2,2,2,3,7,2,5,9,6,7,9,5,7,9,8,6,3], "WEAK",
    customer="FP&A/controllers at mid-market and subsidiaries", problem="Hand-written packs", existing_solution="Excel, Copilot, Datarails/Pigment",
    direct="Microsoft Finance Agents (GA Apr 2026) + Copilot Excel Skills (Jun 2026), Syft $39-79, Fathom GBP 33, Datarails $24k+, Endex", indirect="Consultants",
    pricing="See direct (VERIFIED)", market="Services ceiling EUR 60-180k/yr", barrier_type="VERY LOW; BAD (platform bundling)", capital="EUR 0-500", ttr="3 months", regulatory="None", technical="Low", distribution="Fold into U-031")
add("U-024", "Reporting-pack tie-out agent", [5,3,3,5,8,2,2,1,4,3,8,2,4,9,6,7,10,4,8,8,7,4,2], "WEAK",
    customer="FP&A/CFO office", problem="Deck vs workbook vs ERP inconsistencies", existing_solution="Manual four-eyes, linking add-ins", direct="Endex ($14M, ties schedules to source), Copilot Skills, think-cell/UpSlide/Macabacus $200-360/user/yr",
    indirect="python-pptx scripts", pricing="Linking tools $200-360/user/yr (VERIFIED)", market="Feature-sized", barrier_type="VERY LOW; BAD", capital="EUR 0", ttr="n/a", regulatory="None", technical="Low", distribution="Feature of U-031")
add("U-022", "ERP data-extraction / reporting layer for Exact/Odoo/BC", [5,3,4,6,6,3,2,2,2,2,7,2,5,9,7,6,9,5,7,7,7,5,2], "WEAK",
    customer="Controllers, firms", problem="Native reporting weak", existing_solution="Manual exports, Power BI boutiques", direct="Peliqan $199/mo, 8+ Exact-Power BI vendors incl. free Invantive, Odoo App Store connectors, Jet/Exsion/Velixo",
    indirect="OSS Odoo MCP (384 stars)", pricing="Free to $199/mo (VERIFIED)", market="Commoditised", barrier_type="VERY LOW; BAD", capital="EUR 0", ttr="n/a", regulatory="None", technical="Moderate", distribution="OSS asset only")
add("U-027", "Month-end close orchestration for EU SME/lower mid-market", [7,6,6,7,8,4,3,2,2,3,4,4,4,8,6,7,6,3,4,8,8,8,6], "WEAK",
    customer="Controllers 50-1,000 FTE", problem="Spreadsheet close 6-15 days", existing_solution="Excel checklists", direct="Eagl (Ghent EUR 825k), Stacks ($35M), Easyclose/FinClose (any package), Numeric $51M, FloQast, Odoo 20 native agent",
    indirect="Datarails close", pricing="Easyclose EUR 705-905/mo (VERIFIED)", market="Contested", barrier_type="MODERATE; BAD (Ghent contested)", capital="EUR 5-20k", ttr="6-12 months", regulatory="None", technical="High", distribution="Hard")
add("U-005", "Multi-country e-invoicing control layer for small groups", [5,5,5,8,5,5,4,3,2,3,4,5,3,7,7,9,6,3,3,6,6,8,6], "WEAK",
    customer="CFO of Benelux group with 3-10 EU entities", problem="Patchwork of mandates", existing_solution="Multiple vendor contracts", direct="381 e-invoicing startups; DDD Invoices, A-Cube (May 2026 seeds), Storecove ~EUR 495/mo/entity, Banqup 85k SMEs, Sovos USD 15k-250k",
    indirect="Local accountants", pricing="VERIFIED above", market="Buyer count: Evidence not found", barrier_type="HIGH; BAD", capital="EUR 20k+", ttr="12+ months", regulatory="Multi-country", technical="High", distribution="Enterprise sales")
add("U-009", "Client document-chasing agent for firms", [8,6,6,5,8,4,3,2,1,1,5,3,4,8,7,6,7,4,5,5,5,8,4], "WEAK",
    customer="BE/NL firms", problem="#1 workflow pain", existing_solution="Email, penalties", direct="OkiOki (Xerius, EUR 8-11/mo, follows up with clients), Dytto EUR 1.5M, Silverfin Assistant, Ravical, ClearFacts, Liscio, Uku",
    indirect="Codabox feeds, Peppol", pricing="OkiOki EUR 8-11/mo (VERIFIED)", market="EUR 70-130M/yr contested", barrier_type="MODERATE; BAD", capital="EUR 2-5k", ttr="6+ months", regulatory="None", technical="Moderate", distribution="Channel-owned by Xerius")
add("U-010", "Accounting-firm own receivables / WIP-to-cash", [5,4,3,3,5,4,3,2,3,3,7,2,5,8,8,5,9,5,7,6,4,6,2], "WEAK",
    customer="BE firms 5-50 staff", problem="Unpaid fees (23% >EUR 100k: unverified)", existing_solution="Manual reminders", direct="Practice-management billing, Twikey, Clearnox EUR 100/mo",
    indirect="iController", pricing="Clearnox EUR 100+/mo (VERIFIED)", market="Narrow", barrier_type="LOW; BAD", capital="EUR 0-500", ttr="3 months", regulatory="None", technical="Low", distribution="Direct")
add("U-013", "Silverfin-lite working papers for small practices", [5,5,4,4,6,4,3,2,2,2,3,4,4,6,8,5,5,3,3,5,5,8,4], "WEAK",
    customer="1-10 person BE firms", problem="Silverfin quote-only, 50-file minimum", existing_solution="Excel, Octopus", direct="Octopus (free files), Fid-Manager EUR 92/mo, AdminPulse EUR 290/mo, Silverfin (claimed 90% of Flemish accountants, unverified)",
    indirect="WinBooks/Bob50", pricing="VERIFIED above", market="Served", barrier_type="HIGH; BAD (template moat)", capital="EUR 5-20k", ttr="12 months", regulatory="Belgian GAAP templates", technical="High", distribution="Hard")
add("U-098", "PSP/marketplace settlement reconciliation for EU e-commerce", [7,6,5,6,6,5,3,3,3,3,3,6,3,7,6,8,5,3,3,5,6,8,6], "WEAK",
    customer="E-commerce SMEs, marketplaces", problem="Payouts and fees don't reconcile", existing_solution="Excel, scripts", direct="Actuals (NL EUR 3M, Adyen partner), Ledge $9M, A2X/Synder $29-65/mo",
    indirect="Bookkeepers", pricing="VERIFIED above", market="Real but contested", barrier_type="HIGH; GOOD for incumbents", capital="EUR 5-20k", ttr="9+ months", regulatory="PSP data access", technical="High (connectors, always-on)", distribution="Hard")
add("U-044", "Finance-grade VSME data via accountants", [5,4,5,6,6,3,3,3,2,3,7,2,5,8,7,7,9,6,7,5,4,6,3], "WEAK",
    customer="SME suppliers; their accountants", problem="VSME requests from late 2026", existing_solution="Excel, EcoVadis", direct="10+ tools free to EUR 99/mo; VSME Ready EUR 199/yr; Eevery (accountant channel)",
    indirect="Consultancy EUR 3-15k", pricing="VERIFIED above", market="Cheap", barrier_type="VERY LOW; BAD", capital="EUR 0-500", ttr="3 months", regulatory="None", technical="Low", distribution="Accountants")
add("U-054", "Pay-transparency analysis for 100-249 FTE Belgian employers", [5,5,4,6,6,4,3,3,3,3,5,3,3,5,6,7,8,2,6,6,4,6,3], "WEAK",
    customer="HR/finance of mid-sized employers", problem="Gap analysis, joint pay assessment", existing_solution="Excel, social secretariat", direct="Figures EUR 2,500/yr, PayAnalytics, Syndio, Ravio; SD Worx/Acerta/Securex",
    indirect="Law firms", pricing="Figures EUR 2,500/yr (VERIFIED)", market="Transposition delayed; 100-249 count: Evidence not found", barrier_type="MODERATE; BAD (channel owned)", capital="EUR 500-2k", ttr="12+ months", regulatory="Belgian law pending", technical="Low", distribution="Social secretariats own it")
add("U-062", "Transfer-pricing documentation for mid-size Belgian groups", [5,6,3,4,6,4,3,3,3,2,3,3,3,4,6,6,8,4,5,5,4,6,2], "WEAK",
    customer="Tax managers at >EUR 50M/100 FTE entities", problem="Per-country detail from FY2025", existing_solution="Advisers", direct="TPGenie, Reptune, Aibidia, Exactera, Coperitas (quote-based); Big-4/mid-tier",
    indirect="Excel", pricing="Evidence not found", market="Small, adviser-guarded", barrier_type="HIGH; BAD (credentials)", capital="EUR 500-2k", ttr="6+ months", regulatory="Adviser-guarded", technical="Moderate", distribution="Hard")
add("U-038", "Micro-contractor retention/cash forecast", [7,4,5,4,5,4,3,3,2,2,5,3,3,8,8,4,7,4,5,5,4,7,3], "WEAK",
    customer="Small contractors", problem="Late payment, retentions", existing_solution="Excel", direct="Robaws (700+ BE customers, dealers), Vertuoza (EUR 11.2M, 3,000 users), Trezy (retention module EUR 7.50-32.50/mo)",
    indirect="Accountants", pricing="Trezy EUR 7.50-32.50/mo (VERIFIED)", market="79.5% of ~160k BE construction firms have no employees", barrier_type="MODERATE; BAD", capital="EUR 2-5k", ttr="6+ months", regulatory="None", technical="Moderate", distribution="Hard, cash-poor")
add("U-072", "Architect project profitability tool", [6,3,3,3,5,4,3,3,4,4,7,3,5,9,8,4,9,5,7,6,4,6,2], "WEAK",
    customer="Small architecture firms", problem="Fees below fair rate", existing_solution="Excel, B-abel", direct="B-abel, PlanMolder (BE); NAV (2,200 offices) builds member tools",
    indirect="Generic time tracking", pricing="Evidence not found", market="Tiny WTP", barrier_type="LOW; BAD", capital="EUR 0-500", ttr="6 months", regulatory="None", technical="Low", distribution="NAV")
add("U-067", "Syndic accounting/admin capacity", [7,5,4,5,6,4,3,3,2,2,4,4,4,4,9,4,6,4,4,5,4,7,3], "WEAK",
    customer="Professional syndics", problem="Shortage, admin overload", existing_solution="Syndic software", direct="7+ BE tools at EUR 2-4/lot/month plus free tier (Konvivio); Syndic24, TheSyndic, FMT",
    indirect="Volunteer syndics", pricing="EUR 2-4/lot/mo (VERIFIED)", market="Software cheap; labour is the gap", barrier_type="MODERATE; BAD (regulated profession)", capital="EUR 2-5k", ttr="6+ months", regulatory="IPI/BIV", technical="Moderate", distribution="Federations")
add("U-092", "Odoo Belgian-localisation setup/QA service", [5,6,4,6,5,4,3,2,2,2,6,2,5,9,9,5,9,7,6,6,6,3,2], "WEAK",
    customer="Belgian SMEs adopting Odoo", problem="Implementation heavier than marketed", existing_solution="~130 official BE partners, EUR 5-30k implementations", direct="Odoo partner network; Odoo ships l10n_be + Peppol natively",
    indirect="Freelancers", pricing="EUR 5-30k (VERIFIED)", market="Crowded", barrier_type="LOW; BAD", capital="EUR 0-500", ttr="1-3 months", regulatory="None", technical="Moderate", distribution="Partner ecosystem")
# CI rejects
add("U-007", "Structured-e-invoice AP coding for Odoo/Exact/Yuki", [6,5,5,6,8,2,2,2,1,1,5,2,4,8,7,6,7,4,5,6,6,7,3], "REJECT",
    customer="SME bookkeepers", problem="Manual coding", existing_solution="Bookkeeper", direct="Exact Purchase Agent, Yuki auto-booking, ClearFacts AIR, Odoo 19 AI, Cashfeed (350 clients)", indirect="OCR tools", pricing="Bundled", market="Owned by incumbents", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-014", "Belgian corporate compliance calendar for firms", [4,3,3,3,4,3,2,2,1,1,8,2,4,8,8,4,9,5,7,5,4,6,2], "REJECT",
    customer="ITAA firms", problem="Deadline juggling", existing_solution="Practice management", direct="COMAX UBO (integrates Silverfin), AdminPulse, Fid-Manager; regulator reminders", indirect="Outlook", pricing="Bundled", market="Solved", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Low", distribution="n/a")
add("U-015", "Biztax corporate-tax preparation agent", [5,5,4,5,7,3,2,2,1,1,3,3,3,3,8,3,7,3,4,6,5,7,3], "REJECT",
    customer="BE firms", problem="Tax season", existing_solution="Biztax/Silverfin", direct="Superfisc (>40% of ISOC returns), Silverfin, Adsolut, Sofisk, Wally, WK monKEY AI, GenIA-L", indirect="Manual", pricing="ENF", market="Attacked by incumbents", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="ITAA advice layer", technical="High", distribution="n/a")
add("U-028", "Odoo bank-reconciliation exception agent", [6,4,4,5,8,1,1,1,1,1,6,1,4,9,8,5,8,4,6,6,6,6,2], "REJECT",
    customer="Odoo SMEs", problem="Matching degrades", existing_solution="Manual", direct="Odoo 19 AI rules, Odoo 20 learning matcher, App Store AI modules, OCA modules", indirect="Yuki/Exact", pricing="Bundled", market="Platform absorbed", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-037", "Late-payment dunning for Belgian B2B SMEs", [6,5,5,5,6,3,2,2,1,1,5,2,4,8,8,5,7,5,5,5,4,7,3], "REJECT",
    customer="SMEs", problem="Payment gap 21 days", existing_solution="Manual", direct="Clearnox EUR 129-549/mo, Chaser GBP 199-599, iController/KBC, reminders in Billit/Yuki/Exact/Odoo, ATTA", indirect="Collection agencies", pricing="VERIFIED above", market="Crowded", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Low", distribution="n/a")
add("U-040", "30bis withholding check at AP payment run", [5,3,2,3,4,3,2,3,1,1,8,2,4,8,9,2,9,5,7,5,4,5,1], "REJECT",
    customer="Contractors", problem="Per-invoice check", existing_solution="Portal", direct="Official billRetainment REST API + free portal; Robaws, Billit, AFAS ship it; 30bis.be webservice", indirect="Social secretariats", pricing="Free/bundled", market="Solved", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Low", distribution="n/a")
add("U-045", "NIS2 evidence pack via MSP/accountant channel", [6,5,4,6,5,3,2,3,1,1,5,3,3,5,8,6,7,5,5,3,3,6,3], "REJECT",
    customer="Important entities", problem="84% not ready", existing_solution="MSPs", direct="Easy Cyber Protection (BE, MSP channel, EUR 25-9,075/client/mo), free CCB/Asphalia tools; only 2 BELAC CABs", indirect="Consultants", pricing="VERIFIED", market="Bottleneck is audit capacity", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-047", "CBAM certificate liability forecasting", [4,4,2,3,5,3,2,3,1,1,4,3,3,4,6,6,7,4,5,5,4,5,2], "REJECT",
    customer="Importers >50t", problem="Provisioning", existing_solution="Excel", direct="CBAMBOO, SAP, Coolset, IntegrityNext ship forecasting; ~4,100 declarants EU-wide", indirect="Big-4", pricing="ENF", market="Tiny", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-048", "PPWR multi-country EPR fee calculation", [4,4,4,5,5,3,2,3,1,1,4,3,3,5,5,7,6,4,5,3,3,6,3], "REJECT",
    customer="Consumer-goods SMEs", problem="Per-country EPR", existing_solution="Suppliers' declarations", direct="12+ tools, five under EUR 25/mo or GBP 200/registration; Lizenzero, Cleo Labs", indirect="Fost Plus/Valipac", pricing="VERIFIED", market="Cheap, product-heavy", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-071", "Pharmacy pricing/margin analytics", [5,4,3,3,5,3,2,2,1,1,3,3,3,4,8,3,8,4,6,5,4,6,2], "REJECT",
    customer="4,581 open pharmacies (2026)", problem="Margin setting", existing_solution="Wholesaler feeds", direct="Corilus ships price checker/margin tables and markets on the Sept 2025 change", indirect="Wholesalers", pricing="Bundled", market="Locked data, declining count", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Moderate", distribution="n/a")
add("U-073", "Haulier cost-per-km tool", [6,2,2,3,4,3,2,3,1,1,6,2,3,8,8,3,9,4,7,4,3,4,1], "REJECT",
    customer="Micro hauliers", problem="2% margins", existing_solution="Federation tool", direct="TLV/ITLB free member cost tool (road-cost.uantwerpen.be)", indirect="TMS", pricing="Free", market="Cash-poor, failing", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Low", distribution="n/a")
add("U-090", "Finance-automation playbooks for AI agencies", [3,3,3,5,6,2,1,1,3,2,9,1,5,9,8,5,10,7,8,5,4,4,1], "REJECT",
    customer="AI agencies", problem="Shallow finance depth", existing_solution="Improvise", direct="None; fold into U-089 as upsell", indirect="Agencies", pricing="ENF", market="Low ticket", barrier_type="n/a", capital="n/a", ttr="n/a", regulatory="None", technical="Low", distribution="n/a")

assert len(S) == 40, len(S)

def score(scores):
    return round(sum(s * w for s, (_, w) in zip(scores, CRITERIA)) / 10, 1)  # 0-100 scale

rows = []
for id_, d in S.items():
    sc = dict(zip([k for k, _ in CRITERIA], d["scores"]))
    t = d["text"]
    rows.append({
        "id": id_, "opportunity": d["name"], "customer": t["customer"], "problem": t["problem"],
        "existing_solution": t["existing_solution"], "direct_competitors": t["direct"], "indirect_competitors": t["indirect"],
        "pricing": t["pricing"], "market_size": t["market"], "willingness_to_pay": sc["willingness_to_pay"],
        "market_growth": sc["market_growth"], "ai_leverage": sc["ai_leverage"],
        "ai_commoditization_risk": 10 - sc["ai_commoditization_resistance"], "agi_resilience": sc["agi_resilience"],
        "asi_resilience": sc["asi_resilience"], "barrier_to_entry": 10 - sc["barrier_to_entry"], "barrier_type": t["barrier_type"],
        "capital_required": t["capital"], "time_to_first_revenue": t["ttr"], "belgium_feasibility": sc["belgium_launchability"],
        "eu_expansion": sc["eu_expansion"], "regulatory_difficulty": 10 - sc["regulatory_feasibility"],
        "technical_difficulty": t["technical"], "distribution_difficulty": 10 - sc["distribution_feasibility"],
        "defensibility": sc["defensibility"], "recurring_revenue": sc["recurring_revenue"], "founder_fit": sc["founder_fit"],
        "interest_fit": sc["interest_fit"], "overall_score": score(d["scores"]), "status": d["status"], "rejection_reason": "",
        "criteria": sc,
    })
rows.sort(key=lambda r: -r["overall_score"])
for i, r in enumerate(rows, 1):
    r["rank"] = i

# Final status after deep research, red teams and independent review (overrides CI status in the export).
FINAL = {
    "U-031": ("TOP-1 cash engine (OPP-A)", ""),
    "U-021": ("TOP-1 cash engine (OPP-A, service leg); product leg rejected", "Odoo 19/20 and EUR 39/entity SaaS cover consolidation tooling"),
    "U-064": ("TOP-2 only with ITAA/IBR signatory (OPP-C)", "Art. 3, 5 reserved activity; Analyzediz/Syno/Bol exist"),
    "U-046": ("TOP-3 side service (OPP-E)", "DoraPilot EUR 29-49/mo; weak recurrence; 500-1,050 vendors"),
    "U-002": ("RESERVE service wedge (OPP-B); product rejected", "Belgian Peppol Authority scanner cut errors 2.41%->0.31%; vendor views; Peliqan"),
    "U-004": ("RESERVE 2027 build (OPP-B second act)", "Dataset only in early-2027 Royal Decree; foreign analogues bundled into software"),
    "U-068": ("RESERVE (OPP-D)", "Primes gone; ECORENO closed to ACPs; free facilitator; calendar slipped"),
    "U-043": ("RESERVE (OPP-F)", "Kube ESG, EcoVadis Vitals, CyFun Small occupy the passport layer; Sunhat funded"),
    "U-011": ("FOLDED into OPP-A / venture experiment", "ITAA reserved activities; subcontracting route only"),
    "U-089": ("CASH-ENGINE option, not a company", "No moat; agency lead-magnet"),
    "U-042": ("WEAK", "TenderWolf and Tender Experts add AI; bid-ops WTP unproven"),
}
for r in rows:
    if r["id"] in FINAL:
        r["status"], reason = FINAL[r["id"]]
        r["rejection_reason"] = reason
    elif r["status"] == "WEAK":
        r["rejection_reason"] = "Crowded or platform-absorbed software layer; kept only as asset or reference (see top-20.md)"
    elif r["status"] == "REJECT":
        r["rejection_reason"] = "Already built by incumbents or no wedge (see rejected-opportunities.md, stage CI)"
(HERE / "opportunity-database.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False))
for r in rows:
    print(f'{r["rank"]:2d} {r["id"]} {r["overall_score"]:5.1f} {r["status"]:9s} {r["opportunity"][:70]}')
