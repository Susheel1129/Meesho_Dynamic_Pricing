# Methodology

## Step 1: Data Simulation
- Simulated 50,000 transactions across 5 categories, 3 city tiers.  
- Columns: transaction_id, category, city_tier, base_price, discount_percent, final_price, purchased, margin_after_discount, date.

## Step 2: Exploratory Data Analysis
- Summary stats, missing values check, conversion vs discount trends.

## Step 3: Causal Inference
- Used **DoWhy** to estimate causal effect of discount on purchase:
  - Estimand: Average Treatment Effect (ATE)
  - Result: 0.00983 increase in purchase probability per 1% discount
- Verified assumptions: unconfoundedness, backdoor criterion.

## Step 4: Prescriptive Pricing Engine
- Inputs: causal effect, SKU stats
- Outputs:
  - Recommended discount per SKU
  - Discount holidays for high-conversion SKUs
  - Bundling suggestions for low-conversion Tier-2/3 SKUs
- Margin protection: ensures margin >= 50% of avg_margin

## Step 5: Export for Visualization
- Saved CSV for dashboard visualization (Streamlit / Power BI)
