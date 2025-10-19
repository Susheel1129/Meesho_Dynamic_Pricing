# Meesho_DynamicPricing

Repository scaffold for a dynamic pricing causal inference and prescriptive engine for Meesho.

Structure:
- data/: raw and processed datasets
- notebooks/: analysis and visualization notebooks
- src/: code for pricing engine and helpers
- reports/: dashboards and figures
- docs/: problem statement and playbooks

Quick start
1. Create a Python virtual environment (Python 3.10+ recommended).
2. pip install -r requirements.txt
3. Run `python data/generate_synthetic.py` to create example transactions at `data/raw/sim_transactions.csv`.
