import pandas as pd
import numpy as np
import os

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "synthetic_transactions.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "src", "models", "sku_discount_recommendations.csv")

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv(DATA_PATH, parse_dates=["date"])

# -----------------------------
# Base causal effect (from Step 3)
# -----------------------------
causal_effect = 0.00983  # effect per 1% discount on purchase probability

# -----------------------------
# Aggregate SKU-level stats
# -----------------------------
sku_stats = df.groupby(["category", "city_tier"]).agg(
    base_conversion=("purchased", "mean"),
    avg_margin=("margin_after_discount", "mean")
).reset_index()

# -----------------------------
# Optimal discount calculation
# -----------------------------
def compute_optimal_discount(row):
    """
    1. Start from 1% discount up to 40%
    2. Stop if marginal conversion gain < 0.005 (0.5%)
    3. Protect margin: margin_after_discount >= 50% of avg_margin
    """
    max_discount = 40
    step = 1
    base_margin = row["avg_margin"]

    for d in range(1, max_discount+1, step):
        marginal_conversion = causal_effect  # per 1% discount
        margin_after_discount = base_margin * (1 - d / 100)

        if marginal_conversion < 0.005 or margin_after_discount < 0.5 * base_margin:
            return max(1, d-1)
    return max_discount

sku_stats["recommended_discount"] = sku_stats.apply(compute_optimal_discount, axis=1)

# -----------------------------
# Discount Holidays Logic
# -----------------------------
# Example: if avg conversion > 0.7 and avg_margin > 30, skip discount to reset perception
def discount_holiday(row):
    if row["base_conversion"] > 0.7 and row["avg_margin"] > 30:
        return True
    return False

sku_stats["discount_holiday"] = sku_stats.apply(discount_holiday, axis=1)
# Set recommended_discount to 0 if discount holiday
sku_stats.loc[sku_stats["discount_holiday"], "recommended_discount"] = 0

# -----------------------------
# Bundling Logic
# -----------------------------
# Simple heuristic: bundle products if both categories are Tier-2 or Tier-3
def bundle_opportunity(row):
    if row["city_tier"] in ["Tier-2", "Tier-3"] and row["base_conversion"] < 0.6:
        return "Consider Bundle"
    return "No Bundle"

sku_stats["bundle_suggestion"] = sku_stats.apply(bundle_opportunity, axis=1)

# -----------------------------
# Save recommendations
# -----------------------------
os.makedirs(os.path.join(BASE_DIR, "src", "models"), exist_ok=True)
sku_stats.to_csv(OUTPUT_PATH, index=False)
print(f"SKU-level discount recommendations saved at: {OUTPUT_PATH}")
print(sku_stats)
