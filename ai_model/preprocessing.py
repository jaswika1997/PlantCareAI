
import tensorflow as tf
from pathlib import Path

# Dataset paths
BASE_DIR = Path(
    r"C:\Users\prajn\Downloads\PlantDiseaseDataset"
    r"\New Plant Diseases Dataset(Augmented)"
    r"\New Plant Diseases Dataset(Augmented)"
)

TRAIN_DIR = BASE_DIR / "train"
VALID_DIR = BASE_DIR / "valid"

# Configuration
IMAGE_SIZE = (160, 160)
BATCH_SIZE = 32
SEED = 42

# Crops we want
SELECTED_CROPS = ["Apple", "Potato", "Tomato"]


def get_selected_classes(directory):

    classes = []

    for folder in directory.iterdir():

        if folder.is_dir():

            crop = folder.name.split("___")[0]

            if crop in SELECTED_CROPS:
                classes.append(folder.name)

    return sorted(classes)


# Get selected classes
class_names = get_selected_classes(TRAIN_DIR)

print("Selected classes:", len(class_names))

for name in class_names:
    print(name)


# Load training dataset
train_ds = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    class_names=class_names,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    shuffle=True,
    seed=SEED
)


# Load validation dataset
valid_ds = tf.keras.utils.image_dataset_from_directory(
    VALID_DIR,
    class_names=class_names,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    shuffle=False
)


# Optimize loading
AUTOTUNE = tf.data.AUTOTUNE

train_ds = train_ds.prefetch(AUTOTUNE)
valid_ds = valid_ds.prefetch(AUTOTUNE)


# Verify
print("\nTraining dataset ready!")
print("Validation dataset ready!")
print("Number of classes:", len(class_names))

import matplotlib.pyplot as plt

# Display 9 sample training images
plt.figure(figsize=(10, 10))

for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i].numpy()])
        plt.axis("off")

plt.tight_layout()
plt.show()