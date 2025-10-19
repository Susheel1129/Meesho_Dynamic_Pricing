# utils/data_loader.py
import pandas as pd
import os

def load_synthetic_data(base_dir=None):
    """
    Load processed synthetic transaction data
    Returns: pd.DataFrame
    """
    if base_dir is None:
        base_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    data_path = os.path.join(base_dir, "data", "processed", "synthetic_transactions.csv")
    df = pd.read_csv(data_path, parse_dates=["date"])
    
    # Optional: add any preprocessing steps
    # e.g., create dummy variables for categories/city_tier
    df = pd.get_dummies(df, columns=["category", "city_tier"], drop_first=False)
    
    return df
