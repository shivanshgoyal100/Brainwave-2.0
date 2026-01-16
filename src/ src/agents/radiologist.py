from ondemand_sdk import AirevClient
import os

class RadiologyAgent:
    def __init__(self, client: AirevClient):
        self.client = client
        self.agent_id = "neuro_sighter_v1"

    def analyze_scan(self, media_id):
        """
        Triggers MedGemma 1.5 to perform 3D segmentation.
        """
        response = self.client.agents.execute(
            agent_id=self.agent_id,
            input_media=media_id,
            prompt="Perform a volumetric analysis. Output tumor center-mass and margins."
        )
        return response['analysis_report']
