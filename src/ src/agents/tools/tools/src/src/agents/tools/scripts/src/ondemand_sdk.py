import requests
import os

class OnDemandClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.on-demand.io/v1"

    def upload_media(self, file_path):
        # Implementation for Media API
        print(f"DEBUG: Uploading {file_path} to Media API...")
        return "media_id_998877"

    def call_agent(self, agent_id, user_input, media_id=None):
        # Implementation for Agent Orchestration
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {"agent_id": agent_id, "input": user_input, "media": media_id}
        # In demo: simulate response
        return {"status": "success", "output": f"Processed by {agent_id}"}
