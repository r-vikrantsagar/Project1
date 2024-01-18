from flask import *
import joblib
from flask import request, render_template
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


app = Flask(__name__)
model = joblib.load("data/model_RF.sav")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def female():
    return render_template("about.html")

@app.route("/data")
def male():
    return render_template("data.html")





@app.route("/predict1", methods = ['POST'])
def predict1():
    
    int_features= [float(x) for x in request.form.values()]
    print(int_features,len(int_features))
    final1=[np.array(int_features)]
    print(final1)
    #RF = RandomForestClassifier()
    #RF.fit(X_train1, y_train1)
    prediction = model.predict(final1)
    output1=round(prediction[0],2)
    print(output1)

    
    if (int(output1)==0):
        prediction = "Level 0 - Sufficiency Severity!"

    elif (int(output1)==1):
        prediction = "Level 1 - Insufficiency Severity! "

    elif (int(output1)==2):
        prediction = "Level 2 - Deficiency Severity! "
    
    else:
        prediction = "Level 3 - Severe Deficiency!"
    return (render_template('index.html', prediction_text = prediction))


if __name__ == '__main__':
    app.run(debug = True)

