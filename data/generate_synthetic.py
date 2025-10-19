import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# -----------------------------
# Configuration
# -----------------------------
np.random.seed(42)
random.seed(42)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "processed", "synthetic_transactions.csv")

# Parameters
NUM_TRANSACTIONS = 50000
CITIES = ["Tier-1", "Tier-2", "Tier-3"]
CATEGORIES = ["Beauty", "Electronics", "Home", "Fashion", "Groceries"]
DISCOUNT_LEVELS = [0, 5, 10, 15, 20, 25, 30, 40]

# -----------------------------
# Simulation Logic
# -----------------------------
def generate_data():
    data = []
    start_date = datetime(2024, 1, 1)

    for i in range(NUM_TRANSACTIONS):
        city_tier = random.choices(CITIES, weights=[0.2, 0.4, 0.4])[0]
        category = random.choice(CATEGORIES)
        base_price = random.uniform(200, 3000)

        # Discounting pattern — more aggressive in lower tiers
        discount = random.choices(
            DISCOUNT_LEVELS,
            weights=[0.05, 0.1, 0.15, 0.2, 0.2, 0.15, 0.1, 0.05],
        )[0]

        final_price = base_price * (1 - discount / 100)
        date = start_date + timedelta(days=random.randint(0, 270))

        # Simulate purchase probability (price sensitivity higher in Tier-3)
        base_prob = 0.6 if city_tier == "Tier-1" else (0.45 if city_tier == "Tier-2" else 0.3)
        discount_boost = 0.01 * discount
        purchase_prob = min(base_prob + discount_boost, 0.95)

        purchased = np.random.binomial(1, purchase_prob)
        margin = base_price * 0.2  # 20% nominal margin before discount
        margin_after_discount = margin - (base_price * (discount / 100))

        data.append([
            i + 1,
            city_tier,
            category,
            base_price,
            discount,
            final_price,
            purchased,
            margin_after_discount,
            date
        ])

    df = pd.DataFrame(data, columns=[
        "transaction_id",
        "city_tier",
        "category",
        "base_price",
        "discount_percent",
        "final_price",
        "purchased",
        "margin_after_discount",
        "date"
    ])
    return df

# -----------------------------
# Run Simulation
# -----------------------------
if __name__ == "__main__":
    df = generate_data()
    os.makedirs(os.path.join(BASE_DIR, "processed"), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"✅ Synthetic dataset created successfully at: {OUTPUT_PATH}")
    print(df.head(10))
