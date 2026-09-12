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
Q47 NL: Wolters Kluwer e-Invoicing portal -> WK portal shows delivered documents and, if not delivered, the reason; Flowin = WK's own AP; portal EUR 5/file/month excl. VAT; Clearfacts pre-accounting portal for accountants (taasupport.wolterskluwer.be; wolterskluwer.com/nl-be/know/e-invoicing).
Q48 EN: e-invoice.be Peppol Radar accountants -> company search + "notify you when your suppliers become Peppol-ready"; no accountant-portfolio product surfaced.
Q49 FR: Horus/WinBooks status -> WinBooks Peppol History: Non envoyé / Envoyé / Échec statuses per company (help-winbooks.atlassian.net 5379870); Horus approved Peppol partner; no cross-dossier dashboard surfaced.
Q50 EN: vendors e-reporting 2028 ready -> Banqup compliance page covers BE e-invoicing + e-reporting; ITAA/Banqup survey: 85% of members had/plan an action plan; no vendor "reported vs booked" feature yet.
Q51 EN: Invoice Response support in BE ledgers -> Evidence not found beyond Billit IMR; Chift 2026 landscape: Exact Online market leader (Flanders), Yuki/Octopus Flanders, Horus mainly Wallonia.
Q52 NL: FPS Finance free registration check tool -> only generic FAQ; official lookup = Peppol Directory; no FPS bulk tool for taxpayers found.
Q53 EN/NL/FR: "Peppol-toeslag"/"supplément Peppol" honoraires -> Evidence not found.
Q54 EN: Banqup "what have we learned" -> "network stability confirmed; early challenges relate to registration gaps and data quality"; no percentages.
Q55 EN: Chift unified API -> connectors Exact Online, Horus, Octopus, Yuki, WinBooks etc.; "Flanders: Exact, Octopus, Adsolut, Yuki; Wallonia more on-premise and integrator-managed: Horus, WinBooks, Sage BOB50, Odoo" (chift.eu landscape 2026; docs.chift.eu connectors). Pricing not surfaced.
Q56 EN: RFC Peppol-20448 -> first BPA scan 20 Oct 2025: 5,500 non-compliances over 78 SMP URLs; second 24 Nov 2025: 80,027 over 115 SMPs; then 2.41% -> 0.31% by Apr 2026; globalisation focus group via BOSA.
Q57 EN: MLS timeline -> MLS v1.1.0 7 Jul 2026; OpenPeppol Service Provider Operational Guideline 2 Jul 2026 sets obligations and MLR->MLS transition; MLS is C3->C2 and needs no C4 participation; exact mandatory date not surfaced.
Q58 EN/NL/FR: Peppol consultant day rate Belgium -> Evidence not found.
GitHub: search_repositories "peppol mcp" (see Q38).

Total: 58 WebSearch queries + 1 GitHub API search.

---

## 2. Kill hypotheses — evidence, verdict, mitigation

