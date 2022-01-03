import pandas as pd
import mysql.connector as sql #importing the connector that connects the database
import json



#This is the connector used to connect to the db
mydb = sql.connect(
    host= "localhost",      #mysql db host
    user="root",            #username
    password= "Owhondah1"   #password
)                             #Entering DataBase Credentials

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE `pollution-db2` ") #This creates a new database instance



mydb = sql.connect(
    host= "localhost",      #mysql db host
    user="root",            #username
    password= "Owhondah1",  #password
    database= "pollution-db2"   #selecting newly created database instance
)                             #Entering DataBase Credentials

mycursor = mydb.cursor()


mycursor.execute("DROP TABLE IF EXISTS `readings`;") #This drops a table if it already exists in the database



mycursor.execute(""" CREATE TABLE readings (
    id INTEGER(11) NOT NULL AUTO_INCREMENT,
    `Date Time` DATETIME,
    NOx FLOAT(10),
    NO2 FLOAT(10),
    NO FLOAT(10),
    SiteID INTEGER(10),
    PM10 FLOAT(10),
    NVPM10 FLOAT(10),
    VPM10 FLOAT(10),
    `NVPM2.5` FLOAT(10),
    `PM2.5` FLOAT(10),
    `VPM2.5` FLOAT(10),
    CO FLOAT(10),
    O3 FLOAT(10),
    SO2 FLOAT(10),
    Temperature FLOAT(10),
    RH FLOAT(10),
    AirPressure FLOAT(10),
    Location VARCHAR(255),
    geo_point_2d VARCHAR(255),
    DateStart DATETIME,
    DateEnd DATETIME,
    Current BOOLEAN,
    `Instrument Type` VARCHAR(255),
    primary key (id)
    )""")





data = pd.read_csv("3a/clean.csv", low_memory=False)
df = pd.DataFrame(data)

data_json = df.to_json(   orient = "records", 
                        date_format = "epoch", 
                        double_precision = 10, 
                        force_ascii = True, 
                        date_unit = "ms", 
                        default_handler = None
                    )
data_list = json.loads(data_json)



formula = """INSERT INTO readings (
            `Date Time`,
            NOx,
            NO2,
            NO,
            SiteID,
            PM10,
            NVPM10,
            VPM10,
            `NVPM2.5`,
            `PM2.5`,
            `VPM2.5`,
            CO,
            O3,
            SO2,
            Temperature,
            RH,
            AirPressure,
            Location,
            geo_point_2d,
            DateStart,
            DateEnd,
            Current,
            `Instrument Type`
            ) VALUES (  %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, 
                        %s, %s, %s)"""
for row in data_list:
    mycursor.execute(formula, ( row['Date Time'], row['NOx'], row['NO2'], row['NO'], row['SiteID'], 
                                row['PM10'], row['NVPM10'], row['VPM10'], row['NVPM2.5'], row['PM2.5'], 
                                row['VPM2.5'], row['CO'], row['O3'], row['SO2'], row['Temperature'], 
                                row['RH'], row['Air Pressure'], row['Location'], row['geo_point_2d'], row['DateStart'], 
                                row['DateEnd'], row['Current'], row['Instrument Type'])  )




mydb.commit()
