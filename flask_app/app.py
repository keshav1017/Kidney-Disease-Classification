import base64
import os

import numpy as np
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from keras.models import load_model
from keras.utils import img_to_array, load_img

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    # os.system("dvc repro")
    return "Training done successfully!"


def predict(base64_string):
    # preprocess the string
    if "," in base64_string:
        base64_string = base64_string.split(",")[1]

    # Load model
    model = load_model(os.path.join("models", "model.h5"))

    # Decode base64 image string
    decoded = base64.b64decode(base64_string)
    with open("input_image.jpg", "wb") as f:
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


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    data = request.get_json()
    image_data = data["image"]
    result = predict(image_data)
    return jsonify(result)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)  # for AWS