### H1. Transient problem: rejection/identifier issues fall to negligible levels by 2027
Evidence:
- VERIFIED (search-summary): Belgian Peppol Authority + FPS Finance + OpenPeppol Operations Office run a "Belgian Peppol Network Data Scanner" that checks every SMP registration for the exact error classes the health check targets (no 0208, wrong 0208, wrong 9925, missing BIS Billing receive capability). Error rate fell from 2.41% (Dec 2025) to 0.31% (Apr 2026) over 7 runs while records scanned grew 1.2M -> 2.06M. The plenary voted to globalise the scanner (RFC Peppol-20448). https://openpeppol.atlassian.net/wiki/spaces/Belgium/pages/5265883137 ; https://openpeppol.atlassian.net/wiki/spaces/Belgium/pages/5009342467
- VERIFIED: first scan 20 Oct 2025 found 5,500 issues on 78 SMPs; 24 Nov 2025 80,027 issues on 115 SMPs; i.e. the identifier problem was real, was measured, and is being driven out at the SMP/service-provider level, not per client. Same URLs.
- VERIFIED: Banqup mid-2026: "network stability confirmed; early challenges relate to registration gaps and data quality" — framed as early-phase. https://www.banqup.com/resources/blog/belgium-s-2026-e-invoicing-mandate-what-have-we-learned-so-far-
- VERIFIED: MLS (transport-level delivery status between service providers, no end-user participation needed) v1.1.0 released 7 Jul 2026; OpenPeppol Service Provider Operational Guideline 2 Jul 2026 governs the MLR->MLS transition. Once MLS is live, "undelivered" becomes visible inside every AP by design. https://www.vatupdate.com/2026/08/24/peppol-status-messages-explained-why-mls-is-not-the-same-as-a-business-level-response/ ; https://docs.peppol.eu/edelivery/specs/mls/v1.0.0/mls/spec/
- VERIFIED: FPS FAQ (May 2026): if delivery exceeds one business day, the software supplier must investigate — the regulator assigns the delivery-monitoring duty to vendors. https://www.vatupdate.com/2026/05/18/belgium-updates-b2b-e-invoicing-new-faq-on-rejection-reverse-charge-and-peppol-delays/
- Counter-evidence: no post-June 2026 data on business-level rejections (wrong VAT text, missing PO reference, duplicates from dual 0208/9925 registration). WK knowledge base still documents 9925-addressed invoices being invisible in its portal (undated). https://wktaaeu.my.site.com/customers/articles/nl_BE/Knowledge/Peppol-aankoopfacturen-geadresseerd-aan-een-9925-Peppol-ID-zijn-niet-zichtbaar-in-het-e-Invoicing-portaal
Verdict: FATAL for the identifier-layer health check (phase 1 as scoped). The registration-quality problem is now measured by the state at 0.31% and falling, and the state itself owns the scanner. The residual business-level rejection layer is unmeasured (Evidence not found), so it is not proven dead — but it is also not proven alive.
Mitigation: drop "identifier validation" as the paid core; the only surviving phase-1 scope is content-level rejections and duplicates, which need ledger access, not directory lookups.

### H2. Firms will not pay: vendor support handles it; no evidence of firms paying third parties
Evidence:
- Evidence not found (NL/FR/EN, 6 queries): no Belgian accounting firm advertising a paid Peppol audit/scan/clean-up; no "Peppol-toeslag"/"supplément Peppol" in fee schedules; no third-party clean-up provider with references.
- VERIFIED: the only "Peppol audit" found is a free lead magnet by an Odoo integrator. https://blog.agile-minds.be/en/odoo-erp-en/peppol-belgium-2026-complete-guide-smes/
- VERIFIED: vendors sell the monitoring at SME price points: WK e-Invoicing portal EUR 5/file/month incl. delivered/not-delivered reason; Peppol Box EUR 5-7/month with identifier support; Codabox CODA from EUR 7.53/month. https://www.wolterskluwer.com/nl-be/know/e-invoicing ; https://faq.codabox.com/en/support/solutions/articles/75000118467-codabox-pricing-one-time-fees-and-recurring-costs
- Counter-evidence (over-kill side): France — expert-comptable author states transition mandates bill EUR 500-2,000 per client (diagnostic, platform, config, training). https://www.village-justice.com/articles/facturation-electronique-1er-septembre-2026-que-tout-cabinet-doit-avoir-fait,58836.html ; Belgium — KVABB/VRT show acute pain in Jan-Mar 2026 (see over-kill). Pain existed; paid third-party remedy did not appear.
Verdict: SERIOUS. Absence of evidence after 9 months of a mandated pain is meaningful: firms absorbed the work or pushed it to vendors. WTP is unproven, not disproven.
Mitigation: only interviews can settle it; price as a fixed-fee engagement (EUR 1,000+) in French-speaking firms where vendor support is weaker (Horus/WinBooks/BOB integrator-managed stacks).

