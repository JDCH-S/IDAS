# Stream A — Finance, accounting & controlling workflows in EU SMEs, mid-market and accounting firms

Explorer run: 2026-09-11. Tooling: WebSearch only (no page fetches). All figures come from search-result summaries; the URL relied on is recorded per item. Numbers taken from vendor blogs are flagged as such — treat them as directional, not audited.

## Queries run (44)

1. Peppol e-invoicing Belgium 2026 mandate SME problems boekhoudkantoor
2. boekhoudkantoor personeelstekort 2026 accountants tekort België
3. fiduciaire pénurie comptables Belgique 2026 charge de travail
4. month-end close survey 2026 days to close spreadsheets mid-market finance teams
5. consolidatie KMO groepen Excel intercompany afstemming software
6. cash flow forecasting SME spreadsheet pain survey 2025 2026 Europe
7. Belgium e-reporting 2028 near real-time VAT reporting requirements
8. Germany e-invoicing 2027 2028 mandate KMU Herausforderungen Steuerberater
9. FP&A budgeting Excel survey 2026 percentage finance teams still use spreadsheets mid-market Europe
10. Exact Online rapportage beperkingen Power BI export grootboek klachten accountant
11. Odoo accounting reporting limitations Belgium consolidation intercompany complaints
12. Silverfin funding accounting firms Belgium 2025 2026 Visma acquisition adoption
13. accounts payable automation Belgium SME funding 2025 2026 startup Peppol invoice processing
14. transfer pricing documentation SMEs Belgium local file threshold 2026 cost consultant
15. retards de paiement Belgique PME 2026 délai moyen recouvrement créances impayées étude Graydon
16. audit preparation SME time spent auditor requests PBC list pain 2026
17. sociaal secretariaat loonboeking import boekhouding manueel Excel koppeling SD Worx Acerta Exact Online klachten
18. subsidie financiële rapportering VLAIO Horizon Europe timesheets KMO administratieve last audit
19. financial due diligence small M&A SME Belgium cost quality of earnings price €
20. SME FX hedging treasury management mid-market Europe survey spreadsheets 2025 2026 pain
21. facturation électronique France septembre 2026 PME expert-comptable difficultés PDP réforme
22. Luxembourg fiduciaire shortage accountants 2026 e-invoicing Peppol Luxembourg B2B mandate
23. accounting firms offshoring India outsourcing bookkeeping Belgium Netherlands 2026 growth capacity
24. management reporting accountantskantoor KMO klant dashboard maandrapportering tijd kosten adviesrol
25. Steuerberater Fachkräftemangel 2026 Mandanten ablehnen Kanzlei Kapazität Umfrage
26. maandafsluiting MKB financieel controller Excel handmatig tijd afsluiting onderzoek Nederland 2025 2026
27. clôture mensuelle PME Excel rapprochements bancaires DAF temps perdu enquête 2025 2026
28. Business Central financial reporting Excel export pain Jet Reports consolidation multi-company SME
29. European finance automation startup raises seed Series A 2026 accounting close AI agents month-end
30. Belgian fintech startup raises 2026 accountants AI bookkeeping Peppol Ghent Brussels funding
31. ViDA VAT in the digital age 2030 digital reporting requirements SME impact intra-EU cost
32. expense management Belgium SME onkostennota's manueel verwerking kosten software Rydoo Spendesk prijs
33. consolidatieplicht België groottecriteria 2024 kleine groep vrijstelling geconsolideerde jaarrekening holding KMO
34. Peppol facturen zonder PDF boekhouder leesbaar UBL visualisatie probleem 2026 accountant
35. CODA bestanden bank afpunten boekhouding manueel tijd KMO automatisering afpunting open posten
36. credit management software Belgium iController Clearnox pricing SME dunning automation
37. multi-entity accounting close UK US mid-market pain "intercompany" spreadsheets survey 2026 CFO
38. ITAA aantal kantoren België accountants omzet per dossier prijsdruk forfait boekhouding tarief 2026
39. Silverfin Yuki Billit API data export accountant reporting limitations Excel klachten
40. accountants time chasing clients missing documents bookkeeping client collaboration pain survey 2026
41. ITAA blog softwaremarkt onder druk 1.642 confraters concentratie afhankelijkheid softwareleveranciers prijsstijgingen
42. jaarrekening neerleggen NBB XBRL Biztax export Odoo Exact Online probleem accountant manueel overtypen
43. Making Tax Digital ITSA April 2026 accountants capacity workload quarterly updates practice survey
44. vacature financial controller Brussel consolidatie Excel intercompany rapportering 2026 KMO groep

---

## Raw opportunities

### A-01. Post-mandate Peppol clean-up for Belgian SMEs (late registrants, penalties, master-data)
- Problem: The Belgian B2B Peppol mandate went live 1 Jan 2026 as a "big bang"; tolerance ended 31 Mar 2026 and progressive fines (EUR 1,500 / 3,000 / 5,000) apply since 1 Apr 2026. A large share of SMEs registered late and many still struggle with data quality (customer/supplier master data, Peppol IDs) and mixed-format inbound flows.
- Who suffers: Belgian VAT-registered SMEs (est. 1.2M VAT entities in scope) and the boekhoudkantoren/fiduciaires that carry their compliance.
- Frequency/cost signal: VERIFIED (search-summary): 54% of SMEs waited until the final six months to register on Peppol, 20% registered after the mandatory date; half of SMEs report time savings but a third report time loss; penalty ladder EUR 1,500/3,000/5,000. Continuous (every invoice).
- Current workaround: Software vendor "Peppol modules", PDF-to-UBL conversion services, accountant does it for the client.
- Spend signal (WTP): Certified access points and Peppol registration providers marketplace (peppolcheck.be); Cashfeed raised EUR 1.3M for AI invoice collection incl. Peppol; penalties create forced WTP.
- Existing players noticed: Banqup/Unifiedpost, Billit, Cashfeed, Peppol Box, EasyPost (PDF->UBL), Odoo, Exact, Yuki, Wappli, InvoX.
- Why now / what changed: Mandate live since Jan 2026; enforcement since Apr 2026; 2028 e-reporting layered on top.
- Evidence URLs: https://itdaily.com/blogs/software/peppol-smes-time-savings/ ; https://www.banqup.com/resources/blog/belgium-s-2026-e-invoicing-mandate-what-have-we-learned-so-far- ; https://peppolvalidator.com/peppol-belgium
- Quick take: crowded on "send/receive", but the operational mess (data quality, exceptions, late adopters, penalties) still looks under-served; promising as a wedge, weak as a standalone product.

