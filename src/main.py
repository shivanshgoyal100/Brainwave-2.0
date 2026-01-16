import os
import torch
from transformers import pipeline
from ondemand_sdk import AirevClient  # Mocking OnDemand SDK based on track info

# Initialize OnDemand Platform (Airev)
client = AirevClient(api_key=os.getenv("AIREV_API_KEY"))

def run_neuro_bridge(mri_file):
    """
    Orchestrates the patient journey from scan to medication.
    """
    # 1. Vision Step: Use Media API to process 3D MRI
    print("--- Step 1: MRI Analysis ---")
    media_id = client.media.upload(mri_file)
    
    # Analyze using MedGemma 1.5 4B Multimodal
    radiology_output = client.agents.execute(
        agent_id="radiology_agent",
        input_media=media_id,
        prompt="Identify tumor margins and type in this 3D scan."
    )

    # 2. Reasoning Step: Use Chat API for Medication Advice
    print("--- Step 2: Medication Planning ---")
    chat_session = client.chat.start(model="medgemma-27b-it") # Text-optimized
    
    treatment_plan = chat_session.ask(
        f"Based on this report: {radiology_output}, generate a 7-day "
        "medication schedule and check for Dexamethasone interactions."
    )

    return treatment_plan

if __name__ == "__main__":
    result = run_neuro_bridge("data/sample_mri.dcm")
    print(f"\nFinal Treatment Bridge Output:\n{result}")
