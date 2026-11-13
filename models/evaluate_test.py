
import os
from collections import defaultdict

from models.predict import predict_disease

TEST_DIR = r"C:\Users\prajn\Downloads\PlantDiseaseDataset\test\test"

# Actual labels based on test image filenames
label_mapping = {
    "AppleCedarRust": ("Apple", "Cedar apple rust"),
    "AppleScab": ("Apple", "Apple scab"),
    "PotatoEarlyBlight": ("Potato", "Early blight"),
    "PotatoHealthy": ("Potato", "healthy"),
    "TomatoEarlyBlight": ("Tomato", "Early blight"),
    "TomatoHealthy": ("Tomato", "healthy"),
    "TomatoYellowCurlVirus": (
        "Tomato", "Tomato Yellow Leaf Curl Virus"
    )
}

correct = 0
total = 0
results = []

for filename in sorted(os.listdir(TEST_DIR)):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    # Exclude unsupported crops
    prefix = "".join(
        char for char in filename if not char.isdigit()
    ).rsplit(".", 1)[0]

    if prefix.startswith("Corn"):
        continue

    actual = label_mapping[prefix]

    image_path = os.path.join(TEST_DIR, filename)
    prediction = predict_disease(image_path)

    predicted = (
        prediction["crop"],
        prediction["disease"]
    )

    is_correct = predicted == actual

    if is_correct:
        correct += 1

    total += 1

    results.append((filename, actual, predicted, is_correct))

    print(
        f"{filename} | Actual: {actual} | "
        f"Predicted: {predicted} | "
        f"{'CORRECT' if is_correct else 'WRONG'}"
    )

print("\nTEST RESULTS")
print("Total images:", total)
print("Correct predictions:", correct)
print("Incorrect predictions:", total - correct)
print("Test accuracy:", round(correct / total * 100, 2), "%")