### A-02. Machine-only Peppol invoices (UBL without PDF) break the bookkeeper's review workflow
- Problem: Peppol BIS 3.0 makes the PDF attachment optional; many suppliers omit it, so accountants receive XML that humans cannot read, breaking review, approval and archiving habits. Software vendors used the mandate to push their own invoicing tools onto firms.
- Who suffers: Belgian accounting firms (esp. <10 staff, which is ~3/4 of ITAA firms) and SME AP clerks.
- Frequency/cost signal: VERIFIED (search-summary) that the problem is widely reported by Belgian practitioners (Peppol Box "real problems 2026", codaboekhouders FAQ); volume/cost not quantified — ESTIMATE: every inbound invoice from a supplier without PDF.
- Current workaround: Free UBL viewers, convert-to-PDF tools, vendor-locked accounting software imports.
- Spend signal (WTP): Not quantified. Evidence not found for pricing.
- Existing players noticed: Peppol Box, e-invoice.be, EasyPost, Codabox, Billit.
- Why now / what changed: Mandate since Jan 2026; scale of UBL-only flows growing.
- Evidence URLs: https://www.peppol-box.be/nl/blog/peppol-belgie-problemen-2026/ ; https://codaboekhouders.be/7-veelgestelde-vragen-over-peppol-met-praktische-antwoorden/ ; https://liberoo.be/blog/bereid-je-voor-peppol-facturatie-verplicht-voor-ondernemers-vanaf-2026
- Quick take: real but small; likely a feature, not a company. Weak-to-unclear.

### A-03. Belgian 2028 near-real-time VAT e-reporting (5-corner Peppol) for SMEs and their accountants
- Problem: From 1 Jan 2028 both supplier AND customer must report a subset of invoice data to FPS Finance via Peppol (5-corner model) within ~5 days; POS/payment/invoicing systems must transmit automatically; annual client listing disappears. SMEs with legacy or mixed systems and accountants doing periodic bookkeeping cannot meet near-real-time cadence with batch processes.
- Who suffers: Belgian SMEs with POS/payment flows and B2B sales; accounting firms doing quarterly VAT for hundreds of clients.
- Frequency/cost signal: VERIFIED (search-summary): law approved (VATupdate 23 Jul 2026), effective 1 Jan 2028, 5-day deadline aligned with ViDA. Cost per business not found.
- Current workaround: Nothing yet; periodic VAT returns and annual client listing.
- Spend signal (WTP): Compliance-driven; vendors (EDICOM, Fonoa, Taxually, RTC Suite, Nymus) already marketing.
- Existing players noticed: Fonoa, Taxually, EDICOM, RTC Suite, Innovate Tax, Nymus, Banqup, Billit.
- Why now / what changed: Law passed July 2026; 16 months to go; accounting firms have to re-engineer periodic bookkeeping into continuous flows.
- Evidence URLs: https://www.vatupdate.com/2026/07/23/belgium-approves-dual-near-real-time-vat-e-reporting-for-2028/ ; https://www.fonoa.com/resources/blog/belgium-introduce-near-real-time-e-reporting-from-2028 ; https://nymus.be/en/belgium-takes-next-step-in-e-reporting-whats-in-store-for-companies/
- Quick take: promising timing-wise (window before 2028), but big vendors will own the pipes; opportunity is in readiness/reconciliation (what was reported vs what was booked) rather than transmission.

### A-04. Belgian accounting firms turn away clients because of structural staff shortage
- Problem: Firms cannot hire; workload rises; they refuse new dossiers and quality risk increases.
- Who suffers: Belgian boekhoudkantoren/fiduciaires (ITAA: ~15,000 members, ~35,000 people in the sector serving 99% of Belgian enterprises); SMEs who cannot find an accountant.
- Frequency/cost signal: VERIFIED (search-summary): 60% of Belgian accountancy firms report staff shortages (Exact survey); ">80% of Belgian firms report a structural shortage, main reason for refusing new client files; 1 in 5 firms contacted turns the entrepreneur away" (extrait-de-kbis.net, secondary source); "comptable" is an official shortage occupation; firms offering signing bonuses and 4-day weeks (FED Group).
- Current workaround: Refusing clients, overtime, offshoring (Eastvantage markets to Belgian accountants), AI pilots (22% have integrated AI per Exact survey).
- Spend signal (WTP): Hourly rates 50-150 EUR; offshoring at USD 8-12/h bookkeeping; Dytto raised EUR 1.5M pre-seed to "free the accountant"; Silverfin sold for EUR 300M.
- Existing players noticed: Silverfin (Visma), Dytto, Yuki, Exact, Wolters Kluwer Adsolut, Octopus, Billit, Eastvantage.
- Why now / what changed: Demographics + Peppol + e-reporting 2028 pile work onto a shrinking workforce; generative AI makes junior-level work automatable.
- Evidence URLs: https://www.exact.com/benl/nieuws/1-op-de-2-belgische-accountancykantoren-kampt-met-personeelstekort-met-grote-gevolgen-voor-werkdruk-en-omzet ; https://www.extrait-de-kbis.net/expert-comptable-belgique-2/ ; https://itaa.prezly.com/
- Quick take: promising as macro driver; too broad on its own — needs a specific task wedge (see A-06, A-08, A-13).

### A-05. Accounting firms' own receivables: unpaid client invoices cost firms >EUR 100k
- Problem: Accounting firms are bad at collecting their own fees; revenue leakage from unpaid invoices while staff are overloaded.
- Who suffers: Belgian accountancy firms (esp. 5-50 staff).
- Frequency/cost signal: VERIFIED (search-summary, Exact survey): 23% of responding firms lose more than EUR 100,000 in revenue due to unpaid invoices.
- Current workaround: Manual reminders, withholding filings, ad hoc.
- Spend signal (WTP): Not found specific to firms; generic dunning tools exist (Clearnox, iController).
- Existing players noticed: Clearnox, iController (KBC-backed), Chaser; practice-management tools (Uku, Silverfin) have some billing.
- Why now / what changed: Margin pressure + shortage make leakage more painful; e-invoicing makes fee invoices structured.
- Evidence URLs: https://accountancyvandaag.be/1-op-de-2-belgische-accountancykantoren-kampt-met-personeelstekort-met-grote-gevolgen-voor-werkdruk-en-omzet/ ; https://clearnox.com/en/
- Quick take: surprising, narrow, but a clean niche (WIP-to-cash for firms). Unclear size.

