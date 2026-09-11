# Stream C — Belgian physical & vertical SMEs, structural conditions (raw problem discovery)

Date: 2026-09-11. Method: WebSearch only (summaries + URLs); no page fetches. Numbers are quoted from search-result summaries and labelled VERIFIED (search-summary) / ESTIMATE / INFERENCE. Search budget was exhausted after 36 successful queries; two planned queries (FR freight-forwarder customs software; syndic AG renovation-financing blockage) could not be run.

## Queries run (36 successful, 2 blocked by budget)
1. aannemer offerte software België kleine bouwbedrijven administratie Excel
2. Checkinatwork 30bis inhoudingsplicht onderaannemer administratie last bouwbedrijven
3. Embuild 2025 bouwsector tekort arbeidskrachten faillissementen administratieve last
4. Antwerp port freight forwarder SME customs administration post-Brexit cost digitalisation 2025
5. CBAM 2026 declarant SME administrative burden importers Belgium
6. huisartsenpraktijk administratie RIZIV facturatie software België tekort huisartsen 2025
7. woonzorgcentra personeelstekort 2025 België planning administratie
8. syndic logiciel copropriété Belgique pénurie syndics assemblée générale 2025
9. IPI BIV pénurie syndics 90.000 copropriétés chiffres 2025 nombre de syndics
10. renovatieplicht Vlaanderen EPC label D 2025 boete kosten eigenaars appartementen mede-eigendom
11. horeca België 2025 faillissementen marges energie personeelskosten cijfers
12. zonnepanelen installateurs Vlaanderen 2025 faillissementen batterij thuisbatterij premie capaciteitstarief
13. energiedelen energiegemeenschap België administratie verrekening deelnemers software 2025
14. advocatenkantoor België tijdregistratie facturatie software klachten kleine kantoren
15. vzw boekhouding software kleine vzw's jaarrekening neerlegging UBO administratieve last 2025
16. knelpuntberoepen VDAB 2026 lijst boekhouder administratief medewerker
17. Forem métiers en pénurie 2026 liste fonctions critiques Wallonie comptable
18. KMO-portefeuille 2025 2026 hervorming digitalisering steun cijfers budget
19. chèques-entreprises Wallonie digitalisation 2025 montant PME transformation numérique
20. Belgium SME digital intensity 2025 DESI Statbel ICT usage enterprises percentage cloud ERP
21. aantal kmo's België 2025 Statbel ondernemingen minder dan 10 werknemers percentage
22. ITAA aantal accountants België tekort accountantskantoren 2025 werkdruk
23. verplichte e-facturatie 2026 België Peppol kmo's niet klaar percentage enquête
24. groothandel distributie België kmo ERP software verouderd voorraadbeheer Excel 2025
25. landbouwers administratieve last MAP7 Vlaanderen 2025 boekhouding land- en tuinbouw software
26. overheidsopdrachten kmo's België drempel 2025 lokale besturen aankoop software administratieve last inschrijving
27. notaris België digitalisering 2025 dossiers wachttijd administratie Fednot
28. verhuurbeheer software België private verhuurders huurwaarborg indexatie huurprijs 2025 rentmeester
29. apotheek België 2025 administratie tarifering software rentabiliteit apothekers tekort
30. transportbedrijven België 2025 faillissementen kmo transport rentabiliteit administratie Febetra TLV
31. architectenbureau België ereloon facturatie tijdregistratie rendabiliteit 2025 NAV enquête
32. laadpalen bedrijven België 2025 installateurs verplichting parkings 2025 beheer facturatie laadpassen kmo
33. bouwsector België betalingstermijnen vorderingsstaten wanbetaling aannemers cashflow 2025 Graydon Embuild
34. Actiris knelpuntberoepen Brussel 2026 lijst view.brussels analyse
35. Bruxelles copropriétés PEB obligation rénovation 2030 2033 syndic plan de rénovation immeubles Rénolution
36. Belgian startup ecosystem 2025 report gaps funding scale-ups Agoria hub.brussels B2B SaaS Sirris
37. Mijn VerbouwPremie warmtepomp 2025 2026 installateurs premieaanvraag administratie wachttijd klachten
38. kleinhandel België 2025 winkels sluiten zelfstandige handelaars Comeos Unizo cijfers leegstand
(blocked) transitaire PME Belgique douane 2025 charge administrative logiciel PLDA IDMS ICS2
(blocked) syndics Belgique assemblée générale rénovation énergétique copropriété financement prêt collectif

---

## Raw opportunities

### C-01. Subcontractor social/fiscal-debt check before every payment (new 2026 inhoudingsplicht)
- Problem: From 2026 every client/main contractor in construction (and cleaning) must check whether the contracting party has social or fiscal debts before paying each invoice and withhold 15%/35%/15% (max 50%) if so. This turns accounts-payable into a compliance step on every subcontractor invoice, with personal liability if missed.
- Who suffers: Main contractors and general contractors with subcontractors; Belgian construction sector has tens of thousands of firms (Embuild: net loss of 1,402 firms in 2025 alone). Also cleaning companies.
- Frequency/cost signal: Per-invoice, continuous. New withholding rules effective 1 Jan 2026 / 1 May 2026 with rates 15% fiscal, 35% RSZ, 15% RSVZ, capped 50% — VERIFIED (search-summary, Baker Tilly / Meesters / ProBusinessCenter). Admin burden is the #1 obstacle cited by 23.5% of construction respondents — VERIFIED (Embuild/Voka survey summaries).
- Current workaround: Manual lookup on the socialsecurity.be 30bis portal per invoice, checklists from social secretariats (Securex PDF), law-firm checklists (Odigo), accountant advice.
- Spend signal (WTP): Firms pay accountants/social secretariats for this; Embuild membership. Prices not found.
- Existing players noticed: Securex (checklist), Baker Tilly/Meesters (advice), Geodynamics (CheckInAtWork), Robaws/Buildbase (construction ERP, not clearly covering debt-check).
- Why now: New stricter withholding regime 2026 + more inspections; ties into mandatory Peppol e-invoicing (structured invoices make an automated pre-payment check feasible).
- Evidence URLs: https://bakertilly.be/nl/news/nieuwe-inhoudingsplicht-vanaf-1-mei-2026/ ; https://www.meesters.be/nieuws/strengere-inhoudingsplicht-vanaf-2026-meer-controles-voor-bedrijven-in-bouw-en-schoonmaak ; https://www.socialsecurity.be/site_nl/employer/applics/30bis/index.htm
- Quick take: promising — regulation-created, per-transaction, finance-process pain; need to verify whether construction ERPs already automate the 30bis lookup (not seen in summaries).

