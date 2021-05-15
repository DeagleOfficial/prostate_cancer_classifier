# import pickle
# file = open('knnPickle_file', 'rb')
# model = pickle.load(file)
# result = model.predict([[13,	19,	135, 1297,	0.141,	0.133,	0.181,	0.059]])
# print(result)

from flask import Flask, render_template,request
import pickle
import numpy as np
import os
app = Flask(__name__)
model = pickle.load(open('knnPickle_file', 'rb'))

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)