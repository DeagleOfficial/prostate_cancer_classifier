from flask import Flask, render_template,request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('knnpickle_file', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST', 'GET'])
def predict():
    radius = float(request.form['radius'])
    texture = float(request.form['texture'])
    perimeter = float(request.form['perimeter'])
    area = float(request.form['area'])
    smoothness = float(request.form['smoothness'])
    compactness = float(request.form['compactness'])
    symmetry = float(request.form['symmetry'])
    fractaldimension = float(request.form['fractaldimension'])
    x = [[radius, texture, perimeter, area, smoothness, compactness, symmetry, fractaldimension]]
    prediction = model.predict(x)
    print (prediction[0])
    return render_template('index.html', prediction_test=prediction[0])


if __name__ == "__main__":
    app.run(debug=True)