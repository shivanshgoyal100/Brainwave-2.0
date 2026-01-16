import pydicom
import numpy as np

def preprocess_mri(dicom_path):
    """
    Standardizes raw MRI slices into a 3D voxel array for MedGemma 1.5.
    """
    ds = pydicom.dcmread(dicom_path)
    pixel_data = ds.pixel_array
    # Normalize intensity
    normalized = (pixel_data - np.min(pixel_data)) / (np.max(pixel_data) - np.min(pixel_data))
    return normalized.tolist()

# Registering as an OnDemand Tool
TOOL_METADATA = {
    "name": "MRI_Voxel_Standardizer",
    "description": "Converts DICOM files into normalized arrays for AI processing."
}
