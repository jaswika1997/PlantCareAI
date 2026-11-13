import os

path = r"C:\Users\prajn\Downloads\PlantDiseaseDataset\test\test"

for filename in sorted(os.listdir(path)):
    print(filename)