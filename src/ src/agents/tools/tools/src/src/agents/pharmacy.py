from ondemand_sdk import AirevClient

class PharmacyAgent:
    def __init__(self, client: AirevClient):
        self.client = client

    def generate_schedule(self, radiology_report):
        """
        Uses MedGemma 27B to create a patient-centric drug regimen.
        """
        prompt = (
            f"Given this radiology report: {radiology_report}, create a "
            "simplified medication schedule for a patient. Include dosage for "
            "Dexamethasone and check for common interactions."
        )
        
        # Calling OnDemand Chat API with session persistence
        response = self.client.chat.create_session(
            model="medgemma-27b",
            instructions="You are a clear, patient-friendly Oncology Pharmacist."
        ).query(prompt)
        
        return response