### A-06. Chasing clients for missing documents/data is the #1 workflow pain in accounting firms
- Problem: Firms spend enormous time asking clients for missing invoices, bank statements, explanations; late/unprepared clients block closes and filings.
- Who suffers: Accounting firms in BE/NL/UK/US; SME owners who are the bottleneck.
- Frequency/cost signal: VERIFIED (search-summary): 2026 survey across 8 countries: ~7 in 10 firms would hand "chasing clients for missing documents" to an AI agent first; Wolters Kluwer survey of ~2,000 US firms ranks "late and unprepared clients" #1; 65.2% cite getting documents from clients as biggest workflow challenge (2024, up from 53.8%); vendor estimate 18-25 h/month per senior staff on follow-up (USD 1,350-2,375/month). Sources are largely vendor blogs.
- Current workaround: Email, WhatsApp, portals, spreadsheets of open items.
- Spend signal (WTP): Client portals/collection tools (Liscio, Jupid, Uku, Finlens, OnboardMap) exist; pricing not captured.
- Existing players noticed: Liscio, Jupid, Uku, Finlens, Silverfin (client requests), Dytto.
- Why now / what changed: Peppol removes the "missing purchase invoice" class of chase partially, but explanations/context chases remain; AI agents now credible.
- Evidence URLs: https://www.liscio.me/resources/how-accounting-firms-can-automate-client-document-collection ; https://jupid.com/blog/client-document-collection-software ; https://gridex.dev/blog/why-cpa-firms-lose-time-chasing-client-documents/
- Quick take: crowded in the US; BE/NL-localised, Peppol/CODA-aware version could be promising.

### A-07. Month-end close still spreadsheet-driven; mid-market closes take 6-15 days
- Problem: Close coordination, task tracking, reconciliations and journal support live in Excel and email; controllers spend time on file management rather than analysis.
- Who suffers: Mid-market finance teams (50-1,000 employees) in BE/NL/FR/DE; SMEs without a controller.
- Frequency/cost signal: VERIFIED (search-summary): only 18% of finance teams close in <=3 days, 50% take >5 business days, APQC median 6.4 days; Gartner estimate 62% of finance orgs use spreadsheets as primary close tool; NL practitioner blogs report real cycles of 8-15 working days; vendor claim 300-1,000 person-hours per mid-market close (vendor blog, ESTIMATE).
- Current workaround: Excel checklists, shared drives, email, manual JE support.
- Spend signal (WTP): Close-management software category (FloQast, BlackLine, Spendesk close, Easyclose NL, XLReporting NL); Stacks raised USD 23M Series A for agentic close automation; Round Treasury EUR 5.1M seed.
- Existing players noticed: BlackLine, FloQast, Stacks, Easyclose, XLReporting, Datarails, ChatFin.
- Why now / what changed: AI agents for reconciliations and JE; APIs on Exact/Odoo/BC make data pulls feasible.
- Evidence URLs: https://chatfin.ai/blog/month-end-close-time-by-industry-finance-benchmark-2026/ ; https://www.xlreporting.com/blog-nl/duurt-maandafsluiting-langer-dan-week ; https://stacks.ai/resources/stacks-raises-23-million-to-reinvent-finance-operations-with-agentic-ai
- Quick take: crowded at enterprise; under-served for EU SME/lower mid-market on Exact/Odoo/BC — promising if narrowed.

### A-08. Bank reconciliation / afpunten of open items remains manual in SMEs despite CODA
- Problem: Matching bank lines to open AR/AP items, splitting payments, handling unknown payers still consumes daily time; Belgian CODA/Codabox automates statement ingestion, not the judgement.
- Who suffers: SME bookkeepers and accounting-firm staff (BE, FR).
- Frequency/cost signal: VERIFIED (search-summary, FR vendor blog): manual bank reconciliation takes 30 min-1 h per day in an active SME (125-250 h/year); "up to 5 h freed per monthly close". Belgian-specific quantification: Evidence not found.
- Current workaround: CODA + accounting package suggestions, Excel reconciliations.
- Spend signal (WTP): Codabox subscriptions for CODA delivery (price not captured); AI matching features being bundled by packages.
- Existing players noticed: Codabox, Octopus, Youinv, Scrada, Spendesk, JUWA (FR), Odoo.
- Why now / what changed: AI matching commoditising inside packages.
- Evidence URLs: https://juwa.co/blog/actualites-tendances-ia/automatisation-reconciliation-bancaire-ia-pme/ ; https://faq.codabox.com/nl/support/solutions/articles/75000057589-word-klant-als-kmo-ontvang-coda-bestanden ; https://youinv.com/nl/blog/reconciliation-bancaire
- Quick take: weak as standalone — being absorbed by accounting packages.

