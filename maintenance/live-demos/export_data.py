"""Regenerate public demo data exclusively from the portfolio's demo sources."""
from pathlib import Path
import ast
import json
import shutil
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def save(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, allow_nan=False, separators=(",", ":")), encoding="utf-8")

def records(path):
    df = pd.read_csv(path)
    return json.loads(df.to_json(orient="records"))

np = ROOT / "northpeak-fpna-main"
northpeak = {name: records(np / path) for name, path in {
    "actuals": "data/raw/actuals_pl.csv", "budget": "data/raw/budget_fy2025.csv",
    "drivers": "data/raw/subscription_drivers.csv", "scenarios": "outputs/scenarios.csv",
    "bridge": "outputs/dashboard_bridge.csv", "dashboard": "outputs/dashboard_data.csv",
}.items()}
save(OUT / "northpeak/dist/data.json", northpeak)
for name in ["EXECUTIVE_MEMO.md", "scenarios.csv", "dashboard_data.csv"]:
    shutil.copyfile(np / "outputs" / name, OUT / "northpeak/dist" / name)

rp = ROOT / "Actuariat_dashboard"
tree = ast.parse((rp / "subscription_backend.py").read_text(encoding="utf-8-sig"))
mappings = {}
for node in tree.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in ["REGION_MAPPING", "LOB_MAPPING"]:
                mappings[target.id] = ast.literal_eval(node.value)
# Explicit demo path: never use DATA_FILE or any other user-provided private source.
df = pd.read_csv(rp / "data/demo_dataset.csv.gz")
source_count = len(df)
df = df[df.UNDERWRITING_YEAR.between(2016, 2024)].copy()
df["region"] = df.DOMICILE_REGION.str.strip().str.upper().map(mappings["REGION_MAPPING"])
df = df.dropna(subset=["region"])
df["lob"] = df.LOB.map(mappings["LOB_MAPPING"]).fillna("Unclassified").replace("", "Unclassified")
df["product"] = df.BRANCH_NAME.eq("V I E").map({True: "Life", False: "Non-life"})
fac = df.TYPE_OF_BUSINESS.fillna("").str.upper().str.contains("FACULTATIVE|FACOB") | df.PORTFOLIO_TYPE.eq("2 - FACULTATIVE")
df["segment"] = fac.map({True: "Facultative", False: "Treaty"})
amounts = ["LAST_EPI_N", "LAST_CLAIMS_N", "LAST_CLAIM_RES_LATEST_N", "LAST_COMMISSION_N", "LAST_BROKERAGE_N", "LAST_OTHER_CHARGE_N", "LAST_OVERRIDER_COMMISSION_N"]
df[amounts] = df[amounts].fillna(0)
df["loss"] = df.LAST_CLAIMS_N + df.LAST_CLAIM_RES_LATEST_N
df["charges"] = df[amounts[1:]].sum(axis=1)
df["count"] = 1
keys = ["region", "lob", "product", "segment", "CEDANT", "UNDERWRITING_YEAR"]
agg = df.groupby(keys, dropna=False)[["LAST_EPI_N", "loss", "charges", "count"]].sum().reset_index()
agg.UNDERWRITING_YEAR = agg.UNDERWRITING_YEAR.astype(int)
# Positional rows keep the download small without changing aggregation precision.
payload = {
    "columns": ["region", "lob", "product", "segment", "cedant", "year", "premium", "loss", "charges", "count"],
    "rows": json.loads(agg.to_json(orient="values", double_precision=10)),
    "sourceRows": source_count, "includedRows": len(df),
    "totals": {"premium": float(df.LAST_EPI_N.sum()), "loss": float(df.loss.sum()), "charges": float(df.charges.sum())},
}
save(OUT / "reinsight/dist/data.json", payload)
assert abs(agg.LAST_EPI_N.sum() - payload["totals"]["premium"]) < 0.01
assert abs(agg.loss.sum() - payload["totals"]["loss"]) < 0.01
assert abs(agg.charges.sum() - payload["totals"]["charges"]) < 0.01
print(f"NorthPeak: {len(northpeak['scenarios'])} scenario months exported")
print(f"Reinsight: {len(df):,} demo rows -> {len(agg):,} aggregate rows; totals reconcile")
