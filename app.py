import os

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

from cnnClassifier.pipeline.prediction import PredictionPipeline
from cnnClassifier.utils.common import decodeImage

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


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    data = request.get_json()
    image_data = data["image"]
    pipeline = PredictionPipeline(image_data)
    result = pipeline.predict()
    return jsonify(result)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080)  # for AWS
