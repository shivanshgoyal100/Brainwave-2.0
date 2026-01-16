from ondemand_sdk import OnDemandClient
from agents.specialized_swarm import OncologyAgent, LabTechAgent, AdvocateAgent
from tools.fhir_formatter import convert_to_fhir

def full_workflow_execution(file_path):
    client = OnDemandClient(api_key="HACKATHON_KEY_2026")
    
    # 1. Vision & Detection (Media API)
    m_id = client.upload_media(file_path)
    scan_report = client.call_agent("radiology_agent", "Detect tumor", m_id)

    # 2. Medication Reasoning (Agent Swarm)
    onc_agent = OncologyAgent()
    dosage = onc_agent.recommend_dose(weight=70, tumor_grade="II")
    
    # 3. Lab Monitoring
    lab_agent = LabTechAgent()
    safety_status = lab_agent.monitor_labs(wbc_count=4500)

    # 4. EHR Export (Custom Tool)
    fhir_json = convert_to_fhir({"id": "P-101", "diagnosis": scan_report['output']})

    return {
        "Treatment": dosage,
        "Safety": safety_status,
        "FHIR_Ready": True
    }

if __name__ == "__main__":
    print(full_workflow_execution("data/sample_mri.dcm"))
