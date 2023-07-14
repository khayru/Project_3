from flask import Flask, render_template, redirect, url_for,jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/project3_database"
mongo = PyMongo(app)
#################################################
@app.route("/")
def homepage():
    #data1 = mongo.db.project3_database.find_one({},{"Vehicle_Id": "1G1RD6E47C"})
    #print(jsonify(data1))
    #print(dumps(data1))
    return render_template("home.html")

@app.route("/electric_cars")
def electric_cars():
    data1 = mongo.db.project3_database.find({},{"Clean Alternative Fuel Vehicle Type": 1,"Vehicle_Id": 1,"Model Year": 1,"Make": 1,"Model": 1,"Electric Range": 1,"New or Used Vehicle": 1,"Sale Price": 1,"Transaction Year": 1,"City": 1,"State of Residence": 1,"Postal Code": 1})
   

  
    return dumps(data1)

if __name__ == "__main__":
    app.run()