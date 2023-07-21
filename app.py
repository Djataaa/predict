import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model_2.pkl", "rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction==0:
        hasil = "Lulus"
    elif prediction==1:
        hasil = "Tidak Lulus"
    else: hasil="error"

    return render_template("index.html", prediction_text = "Mahasiswa/i diprediksi akan {}".format(hasil))

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)