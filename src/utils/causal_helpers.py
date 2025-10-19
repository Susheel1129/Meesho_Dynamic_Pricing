# utils/causal_helper.py
import dowhy
from dowhy import CausalModel

def estimate_ate(df, treatment, outcome, common_causes):
    """
    Estimate Average Treatment Effect using DoWhy
    Args:
        df: pd.DataFrame
        treatment: str, column name of treatment variable (e.g., 'discount_percent')
        outcome: str, column name of outcome variable (e.g., 'purchased')
        common_causes: list of str, covariates for backdoor adjustment
    Returns:
        ate: float, estimated causal effect
        model: dowhy CausalModel object
    """
    model = CausalModel(
        data=df,
        treatment=treatment,
        outcome=outcome,
        common_causes=common_causes
    )
    
    # Identify causal effect
    identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)
    
    # Estimate effect
    estimate = model.estimate_effect(identified_estimand,
                                     method_name="backdoor.linear_regression")
    
    return estimate.value, model
