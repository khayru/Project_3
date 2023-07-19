# import necesary libraries  
from flask import Flask,render_template, redirect, url_for,jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json

from flask import Flask, jsonify
import pandas as pd
import datetime as dt
#  create an flask app
app = Flask(__name__)
# pass the connection to the mongo 

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/project3"
mongo = PyMongo(app)
#################################################
@app.route("/")
def homepage():
    #data1 = mongo.db.project3_database.find_one({},{"Vehicle_Id": "1G1RD6E47C"})
    #print(jsonify(data1))
    #print(dumps(data1))
    return render_template("home.html")

@app.route("/get-data")
def get_data():
    data=mongo.db.project3_city_car.find()
    return render_template("home.html",data=data)
    # print(data)
    return jsonify(data)

#  this is not running 
@app.route("/summary_sale")
def summary_sale():
   car= list(mongo.db.project3.summary_sale())
   return render_template('sale.html',car=car)
  


# @app.route("/cars_Model_Year")
# def cars_Model_Year():
#     data = mongo.db.project3__electric_car.find({},{"Clean Alternative Fuel Vehicle Type": 1,
#     "Model Year": 1,"Make": 1,"Model": 1,"Electric Range": 1,
#     "New or Used Vehicle": 1,"Sale Price": 1,"Transaction Year": 1,
#     "City": 1,"State of Residence": 1,"Postal Code": 1})
#     return jsonify(data)


# @app.route("/get_model")
# def electric_cars():
#     data1 = mongo.db.project3__electric_car.find({"Model Year" ,"Make" ,"Model"})
#     return dumps(data1)

if __name__ == "__main__":
 app.run(debug=True)
    
    
