
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import classification_report, confusion_matrix
from ai_model.preprocessing import valid_ds, class_names

# Load trained model
model = tf.keras.models.load_model(
    "models/plant_disease_model.keras"
)

# Get actual labels and predictions
y_true = np.concatenate([
    labels.numpy() for images, labels in valid_ds
])

predictions = model.predict(valid_ds)
y_pred = np.argmax(predictions, axis=1)

# Classification report
print("\nCLASSIFICATION REPORT\n")
print(classification_report(
    y_true,
    y_pred,
    target_names=class_names,
    digits=4
))

# Confusion matrix
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(16, 14))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=class_names,
    yticklabels=class_names
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Plant Disease Classification - Confusion Matrix")
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