### C-02. Construction SME cash-flow / progress-billing (vorderingsstaten) and late-payment control
- Problem: Small contractors bill by progress statements, wait 30-60+ days, get partial payments and retentions, and run 2%-level margins; 7 in 10 construction firms suffer late payment. Cash visibility is done in heads/Excel.
- Who suffers: Small and mid contractors/installers; 1,443 construction bankruptcies in H1 2025 — VERIFIED (GraydonCreditsafe via Embuild).
- Frequency/cost signal: "7 op 10 bedrijven in de bouw hebben last van wanbetaling" — VERIFIED (Habitos summary). Sector stagnation at least until 2026 — VERIFIED (Embuild). Record bankruptcies — VERIFIED.
- Current workaround: Excel, accountant's quarterly view, factoring, chasing by phone.
- Spend signal (WTP): Construction ERPs charge subscriptions (Robaws, Buildbase, AFAS); Billit for micro-firms. Prices not found.
- Existing players noticed: Robaws, Buildbase, AFAS Bouw, Exact Bouw, Billit, Vastlegg (NL), UNIVO/erpvergelijker comparators.
- Why now: Public-contract payment rules improved from 1 Jan 2025; Peppol makes invoice data structured; bankruptcies at record.
- Evidence URLs: https://www.habitos.be/nl/bouwen-verbouwen/7-op-10-bedrijven-de-bouw-hebben-last-van-wanbetaling-hoe-vermijden-en-aanpakken ; https://embuild.be/nl/faillissementen-de-bouw-neerwaartse-spiraal-blijft-aanhouden-door-combinatie-van-factoren ; https://www.sbb.be/nl/magazine/cashflow-de-bouwsector-6-aandachtspunten
- Quick take: promising but crowded on the ERP side; the uncovered angle is a lightweight cash/AR forecast + retention tracker for firms too small for Robaws.

### C-03. Quoting/offer software for micro-contractors still on Excel
- Problem: Many small contractors still quote and track jobs in Excel; time-consuming and error-prone.
- Who suffers: Micro construction firms (<10 staff) — the vast majority of the sector.
- Frequency/cost signal: "Veel kleine aannemers voeren hun administratie nog uit in Excel-sheets" — VERIFIED (vendor blog, so biased).
- Current workaround: Excel + Word + accountant.
- Spend signal (WTP): Many paid SaaS tools exist.
- Existing players noticed: Robaws, Buildbase, Billit, AFAS, Exact Bouw, Vastlegg, makeanapplike top-5 list.
- Why now: Peppol mandate forces tool adoption in 2026.
- Evidence URLs: https://robaws.com/nl-BE/bouwsoftware ; https://www.erpvergelijker.be/software/functies/aannemers-software/
- Quick take: crowded — many well-funded Belgian incumbents; avoid a generic quoting tool.

### C-04. CheckInAtWork daily presence registration on large sites (incl. concrete deliveries)
- Problem: Daily registration before anyone starts on sites >= EUR 500k, extended to deliveries such as concrete; contractors must make it workable across many subcontractors.
- Who suffers: Contractors on larger sites, concrete suppliers, temp agencies.
- Frequency/cost signal: Daily obligation — VERIFIED (Geodynamics summary).
- Current workaround: Badge/app solutions.
- Spend signal (WTP): Geodynamics sells hardware/software; prices not found.
- Existing players noticed: Geodynamics; social secretariats.
- Why now: Scope extensions (deliveries).
- Evidence URLs: https://geodynamics.eu/nl-be/checkinatwork-betonleveringen/
- Quick take: weak — already served by specialised hardware/software vendors.

### C-05. Micro transport companies: 2% margins, record bankruptcies, no cost-per-km visibility
- Problem: Small hauliers do not know their real cost per km/vehicle and price below cost; 413 transport bankruptcies in 2025 (record), 78.69% of bankrupt licensed carriers had <=5 vehicles.
- Who suffers: Belgian road-transport SMEs — 1 in 2 firms has no employees, 31% have 1-4 staff — VERIFIED (TLV/logistiek.be summaries).
- Frequency/cost signal: 413 bankruptcies 2025, +1/3 vs 2024; 251 in Flanders; margins ~2%; only 1 in 3 has sufficient buffers — VERIFIED (TLV, Flows, DVO summaries).
- Current workaround: Federation (TLV/Febetra) cost indices, accountant, gut feel.
- Spend signal (WTP): TLV/Febetra membership; TMS subscriptions. Low WTP inferred from micro size — INFERENCE.
- Existing players noticed: TLV (also sells OBU for km-charge), Febetra; TMS vendors not surfaced.
- Why now: NL kilometre charge (2026), fuel/wage costs, last-mile squeeze.
- Evidence URLs: https://www.tlv.be/nieuws/recordaantal-faillissementen-in-transportsector-vooral-kleine-spelers-in-last-mile-delivery-zwaar-getroffen ; https://www.logistiek.be/record-faillissementen-waarom-vooral-kleine-transportbedrijven-omvallen/ ; https://www.flows.be/transport/2026/07/transportsector-ziet-faillissementen-verder-oplopen/
- Quick take: unclear — pain is real and finance-shaped, but customers are one-truck firms with little money; a channel via TLV/Febetra or accountants would be needed.

### C-06. Freight-forwarder / customs admin for SMEs post-Brexit
- Problem: SMEs trading with the UK face extra data consistency and safety/security requirements; many outsource to brokers at 10%+ budget increases.
- Who suffers: Belgian SME exporters/importers to UK; small forwarders in Antwerp.
- Frequency/cost signal: "SMEs face 10%+ budget increases from Brexit compliance" — VERIFIED (UK-centric source, youtrust.com); Belgium-specific evidence not found.
- Current workaround: Licensed customs brokers; port systems (RX Seaport, Certified Pick-up, BE-GATE).
- Spend signal (WTP): Broker fees (not quantified).
- Existing players noticed: OTS Broker, Port of Antwerp-Bruges digital platforms, BE-GATE.
- Why now: Port digitalisation programmes; ICS2; CBAM.
- Evidence URLs: https://youtrust.com/blog/supply-chain-management ; https://www.portofantwerpbruges.com/en/business/cargo/customs ; https://pressroom.brusselsairport.be/en-belgium-launches-digital-customs-platform
- Quick take: unclear — evidence thin and Belgian-specific numbers not found; port authority and brokers are strong incumbents.

