#!/usr/bin/env python3
"""Generate research/sources.md from every URL cited in research/_raw/*.md.
Run: python3 research/build_sources.py
"""
import re, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
RAW = HERE / "_raw"
URL = re.compile(r'https?://[^\s\)\]>"|,;]+')

DESC = {
    "belgium-founder-facts.md": "Belgian founder-level facts (side-business status, VAT franchise, legal form, subsidies, employment law)",
    "stream-A.md": "Discovery stream A: finance, accounting and controlling workflows",
    "stream-B.md": "Discovery stream B: regulation-created pain",
    "stream-C.md": "Discovery stream C: Belgian vertical and physical SMEs, structural facts",
    "stream-D.md": "Discovery stream D: AI-adoption gap and startup landscape",
    "stream-E.md": "Discovery stream E: customer-pain mining (reviews, forums)",
    "ci-batch-1.md": "Competitive/existence checks, batch 1 (e-invoicing, accounting-firm tooling)",
    "ci-batch-2.md": "Competitive/existence checks, batch 2 (consolidation, close, FP&A)",
    "ci-batch-3.md": "Competitive/existence checks, batch 3 (compliance cascades, regulation)",
    "ci-batch-4.md": "Competitive/existence checks, batch 4 (verticals and services)",
    "deep-OPP-A.md": "Deep dive OPP-A: fractional controlling and consolidation",
    "deep-OPP-B.md": "Deep dive OPP-B: Peppol portfolio operations",
    "deep-OPP-C.md": "Deep dive OPP-C: QoE-light for small acquisitions",
    "deep-OPP-D.md": "Deep dive OPP-D: co-ownership renovation financing packs",
    "deep-OPP-E.md": "Deep dive OPP-E: DORA vendor pack",
    "deep-OPP-F.md": "Deep dive OPP-F: supplier compliance passport",
    "red-OPP-A.md": "Red team OPP-A", "red-OPP-B.md": "Red team OPP-B", "red-OPP-CD.md": "Red team OPP-C and OPP-D",
    "red-OPP-EF.md": "Red team OPP-E and OPP-F", "final-review.md": "Independent final review",
}

