import requests

def check_oncology_interactions(prescribed_drugs):
    """
    Custom tool to cross-reference prescriptions with oncology safety databases.
    """
    # Logic to ping a medical knowledge graph or database
    interactions = []
    # Mocking check for high-risk brain tumor meds like Temozolomide
    if "Temozolomide" in prescribed_drugs:
        interactions.append("Alert: Monitor platelet count weekly.")
    return interactions