### C-07. CBAM compliance for mid-size importers (definitive regime 2026)
- Problem: Importers above 50 t/yr of CBAM goods must be authorised declarants, buy certificates and report embedded emissions.
- Who suffers: Mid-size importers of steel, aluminium, cement, fertilisers; ~4,100 authorised declarants EU-wide — VERIFIED (EC summary).
- Frequency/cost signal: Annual/quarterly reporting; the 50 t threshold removes ~90% of small importers — VERIFIED (ICAP/EY summaries). Belgian counts: Evidence not found.
- Current workaround: Big-4 / consultancies; spreadsheets.
- Spend signal (WTP): Consultancy spend (unquantified).
- Existing players noticed: EY, Linklaters (advice); sprih, zerocircle (SaaS).
- Why now: Definitive regime live 1 Jan 2026.
- Evidence URLs: https://taxation-customs.ec.europa.eu/news/cbam-successfully-entered-force-1-january-2026-2026-01-14_en ; https://icapcarbonaction.com/en/news/eu-adopts-simplifications-cbam-rules-ahead-compliance-phase-starting-2026
- Quick take: weak for an SME-focused side hustle — Omnibus shrank the SME market to ~10% of importers; remaining buyers are mid/large and already served.

### C-08. GP practices: new "New Deal" mixed financing + mandatory e-invoicing to insurers
- Problem: GP practices now juggle three financing pillars (per service, per patient capitation, premiums) and must e-invoice insurers since 1 Sept 2025, while facing a GP shortage and little practice support.
- Who suffers: GP practices, especially group practices; count not found.
- Frequency/cost signal: E-invoicing mandatory for doctors/dentists from 1 Sept 2025 — VERIFIED (RIZIV). New Deal model — VERIFIED (RIZIV).
- Current workaround: Certified EMD software (Corilus etc.), medical secretariats.
- Spend signal (WTP): RIZIV integrated practice premium requires certified software — VERIFIED; practice-support staff subsidised in New Deal.
- Existing players noticed: Corilus, Domus Medica guidance.
- Why now: New Deal + e-invoicing 2025.
- Evidence URLs: https://www.riziv.fgov.be/nl/nieuws/verplichte-elektronische-facturatie-voor-artsen-en-tandartsen-vanaf-1-september-2025 ; https://www.riziv.fgov.be/nl/nieuws/new-deal-akkoord-voor-een-nieuw-organisatie-en-financieringsmodel-voor-de-huisartsenpratijk
- Quick take: unclear — real financial-modelling need (which model pays for my practice?) but core software is gated by eHealth certification; a non-certified "practice finance dashboard" could sit alongside.

### C-09. Care homes: staffing-norm compliance and workforce planning under shortage
- Problem: Care homes fail legal staffing norms; 25 elderly-care facilities under heightened inspection (record), 7% have admission stops and a quarter expect to; planning is manual.
- Who suffers: Woonzorgcentra (esp. commercial ones) in Flanders; ~800+ facilities — ESTIMATE (not verified in search).
- Frequency/cost signal: 25 under verhoogd toezicht, personeelstekort main cause — VERIFIED (PVDA/Zorginspectie summary); 13 WZC (7%) admission stop — VERIFIED (Zorgnet-Icuro survey summary); 3,000 planned beds not built — VERIFIED.
- Current workaround: Manual rosters, interim agencies, closing wards.
- Spend signal (WTP): Interim nursing agencies; roster software. Prices not found.
- Existing players noticed: None surfaced for roster/norm analytics (Evidence not found).
- Why now: Record inspections, admission stops, financing uncertainty.
- Evidence URLs: https://www.pvda.be/nieuws/recordaantal-woonzorgcentra-op-zwarte-lijst-door-personeelstekort ; https://www.zorgneticuro.be/nieuws/personeelstekort-dwingt-vlaamse-ziekenhuizen-en-woonzorgcentra-om-zorgaanbod-af-te-bouwen
- Quick take: unclear — strong pain, but the bottleneck is people, not software; a norm-compliance/forecasting tool is a small wedge.

### C-10. Pharmacies: free pricing after APB dropped suggested prices (2025)
- Problem: Since 2025 the APB database no longer supplies suggested prices for non-regulated products; pharmacists must set their own margins per product while admin (tarification, attestations, reimbursements) already consumes hours.
- Who suffers: ~4,500+ community pharmacies in Belgium — ESTIMATE (count not verified in search).
- Frequency/cost signal: "Geen richtprijzen meer in onze databanken" from April/Sept 2025 — VERIFIED (Apotheia/APB summary); admin workload high — VERIFIED (Polly.be summary).
- Current workaround: Wholesaler protocol pushes purchase price into pharmacy software; pharmacist sets margin manually.
- Spend signal (WTP): All pharmacies pay for management software (Corilus CareConnect etc.).
- Existing players noticed: Corilus CareConnect Pharmacist, Polly, wholesalers (CERP), APB.
- Why now: Pricing freedom 2025; margin pressure; shift to services.
- Evidence URLs: https://www.apotheia.be/nieuws/nieuws-van-apb-geen-richtprijzen-meer-in-onze-databanken-april-2025 ; https://blog.corilus.be/pharma/welke-functionaliteiten-verwachten-apothekers-van-hun-apotheeksoftware
- Quick take: promising niche (pricing/margin analytics, finance angle) but risk that Corilus/wholesalers bundle it.