### A-09. Management consolidation and intercompany reconciliation for SME groups (holding + opcos)
- Problem: Belgian and Dutch SME groups (family holdings, management companies, multi-entity operators) consolidate monthly in Excel; intercompany balances don't reconcile; Odoo/Exact lack legal consolidation and eliminations; small groups are legally exempt from statutory consolidation so they never bought proper tooling, but banks/boards/buyers still want group numbers.
- Who suffers: Group controllers / part-time CFOs in SME groups (3-30 entities, EUR 10-200M revenue); accounting firms that do the consolidation for them.
- Frequency/cost signal: VERIFIED (search-summary): 80% of multi-entity firms report intercompany bottlenecks (Intuit benchmark); 99% of finance stakeholders struggle with intercompany (BlackLine 2023); multi-entity consolidation takes 5-12 days in mid-market (vendor blog); intercompany elimination errors described as the most common audit finding in mid-market group accounts (vendor blog). Belgian job market: multiple live "Financial Controller & consolidatie" vacancies at SMEs (Michael Page Waregem/Deerlijk, Sept 2026) — hiring signal. Belgian statutory: small groups exempt (thresholds EUR 11.25M turnover / EUR 6M balance sheet / 50 FTE, +20% on aggregated basis).
- Current workaround: Excel workbooks, Emasphere, Speedbooks, Liquid, Lucanet (too expensive), Jet Reports on BC.
- Spend signal (WTP): Hiring a group controller (BE salary range not captured but roles exist); Lucanet/Emasphere licences; vendor claim "save up to 67% of time" (Emasphere).
- Existing players noticed: Lucanet, Emasphere (BE), Speedbooks (NL), Liquid (NL), Jet Reports/insightsoftware, Odoo consolidation module, Velixo, Exsion365.
- Why now / what changed: Odoo/Exact/BC APIs; new 2024 size thresholds; PE/holding roll-ups of SMEs increase multi-entity count; AI can propose eliminations.
- Evidence URLs: https://chatfin.ai/blog/ai-agents-multi-entity-consolidation-cfo-guide-2026/ ; https://www.odoo.com/forum/help-1/does-odoo-also-have-a-legal-consolidation-instead-of-only-an-aggregation-175419 ; https://jobs.accaglobal.com/job/13914949/financial-controller-and-consolidatie-waregem-/?TrackID=9
- Quick take: promising — fits founder skills exactly; crowded at top (Lucanet) but thin at Odoo/Exact/Yuki-based SME groups.

### A-10. Getting data out of Exact Online / Odoo / Business Central for reporting is a cottage industry
- Problem: Native reporting cannot do multi-entity, YoY comparisons, custom KPIs or blend external data; exports are slow and API limits/authorisation errors break dashboards. Result: manual Excel exports every month.
- Who suffers: Controllers at SMEs on Exact Online (NL/BE), Odoo (BE), Business Central; accounting firms serving them.
- Frequency/cost signal: VERIFIED (search-summary): Exact Online standard reporting "does not support multiple entities, limited YoY, custom KPIs hardly possible"; many organisations "run into slow exports and limited reporting"; BC has at least 7 competing Excel-reporting add-ons (Jet, Exsion365, Velixo, Solver...). Monthly recurrence; cost not quantified.
- Current workaround: Manual export to Excel; buying a Power BI connector (exactpowerbi.nl, brixxs, Chef Data, Datakingdom, Dataspark); Jet Reports.
- Spend signal (WTP): Several NL boutiques exist solely to connect Exact Online to Power BI (prices not captured); insightsoftware/Jet is a large business.
- Existing players noticed: Brixxs, Chef Data, Datakingdom, Dataspark, Peliqan (BE, cross-source SQL incl. Silverfin/Yuki/Billit/Exact/AFAS), Jet Reports, Exsion365, Velixo, Cosmos.
- Why now / what changed: APIs + MCP/AI agents; Peliqan already marketing "Silverfin MCP for Belgian accountants".
- Evidence URLs: https://www.datakingdom.nl/exact-online-rapportages-automatiseren/ ; https://erpsoftwareblog.com/2026/08/7-excel-reporting-tools-for-business-central-finance-teams/ ; https://peliqan.io/blog/silverfin-mcp-belgian-accountants/
- Quick take: crowded but fragmented; promising as an enabling layer for A-09/A-11, not as an end product.

### A-11. FP&A/budgeting in spreadsheets with stale data in mid-market
- Problem: Budgets, forecasts and management reports are built in Excel from stale exports; version chaos; decisions on old data.
- Who suffers: FP&A/controlling teams in 100-1,000 employee companies; SMEs without FP&A.
- Frequency/cost signal: VERIFIED (search-summary): 96% of FP&A professionals use spreadsheets weekly for planning (AFP 2025); spreadsheets cited as primary budgeting tool by 61% of finance leaders; Limelight 2026 report: ~100% spreadsheet dependency, 82% deciding on stale data, 33% say spreadsheet reliance is #1 tech challenge. Europe-specific split not found.
- Current workaround: Excel + templates; Datarails/Vena/Cube style "Excel-connected" platforms.
- Spend signal (WTP): Record finance tech spend reported (Limelight); many funded vendors.
- Existing players noticed: Datarails, Vena, Cube, Prophix, Limelight, Abacum, Agicap, Pigment.
- Why now / what changed: AI in Excel; mid-market tools still priced for >EUR 50M companies.
- Evidence URLs: https://goinvest.com/2026/05/27/limelights-2026-fpa-statistics-report-finds-record-finance-tech-spend-alongside-100-spreadsheet-dependency/ ; https://www.venasolutions.com/blog/fpa-trends-predictions
- Quick take: crowded; only promising with a vertical or ERP-specific angle (e.g. Odoo-native FP&A for Belgian SMEs).

### A-12. Cash-flow forecasting for SMEs remains unreliable and spreadsheet-based
- Problem: SMEs cannot build/maintain a rolling 13-week cash forecast; surprises cause deficits and expensive borrowing.
- Who suffers: SME owners and part-time CFOs; accounting firms trying to sell advisory.
- Frequency/cost signal: VERIFIED (search-summary): 65% of SMEs cite cash-flow management as top financial challenge (IFC 2023); 43% of US mid-market admit unreliable forecasts leading to unexpected deficits >USD 50k roughly every 20 days (vendor-cited); a third of UK SMEs cannot define cash flow (Novuna, late 2025). Market ~USD 726M in 2025, 7.4% CAGR.
- Current workaround: Excel, bank balance watching, accountant's quarterly view.
- Spend signal (WTP): Agicap (FR, large funding), Trezy, Abacum, Access Group products; price points not captured.
- Existing players noticed: Agicap, Trezy, Abacum, Electe, Float, Fygr.
- Why now / what changed: Open banking (PSD2) data + Peppol invoices give structured inflow/outflow data.
- Evidence URLs: https://agicap.com/en-us/article/cash-flow-forecast/ ; https://www.abacum.ai/blog/best-cash-flow-forecasting-software-for-smbs ; https://www.electe.net/en/post/ai-cash-flow-forecasting-sme
- Quick take: crowded (Agicap alone is very well funded); weak for a solo founder unless bundled with A-09.

