from bson.objectid import ObjectId
from pymongo import MongoClient

import pandas as pd
import json

conn = MongoClient("mongodb://localhost:27017/replicaSet=rs") #connects to the mongodb host
db = conn["pollution-bd3"] #creates a new database or connects to one is it already exists

# data = pd.read_csv("clean.csv", low_memory=False) #reads the csv file from directory
# df = pd.DataFrame(data)

# data_json = df.to_json(   orient = "records", 
#                         date_format = "epoch", 
#                         double_precision = 10, 
#                         force_ascii = True, 
#                         date_unit = "ms", 
#                         default_handler = None
#                     ) # converts the dataframe to a json format

# data_list = json.loads(data_json) #converts the json string to a list of python dictionary objects

# for datum in data_list: #loops through the list of objects
#     if datum["Location"] == 'AURN St Pauls': #checks if the Station is AURN st Pauls
#         db.readings.insert_one(datum) # Inserts the object as a document into a 'readings' collection in the db


document = db.readings.find_one({"_id": ObjectId('61d2c09dbac2b8724e9f1116')})

print(document)