### C-11. Syndic shortage vs 90,000+ co-ownerships: admin overload
- Problem: Belgium has >90,000 co-ownerships (about a third of the residential stock) but only ~500-560 real-estate agents working exclusively as syndics; syndics are overloaded, general meetings require evening availability and strict formalities, 72% face demands outside their competence.
- Who suffers: Professional syndics (~500-560 exclusive + mixed agents), ~90,000 co-owner associations, co-owners who cannot find/change a syndic.
- Frequency/cost signal: >90,000 copropriétés (2021), 497-562 exclusive syndics, 4-4.7% of agents — VERIFIED (IPI/BIV summaries); shortage occupation at Forem since 2021 — VERIFIED (CondoLegal).
- Current workaround: Overloaded syndics, volunteer syndics for small buildings, Syndic24-type tools, coaching services.
- Spend signal (WTP): Syndic fees per lot; software subscriptions (Syndic24, TheSyndic, FMT Solutions); Syndicoach/Serenity services.
- Existing players noticed: Syndic24, TheSyndic, FMT Solutions, Syndicoach, Serenity, Happy Syndic; Federia/ABSA sector bodies.
- Why now: Growing stock of collective buildings (+401/yr per summary), regulation on energy renovation (see C-12).
- Evidence URLs: https://www.ipi.be/actualites/communiques-de-presse/lipi-tire-la-sonnette-dalarme-la-penurie-importante-dagents-immobiliers-syndics-pourrait-devenir-problematique-pour-plus-de-90000-coproprietes ; https://www.condolegal.com/gestion/chroniques/3255-reflexion-sur-les-causes-de-la-penurie-de-syndic-en-belgique
- Quick take: promising — regulated, capacity-constrained profession with accounting-heavy workload (charges, budgets, AG minutes); several incumbents but none looks dominant from summaries.

### C-12. Co-ownership energy-renovation plans and financing (Brussels PEB 2030/2033, Flanders label D)
- Problem: Brussels co-ownerships must hold a valid PEB certificate by 31 Dec 2030, reach <=275 kWh/m2 by 2033 and 150 by 2045, designate a PEB expert and adopt a collective renovation plan; Flemish buyers of E/F units must reach label D within 6 years (fine EUR 500-5,000, repeatable). Syndics must get AGs to vote multi-year capex and financing — a budgeting/financing problem.
- Who suffers: Syndics and ACPs in Brussels (thousands of buildings; count not found) and Flanders; owners of E/F apartments.
- Frequency/cost signal: Deadlines and thresholds — VERIFIED (environnement.brussels, Renolution, notaire.be summaries); Flemish fine range and 6-year deadline — VERIFIED.
- Current workaround: Free regional support (Renolution/Homegrade), PEB experts, ad-hoc Excel budgets, AG deferrals.
- Spend signal (WTP): Renolution subsidies exist if ACP registered in BCE; PEB expert fees; renovation loans.
- Existing players noticed: Renolution (public), Happy Syndic, AL Energy (blogs), Federia.
- Why now: CoBrACE revision; 2030 certificate deadline approaching; Flemish 2025 relaxation of long-term targets but 6-year rule stays.
- Evidence URLs: https://environnement.brussels/citoyen/reglementation/obligations-et-autorisations/la-peb-en-copropriete ; https://renolution.brussels/fr/coproprietes ; https://www.epc-keuring.vlaanderen/epc-renovatieplicht-label-d/
- Quick take: promising — a finance/FP&A-shaped problem (multi-year capex plan, per-lot allocation, subsidy stacking, loan vs reserve fund) inside a regulated deadline; needs validation of AG-blocking frequency (query blocked).

### C-13. Flemish renovation-obligation tracking for buyers and notaries
- Problem: Buyers of E/F homes since 2023 must renovate to D within 6 years and file a new EPC; enforcement by VEKA; deadlines get lost.
- Who suffers: Buyers; notaries (1,200 offices) who inform them.
- Frequency/cost signal: Fine EUR 500-5,000, repeatable — VERIFIED.
- Current workaround: Nothing; notary letter.
- Spend signal (WTP): Low (consumer).
- Existing players noticed: EPC certifiers' blogs; none for tracking.
- Why now: First 2023 cohort deadlines fall 2029.
- Evidence URLs: https://www.energiebewustontwerpen.be/energieprestatiecertificaat-epc/wat-als-je-epc-d-niet-haalt/
- Quick take: weak — consumer, low WTP, deadline far away.

### C-14. Rental management for small private landlords (indexation, deposits, MyRent)
- Problem: Private landlords track indexation, deposits and registration manually.
- Who suffers: Private landlords; rentmeesters.
- Frequency/cost signal: Annual indexation, per-contract admin — INFERENCE.
- Current workaround: Excel; rentmeester at a % of rent.
- Spend signal (WTP): Rentmeester fees; SaaS (Kotmaster, Rentio, Rent Expert).
- Existing players noticed: Kotmaster, Rentio, Rent Expert, Index At Work, Vastio, Korfine (deposits).
- Why now: Rent-index rules changing by region.
- Evidence URLs: https://kotmaster.be/ ; https://www.rentio.be/nl-be ; https://steunpuntwonen.be/wp-content/uploads/2025/02/Ad-hoc_Rendementsanalyse-private-huur_EIND.pdf
- Quick take: crowded.

### C-15. Horeca margin squeeze (food, wages, energy) with no margin visibility
- Problem: Restaurants cannot pass on cost increases; margins collapse; 154 horeca bankruptcies in first 5 months of 2025 (highest in years).
- Who suffers: Independent cafés/restaurants.
- Frequency/cost signal: 154 bankruptcies Jan-May 2025; Q2 2025 3,410 total Belgian bankruptcies, horeca/construction/retail hardest hit; horeca prices +5% (ING) — VERIFIED (summaries).
- Current workaround: Accountant, gut feel, POS reports.
- Spend signal (WTP): POS/ordering subscriptions; low cash.
- Existing players noticed: Not surfaced in search (POS vendors known generally).
- Why now: Cost inflation 2022-2025.
- Evidence URLs: https://www.kmoinsider.be/finance/faillissementen-pieken-in-2025-maar-belgische-bedrijven-blijven-opvallend-veerkrachtig ; https://www.nieuws365.be/financieel/recordaantal-faillissementen-in-belgie-toch-zien-experts-lichtpunten
- Quick take: weak — real pain, but low WTP and cash-poor customers; crowded POS/analytics.

### C-16. Retail vacancy and independent-shop closures
- Problem: Shop vacancy at record >11% end-2025 (Flanders 11.9%); independent retailers closing.
- Who suffers: Independent retailers; municipalities.
- Frequency/cost signal: 10.4% (end 2023) -> 11.2% (early 2025) -> >11% record end 2025; a third vacant >3 years — VERIFIED (Locatus via UNIZO/Business AM).
- Current workaround: n/a.
- Spend signal (WTP): Low.
- Existing players noticed: Locatus (data).
- Why now: Bankruptcies, bank-branch closures.
- Evidence URLs: https://www.unizo.be/berichten/pers/unizo-zeer-bezorgd-over-stijging-leegstand-handelskernen-winkelshift-nu-de-praktijk ; https://businessam.be/leegstand-van-handelpanden-in-belgie-stijgt-tot-een-recordhoogte
- Quick take: weak — macro problem, not a software wedge.

