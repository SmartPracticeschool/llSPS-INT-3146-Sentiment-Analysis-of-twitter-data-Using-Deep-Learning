import numpy as np
import h5py
import cv2
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model= h5py.File('Mymodel.h5', 'r')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = request.form['tweet']
    x_intent=cv.transform([x_test])
    prediction=model.predict(x_intent)
    if(prediction> 0.5):
        return render_template('index.html',prediction_text='it is positive review')
    else:
        return render_template('index.html',prediction_text='it is a negative review')


if __name__ == "__main__":
    app.run(debug=True)