### A-13. Late payment / credit control in Belgian B2B: payment gap widening to 21 days
- Problem: SMEs get paid late; dunning is manual; probability of recovery drops after 60 days; late payment linked to a quarter of bankruptcies.
- Who suffers: Belgian SMEs with B2B receivables; accounting firms doing AR follow-up as a service.
- Frequency/cost signal: VERIFIED (search-summary): B2B payment gap 21 days in 2026 vs 15 in 2023 (Intrum); 84% of Belgian suppliers face late B2B payments (Atradius); Graydon: ~25% of Belgian bankruptcies caused by late payment; 62% of Belgian companies pay late (Yago).
- Current workaround: Excel ageing lists, manual reminders, collection agencies.
- Spend signal (WTP): iController (KBC partnership, enterprise clients), Clearnox (SME, claims 50% time saving), Chaser; pricing not found.
- Existing players noticed: iController, Clearnox, Chaser, Yago, ATTA (AI agency selling dunning automation to Belgian SMEs).
- Why now / what changed: Peppol makes invoice status/data structured; AI agents can run polite, multilingual (NL/FR) dunning.
- Evidence URLs: https://www.intrum.be/fr/business-solutions/rapports-et-insights/l-ecart-de-paiement-entre-les-entreprises-belges-atteint-21-jours-la-moitie-rate-ses-objectifs-de-croissance-a-cause-d-un-effet-domino/ ; https://clearnox.com/fr-be/retards-de-paiement-en-belgique-5-chiffres-a-retenir/ ; https://yagodata.com/2026/02/15/62-des-entreprises-belges-paient-en-retard/
- Quick take: crowded but the pain is real and growing; weak as greenfield, possible as accountant-channel add-on.

### A-14. Transfer-pricing documentation for mid-size Belgian groups after RD 2024/2025 changes
- Problem: Belgian entities above EUR 50M income or 100 FTE (or with >EUR 1M cross-border intra-group transactions per business unit) must file master/local files; from FY2025 the detail must be given per country and per operational unit rather than consolidated; two royal decrees (2024, Dec 2025) changed formats. Data is scattered across ERPs and intercompany agreements.
- Who suffers: Tax/finance managers at mid-size Belgian subsidiaries and family groups; Big4/mid-tier advisers do the work manually.
- Frequency/cost signal: VERIFIED (search-summary) on thresholds and rule changes; annual recurrence. Consultant cost per file: Evidence not found.
- Current workaround: Advisers (Grant Thornton, Moore, Vandelanotte, KPMG) with Excel/Word templates.
- Spend signal (WTP): Advisory fees (not quantified in results).
- Existing players noticed: Big4, Grant Thornton, Moore, Vandelanotte, Fieldfisher (advice); software: not surfaced in searches.
- Why now / what changed: RD of 7 Dec 2025 recalibrated how information is provided; per-country detail from FY2025 filings (i.e. filings during 2026).
- Evidence URLs: https://www.grantthornton.be/en/the-field/articles-and-publications/Direct-tax/2026-outlook-revised-transfer-pricing-documentation-requirements-now-in-effect/ ; https://www.vandelanotte.be/en/news/new-requirements-for-transfer-pricing-documentation-in-belgium-from-2025 ; https://www.lexgo.be/en/news-and-articles/3791-belgium-introduces-new-transfer-pricing-documentation-rules
- Quick take: unclear — thresholds exclude most SMEs; niche of ~mid-size groups; advisers guard it.

### A-15. Audit preparation (PBC lists) eats 60-120 staff hours per engagement in spreadsheets and email
- Problem: Auditees assemble support documents and schedules by hand; auditors chase; request tracking is email-based.
- Who suffers: Finance teams of audited Belgian companies (statutory audit above size thresholds), and audit firms' senior staff.
- Frequency/cost signal: VERIFIED (search-summary, vendor sources): 60-120 staff hours per engagement; senior auditors ~72 h prep per engagement; document follow-up 22% and request tracking 15% of prep time. Annual (plus interim).
- Current workaround: Excel PBC list, email, shared drives, auditor portals.
- Spend signal (WTP): Audit fees embed this inefficiency; tools (Jadian, TallyScan, US Tech Automations) marketed.
- Existing players noticed: Jadian, TallyScan, Suralink (not surfaced but known), audit-firm portals.
- Why now / what changed: Structured e-invoices and CODA make evidence retrievable by API; AI can pre-assemble support packs.
- Evidence URLs: https://www.jadian.com/audit-pbc-list-explained/ ; https://ustechautomations.com/resources/blog/accounting-audit-prep-automation-roi
- Quick take: weak-to-unclear for Belgium (audit universe is smaller than US); decent for mid-market.

### A-16. Accounting profession locked into a concentrating software oligopoly (ITAA survey)
- Problem: The tools firms rely on daily are owned by ever fewer vendors (Visma, Wolters Kluwer, Exact...). Firms fear price hikes, unilateral term changes, product discontinuation; migration is an operational crisis because whole document flows are built on one platform.
- Who suffers: Belgian accounting firms (survey panel 79% owners, ~3/4 with <=10 staff).
- Frequency/cost signal: VERIFIED (search-summary): ITAA survey of 1,642 members (992 NL, 650 FR), July 2026: more than half experience the market as strongly to very strongly concentrated; ITAA followed with an Aug 2026 piece framing "digital dependency" as a professional risk to be managed.
- Current workaround: None; ITAA lobbying; accepting price rises (bookkeeping fees rising ~4% in 2026 partly to offset costs).
- Spend signal (WTP): Visma paid EUR 300M for Silverfin; Visma did 15 acquisitions in H1 2025 — consolidation is accelerating.
- Existing players noticed: Visma (Silverfin, Yuki, Teamleader...), Wolters Kluwer (Adsolut), Exact, Octopus, Billit, Codabox.
- Why now / what changed: Concentration peaked with Visma roll-up; ITAA is now vocal; open APIs/MCP make an independent data layer feasible.
- Evidence URLs: https://www.blogitaa.be/2026/07/07/softwaremarkt-onder-druk-wat-1-642-confraters-ons-vertellen-over-concentratie-en-afhankelijkheid/ ; https://www.blogitaa.be/2026/08/26/digitale-afhankelijkheid-een-beroepsrisico-dat-om-beheer-vraagt/ ; https://www.accountingweb.co.uk/tech/accounting-software/visma-snaps-up-silverfin-in-eu300m-deal
- Quick take: surprising and promising as positioning (vendor-neutral data/portability/AI layer endorsed by the profession); risky as a product on its own.

