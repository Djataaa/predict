import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create flask app
app = Flask(__name__)
model = pickle.load(open("model_2.pkl", "rb"))

def is_valid_input(value):
    try:
        num = float(value)
        return 0 <= num <= 100
    except ValueError:
        return False

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    
    UTS = request.form["UTS"]
    tugasonline = request.form["tugasonline"]
    quizonline = request.form["quizonline"]

    # Validate input (check if they are numbers within the range 0 to 100)
    if not is_valid_input(UTS) or not is_valid_input(tugasonline) or not is_valid_input(quizonline):
        return render_template("index.html", error_message="Input harus angka dan dengan nilai minimal 0 dan maksimal 100")

    # Convert input values to float
    float_features = [float(UTS), float(tugasonline), float(quizonline)]
    features = [np.array(float_features)]
    prediction = model.predict(features)

    if prediction==0:
        hasil = "Lulus, pertahankan dan tingkatkan pola belajar anda"
    elif prediction==1:
        hasil = "Tidak Lulus, perbaiki pola belajar anda dan segera hubungi dosen anda untuk tugas tambahan"
    else: hasil="error"

    return render_template("index.html", prediction_text = "Mahasiswa/i diprediksi akan {}".format(hasil))

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
