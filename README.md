# Brainwave-2.0
Repository Structure: NeuroBridge-AI
Plaintext

NeuroBridge-AI/
├── README.md              # Project overview, problem, and solution
├── AGENTS.md              # Configuration for the 6 mandatory agents
├── requirements.txt       # Python dependencies (transformers, pydicom, etc.)
├── src/
│   ├── main.py            # Main entry point for the NeuroBridge application
│   ├── ondemand_sdk.py    # Wrapper for OnDemand Chat and Media APIs
│   └── agents/            # Specialized agent logic
│       ├── radiologist.py # MRI analysis using MedGemma 1.5
│       └── pharmacy.py    # Medication schedule generator
├── tools/                 # 3 Custom tool integrations
│   ├── mri_processor.py   # DICOM to 3D voxel converter
│   ├── drug_safety.py     # FDA drug-interaction checker
│   └── calendar_sync.py   # Patient notification pusher
└── data/
    └── sample_mri.dcm     # Example DICOM file for testing



1. README.md
Markdown

# NeuroBridge AI: Closing the Oncology Gap 
Track: brAInwave 2.0 OpenInnovation Track 

# The Problem
Patients diagnosed with brain tumors face a "Black Hole" after leaving the hospital. 
1. **Diagnostic Lag:** Radiologists are overwhelmed, delaying treatment start.
2. **Medication Failure:** 40% of oncology patients fail to follow complex post-op drug regimens.

##  The Solution: NeuroBridge
A comprehensive oncology OS that uses **MedGemma 1.5** via the **OnDemand platform** to:
- **Analyze:** Instant 3D MRI tumor detection using MedSigLIP encoders.
- **Act:** Six specialized agents manage everything from dosage to drug safety.
- **Advise:** A 24/7 patient-facing chat interface for real-time symptom management.

##  Technical Stack
- **AI Core:** Google MedGemma 1.5 (4B Multimodal for vision, 27B for reasoning).
- **Orchestration:** OnDemand AI OS .
- **APIs:** OnDemand Chat API, OnDemand Media API.
