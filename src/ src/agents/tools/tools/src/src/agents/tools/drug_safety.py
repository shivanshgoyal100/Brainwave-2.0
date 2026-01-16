import requests

def check_drug_safety(med_list):
    """
    Simulates a lookup in an oncology drug-interaction database.
    """
    # In a real app, this would query a medical API like DrugBank
    risk_factors = []
    if "Temozolomide" in med_list and "Seizure_Med" in med_list:
        risk_factors.append("High Risk: Potential for hepatic stress. Monitor ALT levels.")
    
    return {
        "status": "Warning" if risk_factors else "Safe",
        "alerts": risk_factors
    }
