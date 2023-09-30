
import os

import cv2
import tensorflow_hub as hub
import numpy as np
import tensorflow as tf

from api import config


MODEL_NAME = "model.hdf5"
MODEL_DIR_NAME = "ml_model"
MODEL_PATH = os.path.join(config.BASE_DIR, MODEL_DIR_NAME, MODEL_NAME)

CLASS_NAMES = ["buildings", "forest", "glacier", "mountain", "sea", "street"]


def predict(image):
  classifier_model = tf.keras.models.load_model(MODEL_PATH)
  model = tf.keras.Sequential(
    [hub.KerasLayer(classifier_model, input_shape=(128, 128,3))]
  )
  test_image = cv2.resize(image, (128, 128))
  test_image = tf.keras.preprocessing.image.img_to_array(test_image)
  test_image = test_image/255.0
  test_image = np.expand_dims(test_image, axis = 0)
  
  predictions = model.predict(test_image)
  scores = tf.nn.softmax(predictions[0])
  scores = scores.numpy()
  image_class = CLASS_NAMES[np.argmax(scores)]

  return image_class, f"{scores.max():.2f}"