### H3. Vendors absorb it
Evidence:
- VERIFIED: state-run scanner (H1) absorbs identifier validation at network level.
- VERIFIED: FPS FAQ places >1-business-day delivery investigation on the software supplier (H1 URL).
- VERIFIED: per-vendor status views already exist: WK portal (delivered / reason not delivered), WinBooks Peppol History (Non envoyé / Envoyé / Échec), Yuki not-delivered notification + activity log, OkiOki three badges, Billit customer/supplier Peppol status + IMR/MLR display. https://help-winbooks.atlassian.net/wiki/spaces/HelpWBC/pages/5379870 ; https://www.billit.eu/en-int/help-page/expenditure/invoices/where-can-i-see-imr-messages-from-invoices-sent-via-peppol/
- VERIFIED: Peliqan sells cross-ledger warehouse + MCP: platform EUR 150/month annual or ~EUR 199/month; Billit MCP from EUR 75/month; Yuki, Exact, Silverfin MCPs published. https://peliqan.io/blog/billit-claude-peppol/ ; https://peliqan.io/blog/yuki-claude-mcp/
- VERIFIED: Chift unified API already abstracts Exact Online, Yuki, Octopus, Horus, WinBooks etc. — the "cross-access-point" plumbing is a commodity. https://docs.chift.eu/unified-apis/accounting/connectors
- Evidence not found: any vendor roadmap item for a cross-dossier "rejected invoices" tab (Exact configuratiemonitor is settings only); Invoice Response (business-level) support outside Billit.
Verdict: SERIOUS (not fatal): per-vendor views exist and are enough for single-stack firms; cross-vendor consolidation is not shipped by ledgers, but Peliqan + Chift make it a weekend project, not a moat.

### H4. Reserved activity (ITAA)
Evidence:
- VERIFIED: "checking and correcting all accounting documents" is a reserved activity; a non-member may not perform reserved activities even as a subcontractor of an ITAA member; members must verify counterparties in the public register. https://www.itaa.be/nl/instituut/meldpunten/illegale-uitoefening/ ; https://issuu.com/institutetaxadvisorsaccountants/docs/itaa-zine_05-2022_juni_nl/s/16280466
- VERIFIED: ITAA frames data-quality guidance as the accountant's own advisory role (deep-dive 2.1) and frames e-reporting as separate from the accounts, with processing/return/advice remaining the professional's responsibility. https://www.blogitaa.be/2026/05/29/e-reporting-vanaf-2028-6-punten-om-uw-kantoor-en-uw-clienten-voor-te-bereiden/
- Evidence not found: any ITAA guidance specifically on IT/data providers touching master data.
Verdict: MANAGEABLE. Identifier/master-data hygiene (KBO number, Peppol scheme, VAT text) is not "correcting accounting documents"; delivering a fix LIST that the firm applies keeps the founder outside the reserved perimeter. The 2028 "reported vs booked" reconciliation is closer to the line (checking accounting documents) and must be sold as software the ITAA member operates, never as a service the founder performs.

### H5. Data-access kill
Evidence:
- VERIFIED: Billit — OAuth credentials by request, production integrations require approval; multi-tenant = commercial integration; accountant context via ContextCompanyID + PartyID. https://docs.billit.be/docs/how-do-i-get-started-with-oauth
- VERIFIED: Yuki — integration request via Visma Connect Developer Portal, scopes, Yuki approval; domain call quotas 1,000-5,000/day (Webservice) or 5,000-10,000/day (Extended) are paid accountant features. https://developer.yukisoftware.com/guides/guides-getting-started ; https://support.yuki.nl/en/support/solutions/articles/80000787670-yuki-api-link
- VERIFIED: Octopus — "100% free API", light rate limits. https://www.octopus.be/nl/boekhoudsoftware-integraties/
- VERIFIED: Exact — App Center registration; partner fee terms not surfaced (Evidence not found).
- VERIFIED: Peppol Directory — free, open source, full export; no commercial-reuse restriction surfaced. https://directory.peppol.eu/public/locale-en_US/menuitem-docs-export-all
- VERIFIED: KBO Open Data — free open licence, commercial reuse allowed with attribution; no direct marketing with personal data. https://economie.fgov.be/sites/default/files/Files/Entreprises/KBO/Licentie-KBO-Open-Data-gebruiksvoorwaarden.pdf
- VERIFIED: Chift already sells unified read access across the Belgian ledgers (pricing not surfaced).
Verdict: MANAGEABLE. Nothing blocks read access; the costs are vendor approvals (Billit, Yuki) and Yuki's per-domain call fees. The kill is not access — it is that access is already productised by Chift/Peliqan.

