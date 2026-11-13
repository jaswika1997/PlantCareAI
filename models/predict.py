
import json
import numpy as np
import tensorflow as tf

from pathlib import Path
from PIL import Image
from io import BytesIO

# Get project paths
BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "plant_disease_model.keras"
CLASS_PATH = BASE_DIR / "class_names.json"

# Load model and class names once
model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r") as f:
    class_names = json.load(f)


def predict_disease(image):

    # Handle different image input formats
    if hasattr(image, "file"):
        image = image.file

    if isinstance(image, (str, Path)):
        img = Image.open(image)
    elif isinstance(image, bytes):
        img = Image.open(BytesIO(image))
    else:
        img = Image.open(image)

    # Preprocess image
    img = img.convert("RGB")
    img = img.resize((160, 160))

    img_array = np.array(img, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array, verbose=0)[0]

    # Get top 3 predictions
    top_indices = np.argsort(predictions)[-3:][::-1]

    top_predictions = []

    for index in top_indices:
        crop, disease = class_names[index].split("___")

        top_predictions.append({
            "crop": crop,
            "disease": disease.replace("_", " "),
            "confidence": round(float(predictions[index]), 4)
        })

    best_prediction = top_predictions[0]

    return {
        "crop": best_prediction["crop"],
        "disease": best_prediction["disease"],
        "confidence": best_prediction["confidence"],
        "top_predictions": top_predictions
    }