### C-17. Energy sharing (energiedelen) killed by supplier admin fees
- Problem: Only 0.8% of ~600,000 solar owners with digital meters share energy; suppliers charge up to EUR 300 admin fees (ENGIE EUR 121 incl. VAT) so participants lose money ("cost 129, earned 17").
- Who suffers: Solar owners, energy communities, apartment buildings wanting collective self-consumption.
- Frequency/cost signal: 0.8% adoption; EUR 100-300 fees — VERIFIED (VRT, ENGIE summaries).
- Current workaround: Fluvius "Mijn Fluvius" registration; giving up.
- Spend signal (WTP): Negative today (fees exceed benefit).
- Existing players noticed: Fluvius, ENGIE, DATS 24, VREG dashboard.
- Why now: Regulator scrutiny (VRT coverage June 2025); tariff reform.
- Evidence URLs: https://www.vrt.be/vrtnws/nl/2025/06/20/energiedelen-in-de-vergeethoek-gedrumd-leveranciers-rekenen-tot/ ; https://www.vlaamsenutsregulator.be/cijfers/dashboard-energie-delen-en-verkopen
- Quick take: unclear — the blocker is supplier fee structure, not a missing tool; only attractive if regulation forces fees down or a supplier-agnostic settlement layer becomes possible.

### C-18. Solar/battery installers after subsidies ended: selling on ROI under capacity tariff
- Problem: All Flemish solar and home-battery subsidies are gone (battery since 31 Mar 2023; retroactive subsidy closed 31 Dec 2025); profitability now depends on capacity tariff, smart steering and dynamic tariffs, which installers must model per customer.
- Who suffers: Solar/battery installers (count not found); customers.
- Frequency/cost signal: Subsidy end dates — VERIFIED (multiple installer sites); installer bankruptcies: Evidence not found.
- Current workaround: Vendor calculators, generic ROI claims.
- Spend signal (WTP): Mijn VerbouwLening 0-1.5% loans exist; installer software spend not found.
- Existing players noticed: Fluvius, installer blogs; no dominant ROI-simulation SaaS surfaced.
- Why now: Plug-and-play allowed since 17 Apr 2025; dynamic tariffs; capacity tariff.
- Evidence URLs: https://www.energiebewustontwerpen.be/thuisbatterijen/premie/ ; https://sungreenenergy.be/thuisbatterij/wetgeving/
- Quick take: unclear — demand shock for installers is real, but a simulation tool is easily copied; better as a feature for a lead-gen marketplace.

### C-19. Heat-pump premium dossiers (Mijn VerbouwPremie) handled by installers
- Problem: Heat-pump premiums survive in Flanders but require RESCert installers, digital filing via Fluvius within 24 months, 3-6 months payout, and files get rejected for documentation issues (e.g., cooling function not disabled). Installers end up doing the dossier for customers.
- Who suffers: RESCert HVAC installers; homeowners.
- Frequency/cost signal: Payout 3-6 months; rejection patterns — VERIFIED (installer sites); volume: Evidence not found.
- Current workaround: Installer staff fill in forms; customers wait.
- Spend signal (WTP): Premium amounts significant per file; installer admin time.
- Existing players noticed: Fluvius portal (public); installer blogs (AVS, GeoTherma, AVYclima).
- Why now: 2025-2026 premium reform kept heat pumps; other premiums cut.
- Evidence URLs: https://www.avsservice.be/warmtepompen/premie/ ; https://www.frankenergie.be/nl/kennisbank/energie/mijn-verbouwpremie
- Quick take: unclear — small niche; risk that Fluvius simplifies the portal and removes the need.

### C-20. EV charge-point obligation (>20 parking spaces) compliance and billing for SMEs
- Problem: Since 1 Jan 2025 non-residential buildings with >20 parking spaces need >=2 charge points (Brussels: 10% offices / 5% others); VEKA can fine EUR 2,000 per missing point; SMEs must then manage charging, employee reimbursement and billing.
- Who suffers: SMEs with parkings, building owners, syndics of mixed buildings.
- Frequency/cost signal: Fine EUR 2,000 per missing point — VERIFIED (Certipower/Go Watts summaries).
- Current workaround: CPO packages, installer bundles.
- Spend signal (WTP): Hardware + CPO subscriptions.
- Existing players noticed: Stroohm, Vonk, Evolut-ion, Certipower, Ensatec, BESA (federation).
- Why now: 2025 obligation, enforcement by VEKA.
- Evidence URLs: https://www.certipower.be/nl/over-ons/blog/verplichting-van-laadpalen-belgie ; https://gowatts.be/verplichtingen-voor-laadpunten-wat-bedrijven-moeten-weten-in-2025/
- Quick take: crowded — CPO/installer market is saturated.

### C-21. Small law firms: 10-20% of billable hours never invoiced
- Problem: Fragmented tools (documents, email, time, billing) cause double entry; firms fail to bill 10-20% of billable hours.
- Who suffers: Solo and 1-5 lawyer firms.
- Frequency/cost signal: 10-20% unbilled hours, "tens of thousands of euros per year" for a mid firm — VERIFIED (vendor blogs, biased).
- Current workaround: Multiple tools, Excel, memory.
- Spend signal (WTP): Kleos, LEAP, Septeo, MV Office, Hammock, Legalsense subscriptions.
- Existing players noticed: Wolters Kluwer Kleos, LEAP, Septeo, MV Office, Hammock, Legalsense, Abakion.
- Why now: E-invoicing 2026.
- Evidence URLs: https://www.septeo.be/nl-be/oplossingen/advocaten-software-facturatie-incasso ; https://mvoffice.be/ ; https://projecthours.nl/2025/11/20/urenregistratie-in-de-advocatuur/
- Quick take: crowded.