### A-17. Odoo in Belgium lacks native statutory outputs (NBB XBRL, Biztax) and legal consolidation
- Problem: Odoo users (very common in Belgian SMEs) cannot natively export NBB XBRL annual accounts or integrate Biztax; legal consolidation with eliminations is not supported, so accountants rekey or use third-party tools.
- Who suffers: Belgian SMEs on Odoo and the accounting firms that finalise their year-end.
- Frequency/cost signal: VERIFIED (search-summary): Odoo forum answers confirm no native XBRL export for BNB, no Biztax integration, no legal consolidation ("auditors want consolidation postings"). Annual (XBRL/Biztax) and monthly (consolidation).
- Current workaround: Manual rekeying into NBB Filing app / Biztax, Silverfin or Venice for year-end, custom modules from integrators.
- Spend signal (WTP): Integrator custom development; Silverfin subscriptions for year-end.
- Existing players noticed: Odoo, Silverfin, Venice, OBS/Odive/Agile-Minds (integrators).
- Why now / what changed: Odoo's growth in Belgium + accountants forced onto Odoo by clients.
- Evidence URLs: https://www.odoo.com/forum/studio-18/accounting-belgium-need-report-171952 ; https://www.odoo.com/forum/help-1/does-odoo-also-have-a-legal-consolidation-instead-of-only-an-aggregation-175419
- Quick take: unclear — Odoo may close gaps itself (platform risk), but SME-group consolidation on Odoo is a plausible niche linked to A-09.

### A-18. Payroll (sociaal secretariaat) to general-ledger reconciliation
- Problem: Monthly payroll journals from SD Worx/Acerta/Partena/Liantis must be booked and reconciled against accounting; differences (provisions, holiday pay, bonuses) are chased manually.
- Who suffers: SME bookkeepers, accounting firms, controllers.
- Frequency/cost signal: INFERENCE: SD Worx sells a paid training course specifically on "reconciliation of remuneration with the accounting" — a signal the reconciliation is non-trivial. Import of payroll XML (SODA/Loon-XML) is supported by Billit, Octopus, AFAS. Quantified pain: Evidence not found.
- Current workaround: XML import + manual reconciliation in Excel.
- Spend signal (WTP): Training courses; integrations bundled in packages.
- Existing players noticed: SD Worx, Acerta, Partena, Liantis, AFAS, Billit, Octopus.
- Why now / what changed: Not much — stable.
- Evidence URLs: https://www.sdworx.be/nl-be/opleidingen/reconciliatie-van-bezoldigingen-met-de-boekhouding ; https://www.billit.eu/nl-be/helpartikelen/snelle-invoer/bestanden-verwerken/loon-xml-ontvangen-en-verwerken-acerta-sd-worx-be/
- Quick take: weak.

### A-19. Subsidy / grant financial reporting (VLAIO, Horizon Europe) compliance burden for SMEs
- Problem: Funded SMEs must track eligible costs, timesheets and produce financial statements per project; audits are document-heavy.
- Who suffers: Flemish/Belgian innovation SMEs with VLAIO or EU grants; their accountants.
- Frequency/cost signal: VERIFIED (search-summary) that Horizon Europe "funding compliance" requires reporting and cost calculations and audit access to all documents; quantification of hours/cost: Evidence not found.
- Current workaround: Excel timesheets, consultants (PNO).
- Spend signal (WTP): Grant consultants (PNO Innovation and similar) charge for compliance support (fees not captured).
- Existing players noticed: PNO, VLAIO guidance; software not surfaced.
- Why now / what changed: No clear trigger.
- Evidence URLs: https://www.pnoinnovation.com/nl/insights/horizon-europe-compliance-checklist/ ; https://www.vlaio.be/nl/subsidies-financiering/subsidiedatabank/maatregelen/europese-onderzoeks-en-innovatiesteun-horizon-europe
- Quick take: weak/unclear — evidence thin.

### A-20. Financial due diligence for small M&A deals is skipped or minimal
- Problem: In small Belgian deals (well under EUR 10M), advisory involvement is limited and diligence is "financial and legal basics"; buyers overpay or miss issues; no affordable quality-of-earnings product.
- Who suffers: SME buyers/sellers, family successions, search funds, accountants asked to "have a look".
- Frequency/cost signal: VERIFIED (search-summary): Belgian mid-market deals EUR 10-200M revenue; smaller deals facilitated by accountants/brokers with limited DD (Synergy AI guide). US: QoE providers target USD 1-20M EV deals (Rapid Diligence). Belgian pricing: Evidence not found.
- Current workaround: Accountant does ad hoc review; buyer skips DD.
- Spend signal (WTP): Limited-scope QoE products exist in US/UK/CH (Scalemetrics CH).
- Existing players noticed: Rapid Diligence (US), Scalemetrics (CH), OGScapital, Big4/mid-tier in BE.
- Why now / what changed: Baby-boomer succession wave; AI can process ledgers quickly.
- Evidence URLs: https://masynergy.eu/blog/belgian-ma-landscape-guide ; https://rapiddiligence.com/ ; https://www.scalemetrics.ai/financial-due-diligence-switzerland-2026-what-it-costs-when-you-need-it-and-how-to-avoid-common-pitfalls/
- Quick take: unclear — plausible but low frequency per customer; interesting as a productised service.

