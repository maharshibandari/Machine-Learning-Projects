from flask import Flask,request,render_template
from keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
global model, graph, c
#c = 1 #timestep size
import tensorflow as tf
graph =  tf.compat.v1.get_default_graph()
model = load_model('airlines-model.h5')
app = Flask(__name__)
@app.route('/')#when even the browser finds localhost:5000 then
def home():#excecute this function
    return render_template('index.html')#this function is returing the index.html file

@app.route('/ind')
def index2():
    return render_template('index2.html')

@app.route('/login', methods =['POST']) #when you click submit on html page it is redirection to this url
def login():#as soon as this url is redirected then call the below functionality
    year = request.form['year']
    month = request.form['month']
    passengers = request.form['passengers']
   
    total = [year,month,passengers]
    with graph.as_default():
    #y_pred = model.predict(x_test)
    	from sklearn.preprocessing import RobustScaler
    	rs = RobustScaler()
    	rs_pas = RobustScaler()
    	y_predict = model.predict(np.array([total]))

    	scaled_training=rs_pas.fit_transform(y_predict)
    	y_pred=rs_pas.inverse_transform(scaled_training.reshape(1,-1))[0][0]*10
    	#ypred1=rs_pas.fit_transform(y_predict.reshape(1,-1))
    	#y_predict1 = rs_pas.fit(y_predict)
    	#y_predict2 = rs_pas.inverse_transform(y_predict)
    	#print(ypred1)
    	#print(y_predict2)
    	#return str(y_pred)
        # from html page what ever the text is typed  that is requested from the form functionality and is stored in a name variable
    return render_template('index.html' ,showcase = str(round(y_pred)))
    #after typing the name show this name on index.html file where we have created a varibale abc
if __name__ == '__main__':
    app.run(debug=True)