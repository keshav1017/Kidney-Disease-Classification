import base64
import numpy as np
from keras.models import load_model
from keras.utils import img_to_array, load_img
from io import BytesIO
from PIL import Image
import os


class PredictionPipeline:
    def __init__(self, base64_string):
        if "," in base64_string:
            base64_string = base64_string.split(",")[1]
        self.base64_string = base64_string

    def predict(self):
        # Load model
        model = load_model(os.path.join("models", "model.h5"))

        # Decode base64 image string
        decoded = base64.b64decode(self.base64_string)
        with open("input_image.jpg", 'wb') as f:
            f.write(decoded)
            f.close()

        # Load and preprocess image
        imagename = "input_image.jpg"
        test_image = load_img(imagename, target_size=(224, 224))
        test_image = img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)

        prediction = "Tumor" if result[0] == 1 else "Normal"
        return [{"image": prediction}]