### A-21. SME treasury/FX: no stress-testing, patchy hedging, cross-border DSO stretch
- Problem: SMEs trading in non-EUR currencies do not manage FX systematically; cross-border DSO 38-52 days vs 32 domestic.
- Who suffers: Exporting SMEs (esp. non-euro exposure), CFOs of mid-market groups.
- Frequency/cost signal: VERIFIED (search-summary): 89% of organisations do not stress-test FX exposures; German SMEs 52% formal hedging, 36% on fintech platforms; Polish SMEs 18%; PLN depreciation 9.4% in 2025 eroded exporter margins 3-7%.
- Current workaround: Bank forwards, nothing, spreadsheets.
- Spend signal (WTP): Fintech FX platforms (Alpha Group, Smart Currency, Alt21, Trezy).
- Existing players noticed: Alpha Group, Smart Currency Business, Alt21, Trezy, iBanFirst (not surfaced but known).
- Why now / what changed: Volatility expectations up for 2026.
- Evidence URLs: https://tradetreasurypayments.com/articles/stop-hedging-when-it-hurts-less-painful-ways-to-manage-fx-risk-in-2026 ; https://www.trezy.io/blog/multi-currency-treasury-management-smes
- Quick take: weak for founder profile (regulated, capital-heavy, crowded).

### A-22. Expense management for Belgian SMEs
- Problem: Expense claims checked manually; one accounting team needed 2-3 days to check travel expense claims before automation (vendor case).
- Who suffers: SMEs 20-200 staff.
- Frequency/cost signal: VERIFIED (search-summary) vendor case only; pricing: Rydoo EUR 8-12/user/month.
- Current workaround: Paper/Excel, email photos.
- Spend signal (WTP): Rydoo (Mechelen), Spendesk (EUR 20B annual spend processed, 200k users), Exact Expense Management.
- Existing players noticed: Rydoo, Spendesk, Exact, Pleo, Mobilexpense (BE).
- Why now / what changed: Nothing new.
- Evidence URLs: https://www.getapp.com/finance-accounting-software/a/xpenditure-expenses/ ; https://www.rydoo.com/nl/onkostenbeheer/
- Quick take: crowded — skip.

### A-23. Germany: e-invoicing 2027/2028 waves land on a Steuerberater profession that cannot hire
- Problem: Issuing obligation from Jan 2027 (>EUR 800k turnover) and Jan 2028 (all, incl. Kleinunternehmer); 8-year structured archiving; audits will check e-invoice compliance. Meanwhile 72.7% of Kanzleien cannot find staff, >10,000 open positions, mandates being rejected, over half of Steuerberater >50 years old.
- Who suffers: German Steuerkanzleien (very large market) and KMU.
- Frequency/cost signal: VERIFIED (search-summary): ifo 2025: >72% of tax firms report hiring difficulty; awicontax Zukunftskompass 2026: staff shortage now bigger challenge than tech transformation.
- Current workaround: Rejecting mandates, DATEV automation, Quereinsteiger, offshoring.
- Spend signal (WTP): DATEV dominance; startups (clara-agent.de) selling AI to Kanzleien.
- Existing players noticed: DATEV, Finmatics (Visma), Clara, Candis, Kanzleiwelt.
- Why now / what changed: 2027/2028 deadlines.
- Evidence URLs: https://www.stb-web.de/news/article.php/id/25966 ; https://visionarydata.de/blog/fachkraeftemangel-steuerberatung-zukunftskompass-2026 ; https://www.fiscal-requirements.com/news/4566
- Quick take: promising as expansion market for whatever wins in Belgium; DATEV lock-in is the wall.

### A-24. France: reception mandatory 1 Sept 2026, PME emission Sept 2027, experts-comptables as PDP mandataries
- Problem: All French companies must receive e-invoices via an accredited platform (PDP/PA) from 1 Sept 2026; PME/micro must emit by Sept 2027; expected failure modes: integration, parameterisation, unfinished internal processes, accounting-software issues. DGFiP explicitly routes SMEs to their expert-comptable, who can register clients' reception addresses via opt-in mandate.
- Who suffers: French PME/TPE and cabinets d'expertise comptable (Belgian firms with French clients too).
- Frequency/cost signal: VERIFIED (search-summary) on timeline and difficulty categories; costs not quantified.
- Current workaround: Vendor PDPs (Cegid, Sage, Pennylane), Ordre des Experts-Comptables platform.
- Spend signal (WTP): PDP subscriptions; Evoliz acquired by Visma.
- Existing players noticed: Cegid, Pennylane, Evoliz/Visma, OEC platform, Bpifrance guidance.
- Why now / what changed: Live now (Sept 2026).
- Evidence URLs: https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/guide_pratique_facturation_electronique.pdf ; https://revuefrancaisedecomptabilite.fr/la-facture-electronique-une-transformation-majeure-pour-la-profession-comptable/ ; https://www.cegid.com/fr/facture-electronique-obligatoire/calendrier-facture-electronique/
- Quick take: crowded (Pennylane-scale players); relevant as second market for Belgian-proven tooling.

### A-25. Luxembourg B2B e-invoicing (Peppol 4-corner) from 2028
- Problem: Draft law approved by Government Council 17 Jul 2026: universal receiving obligation 1 Jan 2028; issuance for large enterprises Jan 2028, medium Jul 2028; Peppol 4-corner as national network.
- Who suffers: Luxembourg companies and fiduciaires (many serve holding/SOPARFI structures with thin admin).
- Frequency/cost signal: VERIFIED (search-summary) on timeline; fiduciaire capacity data: Evidence not found.
- Current workaround: B2G Peppol already in place; B2B by PDF.
- Spend signal (WTP): Access-point providers.
- Existing players noticed: Storecove, Comarch, Pagero, faktura.lu.
- Why now / what changed: Law in progress mid-2026.
- Evidence URLs: https://www.storecove.com/blog/en/luxembourg-b2b-e-invoicing-mandate-peppol-rules-timeline-compliance-guide/ ; https://rtcsuite.com/luxembourg-formalises-mandatory-b2b-e-invoicing-over-a-peppol-four-corner-network/
- Quick take: unclear — small market, but Belgian Peppol know-how transfers directly.

