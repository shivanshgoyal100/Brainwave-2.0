import requests
import datetime

def sync_medication_schedule(patient_id, schedule_data):
    """
    Pushes medication reminders to the patient's calendar via Webhook.
    """
    endpoint = f"https://api.neurobridge.ai/sync/{patient_id}"
    payload = {
        "events": schedule_data,
        "timestamp": datetime.datetime.now().isoformat()
    }
    response = requests.post(endpoint, json=payload)
    return response.status_code == 200
