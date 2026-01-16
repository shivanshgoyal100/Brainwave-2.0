class OncologyAgent:
    """Agent 3: Dose-Optimizer"""
    def recommend_dose(self, weight, tumor_grade):
        return f"Suggested Protocol: Temozolomide 150mg/m² based on Grade {tumor_grade}."

class ScribeAgent:
    """Agent 4: Clinical-Scribe"""
    def summarize(self, raw_data):
        return "Summary: Stable margins, treatment plan established."

class AdvocateAgent:
    """Agent 5: Patient-Companion (24/7 Q&A)"""
    def answer_query(self, question):
        return "It's normal to feel tired after your first cycle. Stay hydrated."

class LabTechAgent:
    """Agent 6: Lab-Sync (Toxicity Monitor)"""
    def monitor_labs(self, wbc_count):
        if wbc_count < 3000: return "ALERT: Low WBC. Consult Oncologist."
        return "Labs within safe chemotherapy range."
