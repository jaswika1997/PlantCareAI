
import json
from models.model import build_model
from ai_model.preprocessing import train_ds, valid_ds, class_names

# Build the model
model = build_model()

# Train the model
history = model.fit(
    train_ds,
    validation_data=valid_ds,
    epochs=3
)

# Save trained model
model.save("models/plant_disease_model.keras")

# Save class names for prediction
with open("models/class_names.json", "w") as f:
    json.dump(class_names, f)

print("Training completed!")
print("Model and class names saved successfully!")
