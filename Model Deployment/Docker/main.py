#!flask/bin/python

import os
from flask import Flask
from flask import request
import pandas as pd
from sklearn import linear_model
from sklearn import datasets
import pickle
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.ensemble
import sklearn.model_selection


iris = sklearn.datasets.load_iris()

train, test, labels_train, labels_test = sklearn.model_selection.train_test_split(iris.data, iris.target, train_size=0.90)

# creating and saving some model
rf = sklearn.ensemble.RandomForestClassifier(n_estimators=500)
rf.fit(train, labels_train)
pickle.dump(rf, open('iris.pkl', 'wb'))

app = Flask(__name__)

@app.route('/isAlive')
def index():
    return "true"

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    data = request.get_json()  # Get data posted as a json
    data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
    model = pickle.load(open('iris.pkl', 'rb'))
    prediction = model.predict(data)  # runs globally loaded model on the data
    return str(prediction[0])

if __name__ == '__main__':
    if os.environ['ENVIRONMENT'] == 'production':
        app.run(port=80,host='0.0.0.0')


