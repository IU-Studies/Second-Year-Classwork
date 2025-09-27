from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('linear_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_value = float(request.form['feature'])
        prediction = model.predict(np.array([[input_value]]))[0]
        return render_template('index.html', prediction=f'Prediction: {prediction:.2f}')
    except ValueError:
        return render_template('index.html', prediction='Invalid input. Please enter a number.')

if __name__ == '__main__':
    app.run(debug=True)
