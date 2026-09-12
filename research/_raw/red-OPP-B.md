# RED TEAM — OPP-B: Peppol portfolio operations for Belgian accounting firms

Date: 2026-09-12. Method: WebSearch only (WebFetch/curl blocked). Labels: VERIFIED (search-summary) / ESTIMATE / INFERENCE / HYPOTHESIS / Evidence not found. All URLs as surfaced by search results; not fetched in full.

Founder constraints: Brussels, full-time controller, 10-15 h/week, limited capital, learning Python/agents, not ITAA-registered, EN + working FR, NL unknown.

## 1. Queries run (appended as executed)

Q01 NL: Peppol België afgewezen facturen percentage 2026 fouten daling PSP forum -> no rejection stats; klippa/topafisc/flpnv generic; note: Peppol invoices paid median 14 days vs 10 non-Peppol (Dec 2025, klippa summary).
Q02 NL: FOD Financiën stand van zaken september 2026 controles boetes opgelegd -> only "sanctions apply since 1 Apr"; no count of fines/controls (peppol.nu, practicali, certifisc, xerius).
Q03 EN: Billit rejected invoices dashboard / invoice response -> Billit help: IMR sent automatically after approval in Fast Input; MLR visible; Peppol status in customer/supplier list. No cross-dossier rejected view found.
Q04 NL: Yuki "niet afgeleverd" overzicht portaal -> notification per user on not-delivered; reason in activity log Notes; portal Peppol column. Nothing new beyond deep-dive.
Q05 NL: ITAA voorbehouden activiteiten niet-lid -> ITAA: non-members may not perform reserved activities even as subcontractors of ITAA members; "checking and correcting all accounting documents" is reserved (itaa.be illegale uitoefening; toelichtende nota).
Q06 NL: Exact Online App Center partner fee -> only generic dev registration pages; partner fee per company not surfaced.
Q07 FR: cabinet comptable "audit Peppol"/"check-up Peppol" payant -> only vendor pages; "free Peppol audit" offered by an Odoo integrator (agile-minds.be) as lead magnet; no paid firm audit found.
Q08 NL: accountantskantoor "Peppol-audit/-scan/-check" prijs -> Yuki/AccountancyVandaag checklist content; "Peppol-check" pricing EUR 4-15/month refers to SME AP subscriptions, not firm audits; only 15% of SMEs got e-invoicing info from their accountant (Yuki trend page).
Q09 NL: Codabox tarieven -> CODA from EUR 7.53/month/subscription (SME), EUR 24 setup per mandate; SODA <EUR 71/month per environment; VOILA per business number, tiered; per-file VOILA price not surfaced (faq.codabox.com 75000118467).
Q10 NL: Bizzcontrol/AdminPulse prijs -> AdminPulse fixed price per user (calculator, figure not surfaced); Bizzcontrol on request.
Q11 EN: Belgium e-reporting royal decree -> Council of Ministers approved pre-draft law 18 Jul 2026; publication expected autumn 2026; dataset by Royal Decree early 2027; entry 1 Jan 2028 (Deloitte, vatupdate 22 Jul 2026, theinvoicinghub).
Q12 EN: Luxembourg mandate -> receive by 1 Jan 2028; issue: large/medium from 1 Jul 2028, all by 1 Jan 2029; Peppol 4-corner (marosavat, vatupdate 23 Jul 2026, banqup).
Q13 EN: rejection rate H1 2026 statistics -> none; FPS FAQ update May 2026 on rejection/reverse charge/Peppol delays (vatupdate 18 May 2026) — follow up.
Q14 NL: Octopus API -> "100% free API", light rate limits, docs via manual, webservice@octopus.be; no partner fee.
Q15 EN: FPS FAQ May 2026 rejection -> wrong-recipient invoice must still be booked in VAT return + corrective credit note referencing Peppol invoice ID; recipient must reject electronically with response code "RE"; delivery >1 business day: the SOFTWARE SUPPLIER must investigate the cause (vatupdate 18/22 May 2026; vatcalc).
Q16 EN: Peliqan pricing -> platform EUR 150/month annual (EUR 1,800/yr) or ~EUR 199/month; Billit MCP from EUR 75/month; Yuki MCP, Exact MCP, Silverfin MCP blog posts; EU-hosted BE, SOC2 Type II (peliqan.io blog pages).
Q17 NL: Yuki API -> integrations via Visma Connect Developer Portal, scopes, Yuki must approve; domain call quota: Webservice 1,000-5,000/day, Extended 5,000-10,000/day as paid accountant features (support.yuki.nl 80000787670; developer.yukisoftware.com).
Q18 EN: Billit API -> OAuth credentials via support; production integration submitted for approval; multi-tenant = commercial integration requiring OAuth; accountant context via ContextCompanyID+PartyID headers (docs.billit.be).
Q19 FR: France gestion des rejets cabinet -> village-justice (expert-comptable, 2026): transition mandates billable EUR 500-2,000 per client (diagnostic, platform choice, config, training); firms must keep evidence of incidents/rejections; no dedicated "rejection desk" product found.
Q20 PL: KSeF odrzucone monitoring -> MF requires monitoring, downloading UPO, resending; firms implement extra control procedures; management reports on rejected invoices; software vendors (wfirma, kluczesoft) bundle it; no third-party paid desk found.
Q21 IT: SDI scarti monitoraggio -> rejection monitoring bundled in invoicing software (CGN email alerts; CloudFinance from EUR 3/month; NTS Digital Hub scarto signalling; Comply platform). Bundled, not standalone.
Q22 NL: boekhouder uren per maand Peppol fouten -> no quantified hours; Teamleader: ~750k invoices Nov-Dec 2025, ~25% via Peppol, Peppol invoices paid slower (median 14 vs 10 days); made-in.be small self-employed "costs me only money and time".
Q23 EN: Peppol Directory terms -> free, open source, full export in several formats; operated jointly by OpenPeppol + service providers; no acceptable-use/commercial restriction surfaced (directory.peppol.eu export-all; peppol.org).
Q24 NL: KBO open data licence -> free open licence, commercial and non-commercial reuse allowed with source citation; no direct-marketing use of personal data; KB 18/07/2008 commercial reuse (economie.fgov.be Licentie-KBO-Open-Data-gebruiksvoorwaarden.pdf; starteralert.be).
Q25 EN: PSP forum registration quality -> KEY: Belgian Peppol Authority + FPS Finance + Operations Office deployed a "Belgian Peppol Network Data Scanner (MVP)"; error rate dropped from 2.41% to 0.31% across 7 runs Dec 2025-Apr 2026; error classes: no 0208 registration, incorrect 0208, incorrect 9925, missing BIS Billing receiving capability (openpeppol.atlassian.net 40th plenary minutes 5265883137; 37th plenary 4611047434).
Q26 NL: Exact Online accountancy Peppol overzicht -> "configuratiemonitor" to configure e-invoicing for all administrations; no cross-admin failed-delivery view surfaced (exact.com benl blog; accountancyvandaag).
Q27 EN: Silverfin/Exact/WK 2028 reconciliation -> nothing announced; Silverfin normalises TB/reconciliation layer (Peliqan blog). Evidence not found.
Q28 FR: Wallonia/Brussels fiduciaire software -> Horus, Sage BOB, Odoo, WinBooks dominant; Horus/Odoo cloud-native, BOB/WinBooks hosted options; Sage Cloud Demat AP; WinBooks native Peppol (polynome.be guide 2026; ibgraf).
Q29 NL: ITAA e-reporting responsibility -> "e-report does not reflect your accounting and is separate from it"; processing/return/advice remain the professional's responsibility; ITAA lobbies for minimal dataset (blogitaa 29 May 2026).
Q30 DE: Steuerberater E-Rechnung Ablehnung service -> only generic rollout guidance (segment clients by error risk); no paid rejection-monitoring service found.
Q31 EN: BPA data scanner confirm -> 40th plenary minutes: scanner error rate 2.41% -> 0.31% over 7 runs Dec 2025-Apr 2026; records scanned 1.2M -> 2.06M; non-listing in Directory = warning; plenary endorsed globalising the scanner (RFC Peppol-20448), Belgian pilot kept until Plenary 41 (openpeppol.atlassian.net 5265883137; 38th 4797956099; 39th 5009342467).
Q32 NL: parlementaire vraag boetes aantal -> no fine statistics; LEAD: KVABB (accountants/bookkeepers association) wrote to Minister Jambon asking VAT-return extension due to e-invoicing problems (made-in.be "Boekhouders vragen uitstel voor btw-aangiftes door problemen met e-facturatie").
Q33 NL: sector rejection rates (bouw/horeca/Mercurius) -> Evidence not found.
Q34 NL: AccountancyVandaag partner / ITAA congress exhibitor price -> ITAA congress 5 Nov 2026 Brussels Expo, 100+ exhibitors incl. start-ups, ~2,000 participants; prices not surfaced.
Q35 NL: Codabox VOILA price per company number -> tiered monthly price per company number, pooled with CODA/CARO volumes; amounts not surfaced; no activation cost, first month free.
Q36 NL: regional cloud adoption -> majority of firms have cloud accounting (TAB 2024 study, Flanders-focused); no regional split found.
Q37 EN: managed exception handling BE (Nymus/Babelway/Storecove) -> nothing beyond AP marketing.
Q38 GitHub search "peppol mcp" -> 22 repos: Helger-IT/phoss-peppol-mcp (Java, 14 stars, Apr 2026), eltyBelgium/billit-mcp (TS, Jun 2026, Cloudflare one-click), InvoiceXML/invoicexml-mcp, validatefin-mcp, cmendezs mcp-einvoicing-* series.
Q39 NL: KVABB letter Jambon -> Jan 2026: KVABB asked VAT-filing extension (25 Jan -> 28 Feb); "invoices correctly sent via Peppol often don't arrive", software crashes/performance problems, asked for a taskforce and lenient enforcement for demonstrable Peppol problems; cabinet refused general postponement, gave 3-month tolerance (businessam.be; nsz.be; accountancyvanmorgen.nl 12 Jan 2026). VRT 30 Mar 2026: accountants + self-employed ask postponement again: "government itself is not ready" (vrt.be/vrtnws/nl/2026/03/30/peppol-vraag-om-uitstel-boekhouders/).
Q40 EN: PSP forum 41st plenary -> not yet indexed; only 37-40 available.
Q41 NL: accountant per-client Peppol activation fee -> no firm price lists; e-invoice.be cost guide: registration usually free, basic config EUR 0-500, ERP integration EUR 500-5,000+.
Q42 NL: ITAA non-member IT subcontracting -> only the general rule (pseudo-professional may not perform reserved activities even as subcontractor); no IT-provider-specific guidance found.
Q43 NL: duplicates 0208/9925 -> Peppol Box: duplicates if registered on both unknowingly; WK knowledge base: purchase invoices addressed to a 9925 ID are not visible in the WK e-Invoicing portal (wktaaeu.my.site.com) — real identifier-layer ops problem persisting.
Q44 FR: Luxembourg fiduciaires -> ~95% of "fiduciaires" are OEC-registered; no count/preparation data found.
Q45 NL: Fid-Manager/AdminPulse/Silverfin Peppol portfolio -> no Peppol status integration surfaced; AdminPulse-Silverfin Talking Points integration Apr 2026; Billit-AdminPulse integration exists.
Q46 EN: undelivered problems Aug/Sep 2026 -> nothing dated after June 2026; Peppol Box (Mar-Jun 2026): "accounting software's Peppol module simply isn't working properly, no support from vendors who aren't Peppol specialists".
