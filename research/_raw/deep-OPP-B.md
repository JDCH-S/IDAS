# Deep-dive OPP-B: Peppol portfolio operations for Belgian accounting firms

Date: 2026-09-11. Analyst brief: market researcher + Belgium/EU analyst + technical architect + financial analyst. Founder: Brussels-based, full-time employed, 10-15 h/week, limited capital, MSc corporate finance, controlling/FP&A background, learning Python/SQL/AI agents; English + working French; Dutch flagged where material.

Method: builds on `opportunity-universe.md` rows U-002/U-004/U-005/U-012, `_raw/ci-batch-1.md` blocks U-002/U-004/U-012, stream items A-01, A-03, B-01, B-02, C-25, D-01, E-02 and `_raw/belgium-founder-facts.md`. ~60 new WebSearch queries (EN/NL/FR) plus one GitHub README fetch (recommand-peppol). Pages could not be opened, so every "VERIFIED" below means VERIFIED (search-summary); figures are labelled VERIFIED / ESTIMATE / INFERENCE / HYPOTHESIS or "Evidence not found" (ENF). Every fact carries its URL.

Thesis under test: (1) a paid "Peppol portfolio health check" for 5-50-staff firms (bulk KBO/VAT/Peppol-directory validation of all client and supplier bases, rejection-log review, fix list); (2) a monitoring agent reading Billit/Yuki/Exact/Octopus/Odoo APIs to surface rejected/undelivered invoices and bad identifiers per client; (3) from 2028, a "reported vs booked" reconciliation engine.

---

## 1. Exact problem and exact customer

### 1.1 The problem, decomposed (what actually breaks after the mandate)
Evidence from practitioner and vendor sources surfaced this batch, ranked by how often it appears:

| # | Failure mode | Who feels it | Evidence label | Source |
|---|---|---|---|---|
| a | Wrong-channel / dual identifiers: supplier sends to 0208 (KBO number) while recipient is only on 9925 (VAT number) or vice versa; invoice never arrives, or arrives twice if registered on both without knowing | SME + its bookkeeper | VERIFIED | https://www.peppol-box.be/en/blog/peppol-belgium-problems-2026/ ; https://trends-business-information.be/en/blog-en-2/1-6-million-peppol-ids-but-registration-is-not-yet-uniform ; https://developer.b2brouter.net/discuss/694158835389c26bf3cd2564 |
| b | Scale of identifier mess: 1.6 million Peppol IDs for ~946,000 unique companies (880,000 VAT-registered); 750,000 IDs created in December 2025 alone; all Belgian companies must be on 0208, 9925 optional | System-wide | VERIFIED | https://trends-business-information.be/en/blog-en-2/1-6-million-peppol-ids-but-registration-is-not-yet-uniform ; https://einvoice.belgium.be/en/FAQ/general-questions-about-peppol ; https://invoice-portal.de/belgium-mandates-peppol-id-0208/ |
| c | Network-level rejections for VAT logic, mandatory fields, rounding, recipient data, sender export settings | Sender's bookkeeper | VERIFIED (advisor content) | https://www.b2btax.be/factuur-geweigerd-peppol-netwerk/ ; https://mindyourownbusiness.eu/peppol-foutmeldingen-en-datakwaliteit/ ; https://www.vatupdate.com/2026/08/23/your-peppol-ubl-invoice-was-rejected-how-to-fix-it/ |
| d | "Invoice not found": SME no longer sees a PDF in the mailbox; invoice sits in software; phantom/duplicate/unreadable-XML documents ("kinderziekten") | SME owner, then the firm's support line | VERIFIED | https://accountancyvandaag.be/peppol-verplicht-vanaf-2026-valkuilen-voor-ondernemers-kansen-voor-accountants/ ; https://www.blogitaa.be/2026/07/07/belgie-als-europese-koploper-de-lessen-na-zes-maanden-verplichte-e-facturatie/ ; https://blog.degandpartners.com/nl/article/verplichte-elektronische-facturatie-hoe-een-chaotische-start-te-overwinnen-zonder-de-boekhouding-in-gevaar-te-brengen/29762 |
| e | Workload up, not down: 33% of bookkeepers in a Clearfacts webinar say workload rose since the mandate; Unizo (Aug 2026): promised time savings not there, some platforms still have teething problems | Firms | VERIFIED | https://accountancyvandaag.be/het-moeilijkste-aan-peppol-heeft-niks-met-peppol-te-maken/ ; https://www.vrt.be/vrtnws/nl/2026/08/03/peppol-stand-van-zaken-fod-financien-unizo/ |
| f | Cash: Peppol invoices paid slower than e-mail invoices in Dec 2025 (median 14 days vs 10; Nov average 20 days) because nobody actively handles the receiving side | SMEs (AR) | VERIFIED (search-summary; original dataset not opened) | https://e-invoice.be/blog/wat-als-niet-peppol-factuur ; https://clearnox.com/nl/peppol-betalingsprobleem-debiteurenbeheer/ |
| g | Legal correctness still the issuer's job; corrections now require credit notes, not a re-sent PDF | SME + firm | VERIFIED | https://www.tudors.be/blog/peppol-efacturatie-fouten/ ; https://www.unpaid.be/en/discover/peppol-and-e-invoicing-which-mistakes-does-it-solve-and-which-does-it-not |
| h | Technical vs business status confusion: MLS/MLR proves transport, not acceptance; a separate Invoice Response or ERP workflow is needed to know whether the customer accepted the invoice | AR teams, firms | VERIFIED | https://www.vatupdate.com/2026/08/24/peppol-status-messages-explained-why-mls-is-not-the-same-as-a-business-level-response/ ; https://www.babelway.com/resources/blog/peppol-messages-france-belgium-poland-e-invoicing/ |

Frequency signal: the Belgian Peppol Service Providers Forum observed after the launch that roughly 1% of exchanges had problems, "several hundred thousand" disrupted exchanges in production volume, and expected better registration data quality to remove a significant part of these — VERIFIED (via peppoledge summary of forum observations; primary minutes not opened): https://www.peppoledge.com/post/peppol-e-invoicing-launch-in-belgium-lessons-learned-after-two-months. FPS Finance updated its FAQ in May 2026 on rejection, reverse charge and Peppol delays — VERIFIED: https://www.vatupdate.com/2026/05/18/belgium-updates-b2b-e-invoicing-new-faq-on-rejection-reverse-charge-and-peppol-delays/.

INFERENCE: the operational problem is real but is (i) concentrated in the identifier/registration layer (a, b), (ii) partly a human-workflow problem inside the SME (d, e, f) rather than a data problem, and (iii) expected by the network operators themselves to shrink as registration data matures. That shapes the product: a one-off clean-up has a clear 2026-27 window; a perpetual "exceptions desk" has a shrinking base unless 2028 e-reporting re-creates mismatch volume.