PRIMARY = [  # hand-picked primary or near-primary sources used for load-bearing claims
    ("Belgian law of 17 March 2019 on the accounting and tax professions (ITAA), Justel", "https://www.ejustice.just.fgov.be/eli/wet/2019/03/17/2019040805/justel"),
    ("ITAA: illegal practice hotline and reserved activities", "https://www.itaa.be/nl/instituut/meldpunten/illegale-uitoefening/"),
    ("ITAA: subcontracting (sous-traitance comptable) page", "https://www.itaa.be/fr/sous-traitance-comptable/"),
    ("ITAA blog: software-market concentration survey of 1,642 members (July 2026)", "https://www.blogitaa.be/2026/07/07/softwaremarkt-onder-druk-wat-1-642-confraters-ons-vertellen-over-concentratie-en-afhankelijkheid/"),
    ("ITAA blog: expert-comptable a shortage profession in all three regions (July 2026)", "https://www.blogitaa.be/fr/2026/07/01/lexpert-comptable-toujours-un-metier-en-penurie-en-flandre-en-wallonie-et-a-bruxelles/"),
    ("FPS Finance: VAT exemption scheme for small businesses", "https://finance.belgium.be/en/enterprises/vat/vat-obligation/vat-exemption-scheme-small-businesses"),
    ("FPS Finance: withholding obligation (30bis)", "https://finance.belgium.be/en/enterprises/withholding-obligation"),
    ("Odoo documentation 19.0: consolidation", "https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/consolidation.html"),
    ("Odoo forum: why was the consolidation module removed in Odoo 18", "https://www.odoo.com/forum/help-1/why-was-the-consolidation-module-removed-in-odoo-18-267924"),
    ("Statbel: multinational groups in Belgium (datalab)", "https://statbel.fgov.be/nl/themas/datalab/multinationale-groepen-belgie"),
    ("EWI Vlaanderen: foreign control in Flanders 2023", "https://www.ewi-vlaanderen.be/nieuws/buitenlands-zeggenschap-vlaanderen-anno-2023"),
    ("VATupdate: Belgium approves dual near-real-time VAT e-reporting for 2028", "https://www.vatupdate.com/2026/07/23/belgium-approves-dual-near-real-time-vat-e-reporting-for-2028/"),
    ("VLAIO: kmo-portefeuille reform from 1 Feb 2026", "https://www.vlaio.be/nl/nieuws/hervorming-kmo-portefeuille-vanaf-1-februari-2026-enkel-nog-advies-voor-cybersecurity"),
    ("Wallonia: cheques-entreprises", "https://www.cheques-entreprises.be/"),
    ("Microsoft release plan: Finance agents 2026 wave 1", "https://learn.microsoft.com/en-us/copilot/release-plan/2026wave1/finance-agents/"),
    ("Apex League: freelance finance rates in Belgium", "https://www.apexleague.be/insights/hoe-bepaal-je-jouw-freelance-finance-tarief-in-belgie"),
    ("Environnement Brussels: PEB in co-ownership", "https://environnement.brussels/citoyen/reglementation/obligations-et-autorisations/la-peb-en-copropriete"),
    ("UNIZO dossier on public procurement (Nov 2025)", "https://www.unizo.be/system/files?file=downloads/nov2025_UNIZO_dossier+overheidsopdrachten_DEF_0.pdf"),
    ("CSSF: DORA ICT and cyber risk", "https://www.cssf.lu/en/ict-and-cyber-risk-for-dora-entities/"),
    ("Laws of 2019: EU size thresholds uplift, Delegated Directive 2023/2775", "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202302775"),
]

def main():
    by_file = collections.OrderedDict()
    seen = set()
    for f in sorted(RAW.glob("*.md")):
        urls = []
        for u in URL.findall(f.read_text(errors="ignore")):
            u = u.rstrip(".:")
            if u not in urls:
                urls.append(u)
            seen.add(u)
        by_file[f.name] = urls
    out = [
        "# Sources", "",
        "## Sourcing method and its limits (read first)", "",
        "- Every factual claim in this research came from **WebSearch result summaries**. The environment's network policy blocked page fetches for every domain except github.com, so no primary page was opened. Labels used throughout: **VERIFIED (search-summary)** = stated in a search result summary and attributed to the URL given; **ESTIMATE** = derived number; **INFERENCE** = analyst reasoning; **HYPOTHESIS** = untested; **Evidence not found** = searched, nothing usable.",
        "- Where a figure appears in two or more independent results it was treated as triangulated. Vendor blogs are flagged as such in the raw files; numbers from them are directional.",
        "- Reddit was blocked for the search agents, so community-voice evidence comes from Hacker News, Indie Hackers, Teamblind, review sites and professional blogs instead.",
        "- Each search agent had a budget of ~200 queries; several ran out and list the queries they could not run. Those gaps are marked in the raw files.",
        "- Before acting on any figure that matters (regulatory scope, thresholds, prices), open the URL and confirm it. The ITAA reserved-activity question in particular needs a written legal opinion.",
        "",
        f"Unique URLs cited: {len(seen)} across {len(by_file)} raw research files.",
        "",
        "## Load-bearing primary or near-primary sources", "",
    ]
    for d, u in PRIMARY:
        out.append(f"- {d}: {u}")
    out += ["", "## All sources by research file", ""]
    for name, urls in by_file.items():
        out.append(f"### `{name}` ({len(urls)} URLs) — {DESC.get(name, '')}")
        out.extend(f"- {u}" for u in urls)
        out.append("")
    (HERE / "sources.md").write_text("\n".join(out))
    print(f"wrote sources.md: {len(seen)} unique URLs, {len(by_file)} files")

if __name__ == "__main__":
    main()
