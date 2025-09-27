from flask import Flask, render_template, request
import joblib
import shap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

model = joblib.load('model.pkl')

feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
background_data = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=feature_names)
explainer = shap.Explainer(model.predict, background_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    shap_image = None

    if request.method == 'POST':
        values = [float(request.form[f]) for f in feature_names]
        input_data = pd.DataFrame([values], columns=feature_names)

        prediction = model.predict(input_data)[0]

        shap_values = explainer(input_data)
        plt.figure()
        shap.plots.waterfall(shap_values[0], show=False)
        if not os.path.exists('static'):
            os.makedirs('static')
        plt.savefig('static/shap_plot.png', bbox_inches='tight')
        plt.close()
        shap_image = 'static/shap_plot.png'

    return render_template('index.html', feature_names=feature_names, prediction=prediction, shap_image=shap_image)

if __name__ == '__main__':
    app.run(debug=True)