### H6. Price anchor kill
Evidence:
- VERIFIED anchors: WK e-Invoicing portal EUR 5/file/month; Peppol Box EUR 5-7/month; Codabox CODA from EUR 7.53/month per subscription (+EUR 24 per mandate setup), SODA <EUR 71/month per environment, VOILA tiered per company number (amounts not surfaced); Peliqan EUR 150-199/month platform, Billit MCP EUR 75/month; AdminPulse fixed price per user (not surfaced); Bizzcontrol on request. URLs above.
- INFERENCE: a monitoring add-on that firms would compare with Codabox/WK is anchored at EUR 5-8 per client per month; a 100-client firm at that anchor = EUR 500-800/month if the tool replaced those — but it does not replace them, it sits on top. Realistic ceiling EUR 100-300/firm/month is consistent with the thesis and with a side-income scale.
Verdict: MANAGEABLE for a service business, SERIOUS for a product ambition. Anchors confirm the deep dive's ceiling.

### H7. Distribution kill
Evidence:
- VERIFIED: Chift: Flanders = Exact/Octopus/Adsolut/Yuki (API-friendly); Wallonia = on-premise, integrator-managed: Horus, WinBooks, Sage BOB50, Odoo. https://www.chift.eu/blog/the-accounting-software-landscape-in-belgium-a-2026-guide
- VERIFIED: WinBooks/BOB Peppol via Codabox/Sage Cloud Demat; Horus cloud-native with its own Peppol partner. https://www.polynome.be/logiciel-gestion-fiduciaire-belgique/
- VERIFIED: ITAA congress 5 Nov 2026, Brussels Expo, 100+ exhibitors incl. start-ups, ~2,000 participants — an outsider can exhibit; pricing not surfaced. https://uitholland.eu/en/exhibition-stand-construction/calendar/itaa-brussels-expo-2026/
- ESTIMATE: French-speaking firms on integrator-managed stacks are reached through the integrators (Polynome, Logidrive, Megabyte, TAT, ibgraf), not directly.
Verdict: SERIOUS. The founder's French matches the stack that is hardest to integrate; the API-friendly stack is Dutch-speaking. The integrator channel is a real but slow route for a 10-15 h/week founder.

### H8. 2028 timing kill
Evidence:
- VERIFIED: pre-draft law approved 18 Jul 2026; publication expected autumn 2026; dataset by Royal Decree early 2027; entry 1 Jan 2028; dual near-real-time reporting (supplier and customer sides). https://www.vatupdate.com/2026/07/22/ahead-of-vida-belgium-formalises-dual-near-real-time-vat-e-reporting-from-2028/ ; https://www.deloitte.com/be/en/services/tax/blogs/belgium-to-introduce-near-real-time-e-reporting-of-invoicing-data.html
- VERIFIED: ITAA: "the e-report does not reflect your accounting and is separate from it" — the profession is being told there is nothing to reconcile by design; ITAA lobbies for a minimal dataset. https://www.blogitaa.be/2026/05/29/e-reporting-vanaf-2028-6-punten-om-uw-kantoor-en-uw-clienten-voor-te-bereiden/
- Evidence not found: any ledger vendor announcing a "reported vs booked" feature (Silverfin, Exact, WK, Billit, Banqup). Banqup markets e-reporting compliance generally.
- INFERENCE: with reporting done by the AP (C2/C3) in a 5-corner model, the reconciliation need arises only where AP-reported data and the ledger diverge — a vendor-internal check for single-stack clients.
Verdict: SERIOUS. Nothing to build before early 2027; ITAA's own framing removes the "second declaration" fear; vendors have 12+ months to bundle.

### H9. AI commoditisation
Evidence:
- VERIFIED: GitHub: Helger-IT/phoss-peppol-mcp (Apr 2026, 14 stars), eltyBelgium/billit-mcp (Jun 2026, one-click Cloudflare deploy, works with Claude/Gemini/ChatGPT), InvoiceXML/invoicexml-mcp, validatefin-mcp, cmendezs mcp-einvoicing-* — 22 repos. https://github.com/Helger-IT/phoss-peppol-mcp ; https://github.com/eltyBelgium/billit-mcp
- VERIFIED: Peppol Directory full export + KBO open data + phoss tooling make identifier validation a deterministic join.
- VERIFIED: Peliqan and Chift ship the multi-ledger layer commercially.
Verdict: FATAL for product differentiation, IRRELEVANT for a service: the buyer of a service is buying the operator, not the code.