### C-22. Architects: structurally under-priced fees and no project profitability tracking
- Problem: Architects earn far below the EUR 65-95/h deemed fair; one in five of 1,800 surveyed considers leaving; workload high; time-per-project rarely measured.
- Who suffers: Small architecture firms (493 Flemish firms surveyed in spring 2025) — VERIFIED.
- Frequency/cost signal: EquiLibre study (HIVA-KU Leuven for the Orde): ~20% consider leaving; fair rate 65-95 EUR/h, "more than half higher than reality" — VERIFIED (NAV/Architectura summaries).
- Current workaround: Percentage fees, Excel, B-abel-type admin tools.
- Spend signal (WTP): 120% deduction for invoicing-software subscriptions 2024-2027; 20% investment deduction for digital — VERIFIED (NAV).
- Existing players noticed: B-abel, NAV guidance, generic time-tracking tools.
- Why now: Orde/NAV push on fees; e-invoicing 2026; survey-backed software development.
- Evidence URLs: https://www.architectura.be/nl/nieuws/een-op-vijf-architecten-denkt-aan-stoppen-bevraging-legt-structurele-problemen-in-de-sector-bloot/ ; https://www.nav.be/artikel/262/15-tips-om-een-realistisch-ereloon-te-bekomen/ ; https://lirias.kuleuven.be/retrieve/e2173dbe-203f-4dbd-832a-58df88288d7e
- Quick take: promising-but-small — clear FP&A-type need (fee vs hours vs margin per project) and a sector body actively looking for tools; WTP modest.

### C-23. Very small VZW/ASBLs: sloppy or unfiled annual accounts, UBO re-confirmation
- Problem: Very small non-profits barely publish annual accounts and those filed are sloppy; UBO register must be confirmed yearly and updated within a month of board changes; filing on paper at the court registry.
- Who suffers: Tens of thousands of micro non-profits run by volunteers (count not verified).
- Frequency/cost signal: IBR-IRE finding on quality — VERIFIED; annual deadlines — VERIFIED (VI.BE, SBB).
- Current workaround: Volunteer treasurer with Excel; penningmeester.be; umbrella-org templates.
- Spend signal (WTP): Very low (free filing, volunteer boards).
- Existing players noticed: penningmeester.be, SBB, Donorinfo, umbrella organisations (KSA, Danspunt).
- Why now: Companies-and-associations code obligations; UBO.
- Evidence URLs: https://www.ibr-ire.be/nl/actueel/news-detail/jaarrekeningen-van-zeer-kleine-vzw-s-worden-amper-gepubliceerd-en-blijven-slordig ; https://vi.be/advies/jaarlijkse-deadlines-voor-vzw-s
- Quick take: weak — huge count, near-zero WTP; only viable via umbrella federations or subsidy bodies as payer.

### C-24. Accounting-firm capacity crunch: half of Belgian firms refuse new clients
- Problem: Accountants are a shortage profession in all three regions; 30% of dossier-manager vacancies go unfilled; 1 in 2 firms has a client stop (56% refuse clients in one survey); 52% plan no hires in 2026; growth ambition dropped from 54% to 40%. SMEs cannot find an accountant, and firms cannot deliver advisory/FP&A work.
- Who suffers: Accounting firms (ITAA members) and the SMEs they cannot serve.
- Frequency/cost signal: All figures above — VERIFIED (Wolters Kluwer Accountancy Trends / ITAA via AccountancyVandaag, HRmagazine, FDmagazine summaries). Expert-comptable on shortage lists in Flanders, Wallonia and Brussels (ITAA blog, July 2026) — VERIFIED.
- Current workaround: Client stops, price increases ("accountant becomes a luxury product"), offshoring, automation tools.
- Spend signal (WTP): 58% of firms say reducing workload is the top priority — VERIFIED; firms already pay for Wolters Kluwer/Exact/Yuki-type stacks.
- Existing players noticed: Wolters Kluwer, Acerta (summit), ITAA; AI bookkeeping tools not surfaced in this stream.
- Why now: Peppol e-invoicing makes source data structured; AI agents; demographic retirement wave.
- Evidence URLs: https://accountancyvandaag.be/meer-dan-56-van-de-accountants-weigert-klanten-wordt-de-accountant-een-luxeproduct/ ; https://hrmagazine.be/nl/posts/personeelstekort-leidt-tot-klantenstops-bij-accountantskantoren ; https://www.blogitaa.be/fr/2026/07/01/lexpert-comptable-toujours-un-metier-en-penurie-en-flandre-en-wallonie-et-a-bruxelles/
- Quick take: promising — the single clearest structural bottleneck found; a founder with FP&A skills can either sell capacity to firms (AI-assisted dossier work, management reporting) or serve orphaned SMEs directly.

### C-25. Peppol e-invoicing mandate: two-thirds of SMEs unprepared, 660k enterprises still to onboard
- Problem: From 1 Jan 2026 all B2B invoices between Belgian VAT-registered enterprises must be structured e-invoices; by late 2025 ~515,000 of ~1,178,000 enterprises had complied; 67% of SMEs did not use e-invoicing; a third were unaware; fines up to EUR 5,000; tolerance until end March 2026.
- Who suffers: ~660,000 enterprises (mostly micro), their accountants.
- Frequency/cost signal: All figures — VERIFIED (VRT/FOD Financiën, Horus survey, Wolters Kluwer summaries).
- Current workaround: Accountant onboarding, free Peppol tools, delay.
- Spend signal (WTP): 120% cost deduction on invoicing-software subscriptions 2024-2027 — VERIFIED (NAV summary).
- Existing players noticed: Billit, Banqup, e-invoice.be, Horus, Wolters Kluwer; dozens of access points.
- Why now: Mandate live; next step e-reporting (expected 2028, not verified here).
- Evidence URLs: https://www.vrt.be/vrtnws/nl/2025/12/04/peppol-ondernemingen-zaak-uitstel-factuur-online/ ; https://www.ictmagazine.be/nieuws/twee-derde-belgische-kmos-nog-niet-klaar-voor-verplichte-e-facturatie-in-2026/ ; https://www.wolterskluwer.com/nl-be/expert-insights/e-invoicing-2026-fines-up-to-5000
- Quick take: crowded for the invoicing tool itself; the durable by-product is structured invoice data on which C-01, C-02, C-24 can build.

