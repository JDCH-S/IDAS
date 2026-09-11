#!/usr/bin/env python3
"""Generate research/opportunity-database.csv from research/opportunity-database.json.

The JSON master is the single source of truth for scores and statuses so that the
markdown deliverables and the CSV cannot drift apart. Run: python3 research/build_csv.py
"""
import csv, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
COLUMNS = [
    "opportunity", "customer", "problem", "existing_solution", "direct_competitors",
    "indirect_competitors", "pricing", "market_size", "willingness_to_pay", "market_growth",
    "ai_leverage", "ai_commoditization_risk", "agi_resilience", "asi_resilience",
    "barrier_to_entry", "barrier_type", "capital_required", "time_to_first_revenue",
    "belgium_feasibility", "eu_expansion", "regulatory_difficulty", "technical_difficulty",
    "distribution_difficulty", "defensibility", "recurring_revenue", "founder_fit",
    "interest_fit", "overall_score", "status", "rejection_reason",
]

def main() -> int:
    rows = json.loads((HERE / "opportunity-database.json").read_text())
    missing = [(r.get("opportunity"), c) for r in rows for c in COLUMNS if c not in r]
    if missing:
        print("missing fields:", missing[:10], file=sys.stderr)
        return 1
    out = HERE / "opportunity-database.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda r: -float(r["overall_score"] or 0)):
            w.writerow(r)
    print(f"wrote {out} ({len(rows)} rows, {len(COLUMNS)} columns)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
