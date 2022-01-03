# **Task 5**

# Database Used: **MongoDB**


# Data Model


Field | Description
------|------------
_id | The unique Id designated by Mongodb as ObjectId
Date Time | A Timestamp field
NOx | A Double field
NO2 | A Double field
NO | A Double field
SiteID | An Integer Field
PM10 | A Double field
NVPM10 | A Double field
VPM10 | A Double field
NVPM2.5 | A Double field
PM2.5 | A Double field
VPM2.5 | A Double field
CO | A Double field
O3 | A Double field
SO2 | A Double field
Temperature | A Double field
RH | A Double field
AirPressure | A Double field
Location | A String field
geo_point_2d | A String field
DateStart | A Timestamp field
DateEnd | A Timestamp field
Current | A Boolean field
Instrument Type | A String field



## Example:

```javascript
{   
    "_id": "61d2c09dbac2b8724e9f1116",
    "Date Time": "2013-08-23T22:00:00+00:00",
    "NOx": 32.00043,
    "NO2": 28.99493,
    "NO": 1.96013,
    "SiteID": 452,
    "PM10": 32.3,
    "NVPM10": 20.9,
    "VPM10": 11.4,
    "NVPM2.5": 16.2,
    "PM2.5": 25.603,
    "VPM2.5": 9.2,
    "CO": null,
    "O3": 30.73378,
    "SO2": null,
    "Temperature": null,
    "RH": null,
    "Air Pressure": null,
    "Location": "AURN St Pauls",
    "geo_point_2d": "51.4628294172,-2.58454081635",
    "DateStart": "2006-06-15T00:00:00+00:00",
    "DateEnd": null,
    "Current": true,
    "Instrument Type": "Continuous (Reference)"
}
```


# Implementation

## **Using Pymongo**

- `pip install pymongo`
- `pip install pandas`

### **Python code to implement it**

```python
from pymongo import MongoClient
import pandas as pd
import json

conn = MongoClient("mongodb://localhost:27017/replicaSet=rs") #connects to the mongodb host
db = conn["pollution-db3"] #creates a new database or connects to one is it already exists

data = pd.read_csv("clean.csv", low_memory=False) #reads the csv file from directory
df = pd.DataFrame(data)

data_json = df.to_json(   orient = "records", 
                        date_format = "epoch", 
                        double_precision = 10, 
                        force_ascii = True, 
                        date_unit = "ms", 
                        default_handler = None
                    ) # converts the dataframe to a json format

data_list = json.loads(data_json) #converts the json string to a list of python dictionary objects

for datum in data_list: #loops through the list of objects
    if datum["Location"] == 'AURN St Pauls': #checks if the Station is AURN st Pauls
        db.readings.insert_one(datum) # Inserts the object as a document into a 'readings' collection in the db

```

## An example document from Mongodb Compass
```
_id: ObjectId("61d2c09dbac2b8724e9f1116")
Date Time: "2013-08-23T22:00:00+00:00"
NOx: 32.00043
NO2: 28.99493
NO: 1.96013
SiteID: 452
PM10: 32.3
NVPM10: 20.9
VPM10: 11.4
NVPM2.5: 16.2
PM2.5: 25.603
VPM2.5: 9.2
CO: null
O3: 30.73378
SO2: null
Temperature: null
RH: null 
Air Pressure: null
Location: "AURN St Pauls"
geo_point_2d: "51.4628294172,-2.58454081635"
DateStart: "2006-06-15T00:00:00+00:00"
DateEnd: null
Current: true
Instrument Type: "Continuous (Reference)"
```

# Conclusion

MongoDB stores data in documents, and documents in collections, collections in database instances.

For a database instance, you can have multiple collections which are identical in purpose to tables in SQL.

And then documents within the collection holds data for different objects or items just rows in SQL

MongoDB data structure is flexible because all documents don't have to follow a particular structure in a collection unlike SQL rows in a table.
