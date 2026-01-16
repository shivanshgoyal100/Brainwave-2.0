import json

def convert_to_fhir(patient_data):
    """
    Custom Tool: Converts AI analysis into HL7 FHIR standard format
    for seamless hospital EHR integration.
    """
    fhir_resource = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{"coding": [{"code": "imaging"}]}],
        "subject": {"reference": f"Patient/{patient_data['id']}"},
        "valueString": patient_data['diagnosis']
    }
    return json.dumps(fhir_resource)
