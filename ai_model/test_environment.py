import tensorflow as tf

print("TensorFlow:", tf.__version__)

print("Keras:", tf.keras.__version__)

print("GPU:", tf.config.list_physical_devices('GPU'))

print("Environment ready!")