### 1.2 The exact customer
- Buyer: the managing partner / "office manager" / digitalisation lead of a Belgian accounting firm ("boekhoudkantoor" / "fiduciaire") with roughly 5-50 staff — big enough to have hundreds of client files across several software stacks, small enough to have no internal IT/data person. Nearly three quarters of ITAA-panel firms have 10 or fewer staff — VERIFIED: https://www.blogitaa.be/2025/11/05/ontdek-de-resultaten-van-de-jaarlijkse-barometer-van-het-beroep/. The 5-50 band is therefore a minority of firms (see section 4).
- User: the dossierbeheerder / assistant who today answers "my invoice never arrived" calls, re-keys, and opens access-point tickets; and the person who onboarded clients on Peppol (often via the firm's own Billit/Yuki/Codabox/Liantis mandate — firms can activate Peppol for clients under their existing mandate: VERIFIED https://support.liantis.be/hc/nl/articles/26084441950610-Hoe-activeer-ik-Peppol-voor-mijn-klanten-als-boekhouder).
- Signer: partner. Firms are already told to put Peppol clauses, risk analysis and deadlines into engagement letters and to document warnings to avoid liability — VERIFIED: https://accountancyvandaag.be/wat-met-klanten-die-de-verplichte-e-facturatie-via-peppol-blijven-uitstellen/ ; https://instaclause.com/be-nl/blog/e-facturatie-peppol-algemene-voorwaarden. That liability framing is the strongest "why the partner cares" hook found.
- Software stack (matters for connectors): Flanders is cloud-native — Exact Online, Octopus, Adsolut, Yuki dominate; Wallonia is on-premise/integrator-managed — Horus, WinBooks, Sage BOB50, Odoo — VERIFIED: https://www.chift.eu/blog/the-accounting-software-landscape-in-belgium-a-2026-guide. Peppol adoption is also regional: Flanders >=75%, Wallonia/Brussels <=65% (Jan 2026 map) — VERIFIED: https://datanews.knack.be/analyse/achtergrond/grote-regionale-verschillen-in-de-belgische-adoptie-van-peppol/. Implication: the API-friendly stack is Dutch-speaking; the French-speaking stack is harder to connect. Dutch matters.
- Secondary customer (not the thesis, but the same data): SMEs 10-250 FTE with their own AR/AP teams (D-01). Not pursued here because the firm is the aggregator.

---

## 2. Evidence of demand

### 2.1 Practitioner voices (what the profession itself says)
- ITAA, 7 Jul 2026 ("Belgium as European front-runner: lessons after six months"): Peppol is a change programme, not an IT project; the accountant's role shifts "from technology to advice: guiding clients in data quality, process adaptation and connection to an increasingly international chain" — VERIFIED: https://www.blogitaa.be/2026/07/07/belgie-als-europese-koploper-de-lessen-na-zes-maanden-verplichte-e-facturatie/. This is the profession's own framing of the OPP-B job ("data quality guidance") — but it frames it as the accountant's job, not a third party's.
- ITAA, 29 May 2026 ("E-reporting from 2028: 6 points"): e-reporting builds on e-invoicing, "not a second big migration"; firms that guided clients correctly in 2026 have a workable base; asks for workable exception handling so small firms need not interpret edge cases; suggests a client mailing by end-2026 ("after e-invoicing in 2026 comes a second phase in 2028: we monitor it for you") — VERIFIED: https://www.blogitaa.be/2026/05/29/e-reporting-vanaf-2028-6-punten-om-uw-kantoor-en-uw-clienten-voor-te-bereiden/.
- ITAA survey Q4 (via Banqup): share of firms where <25% of clients were ready fell from ~60% (Q2) to 38.3% (Q4 2025); firms with >75% of clients ready doubled 9.3% -> 18.3% — VERIFIED: https://www.banqup.com/nl-be/resources/blog/e-facturatie-groeit-door-drie-positieve-ontwikkelingen-in-de-accountancysector.
- ITAA, Jul/Aug 2026: software market perceived as strongly concentrated by >50% of 1,642 respondents; "digital dependency" to be managed as a professional risk — VERIFIED: https://www.blogitaa.be/2026/07/07/softwaremarkt-onder-druk-wat-1-642-confraters-ons-vertellen-over-concentratie-en-afhankelijkheid/ ; https://www.blogitaa.be/2026/08/26/digitale-afhankelijkheid-een-beroepsrisico-dat-om-beheer-vraagt/. Supports a vendor-neutral positioning, not a WTP.
- AccountancyVandaag: "a relatively large percentage of e-invoices still contain errors" (no number); most-asked client question is "where is my invoice"; 33% of Clearfacts-webinar bookkeepers report higher workload; "the hardest part of Peppol has nothing to do with Peppol" (follow-up/payment discipline) — VERIFIED: https://accountancyvandaag.be/peppol-verplicht-vanaf-2026-valkuilen-voor-ondernemers-kansen-voor-accountants/ ; https://accountancyvandaag.be/het-moeilijkste-aan-peppol-heeft-niks-met-peppol-te-maken/ ; https://accountancyvandaag.be/de-zes-meest-gestelde-vragen-over-peppol-beantwoord/.
- FDmagazine ("no momentum in the e-invoicing market", Securex/Nymus): some customers de-register from Peppol because of technical problems at their access point; Securex sends ~5% of invoices via Peppol — VERIFIED but the article appears pre-mandate (date not shown in summary; treat as historical context): https://fdmagazine.be/tech/er-zit-geen-schwung-in-de-markt-van-e-facturatie.
- VRT / FPS Finance / Unizo, 3 Aug 2026: 1,060,000 businesses registered = 89% of VAT-liable; FPS calls ~90% the natural ceiling; Unizo: system works technically, time savings absent, some platforms still have teething problems, confusion because some large organisations/governments are themselves not fully on e-invoicing; older self-employed and side-job entrepreneurs need their accountant's help — VERIFIED: https://www.vrt.be/vrtnws/nl/2026/08/03/peppol-stand-van-zaken-fod-financien-unizo/.
- Firm blogs (Fiskodata, Kantoor ATEXIO, Tudors, Sels & Verhoeven, De Gand & Partners) republish the same "pitfalls" content; none advertises a paid clean-up service — VERIFIED (absence): https://www.fiskodata.be/nieuws/peppol-verplicht-vanaf-2026-met-welke-mogelijke-valkuilen-moet-je-rekening-houden ; https://www.tudors.be/blog/peppol-efacturatie-fouten/ ; https://sva-accountants.be/peppol-tolerantieperiode-en-boetes-vanaf-2026/.
- LinkedIn / forum threads with named practitioners complaining about rejections: Evidence not found (search surfaces only vendor and firm marketing pages). Odoo forum threads exist on "suppliers can't send me invoices via Peppol" and cascading import failures in Odoo 18 — VERIFIED: https://www.odoo.com/forum/help-1/suppliers-cant-send-me-invoices-via-peppol-290584 ; https://github.com/odoo/odoo/issues/211405.

Reading: the pain the profession articulates loudest is (1) client hand-holding/"where is my invoice", (2) workload, (3) payment follow-up, (4) data quality. Rejection triage per se is inside (4) but is never named as a top-3 pain by a practitioner source. That weakens the "exceptions desk" framing and strengthens the "data-quality / readiness" framing.

### 2.2 Rejection volumes / rates
- Network-wide: ~1% problematic exchanges shortly after launch, expected to fall — VERIFIED (secondary): https://www.peppoledge.com/post/peppol-e-invoicing-launch-in-belgium-lessons-learned-after-two-months.
- Per access point (Billit, Banqup, Codabox, Yuki): Evidence not found. Billit claims 120,000+ businesses and 2M+ invoices/month (third-party page) — VERIFIED (claim): https://vinkius.com/apps/billit-mcp. INFERENCE: 1% of ~2M/month at Billit alone would be ~20,000 problem documents/month — but that is an arithmetic illustration, not a measured figure.
- FPS Finance / BOSA published rejection statistics: Evidence not found. Peppolcheck.be publishes growth and SMP statistics (registrations, not rejections) — VERIFIED: https://www.peppolcheck.be/growth ; https://www.peppolcheck.be/smp-stats.

### 2.3 Fine enforcement since 1 April 2026
- Framework: EUR 1,500 / 3,000 / 5,000, three-month buffer between fines, each quarter can count as a new infraction; no warnings promised; "stricter controls announced for H2 2026" — VERIFIED: https://www.xerius.be/nl-be/nieuws/boetes-e-facturatie ; https://www.ibgraf.com/amende-peppol-en-belgique-sanctions-tolerance-et-risques ; https://sayli.be/blog/fr/peppol/amendes-peppol-belgique-2026.
- Number of fines actually issued, controls performed, or any named enforcement case: Evidence not found (searched NL/FR/EN, Sept 2026). This matters: the "fear of fines" urgency lever is currently rhetorical.

### 2.4 Peppol Invoice Response / MLS adoption in Belgium
- MLS v1.0.0 final May 2025; v1.1.0 on 7 Jul 2026; draft MLS implementation plan and MLR phase-out plan under eDEC review; OpenPeppol requires ISO 27001 for all service providers by 1 Jul 2027 — VERIFIED: https://www.vatupdate.com/2026/08/24/peppol-status-messages-explained-why-mls-is-not-the-same-as-a-business-level-response/ ; https://docs.peppol.eu/edelivery/specs/mls/v1.0.0/mls/spec/ ; https://openpeppol.atlassian.net/wiki/spaces/Belgium/pages/5265883137.
- Business-level Invoice Response adoption by Belgian SME software/access points: Evidence not found (Billit, Banqup, Digiteal pages do not mention it). INFERENCE: for the foreseeable period, "accepted by the customer" cannot be read from the network for most Belgian SMEs; a monitoring tool can only see transport status + what each ledger records. This caps the value of an "exceptions" agent at the transport/identifier layer.

### 2.5 Lookup / open-data infrastructure the thesis depends on
- Peppol Directory REST API: free, GET-only, JSON/XML, rate-limited to 2 queries/second (HTTP 429 above), full recipient list downloadable; operated by OpenPeppol and the service providers — VERIFIED: https://directory.peppol.eu/public/menuitem-docs-rest-api ; https://openpeppol.atlassian.net/wiki/spaces/Belgium/pages/2804154401/Who+receives+Peppol+invoices+Is+there+a+list ; https://github.com/phax/phoss-directory/issues/51. Bulk terms beyond the rate limit: Evidence not found (INFERENCE: at 2 q/s a 5,000-counterparty base takes ~40 minutes; feasible, and the full-list download avoids per-query calls entirely).
- Free bulk checkers already exist: e-invoice.be "Peppol Radar" accepts CSV upload of company numbers, no account, free; e-invoice.be lookup API docs; Peppol Practical Belgian participant check; Nymus lookup; Finplex checker; peppolcheck.be — VERIFIED: https://e-invoice.be/peppol-radar ; https://docs.e-invoice.be/guides/lookup-participants ; https://peppol.helger.com/public/menuitem-tools-pid-check-be ; https://nymus.be/en/peppol-lookup/ ; https://app.peppolchecker.eu/ ; https://www.peppolcheck.be/en. This is the single most thesis-weakening fact in section 2: the core of the "health check" (is every counterparty on Peppol, on which scheme) is already a free CSV upload.
- KBO/CBE: Open Data flat files free after registration, published daily; live Public Search SOAP/REST webservice is paid, requires an agreement with FPS Economy, pricing on request — VERIFIED: https://kbopub.economie.fgov.be/kbo-open-data/login?lang=nl ; https://economie.fgov.be/sites/default/files/Files/Entreprises/KBO/Cookbook-KBO-Public-Search-Webservice.pdf ; https://www.businessdataguide.com/blog/jurisdictions/belgium-company-search-guide.
- VIES: shared global and per-member-state concurrency limits (MS_MAX_CONCURRENT_REQ), thresholds undisclosed at member states' request, batch/async services exist via resellers — VERIFIED: https://viesapi.eu/vies-error-the-maximum-number-of-concurrent-requests-has-been-reached-fr/ ; https://viesac.eu/articles/what-to-do-when-vies-unavailable. Founder note: the OpenAccountants MCP `validate_vat_number` tool exists in this environment but requires an account (see founder-facts file).
- Hermes (BOSA e-mail fallback) fully decommissioned 31 Dec 2025, read-only until Mar 2026 — VERIFIED: https://www.banqup.com/resources/blog/belgium-retires-the-hermes-platform-why-your-e-invoicing-strategy-must-change-before-2026. So "undelivered because recipient not on Peppol" is now a hard failure, not a soft fallback.

---

## 3. Willingness to pay (what firms pay today)

| Item | Price | Label | Source |
|---|---|---|---|
| Peppol Box (send/receive, identifier-issue support, export to BOB/WinBooks/Horus) | from EUR 5-7/month per company | VERIFIED | https://www.peppol-box.be/nl/ |
| PepCerto access point | from EUR 9.99/month | VERIFIED | https://www.pepcerto.com/en/peppol |
| Let's Peppol (BARGE vzw) | free, open-source access point for SMEs and accountants | VERIFIED | https://letspeppol.org/nl/ |
| Doccle Peppol registration for self-employed/SMEs | free since end-2024 | VERIFIED | https://faq.codabox.com/nl/support/solutions/articles/75000125889-peppol-op-doccle-voor-zelfstandigen-en-kmo-s |
| Billit accountant portal | free for the accountant; SME licences Starter (<=25 docs/month) / Premium (26-500) / Enterprise (<=1,000); amounts not in summary | VERIFIED (structure), amounts ENF | https://www.billit.eu/nl-be/prijzen/ ; https://www.billit.eu/nl-be/helpartikelen/instellingen/licentie/overzicht-van-de-billit-licenties/ |
| Codabox CODA/CARO/VOILA | monthly fee per client reference, tiered (CODA+CARO+VOILA counts summed; higher volume = lower unit price); one-time fee per mandate; amounts not in summary | VERIFIED (structure), amounts ENF | https://faq.codabox.com/en/support/solutions/articles/75000118467-codabox-pricing-one-time-fees-and-recurring-costs |
| OkiOki (Xerius) intake app incl. Peppol status badges | EUR 8-11/month per accountant seat/dossier (volume) | VERIFIED (batch 1) | https://www.xerius.be/nl-be/partner/accountant/okioki |
| Mid-market Peppol integration (Dragintra) | EUR 50-500/month + EUR 500-5,000 implementation + from EUR 0.10/invoice | VERIFIED (vendor guide) | https://www.dragintra.be/blog/wat-kost-peppol-in-belgie/ |
| Exact Online (larger SMEs, Peppol built in) | from EUR 45/month | VERIFIED | https://www.dsoft.be/peppol-access-point (aggregator summary) |
| Peliqan data platform + hosted MCP (Billit/Exact/Yuki/Silverfin/Peppol) | EUR 150/month annual | VERIFIED (batch 1) | https://peliqan.io/blog/mcp-for-belgian-accountancy/ |
| AdminPulse practice management | EUR 290/month incl. 5 users + 100 files; +EUR 0.75/file | VERIFIED (batch 1) | https://adminpulse.eu/nl-be/prijzen |
| Clearnox dunning | from EUR 100/month | VERIFIED (batch 1) | https://www.capterra.com/p/196592/Clearnox/ |
| Bookkeeper / accountant hourly rates (BE) | bookkeepers EUR 40-60/h; accountants EUR 80-150/h | VERIFIED (directory/guide pages, not ITAA) | https://boekhouders-gids.be/kosten-boekhouder/ ; https://trustlocal.be/belgie/boekhouder/ |
| Firms' own fee for Peppol onboarding of a client | Evidence not found (appears bundled in packages; some vendors do registration free) | ENF | https://www.combell.com/nl/blog/peppol-voor-accountants/ |
| Support-ticket cost at access points | Evidence not found | ENF | — |
| 120% cost deduction for e-invoicing software subscriptions and consulting (small companies, 2024-2027) | applies | VERIFIED (streams A/C) | https://www.vertexinc.com/resources/resource-library/belgiums-2026-e-invoicing-regulations-explained-scope-deadlines-and-penalties |

Derived WTP anchors (ESTIMATE):
- The market's per-SME price anchor for "Peppol" is EUR 0-10/month. Any per-SME pricing above that collides with free or near-free options.
- The firm-level anchor for "tooling that saves staff hours" is EUR 100-300/month (Clearnox, Peliqan, AdminPulse).
- A one-off audit is most credibly priced against the firm's own billable rate: 10-25 hours of a EUR 60-100/h profile = EUR 600-2,500 per health check (ESTIMATE). The 120% deduction (if the deliverable is framed as e-invoicing consulting) softens this for small-company clients but not for the firm itself unless it is itself a "small company".

---

## 4. Bottom-up TAM / SAM / SOM

Inputs:
- Number of Belgian accounting firms: Evidence not found (Statbel be.STAT NACE 69.2 by size class exists but could not be opened: https://bestat.statbel.fgov.be/bestat/crosstable.xhtml?view=b71ca3b1-81b4-43bd-9f52-403a931fec57). Carried INFERENCE from batch 1: 5,000-7,000 firms. ITAA: >16,000 professionals — VERIFIED: https://www.itaa.be/en/itaa-institute-for-tax-advisors-and-accountants-welcome/. ITAA panel: ~3/4 of firms <=10 staff — VERIFIED: https://www.blogitaa.be/2025/11/05/ontdek-de-resultaten-van-de-jaarlijkse-barometer-van-het-beroep/.
- Size band (ESTIMATE): <=4 staff ~55-60%; 5-10 staff ~15-20%; 11-50 staff ~15-20%; >50 ~2-4%. Firms with 5-50 staff = ~30-40% of 5,000-7,000 = 1,500-2,800 firms (ESTIMATE, wide). Firms with 11-50 staff (the ones with hundreds of files and no IT person) = 750-1,400 (ESTIMATE).
- Client files per firm: ESTIMATE 150 (<=10 staff) to 400-1,500 (11-50 staff). Counterparties (customers + suppliers) per client file: ESTIMATE 30-200. A 20-staff firm therefore "owns" master data for roughly 500 files x ~80 counterparties = ~40,000 identifiers (ESTIMATE) — the scale argument for tooling.

| Layer | Belgium | Assumption | Value |
|---|---|---|---|
| TAM (all firms, health check + monitoring) | 5,000-7,000 firms x EUR 600-1,800/yr | INFERENCE x ESTIMATE (batch-1 anchor) | EUR 3-13M/yr |
| SAM (5-50-staff firms on API-accessible cloud stacks, mostly Flanders/Brussels) | 1,500-2,800 firms x ~60% cloud-stack x EUR 1,200-3,000/yr (audit amortised + EUR 75-200/month) | ESTIMATE | EUR 1.1-5.0M/yr |
| SOM (part-time solo founder, 3 years) | 20-60 firms x EUR 1,200-3,000/yr + 10-30 audits/yr x EUR 1,000-2,500 | ESTIMATE | EUR 35-250k/yr |
| 2028 reconciliation add-on | same SAM x EUR 50-100/month/firm from 2028 | ESTIMATE (batch 1) | +EUR 1-3M/yr ceiling, contested by ledger vendors |

Expansion arithmetic (no firm counts verified for FR/LU/DE in this batch): Luxembourg OEC register ~555 firms (single-source claim) — VERIFIED (weak): https://ilicompta.lu/guides/oec-luxembourg-ordre-experts-comptables. France experts-comptables firm count and Peppol-PA usage: Evidence not found. Germany: not searched (out of scope for this founder's language set). See section 9 for why FR/DE do not simply multiply the Belgian model.

Sanity check against comparables: OkiOki at EUR 8-11/seat and Peliqan at EUR 150/month suggest firm-level tools in Belgium clear EUR 1-2k/yr per firm, not EUR 5-10k. A EUR 100k/month business therefore needs ~600-1,000 Belgian firms or another country — i.e. more than the whole SAM. This is a EUR 1-3k/month side business or a EUR 10-20k/month small company in Belgium alone (ESTIMATE).

---

## 5. Competitive landscape

| Player | What they do today on portfolio/exception/master-data | Likelihood they add a portfolio-level exceptions view (HYPOTHESIS, 1-5) | Source |
|---|---|---|---|
| Billit (largest BE AP; 120k+ businesses, 2M+ invoices/month claim) | Free accountant portal linked to all client accounts; green Peppol badge per customer in the customer list; audit logs; per-invoice evidence files; OAuth API for partners after approval | 5 — already has the data and the accountant portal; adding a cross-dossier "failed deliveries" tab is trivial for them, but only for Billit-routed documents | https://www.billit.eu/nl-be/helpartikelen/klanten/klantenlijst-en-klantenfiche/peppol-status-in-de-klantenlijst/ ; https://docs.accesspoint.billit.eu/ ; https://vinkius.com/apps/billit-mcp |
| Peppol Box | EUR 5-7/month; "support for identifier issues"; publishes the clearest 0208/9925 problem content | 2 — SME-facing, not firm-facing | https://www.peppol-box.be/en/blog/peppol-belgium-problems-2026/ |
| Cashfeed (Ghent, EUR 1.3M, 350+ clients) | AI AP agent collecting invoices from Peppol/inboxes/portals; coding for accountants; Exact integration | 3 — AP-side, could add "missing/duplicate invoice" detection per client | https://tech.eu/2025/07/10/cashfeed-raises-1-3m-to-simplify-e-invoicing/ |
| Codabox / VOILA (Wolters Kluwer) | Registers the client on Peppol + Zoomit and delivers purchase invoices into any ledger; per-client-reference tiered fees; managed from MyCodabox per dossier | 4 — owns the firm relationship and the delivery pipe; a "VOILA health" view per firm is natural | https://faq.codabox.com/nl/support/solutions/articles/75000084108-voila-per-dossier-bestellen ; https://codabox.com/nl/aanbod/voila/ |
| Peliqan (Billit MCP + warehouse) | Syncs invoices, customers, Peppol participants, acknowledgements and webhooks into Postgres; "an AI agent can not only flag a rejected invoice but trigger a corrected resend"; EUR 150/month; Exact/Yuki/Silverfin/Odoo connectors; pan-EU Peppol MCP planned 2026-28 | 5 — this is the thesis' phase-2 product, already shipped for Billit and sold to Belgian practices | https://peliqan.io/blog/billit-claude-peppol/ ; https://peliqan.io/model-context-protocol/billit-mcp/ ; https://peliqan.io/blog/peppol-mcp-pan-eu/ |
| GoRoute.ai | Peppol/Mercurius API; "enforces proper identifier registration (0208) automatically"; 2028 five-corner content | 2 — developer API, not a firm product | https://goroute.ai/belgium.html |
| Banqup (Unifiedpost) | Multi-country SME e-invoicing + payments; 85k SMEs; blog "master data quality is now a compliance issue" | 3 — SME-facing; accountant channel exists | https://www.banqup.com/resources/blog/belgium-s-2026-e-invoicing-mandate-what-have-we-learned-so-far- |
| Yuki (Visma) | Domain-level overview of all UBL invoices; per-administration Peppol register/unregister from the accountant portal; configurable user notification when an invoice is received or "not successfully delivered"; activity log with the reason for "Not delivered" | 4 — the notification + domain overview is 80% of an exceptions view for Yuki dossiers | https://support.yuki.nl/nl/support/solutions/articles/80001023219-administratie-s-registreren-of-afmelden-bij-peppol-vanuit-portaal ; https://support.yuki.nl/en/support/solutions/articles/80000985587-activity-log-invoices ; https://www.yukisoftware.com/be-nl/road-to-success-bestemming-peppol-webinar-2-verwerking-aankoopfacturen-via-peppol-domeinniveau-portaalniveau/ |
| Exact Online | Peppol built in; App Center partner model (monthly fee per connected company); Purchase Agent AI | 3 — Exact ships per-company, firm-wide views live in its accountancy edition (not verified) | https://support.exactonline.com/community/s/article/All-All-DNO-Content-partnerprogram?language=nl_NL ; https://www.exact.com/benl/over-ons/artificial-intelligence |
| Octopus | Accountant edition, Peppol built in; API terms ENF | 3 | https://www.octopus.be/nl/voor-accountants/ |
| Odoo | Peppol in 58 countries; Peppol log per invoice; forum threads on delivery failures; Odoo 18 import bug | 3 — Odoo ships per-company; Odoo partners could build a firm view | https://www.odoo.com/forum/help-1/suppliers-cant-send-me-invoices-via-peppol-290584 ; https://github.com/odoo/odoo/issues/211405 |
| OkiOki (Xerius) | Accountant view of the Peppol registration status of all active clients with three badges (registration succeeded / network identification failed / identity verification failed) + manual verify | 4 — already a portfolio-level registration view; adding delivery failures is the next step | https://support.okioki.be/hc/nl-be/articles/20451640532626-Hoe-kan-ik-de-Peppol-registratie-status-opvolgen-van-mijn-actieve-klanten |
| B2Brouter via Combell | "Multiclient tool" for accountants with roles, templates, bulk processing and automatic validations | 3 | https://www.combell.com/nl/blog/peppol-voor-accountants/ |
| Liantis (social secretariat) | Accountants activate Peppol for clients under mandate via DigiLinks | 2 | https://support.liantis.be/hc/nl/articles/26084441950610-Hoe-activeer-ik-Peppol-voor-mijn-klanten-als-boekhouder |
| e-invoice.be | Free Peppol Radar bulk CSV check, free lookup API docs, free UBL viewer, "8 access points compared" content; sells its own AP | 4 — already gives away the health-check core as a lead magnet | https://e-invoice.be/peppol-radar ; https://docs.e-invoice.be/guides/lookup-participants ; https://e-invoice.be/peppol-invoice-viewer |
| Taxilla | Compliance middleware; Belgian rejection-avoidance guide | 1 — enterprise/mid-market | https://www.taxilla.com/avoiding-belgium-peppol-invoice-rejections-2026-common-pitfalls-compliance-middleware-guide |
| Recommand (recommand-peppol, AGPL-3.0) | Open-source Peppol API (send, inbox, documents, `/verify` recipient check), hosted tiers | 1 — infrastructure; useful building block for the founder | https://github.com/recommand/recommand-peppol (README fetched 2026-09-11) |
| Silverfin (Visma) | Assistant flags missing transactions/outliers in client files (batch 1) | 3 for the 2028 reconciliation layer | https://silverfin.com/product/silverfin-assistant/ |

Where the founder enters (INFERENCE): the only white space still visible is cross-vendor — a firm whose files sit on Yuki + Exact + Octopus + Billit + Codabox has five partial views and no consolidated one. Each vendor is unlikely to build the cross-vendor view (they have no incentive to show competitors' data), which is exactly Peliqan's positioning — and Peliqan already sells the warehouse and the MCP servers for EUR 150/month. The founder's realistic entry is therefore not "a product nobody has" but "the person who runs the check and fixes the list for firms that will not operate Peliqan/Peppol Radar themselves" — a service on top of commodity tooling.

---

## 6. Why now, why not incumbents, why firms buy

Why now (VERIFIED chain): mandate live 1 Jan 2026; Hermes gone 31 Dec 2025; tolerance ended 31 Mar 2026; 89% registered by Aug 2026 with 1.6M IDs for 946k companies (identifier duplication); e-reporting pre-draft approved 18 Jul 2026, law expected autumn 2026, Royal Decree with dataset/deadlines early 2027, go-live 1 Jan 2028; FR reception mandate 1 Sep 2026; LU draft law 17 Jul 2026 (2028-29); DE issuance 2027/28. Sources: https://www.vrt.be/vrtnws/nl/2026/08/03/peppol-stand-van-zaken-fod-financien-unizo/ ; https://www.theinvoicinghub.com/belgiums-e-reporting-pre-draft-law-approved/ ; https://www.comarch.com/trade-and-services/data-management/legal-regulation-changes/belgium-confirms-2026-peppol-e-invoicing-mandate-with-2028-near-real-time-reporting-to-follow/ ; https://www.urssaf.fr/accueil/actualites/facturation-electronique.html ; https://www.vatupdate.com/2026/09/01/luxembourg-expands-mandatory-domestic-b2b-e-invoicing-from-2028/.

Why incumbents have not built the cross-vendor view (INFERENCE): each vendor sees only its own pipe; the accountant portal is a retention feature, not a data-quality product; the network operators expect the identifier problem to self-heal; and the profession frames data-quality guidance as the accountant's own advisory job. Counter-evidence: OkiOki, Yuki and Billit already ship portfolio-level registration/delivery status inside their own perimeter, and Peliqan ships the cross-vendor warehouse. So the gap is narrower than batch 1 assumed.

Why a firm would buy (HYPOTHESIS, to test in interviews): (1) liability — engagement-letter guidance tells partners to document warnings and progress; an external audit report is documentation; (2) capacity — 56% of firms refuse clients and 9 in 10 cannot fill vacancies (universe T1; https://www.blogitaa.be/2026/07/01/accountant-blijft-een-knelpuntberoep-in-vlaanderen-wallonie-en-brussel/), so outsourcing a non-billable clean-up is rational; (3) 2028 — the ITAA tells firms to reassure clients "we monitor phase two for you"; a firm can resell a readiness check under its own name. Why a firm would not buy: the check is free (Peppol Radar), the fix is a phone call to the client, and the vendors' badges already show status.

---

## 7. Barrier-to-entry analysis

| Barrier | Assessment | Label | Notes / sources |
|---|---|---|---|
| Capital | Very low: < EUR 1k to start (sole proprietorship, VAT franchise, laptop, Peppol Directory free, KBO open data free); EUR 2-5k if a paid KBO webservice agreement or hosted MCP subscriptions are needed | VERIFIED (founder facts) + ESTIMATE | `_raw/belgium-founder-facts.md` ; https://kbopub.economie.fgov.be/kbo-open-data/login?lang=nl |
| Technical | Low-moderate. Deterministic checks (0208/9925 presence, scheme consistency, VAT validity, KBO status, duplicate endpoints, document-type support) are Python + REST/CSV work. Harder parts: Yuki is SOAP with session auth and daily call caps (1,000 base; 5,000/10,000 with paid "Webservice"/"Extended" features per domain); Exact needs OAuth per company plus App Center partnership for distribution; on-prem Walloon stacks (Horus, WinBooks, BOB50) have no easy API. OSS building blocks: recommand-peppol (AGPL, `/verify`), phoss-directory, Peliqan/Dytto/CodeMill/Tailormade MCP servers | VERIFIED | https://developer.yukisoftware.com/guides/guides-getting-started ; https://www.apideck.com/blog/how-to-integrate-with-the-yuki-api ; https://www.apideck.com/blog/guide-to-exact-online-api-integration ; https://github.com/recommand/recommand-peppol |
| API access terms | Yuki: API key generated by the firm's portal admin per domain; third-party apps need Visma Connect developer approval. Exact: free developer access; App Center listing = monthly fee per connected company negotiated with a partner manager (amount ENF); per-app-company rate limits. Billit: OAuth client via support, sandbox, production after approval. Octopus: ENF. Odoo: standard external RPC API (INFERENCE, not searched). Per-firm consent is therefore the practical model: the firm generates keys for its own domains and hands them to the founder under a DPA — no vendor partnership needed for a service, but needed for a listed product | VERIFIED / ENF as marked | https://support.yuki.nl/en/support/solutions/articles/80000786451-where-can-i-find-the-api-key-and-administration-id-in-yuki- ; https://support.exactonline.com/community/s/article/All-All-DNO-Content-partnerprogram?language=nl_NL ; https://docs.billit.be/docs/authentication |
| Regulatory: reserved profession | Law of 17 Mar 2019 reserves to ITAA members, when done for third parties: organising bookkeeping, drawing up annual accounts, keeping/centralising/closing books, "checking and correcting all bookkeeping documents", and creditworthiness analysis by bookkeeping technique; illegal practice is prosecutable (art. 117). Master-data/identifier validation and delivery-status monitoring are not bookkeeping and are delivered to the firm (which stays the accountant), so INFERENCE: not reserved — but "reviewing and correcting invoices in the ledger" for a client would be. Keep the deliverable at the identifier/transport layer and let the firm make ledger corrections | VERIFIED (law summary) + INFERENCE | https://etaamb.openjustice.be/nl/wet-van-17-maart-2019_n2019040805.html ; https://www.itaa.be/nl/instituut/meldpunten/illegale-uitoefening/ |
| Regulatory: Peppol certification | Not needed: only sending/receiving on the network requires a certified access point; reading ledger APIs and the public directory does not. If the founder ever resends/sends documents, use a certified AP (Billit/Recommand hosted) under the firm's account. Service providers face ISO 27001 by Jul 2027 — irrelevant unless the founder becomes one | INFERENCE from VERIFIED facts | https://www.n2f.com/blog/en/peppol-in-belgium-how-it-works-requirements-and-key-dates/ ; https://www.blogitaa.be/2026/05/29/e-reporting-vanaf-2028-6-punten-om-uw-kantoor-en-uw-clienten-voor-te-bereiden/ |
| GDPR / DPA | Invoice data contain personal data (sole traders, contact persons). The firm is controller or processor depending on the engagement; the founder is a processor under an art. 28 DPA (nine mandatory clauses; sub-processor list incl. any LLM API; EU hosting). ITAA published practical GDPR guidance for firms in May 2026 | VERIFIED | https://www.blogitaa.be/2026/05/28/gdpr-en-accountancy-in-de-praktijk-software-mailverkeer-en-klantdata-onder-controle/ ; https://www.legiscope.com/blog/verwerkersovereenkomst-art-28.html ; https://blog.be.accountants/nl/article/gdpr-1-in-welke-hoedanigheid-verwerk-ik-gegevens-van-mijn-clienten/4586 |
| Distribution | Moderate-high. Firms are reached via ITAA events, AccountancyVandaag (vendor-sponsored content), software-vendor partner directories, Liantis/Xerius accountant channels; none of these is open to an unknown solo provider without content or a referral. Dutch is needed for Flanders (where the cloud stacks are) | INFERENCE | https://accountancyvandaag.be/ ; https://www.blogitaa.be/ |
| Sales cycle | ESTIMATE 2-8 weeks for a one-off audit at a 5-50-staff firm (partner decides), 3-6 months for a recurring subscription (needs DPA, API keys per domain, IT/security questions). No evidence found either way | ESTIMATE | — |
| Operational | The service is labour: exporting counterparties from 3-5 systems, running checks, writing a fix list, walking the firm through it. 10-15 h/week supports ~1-2 audits/month (ESTIMATE). Monitoring adds on-call-like support when APIs break (Yuki SOAP changes, Exact token expiry) | ESTIMATE | — |
| Data | No proprietary data: the Peppol Directory is public and downloadable; KBO open data is free; rejection reasons live in each vendor. A cross-firm benchmark ("your rejection rate vs peers") could become modest proprietary data after 20+ firms | INFERENCE | https://openpeppol.atlassian.net/wiki/spaces/Belgium/pages/2804154401/Who+receives+Peppol+invoices+Is+there+a+list |
| Partnership | Exact App Center and Visma Connect approvals gate a listed product; Codabox/Billit have no public partner programme for third-party "quality" tools (ENF). Realistic partners: Peliqan (white-label their warehouse), Let's Peppol/Recommand (OSS APs), regional accountant networks | ENF / INFERENCE | https://www.exact.com/benl/app-store/developer |
| Trust | High barrier for a solo, part-time, non-ITAA provider asking for API keys to hundreds of client files; mitigated by read-only keys, DPA, EU hosting, ITAA-adjacent visibility | INFERENCE | — |
| Network effects | None in the product. Weak data-network effect only if a benchmark emerges | INFERENCE | — |

Overall classification: LOW barriers to entry (capital, technical, regulatory all low) combined with LOW barriers to imitation. For the founder this is a GOOD barrier to get in and a BAD barrier to stay in: any access point or ledger vendor can ship the in-perimeter view (several already have), and Peliqan already sells the cross-vendor plumbing. Defensibility, if any, must come from service execution, firm relationships, and the 2028 reconciliation logic — not from the tooling.

---

## 8. Belgium analysis

- Advantage: Belgium is the first big-bang B2B Peppol mandate with a 2028 five-corner e-reporting law queued behind it — a live laboratory whose lessons travel to LU (Peppol four-corner, 2028-29), NL (Peppol-based roadmap 2030-32), DE and FR. VERIFIED: https://www.blogitaa.be/2026/07/07/belgie-als-europese-koploper-de-lessen-na-zes-maanden-verplichte-e-facturatie/ ; https://rtcsuite.com/netherlands-roadmap-for-vida-toward-a-peppol-based-domestic-b2b-e-invoicing-regime-by-july-2030/.
- Advantage: firms are the distribution channel for every SME finance tool (Chift), and the profession is publicly asking for vendor-independent tooling (ITAA Jul/Aug 2026).
- Neutral: Brussels location gives access to both language communities but Brussels/Wallonia adoption lags Flanders (<=65% vs >=75% in Jan 2026) and the Walloon stack is on-prem/integrator-managed — the API-driven product is easiest to sell in Flanders, in Dutch. Flag: working Dutch is material for the monitoring phase; French is enough for a Brussels/Walloon service phase with manual exports. VERIFIED: https://datanews.knack.be/analyse/achtergrond/grote-regionale-verschillen-in-de-belgische-adoptie-van-peppol/ ; https://www.chift.eu/blog/the-accounting-software-landscape-in-belgium-a-2026-guide.
- Disadvantage: small market (5-7k firms, INFERENCE), low price anchors (EUR 0-10/SME/month), concentrated vendor landscape (Visma: Yuki/Silverfin/Adsolut; WK: ClearFacts/Codabox/Basecone; KKR: Exact) where each vendor can bundle the feature.
- Subsidies (from founder-facts file): Flanders KMO-portefeuille consulting now limited to "digitalization - cybersecurity" (since 1 Feb 2026) — a Peppol data-quality audit probably does not qualify as consulting but training remains open (ENF whether "Peppol data-quality training" is accepted); Wallonia chèques-entreprises digital-maturity voucher covers 50% of consulting; Brussels consultancy subsidy suspended from 12 Aug 2026. The founder would need to register as a provider (effort ENF). Sources in `_raw/belgium-founder-facts.md`.
- Founder status: side business as complementary self-employed under the VAT franchise (<EUR 25k) is cheap (< EUR 300) and legal; check employment contract for side-activity clauses (founder-facts file).

---

## 9. EU expansion: what changes per country

| Country | Status (VERIFIED) | What changes for the thesis | Source |
|---|---|---|---|
| France | Reception mandatory for all companies 1 Sep 2026; issuance for SMEs/micro 1 Sep 2027 (large/mid 1 Sep 2026-27); 101 Plateformes Agréées listed 16 Jan 2026; formats Factur-X/UBL/CII; DGFiP is Peppol Authority France since 8 Jul 2025 | Different architecture: PA-to-PA with a central directory (annuaire) and e-reporting from day one; identifiers are SIREN/SIRET, not Peppol 0208/9925; experts-comptables choose PAs (compta-online guides). The Belgian identifier-hygiene playbook does not transfer; a "PA-readiness / annuaire hygiene" analogue would need rebuilding. Founder's French helps, but the firm base and PA ecosystem are unknown to him | https://www.urssaf.fr/accueil/actualites/facturation-electronique.html ; https://www.cegid.com/fr/facture-electronique-obligatoire/calendrier-facture-electronique/ ; https://www.compta-online.com/facturation-electronique-plateforme-agreee-ao8120 ; https://village-connecte.fr/la-dgfip-aux-commandes-de-peppol-france-ce-quil-faut-savoir/ |
| Luxembourg | Draft law approved 17 Jul 2026: receipt mandatory 1 Jan 2028; issuance large/medium 1 Jul 2028; all others 1 Jan 2029; Peppol four-corner, EN 16931 UBL/CII; not yet enacted | Closest analogue to Belgium (Peppol, same identifier logic, French-speaking fiduciaires, ~555 OEC firms). Timing: 2028-29 = exactly when Belgian phase-1 pain fades. Natural second market for the health check | https://www.vatupdate.com/2026/08/31/luxembourg-proposes-phased-mandatory-domestic-b2b-e-invoicing-from-2028-to-2029/ ; https://rtcsuite.com/luxembourg-formalises-mandatory-b2b-e-invoicing-over-a-peppol-four-corner-network/ ; https://ilicompta.lu/guides/oec-luxembourg-ordre-experts-comptables |
| Germany | Receive since 1 Jan 2025; issue mandatory for >EUR 800k turnover from 1 Jan 2027, all from 1 Jan 2028; XRechnung/ZUGFeRD; no network mandate (e-mail delivery allowed); e-reporting later | No Peppol directory dependency, no fixed identifier scheme, German language, Steuerberater regulated (StBerG). Not a copy-paste market | https://www.cleartax.com/de/en/e-invoicing-timeline-in-germany ; https://www.vatupdate.com/2026/07/01/germany-e-invoicing-b2b-mandate-timeline-and-compliance/ |
| Netherlands | No domestic B2B mandate; ViDA cross-border 1 Jul 2030; government report (10 Mar 2026) recommends Peppol-based domestic model 2030-32; draft consultation Q4 2026 | Same software vendors (Yuki, Exact) and Peppol; but no urgency until ~2030. Useful only as a vendor/partner market | https://kpmg.com/us/en/taxnewsflash/news/2026/05/tnf-netherlands-proposed-e-invoicing-and-digital-reporting-framework-under-vida.html ; https://rtcsuite.com/netherlands-roadmap-for-vida-toward-a-peppol-based-domestic-b2b-e-invoicing-regime-by-july-2030/ |

INFERENCE: only Luxembourg is a genuine extension of the Belgian product; France requires a re-platform; Germany and NL are off-thesis for this founder. "FR/LU/DE expansion" in the TAM should be read as "LU in 2028, maybe".

---

## 10. AI architecture (service phase and product phase) and build effort

### 10.1 Principle
Split strictly: deterministic validation (must be exact, auditable, cheap) vs LLM tasks (classification of free-text reasons, drafting communications, summarising). Never let an LLM decide whether an identifier is valid.

### 10.2 Service phase (months 0-6): "scripts + spreadsheets"
- Inputs: CSV exports of customers/suppliers per client file (from Yuki/Exact/Octopus/Billit/Odoo exports; on-prem stacks via the firm's own export), the firm's client list, and rejection/undelivered logs exported per vendor.
- Deterministic engine (Python; pandas): normalise identifiers (BE0123.456.789 -> 0123456789), check KBO status (open-data flat file, daily), VAT validity (VIES, throttled/async, or reseller), Peppol Directory presence per scheme (0208 / 9925), document types supported (BIS Billing 3.0 invoice/credit note), duplicate endpoints, mismatched names, inactive KBO entities still invoiced, counterparties under the VAT franchise (out of issuing scope), foreign counterparties (0208 not applicable).
- LLM tasks (optional in phase 1): map heterogeneous rejection texts from different vendors to a fixed taxonomy (recipient-not-registered / scheme-mismatch / schematron-validation / VAT-logic / duplicate / transport-timeout); draft the per-client fix e-mail in NL/FR; write the executive summary of the audit. Human-in-the-loop: the founder reviews every fix list; the firm's staff make ledger changes (reserved-activity boundary, section 7).
- Deliverable: Excel/PDF "Peppol portfolio health report" + fix list per client + a 1-page management summary; optional re-run after 30 days.

### 10.3 Product phase (months 6-18): monitoring agent
- Connectors (per firm, per-domain keys under DPA): Billit OAuth (documents + acknowledgements/webhooks), Yuki SOAP (sales invoices with "Not delivered" status + notes, purchase UBL log), Exact Online OAuth (per company; App Center listing later), Odoo RPC (account.move Peppol state/log), Octopus (ENF — may remain export-based). Alternative: license Peliqan's warehouse/MCP servers instead of writing connectors (EUR 150/month; INFERENCE that white-labelling is negotiable).
- Data model: firm -> client_file -> {counterparty (kbo_no, vat_no, peppol_ids[scheme], directory_doc_types, kbo_status, last_checked), document_event (vendor, doc_id, direction, status, reason_raw, reason_class, ts), exception (type, severity, owner, state, resolved_ts)}.
- Scheduling: nightly directory delta (download full list; no per-query rate-limit issue), nightly vendor pulls within call caps (Yuki 1,000/day base per domain — INFERENCE: sufficient for status polling of a few hundred documents), weekly digest per firm, real-time only for Billit webhooks.
- Agent layer: an MCP-style tool set (lookup_directory, check_kbo, list_undelivered, classify_reason, draft_client_message) callable from Claude/ChatGPT for the firm's staff; guardrails: read-only by default, write-back (resend/correct) only via the firm's own vendor UI or a certified AP.
- Human-in-the-loop: exceptions land in a queue with a suggested fix; staff approve; monthly report doubles as liability documentation.

### 10.4 2028 reconciliation engine (build 2027 after the Royal Decree)
- Inputs: what the ledger booked per period vs what was reported to FPS Finance (via the firm's/clients' reporting software; access path unknown until the RD and vendor APIs exist — ENF). Logic: match on invoice number + counterparty + date + amounts; flag reported-not-booked, booked-not-reported, amount/VAT-code mismatches, late reports beyond the deadline. Same data model, new event source. Analogue products exist in Italy (SIAC FTEL ADRI, TeamSystem) and Spain (Avalara SII reconciliation) — batch 1.

### 10.5 Build effort for this founder (ESTIMATE)
- Service phase scripts: 60-120 hours (identifier normalisation, directory/KBO/VIES checks, report template) — feasible in 2-3 months at 10-15 h/week with Claude Code assistance.
- One connector (Billit, REST) : 30-60 h; Yuki SOAP: 60-120 h; Exact OAuth multi-company: 60-100 h; Odoo: 30-50 h. Monitoring MVP on two vendors: 200-350 h = 5-8 months part-time. Ongoing maintenance: 10-20 h/month.
- Reconciliation engine: cannot be scoped before the 2027 Royal Decree; 150-300 h once specs exist.
- Honest capacity check: service phase yes; two-connector product yes but slow; five-connector product plus support is beyond 10-15 h/week without a co-founder or Peliqan-style outsourcing.

---

## 11. AI leverage, commoditisation, AGI and ASI tests

- AI leverage (for the founder): MODERATE. AI coding assistants cut build time materially (the whole service phase is glue code); LLMs add value in reason-classification across vendors, multilingual client communication, and report writing. But the core value — "is this counterparty correctly registered and did this document arrive" — is deterministic lookup and rules. Classification: mostly deterministic software with a thin AI layer. Honest answer to the brief's question: yes, the AI angle is thin.
- AI commoditisation test: FAILS (high risk). Hosted MCP servers for Billit/Exact/Yuki/Silverfin/Peppol already exist (Peliqan, Apideck, CData, Dytto, Tailormade); a firm's staff can already ask Claude "list my undelivered Peppol invoices across Billit" for EUR 150/month; ledger vendors ship their own agents (Exact Purchase Agent, Silverfin Assistant, Odoo 19). Anything the founder builds as a generic "agent over ledger APIs" is commoditised within 12 months. What survives commoditisation: domain rules (Belgian identifier/VAT/KBO logic), the firm relationship, and the 2028 reconciliation rule set.
- AGI test: if broadly capable agents can be given a firm's API keys and told "keep my portfolio Peppol-clean", the product disappears; the residual is the accountable human who signs the fix list and holds the DPA — a service, priced like a service. Classification: product NOT AGI-robust; service weakly robust for a few years.
- ASI test: irrelevant/erased — nothing here is a durable moat under superintelligence; the regulatory layer itself would be automated end-to-end by the tax authority and vendors.
- Net: OPP-B is an "AI-native services" play (AI reduces the founder's cost of delivery) rather than an "AI product" play. It should be judged on service unit economics, not on AI defensibility.

---

## 12. Business model and unit economics

### 12.1 Pricing options (ESTIMATE unless stated)
- One-off "Peppol portfolio health check": EUR 900-2,500 per firm depending on files (e.g. EUR 900 up to 150 files, EUR 1,800 up to 500, EUR 2,500 up to 1,500), 15-30 hours of founder time -> EUR 60-100/h effective. Re-run/"post-fix verification" EUR 300-500.
- Monitoring subscription: EUR 75-250/month per firm (tiered by files), not per SME (per-SME anchor EUR 0-10 kills it). Anchors: Peliqan EUR 150, Clearnox EUR 100, AdminPulse EUR 290 (VERIFIED).
- Per-file pricing (Codabox/AdminPulse style, EUR 0.50-1.00/file/month) is understood by firms but yields only EUR 75-500/month for a 150-500-file firm — same band, more complex billing.
- 2028 readiness audit (2027): EUR 1,500-3,000 per firm; reconciliation module from 2028: +EUR 50-100/month/firm (batch-1 estimate).

### 12.2 Paths
- EUR 1k/month: 1 health check per month, or 8-10 firms at EUR 100-125/month. Reachable in 6-9 months of part-time effort if 2-3 firms convert from the founder's network (HYPOTHESIS).
- EUR 10k/month: ~50-70 monitored firms at EUR 150 + 1-2 audits/month; requires 2 connectors stable, a DPA template, and a Dutch-language funnel; ~2-3 years part-time or 12-18 months full-time (ESTIMATE). This is roughly the Belgian SOM ceiling for a solo operator.
- EUR 100k/month: 500+ firms at EUR 200 — exceeds the Belgian 5-50-staff SAM; needs LU/FR expansion, vendor OEM (Codabox/Exact/Visma bundling the module) or a pivot to the 2028 reconciliation engine sold through a ledger vendor. Not credible as an independent Belgian firm-by-firm business.

### 12.3 Four capital scenarios
| Scenario | Capital | What it buys | Outcome band (ESTIMATE) |
|---|---|---|---|
| A. Zero-capital side business | < EUR 1k | Scripts, spreadsheets, 1-2 audits/month, no product | EUR 0.5-3k/month; useful as a learning/credibility vehicle; exits into a job offer or a Peliqan/Codabox partnership |
| B. Own savings | EUR 10-25k | Hosted MCP/warehouse subscription, freelance Dutch content/sales help, DPA/legal, two connectors | EUR 3-10k/month by year 2-3; still founder-labour-bound |
| C. Angel / regional (VLAIO, finance&invest.brussels) | EUR 100-250k | Full-time founder + 1 developer, 4-5 connectors, ITAA/AccountancyVandaag presence, LU launch 2028 | EUR 10-30k/month possible; competes head-on with Peliqan/OkiOki/vendor features; exit = acquihire by a ledger/AP vendor |
| D. VC | EUR 1M+ | Not fundable on this thesis: TAM EUR 3-13M, feature-sized, no AI moat; investors already funded the adjacent layers (Cashfeed EUR 1.3M, Dytto EUR 1.5M, Ravical EUR 7.3M, Chift EUR 2.3M — VERIFIED, batch 1) | Do not pursue |

---

## 13. Customer acquisition

- First firm: the founder's own network (his employer's accountant; Brussels firms serving foreign-group subsidiaries where his controlling background is a credential). Offer: free 20-file pilot check in exchange for a case study and a reference. Deliver the report in French or Dutch as the firm prefers.
- Firms 2-10: (a) publish a free, open-source "Peppol portfolio checker" (CSV in, report out) and a monthly "state of Belgian Peppol data quality" note; (b) pitch a guest article to AccountancyVandaag / a talk at an ITAA regional event (both vendor-friendly channels; no evidence of pay-to-play but sponsorship is common — ENF); (c) approach 2-3 Odoo/Exact integrators in Brussels/Wallonia to subcontract clean-ups; (d) offer the audit as a subsidised deliverable where a voucher applies (Wallonia chèques-entreprises; Flanders only if it passes the digitalisation-cybersecurity or training filter — founder-facts file).
- Scaling: partner rather than compete — Codabox (VOILA health), Billit (accountant portal add-on), Peliqan (white-label). Evidence of open partner programmes for such tools: ENF; Billit and Exact have developer/App Center tracks (section 7).
- Objections expected (HYPOTHESIS): "our software already shows this" (true within each vendor); "Peppol Radar is free"; "we don't give API keys to freelancers"; "our clients' data quality is the client's problem"; "we'll wait for the 2027 Royal Decree". Price sensitivity: high per SME, moderate per firm if framed as hours saved and liability documentation.
- Dutch: essential for Flanders where the cloud stack and the higher adoption sit; French sufficient for Brussels/Wallonia service work.

---

## 14. MVP

- Manual first (weeks 1-8): one firm, CSV exports, Python scripts, Excel report, fix list, a 1-hour walkthrough. Measure: hours spent, exceptions found per 100 counterparties, share the firm actually fixes in 30 days, and what the partner says it was worth.
- Automate next (weeks 8-20): identifier normalisation + directory/KBO checks as a reusable CLI; reason taxonomy; NL/FR e-mail templates; a re-run diff ("what changed since last check").
- Do NOT build: an access point; a multi-tenant SaaS UI; Yuki/Exact connectors before 3 paying firms ask for monitoring; Horus/WinBooks/BOB connectors; anything on 2028 reconciliation before the Royal Decree (early 2027); a per-SME product.

---

## 15. Trajectory (service -> product -> platform) and timing risk

- Year 1 (2026-27): 5-15 audits, 3-8 monitoring firms, EUR 1-3k/month; the founder's Dutch and Belgian-firm network are the real deliverables.
- Year 2 (2027-28): 2028-readiness audits as the flagship (the ITAA itself tells firms to prepare and to message clients); monitoring on 2 connectors; EUR 3-8k/month; build the reconciliation logic once the RD fixes the dataset.
- Year 3 (2028-29): reconciliation module live from Q1 2028 in Belgium; Luxembourg receipt mandate 1 Jan 2028 opens a second market for the identifier check; EUR 8-15k/month if the founder is full-time by then (ESTIMATE).
- Year 5: either (a) a 2-4-person Belgian/Lux compliance-ops boutique (EUR 0.5-1M revenue, service-heavy), or (b) module acquired/bundled by a ledger/AP vendor, or (c) wound down as vendors absorb the features.
- Timing risk — the 2028 gap: phase-1 pain (identifier duplicates, wrong channel) is expected by network operators to decline through 2026-27; fines are not visibly enforced; the reconciliation problem does not physically exist until 1 Jan 2028 and its spec arrives only in early 2027. Revenue from mid-2027 to early 2028 depends on selling "readiness" before anything breaks — a consulting sale, not a monitoring sale.
- Escape from founder labour: only via (i) productised monitoring at EUR 150-250/month across 50+ firms, or (ii) OEM to a vendor. Path (i) collides with Peliqan/OkiOki/Yuki features; path (ii) is plausible but is an exit, not a company.

---

## 16. Main risks and reasons NOT to pursue; evidence that would change the recommendation

Reasons not to pursue (ranked):
1. The health-check core is already free: Peppol Radar (CSV bulk check, no account), peppolcheck.be, Peppol Practical BE check, Nymus lookup, Finplex checker. VERIFIED (section 2.5).
2. Portfolio-level status views already exist inside the vendors firms use: OkiOki three-badge registration status per active client; Billit green badges + audit logs + accountant portal; Yuki domain overview + "not delivered" notifications + activity log. VERIFIED (section 5).
3. The cross-vendor "agent flags a rejected invoice and triggers a resend" is already Peliqan's shipped Billit MCP pitch at EUR 150/month, with more connectors and pan-EU Peppol MCP planned. VERIFIED (section 5).
4. The problem is expected to shrink: ~1% problematic exchanges post-launch with registration quality improving; 89% registered and near the natural ceiling. VERIFIED (sections 1-2).
5. No evidence of enforcement (fines issued, controls) since April 2026 — the urgency lever is weak. ENF (section 2.3).
6. Practitioner pain as articulated is about client hand-holding, workload and payment follow-up more than rejection triage. VERIFIED (section 2.1).
7. Low price anchors (EUR 0-10/SME/month; EUR 100-300/firm/month) cap the business at a side-income or small-boutique scale in Belgium. VERIFIED anchors, ESTIMATE conclusion.
8. Language/stack mismatch: the API-friendly, high-adoption market is Flemish; the founder's French fits the on-prem, lower-adoption market. VERIFIED facts, INFERENCE conclusion.
9. Reserved-activity boundary: "checking and correcting bookkeeping documents" is ITAA-reserved; the service must stay at the identifier/transport layer. VERIFIED law summary.
10. Part-time capacity vs multi-vendor API maintenance. ESTIMATE.

What would flip the recommendation toward "pursue":
- 10 practitioner interviews where 5-50-staff firms quantify >8-10 staff hours/month on Peppol exceptions and at least 3 say they would pay EUR 1,000+ for a documented clean-up.
- Access-point data showing sustained (>2-3%) failure rates into H2 2026 rather than decline.
- Visible enforcement (FPS Finance fine statistics or named cases) creating a documentation-driven demand.
- The 2027 Royal Decree placing a reconciliation/verification duty on the buyer side that ledger vendors do not cover.
- A vendor (Codabox, Billit, Peliqan) agreeing to distribute or white-label the module — converts a weak standalone into a channel product.

Recommendation (analyst view): OPP-B does not stand as a standalone product business; it is viable only as a low-capital service wedge that earns Belgian-firm relationships, Dutch-market access and 2028 domain knowledge, with the explicit plan to either OEM the monitoring module or pivot to the reconciliation layer in 2027-28. Treat U-004 (reconciliation) as the real thesis and OPP-B phase 1 as its funded customer-discovery programme.

---

## 17. Open questions for direct interviews

For partners/office managers of 5-50-staff firms (aim: 10 interviews, mixed NL/FR):
1. How many client files, and on which software stacks (Yuki/Exact/Octopus/Billit/Codabox/Odoo/Horus/WinBooks)? Who inside the firm manages Peppol registrations and support?
2. In a typical month since April 2026, how many "invoice not received / rejected / duplicate" cases reach the firm? Who handles them and how long does each take? Does anyone log them?
3. Have you ever run a portfolio-wide check of client/supplier identifiers (Peppol Radar, peppolcheck, your vendor's badges)? What did you do with the result?
4. Which vendor views do you actually use for status (Billit badges, Yuki notifications, OkiOki badges, Codabox MyCodabox)? What is missing across them?
5. Have any of your clients received a fine or a control letter for e-invoicing? Have you seen any enforcement at all?
6. What did you charge clients for Peppol onboarding in 2025-26 (flat fee, hours, nothing)? Would you resell a "data-quality report" under your own name?
7. What would you pay for a one-off documented clean-up (EUR 500 / 1,000 / 2,500)? For monitoring per month (EUR 50 / 150 / 300)? Per file or per firm?
8. Would you hand read-only API keys for client domains to an external provider under a DPA? What security questions would you ask? Would ITAA membership of the provider matter?
9. How are you preparing for 2028 e-reporting today? Have you sent the client mailing ITAA suggested? Which of your clients have POS/GKS or multiple invoicing systems?
10. Who do you expect to solve "reported vs booked" in 2028: your ledger vendor, Codabox, Silverfin, or someone else?
11. Do you use the KMO-portefeuille / chèques-entreprises for external consulting? Would a data-quality audit fit?
12. If Yuki/Exact/Billit shipped a cross-dossier exceptions view tomorrow, would you still want an external check? Why?

For access points / vendors (Billit, Codabox, Peliqan, OkiOki):
13. What share of documents fail delivery or are rejected today, and how has it trended since Q1 2026?
14. Do you expose failed-delivery events per accountant portfolio via API/webhook? Any partner programme for third-party quality tools?
15. When do you plan to support Peppol Invoice Response / MLS, and will Belgian software vendors adopt it?

---

### Query log (this batch, ~60 WebSearch queries)
NL: blogitaa Peppol problemen; accountancyvandaag Peppol ervaringen; Peppol statistieken BOSA 2026; Peppol boete opgelegd; Codabox VOILA prijs; fdmagazine Peppol; Billit tarieven boekhouder; Statbel NACE 69.20; Yuki API voorwaarden; ITAA voorbehouden activiteiten; ITAA zes maanden lessen; VRT Unizo augustus; datanews regionale verschillen; Peppol onboarding kost integrator; uurtarief boekhouder; ITAA barometer kantoren grootte; "Het moeilijkste aan Peppol"; peppolcheck bulk; Yuki domeinniveau afgewezen; ITAA digitale afhankelijkheid; percentage e-facturen fouten Clearfacts; eerste boetes; ITAA e-reporting 6 punten; Hermes fallback; Liantis boekhouder Peppol activeren; aantal accountantskantoren; Peppol begeleiding forfait; Codabox 5,99; Peppol monitoring dashboard kantoor; OkiOki registratie status; ITAA verwerkersovereenkomst; Exact App Center partner kosten. FR: amendes Peppol SPF Finances; e-reporting 2028 loi juillet 2026; France PA septembre 2026; fiduciaire outil suivi Peppol; Luxembourg fiduciaires OEC. EN: Peppol directory API rate limit; KBO open data API; Invoice Response/MLS adoption; Trends BI 1.6M IDs; Chift landscape; Codabox pricing FAQ; MLS Belgium mandatory; Germany/Luxembourg status; Netherlands mandate status; VIES limits; Peliqan Peppol MCP; Billit API partner; Odoo Peppol errors; e-reporting 2028 data fields; rejection rate statistics; Digiteal/Banqup invoice response; peppol-box problems 2026. GitHub: recommand/recommand-peppol README (fetched).
