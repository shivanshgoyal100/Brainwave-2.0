import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, generate_uid
import numpy as np
import datetime

def generate_mock_mri(filename="data/sample_mri.dcm"):
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2' # CT/MRI
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.ImplementationClassUID = generate_uid()
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

    ds = Dataset()
    ds.file_meta = file_meta
    ds.PatientName = "DOE^JOHN"
    ds.ContentDate = datetime.datetime.now().strftime('%Y%m%d')
    
    # Create fake tumor data (random pixel array)
    pixel_data = np.random.randint(0, 255, (512, 512), dtype=np.uint8)
    ds.PixelData = pixel_data.tobytes()
    ds.Rows, ds.Cols = 512, 512
    ds.BitsAllocated = 8
    
    ds.save_as(filename, enforce_file_format=True)
    print(f"Mock MRI generated at {filename}")

if __name__ == "__main__":
    generate_mock_mri()