---

## 3. New kill hypotheses (found during research)

N1. STATE-OWNED SCANNER (FATAL to phase 1): the BPA/FPS scanner already does bulk identifier validation network-wide and reports to SMPs; the founder would be re-selling a check the regulator runs for free and pushes upstream. VERIFIED (H1).
N2. REGULATORY DUTY SITS WITH VENDORS: FPS FAQ makes the software supplier responsible for investigating >1-day delivery delays; firms have a free escalation path. VERIFIED.
N3. MLS REMOVES THE "INVISIBLE FAILURE": once MLS is deployed by APs (guideline Jul 2026), undelivered status is available in every AP without C4 action — the monitoring agent's core signal becomes a standard vendor feature. VERIFIED spec, timeline ESTIMATE.
N4. E-REPORT IS "SEPARATE FROM THE ACCOUNTS" BY DESIGN: ITAA tells members there is no second declaration; a reconciliation product must first convince the profession there is a gap. VERIFIED framing.
N5. INTEGRATOR CHANNEL LOCK IN WALLONIA/BRUSSELS: on-prem stacks are integrator-managed; those integrators (Polynome, Logidrive, Megabyte) already run Peppol webinars for fiduciaires and would be both channel and competitor. VERIFIED (webinar invitations Nov 2025) https://www.logidrive.com/invitation-fiduciaire-presentation-facture-electronique-dans-winbooks-et-horus-18-11-2025-et-26-11-2025/
N6. PEAK PAIN ALREADY PASSED: the acute crisis (KVABB letter Jan 2026, VRT 30 Mar 2026) coincided with go-live; no comparable coverage after June 2026 was found. INFERENCE from absence.

## 4. Over-kill check (evidence in the thesis's favour the deep dive missed or under-weighted)

