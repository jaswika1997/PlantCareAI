import zipfile
import os

zip_path = r"C:\Users\prajn\Downloads\archive (1).zip"

extract_path = r"C:\Users\prajn\Downloads\PlantDiseaseDataset"

os.makedirs(extract_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset extracted successfully!")
print("Location:", extract_path)