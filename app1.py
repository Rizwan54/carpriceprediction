from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)