O1. VERIFIED: KVABB (bookkeepers' association) wrote to Minister Jambon in Jan 2026 asking to postpone the VAT return (25 Jan -> 28 Feb) because "invoices correctly sent via Peppol often do not arrive", software crashed, and asked for a taskforce and leniency for "demonstrable Peppol-related technical problems". https://businessam.be/beroepsvereniging-van-boekhouders-waarschuwt-voor-problemen-met-peppol-en-vraagt-uitstel-voor-btw-aangiftes ; https://www.nsz.be/nl/nieuws/detail/boekhouders-vragen-uitstel-voor-btw-aangiftes-door-problemen-met-e-facturatie — a professional body asking for regulatory relief is stronger demand evidence than any firm blog. Note "demonstrable" — firms need documentation of Peppol failures to claim leniency; that is a documentation product.
O2. VERIFIED: 30 Mar 2026 accountants and self-employed asked for postponement again, saying the government itself was not ready. https://www.vrt.be/vrtnws/nl/2026/03/30/peppol-vraag-om-uitstel-boekhouders/
O3. VERIFIED: FPS FAQ (May 2026) creates a compliance trail obligation: a wrongly addressed invoice must still be booked and reversed by credit note referencing the Peppol invoice ID; recipients must reject with response code "RE". Misrouted invoices therefore generate mandatory accounting work — a per-event cost the firm bears. https://www.vatupdate.com/2026/05/18/belgium-updates-b2b-e-invoicing-new-faq-on-rejection-reverse-charge-and-peppol-delays/
O4. VERIFIED: Peppol Box (Mar-Jun 2026): "the accounting software's Peppol module simply isn't working properly, with no support available from vendors who aren't Peppol specialists" — vendor support is not absorbing it everywhere. https://www.peppol-box.be/en/blog/peppol-belgium-problems-2026/
O5. VERIFIED (FR analogue): expert-comptable states transition mandates are billable at EUR 500-2,000 per client — a same-language price anchor for a fixed-fee engagement. https://www.village-justice.com/articles/facturation-electronique-1er-septembre-2026-que-tout-cabinet-doit-avoir-fait,58836.html
O6. VERIFIED: Luxembourg mandate: receive by 1 Jan 2028, issue from 1 Jul 2028 (large/medium) to 1 Jan 2029 (all); Peppol 4-corner; ~95% of "fiduciaires" are OEC-registered. A French-language second market with the same 0208-style identifier onboarding problem 18 months behind Belgium. https://www.vatupdate.com/2026/07/23/luxembourg-formalises-mandatory-b2b-e-invoicing-over-a-peppol-four-corner-network/ ; https://ilicompta.lu/guides/fiduciaire-vs-expert-comptable-luxembourg
O7. VERIFIED (PL analogue): Polish MF requires firms to monitor KSeF rejections, download UPO and resend; management reporting on rejected invoices is recommended; firms "implement additional control procedures". Exception handling became a named firm process there. https://www.pit.pl/aktualnosci/odrzucona-faktura-w-ksef-mf-kaze-monitorowac-pobierac-upo-i-ponownie-wysylac
O8. VERIFIED (IT analogue): SDI "scarti" monitoring exists — but bundled into invoicing software at EUR 3-36/year, not sold standalone. https://www.rpinet.it/notizie-pubbliche/401-monitoraggio-notifiche-di-scarto-sdi-pi%C3%B9-controllo-sulle-tue-fatture-elettroniche ; https://www.cloudfinance.it/software/software-fatturazione-elettronica
O9. Evidence not found: quantified staff hours lost per firm; sector rejection rates >1%; Belgian firms selling paid Peppol audits; paid exception-desk products in FR/DE/PL/IT after their mandates (all bundled or absent).

Over-kill verdict: the deep dive under-weighted O1-O4 (professional-body pain + regulator-created documentation duties) and Luxembourg (O6). It did NOT over-kill the product thesis: every foreign mandate shows exception handling being bundled into software, never sold standalone.

## 5. Steelman residual

Nothing survives of the thesis as written (bulk identifier validation -> cross-AP monitoring agent -> 2028 reconciliation engine, sold as product). Phase 1's core is done by the state at 0.31% error; phase 2's signal is being standardised (MLS) and its plumbing is sold by Peliqan/Chift; phase 3 is framed by ITAA as a non-problem until a 2027 decree says otherwise.

Steelman residual (HYPOTHESIS, needs interviews): a French-language, fixed-fee "Peppol incident documentation and clean-up" engagement for Brussels/Walloon fiduciaires on Horus/WinBooks/BOB stacks, priced EUR 1,000-2,000 per firm (FR anchor), whose deliverable is (a) the credit-note/RE trail the FPS FAQ requires for misrouted invoices, (b) the "demonstrable Peppol problem" file KVABB asked leniency for, and (c) the duplicate/9925 clean list. It is a consulting side-income, not a company; its only expansion is Luxembourg 2028 in the same language. It is worth 10 interviews and nothing more.

## 6. Five cheapest tests (each < 5 hours, < EUR 100)

T1. Ask 10 French-speaking fiduciaires (Brussels/Namur/Liège, 5-30 staff) two questions by email/LinkedIn: "How many Peppol incidents (undelivered, duplicate, misrouted) did you handle last month, and who fixed them?" and "Did you charge anyone for it?" Kill if median < 5 incidents/month or 0/10 charged.
T2. Run the free stack on one volunteer firm's client list: Peppol Directory export + KBO open data + peppolcheck.be; count residual identifier defects. Kill phase 1 if < 1% (consistent with the 0.31% scanner figure).
T3. Email BOSA/BPA (contact in the 40th plenary minutes) asking whether scanner findings are pushed to SMPs and whether a per-taxpayer view is planned. Kill if yes to both.
T4. Ask Peliqan and Chift for a price quote for a 3-ledger (Yuki+Exact+Horus) read-only connection for one firm. If < EUR 250/month all-in, the monitoring layer has a hard ceiling below the thesis price.
T5. Post one French LinkedIn offer: "Audit Peppol de votre portefeuille clients — 990 EUR, liste de corrections en 5 jours" to 30 fiduciaires; measure replies. Kill if 0 qualified replies in 3 weeks.