### C-26. Public procurement inaccessible to SMEs (80% report barriers; Belgium worst in EU)
- Problem: SMEs find tender documents incomprehensible (lawyer-written), requirements excessive, payment terms long; UNIZO says nobody in Europe does worse than Belgium on SME access.
- Who suffers: SMEs wanting public work (construction, services, IT); local authorities that get few bids.
- Frequency/cost signal: 80% of SMEs that participated experienced barriers — VERIFIED (UNIZO dossier Nov 2025); limited-value threshold raised EUR 30k -> 75k — VERIFIED.
- Current workaround: Skip tenders; consultants; large firms win.
- Spend signal (WTP): Tender consultants; membership bodies.
- Existing players noticed: FOD Economie guidance; e-Procurement platform (public); no SME-side SaaS surfaced.
- Why now: 2025-2026 legal changes and Flemish circular to open procurement to SMEs; AI can summarise/pre-fill tenders.
- Evidence URLs: https://www.unizo.be/system/files?file=downloads/nov2025_UNIZO_dossier+overheidsopdrachten_DEF_0.pdf ; https://www.unizo.be/berichten/pers/niemand-doet-slechter-europa-belgie-sluit-de-deur-voor-kmos-bij-overheidsopdrachten ; https://www.minro-legal.be/post/belangrijke-wetswijzigingen-op-komst-voor-overheidsopdrachten
- Quick take: promising — clear, measured pain, political tailwind, AI-shaped (document parsing, bid drafting, compliance checklist); need to check EU-wide tender-SaaS competitors not surfaced here.

### C-27. Farmers: MAP7 admin (AGR-GPS manure transport) plus e-invoicing since 2026
- Problem: MAP7 adds mandatory GPS-tracked manure transport and more registrations; farmers also fall under e-invoicing from 2026; many rely on forfait tax regimes and paper.
- Who suffers: Flemish farmers (count not found), agricultural contractors.
- Frequency/cost signal: AGR-GPS obligation for all liquid manure — VERIFIED (VLM summaries); e-invoicing applies to farmers — VERIFIED (Landbouwleven).
- Current workaround: Paper, accountant (SBB, Boerenbond), VAC.eu type services.
- Spend signal (WTP): Agricultural accountancy services; low software WTP — INFERENCE.
- Existing players noticed: VAC.eu, SBB, VLM Mestbank tools.
- Why now: MAP7 2025, e-invoicing 2026.
- Evidence URLs: https://www.landbouwleven.be/24251/article/2026-01-06/ook-landbouwers-ontsnappen-niet-aan-de-elektronische-facturatie ; https://www.vlm.be/nl/SiteCollectionDocuments/Mestbank/Algemeen/Nieuwe_maatregelen_Peer.pdf
- Quick take: unclear — captive by Boerenbond/SBB ecosystem; hard to enter from Brussels without sector ties.

### C-28. Wholesale/distribution SMEs on Excel or legacy ERP
- Problem: Many trading SMEs run stock and orders in Excel or outdated ERP.
- Who suffers: Wholesale/distribution SMEs.
- Frequency/cost signal: Vendor claims only — INFERENCE.
- Current workaround: Excel; legacy ERP.
- Spend signal (WTP): ERP subscriptions.
- Existing players noticed: Prodis, Exact Online, Odoo (Belgian), Plugnotes, CAT Solutions, EOS, Dimasys, Priority.
- Why now: Peppol.
- Evidence URLs: https://www.maes-media.be/blog/overzicht-populaire-crm-en-erp-systemen-voor-kmo-s ; https://www.plugnotes.com/nl/blog/10-beste-voorraadbeheer-software
- Quick take: crowded (Odoo is Belgian and dominant in this space).

### C-29. Subsidised digital-advice market shrinks in Flanders, persists in Wallonia
- Problem: From 1 Feb 2026 the Flemish kmo-portefeuille only subsidises advice on cybersecurity; all other advice (incl. digitalisation, finance) lost support. Wallonia's chèques (maturité numérique) still reimburse 90% up to EUR 7,400 (diagnosis EUR 1,900).
- Who suffers: Flemish consultants/advisers relying on the subsidy; SMEs who used it to fund digital projects.
- Frequency/cost signal: ~55,000 enterprises, >125,000 applications in 2025 — VERIFIED (VLAIO); support rates 30%/20%, cap EUR 7,500; digital/cyber themes 45%/35% — VERIFIED; Walloon 90% / EUR 7,400 — VERIFIED (DigitalWallonia).
- Current workaround: Training route (still subsidised in Flanders); Walloon vouchers.
- Spend signal (WTP): Structural fact more than opportunity.
- Existing players noticed: VLAIO, Digital Wallonia, DigiWall, KERN-IT.
- Why now: Jan 2026 Flemish decision.
- Evidence URLs: https://www.vlaio.be/nl/nieuws/hervorming-kmo-portefeuille-vanaf-1-februari-2026-enkel-nog-advies-voor-cybersecurity ; https://www.digitalwallonia.be/fr/fiches-action/transformation-numerique-cheques-maturite-numerique-2025/
- Quick take: weak as an opportunity; important as a go-to-market fact (training is still subsidised in Flanders; advice in Wallonia).

### C-30. Notarial offices: closed, federation-driven digitalisation
- Problem: 1,200 offices / 1,500 notaries / 7,500 staff; digitalisation is centralised via Fednot (eNotariaat, eRegistration) with Proximus NXT; little room for third-party tools.
- Who suffers: n/a for outsiders.
- Frequency/cost signal: Counts — VERIFIED (notaris.be summary).
- Current workaround: Fednot tools.
- Spend signal (WTP): Federation-level.
- Existing players noticed: Fednot, Proximus NXT.
- Why now: n/a.
- Evidence URLs: https://www.notaris.be/over-de-notaris/de-notariele-instellingen/de-koninklijke-federatie-van-het-belgisch-notariaat-fednot ; https://www.proximus.be/nl/id_b_cl_digitization_at_fednot/bedrijven-en-overheden/news/nieuws-blog/klanten-vertellen/digitization-at-fednot.html
- Quick take: weak — closed ecosystem.

---

## Belgian structural facts (verified from search summaries)