### A-26. UK: MTD for Income Tax multiplies accountant submissions 5x; 42% unprepared
- Problem: From April 2026 sole traders/landlords >GBP 50k must submit quarterly updates; practices go from 1 to 5 submissions per client; 59% of accountants say at least half their clients still use no digital tools; 69% of businesses expect the accountant to do everything.
- Who suffers: UK accounting practices, esp. small.
- Frequency/cost signal: VERIFIED (search-summary): IRIS survey 42% not prepared; Wolters Kluwer April 2026: 59% of accountants with >=half clients non-digital.
- Current workaround: Bridging software, bookkeeping outsourcing (South Africa BPO marketing capacity).
- Spend signal (WTP): MTD software market, offshoring.
- Existing players noticed: IRIS, Bright, Xero, Sage, Alpha BPO.
- Why now / what changed: Live April 2026; thresholds widen 2027/2028.
- Evidence URLs: https://www.iris.co.uk/news/m-t-d-readiness-survey/ ; https://brightsg.com/blog/making-tax-digital-for-accountants-your-complete-mtd-it-compliance-guide/
- Quick take: crowded; useful only as a pattern (regulation x capacity shortage = tooling demand).

### A-27. ViDA 2030: intra-EU e-invoicing within 10 days + digital reporting for every cross-border B2B sale
- Problem: From 1 Jul 2030 all intra-EU B2B supplies must be e-invoiced (roughly within 10 days) and reported per transaction; SMEs doing cross-border trade must restructure invoicing/accounting processes.
- Who suffers: Cross-border-trading SMEs across EU; accounting firms with international clients.
- Frequency/cost signal: VERIFIED (search-summary) on scope and timing; per-SME cost not found.
- Current workaround: Periodic EC sales lists/Intrastat.
- Spend signal (WTP): Compliance vendors positioning now.
- Existing players noticed: EDICOM, Continia, Vertex, Banqup.
- Why now / what changed: Member states preparing DRR implementations (VATupdate Mar 2026).
- Evidence URLs: https://www.vatupdate.com/2026/03/15/eus-vida-in-motion-how-eu-member-states-are-preparing-for-implementing-digital-reporting-requirements-drr/ ; https://accountancyeurope.eu/publications/vat-in-the-digital-age-vida/
- Quick take: too far out for a side hustle; strategic backdrop.

### A-28. Management reporting as advisory product for accounting firms' SME clients
- Problem: Firms want to move from compliance to advisory but producing monthly management reports per client is labour-intensive; data quality (inconsistent customer/product/ledger codes) turns reports into arguments.
- Who suffers: Belgian/Dutch accounting firms and their SME clients.
- Frequency/cost signal: INFERENCE from vendor content (VGD, Emasphere "save up to 67% time", Odive); direct survey data: Evidence not found.
- Current workaround: Excel packs, Emasphere, Power BI boutiques, Silverfin insights.
- Spend signal (WTP): Emasphere, Silverfin, Adsolut, Yuki dashboards.
- Existing players noticed: Emasphere, Silverfin, Yuki, Deskflow, Odive.
- Why now / what changed: Advisory push + AI commentary generation.
- Evidence URLs: https://www.emasphere.com/nl/content/blog/geconsolideerde-reporting-spaar-tot-67-tijd-uit ; https://blogbe.vgd.eu/nl/optimaal-beheer/cfo-services/vijf-tips-om-een-goede-managementrapportering-uit-te-bouwen
- Quick take: crowded and evidence weak.

### A-29. Offshoring is the current "capacity valve" for EU accounting firms
- Problem: With hiring impossible, firms buy capacity offshore (India USD 8-12/h bookkeeping, 15-25/h for reporting); vendors explicitly market to Belgian and Dutch firms. This is both a competitor to software and a proof of WTP for capacity.
- Who suffers: Firms managing quality/security/GDPR of offshore teams.
- Frequency/cost signal: VERIFIED (search-summary): 50-70% labour cost reduction claims; India produces ~100k CAs per year; US accounting workforce down ~10% 2019-2024.
- Current workaround: Eastvantage (BE), Valuecent (NL), Wisemonk, Datamatics.
- Spend signal (WTP): Hourly outsourcing rates above.
- Existing players noticed: Eastvantage, Valuecent, Whiz Consulting, Datamatics.
- Why now / what changed: AI agents may undercut offshore rates.
- Evidence URLs: https://www.wisemonk.io/blogs/accounting-outsourcing-india ; https://eastvantage.com/be/nl/news-media/outsourcing-for-belgian-accountants-a-guide-to-overcoming-challenges-debunking-some-myths/
- Quick take: not an opportunity itself; a pricing benchmark (any AI tool must beat ~USD 10/h effective).

### A-30. Demand signal: capital flowing into "AI for accountants / agentic close" in EU
- Problem: (Signal, not a problem.) Investors are funding the same thesis: Dytto (Ghent) EUR 1.5M pre-seed for AI assistant for accounting firms (BE/NL/UK); Cashfeed (Ghent) EUR 1.3M; Round Treasury (London) EUR 5.1M seed for agentic finance workflows; Stacks USD 23M Series A (agentic close, 30+ enterprise customers); Seapoint EUR 7.5M; Silverfin EUR 300M exit; Visma 15 acquisitions H1 2025.
- Who suffers: n/a
- Frequency/cost signal: VERIFIED (search-summary) for all rounds listed.
- Current workaround: n/a
- Spend signal (WTP): Rounds above.
- Existing players noticed: Dytto, Cashfeed, Round, Stacks, Seapoint, Silverfin/Visma, Finmatics/Visma.
- Why now / what changed: 2025-2026 agentic AI wave.
- Evidence URLs: https://www.eu-startups.com/2026/02/ghent-based-dytto-raises-e1-5-million-pre-seed-to-free-the-accountant-using-ai/ ; https://tech.eu/2025/07/10/cashfeed-raises-1-3m-to-simplify-e-invoicing/ ; https://www.eu-startups.com/2026/04/londons-round-treasury-raises-e5-1-million-to-build-ai-powered-finance-automation-platform-for-modern-finance-teams/
- Quick take: validates the space; also means generic "AI for accountants" is already contested in Ghent.

---

## Explorer notes / caveats
- Most quantified pain figures (hours per close, hours chasing documents, PBC hours) originate from vendor content marketing; treat as directional. The strongest primary-ish sources here are: ITAA member survey (1,642 respondents), Exact Belgian accountancy survey, Intrum/Atradius/Graydon payment data, ifo survey (DE), IRIS/Wolters Kluwer (UK), VATupdate/FPS Finance for regulation.
- Evidence not found for: Belgian-specific bank-reconciliation hours; consultant pricing for TP local files; SME FDD pricing in EUR; grant-reporting hours; Luxembourg fiduciaire capacity.
