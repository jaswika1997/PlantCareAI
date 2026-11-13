import os

base_path = r"C:\Users\prajn\Downloads\PlantDiseaseDataset"

for root, dirs, files in os.walk(base_path):

    print("\nFolder:", root)

    for folder in dirs:
        print("  Subfolder:", folder)

    print("  Number of files:", len(files))