- Micro-enterprises: 96.1% of Belgian enterprises have <10 employees (EU: 93.8%). The 1-9 employee group fell 1.5% in 2024 (vs +0.7%/yr average over the previous decade). Net new enterprises: 25,651 in 2023, 18,748 in 2024. — https://news.economie.fgov.be/259020-steeds-meer-actieve-kmo-s-in-belgie/ ; https://sdz.be/2025/01/06/belgie-recordaantal-actieve-kmos/
- Bankruptcies: Q2 2025 3,410 (5-year high), hardest hit horeca, construction, retail; construction H1 2025 1,443; transport 2025 413 (record, +1/3 vs 2024). — https://www.kmoinsider.be/finance/faillissementen-pieken-in-2025-maar-belgische-bedrijven-blijven-opvallend-veerkrachtig ; https://embuild.be/nl/faillissementen-de-bouw-neerwaartse-spiraal-blijft-aanhouden-door-combinatie-van-factoren ; https://www.tlv.be/nieuws/recordaantal-faillissementen-in-transportsector-vooral-kleine-spelers-in-last-mile-delivery-zwaar-getroffen
- Construction: >16,000 open vacancies despite record bankruptcies; net loss of 1,402 firms in 2025 (first decline in 10 years); admin burden #1 obstacle (23.5% national; 19.2% Limburg, 7th year running). — https://www.kenniswest.be/artikel/belgische-bouwsector-kampt-met-personeelstekort-ondanks-recordaantal-faillissementen/263412 ; https://embuild.be/nl/voor-het-eerst-10-jaar-minder-bouwbedrijven-sector-onder-zware-druk ; https://www.voka.be/limburg/nieuws/bouwenquete-2025-limburgse-bouwsector-blijft-zwaar-onder-druk
- Shortage professions: VDAB 2026 list 227 occupations (24 fewer than 2025), boekhouder and verpleegkundige among the biggest; Forem 2026 list 144 occupations (75 carried over, 69 new; new criticality index) incl. expert-comptable, conseiller fiscal, comptable interne, assistant comptable; Actiris list (1 July 2026) 110 occupations; expert-comptable is a shortage profession in all three regions (ITAA, July 2026). — https://www.vdab.be/trends-en-cijfers/knelpuntberoepenlijst ; https://www.leforem.be/a-propos/communiques-presse/metiers-en-penurie-2026.html ; https://economie-werk.brussels/news-knelpuntberoepen-2026 ; https://www.blogitaa.be/fr/2026/07/01/lexpert-comptable-toujours-un-metier-en-penurie-en-flandre-en-wallonie-et-a-bruxelles/
- Accounting firms: 30% of dossier-manager vacancies unfilled; 38% actively take new clients, 1 in 2 has a client stop, 56% refuse clients (one survey); 58% say workload reduction is top priority; 73% see client numbers rising without staff; 52% plan no hires in 2026; organic-growth ambition down 54% -> 40%. — https://accountancyvandaag.be/helft-accountants-weigert-nieuwe-klanten/ ; https://www.wolterskluwer.com/nl-be/expert-insights/accountancy-trends-2024 ; https://fdmagazine.be/accounting-controlling/helft-accountantskantoren-voert-klantenstop-in/
- Digitalisation: 84% of Belgian SMEs at least basic digital intensity (Wallonia 79%), 13% very high; 37% of enterprises give ICT training (73% large vs 21% SMEs); 34.5% of companies use at least one AI application (2025). — https://ec.europa.eu/eurostat/web/interactive-publications/digitalisation-2025 ; https://www.sparagus.be/blog/digital-transformation-belgium-2026-sme-adoption-governance
- E-invoicing: ~1,178,000 enterprises must comply; ~515,000 had by late 2025; 67% of SMEs not using e-invoicing (Horus); a third unaware; tolerance to end March 2026; fines up to EUR 5,000; 120% deduction on invoicing-software subscriptions 2024-2027. — https://www.vrt.be/vrtnws/nl/2025/12/04/peppol-ondernemingen-zaak-uitstel-factuur-online/ ; https://www.nav.be/nieuws/e-facturatie-vanaf-2026-verplicht-wat-je-als-architect-nu-al-moet-weten
- Subsidies: kmo-portefeuille 2025: ~55,000 enterprises, >125,000 applications; from 1 Feb 2026 advice only for cybersecurity; rates 30%/20% (45%/35% for digital-cyber and energy themes), cap EUR 7,500/yr. Wallonia chèques: 90% reimbursement, cap EUR 7,400 (diagnosis EUR 1,900), EUR 20M EU envelope for "Relance par le numérique". — https://www.vlaio.be/nl/nieuws/hervorming-kmo-portefeuille-vanaf-1-februari-2026-enkel-nog-advies-voor-cybersecurity ; https://www.digitalwallonia.be/fr/publications/cheques-relance-par-le-numerique/
- Real estate: >90,000 co-ownerships (~1/3 of residential stock, 2021); ~11,000 registered real-estate agents; 497-562 exclusive syndics (4-4.7%). Notariat: 1,200 offices, 1,500 notaries, 7,500 staff. — https://www.ipi.be/actualites/communiques-de-presse/le-nombre-dagents-immobiliers-semble-se-stabiliser-aux-alentours-de-11-000 ; https://www.notaris.be/over-de-notaris/de-notariele-instellingen/de-koninklijke-federatie-van-het-belgisch-notariaat-fednot
- Public procurement: 80% of participating SMEs report barriers; limited-value threshold raised EUR 30k -> 75k (approved spend EUR 90k). — https://www.unizo.be/system/files?file=downloads/nov2025_UNIZO_dossier+overheidsopdrachten_DEF_0.pdf
- Retail vacancy: 11.2% early 2025, record >11% end 2025 (Flanders 11.9%), a third vacant >3 years (Locatus). — https://businessam.be/leegstand-van-handelpanden-in-belgie-stijgt-tot-een-recordhoogte
- Energy: only 0.8% of ~600,000 digital-meter solar owners share energy; supplier admin fees EUR 100-300. — https://www.vrt.be/vrtnws/nl/2025/06/20/energiedelen-in-de-vergeethoek-gedrumd-leveranciers-rekenen-tot/
- Startup ecosystem (StartupBlink 2025): Belgium #23 globally, 1,325 startups, >$1.07B funding, +7.5%; Brussels #64, 424 startups, $139M, +44.9%; "gazelle gap" for scale-ups noted. — https://www.startupblink.com/startup-ecosystem/belgium ; https://www.sramanamitra.com/2025/12/17/belgiums-startup-accelerator-ecosystem-the-conundrum/

## Gaps / not found
- Belgian-specific numbers for freight-forwarder SME customs costs, CBAM declarants in Belgium, solar-installer bankruptcies, pharmacy and care-home counts, frequency of AG blockages on renovation votes: Evidence not found (two queries blocked by search budget).
