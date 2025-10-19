#  Dynamic Pricing & Discount Sensitivity Dashboard (Power BI)

This project visualizes the results from the **Dynamic Pricing & Discount Sensitivity Model for Tier-2/3 Cities Using Causal Inference**.  
It connects simulated transactional and SKU-level discount recommendation data to highlight how discounts impact **conversion, margins, and ROI** — optimized for management reporting.

---

##  Dashboard Overview

###  Objective
To monitor pricing performance and understand **discount elasticity** across product categories and city tiers.  
The dashboard allows interactive exploration of:
- Conversion rate by discount level  
- Margin impact across categories  
- City-tier sensitivity to discount changes  
- Key KPIs like conversion, margin, and discount holidays
  <img width="962" height="541" alt="image" src="https://github.com/user-attachments/assets/aea56f8f-848f-4871-a04e-65fded71b581" />



---

## Data Sources

| Dataset | Description |
|----------|--------------|
| `synthetic_transactions.csv` | Simulated transaction-level data (category, city_tier, discount%, purchase outcome, margin) |
| `sku_discount_recommendations.csv` | SKU-level discount recommendations with optimal discount range and flags for discount holidays |

---

##  Data Model

| Relationship | Type | Direction |
|---------------|------|-----------|
| `synthetic_transactions[category] → sku_discount_recommendations[category_key]` | Many-to-One | Single |
| `synthetic_transactions[city_tier] → sku_discount_recommendations[city_tier_key]` | Many-to-One | Single |

Custom columns added in Power BI:
```DAX
category_key = synthetic_transactions[category]
city_tier_key = synthetic_transactions[city_tier]
