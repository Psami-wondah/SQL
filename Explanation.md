# Dependencies Used
- pandas
- mysql-connector-python
- pymongo



# 3a
- Connect to the db
- Create database instance: pollution-db2
- Connect to newly created database instance
- Create Table called 'readings'
- Read clean.csv file and covert to a pandas dataframe
- Convert Dataframe in to a json string and then a list of python dictionaries
- Create an order for insertion of data
- Loop through the list of python dictionaries and populate the database
- Commit the database to save insertions.

# 3b
- Read clean.csv file and covert to a pandas dataframe
- Convert Dataframe in to a json string and then a list of python dictionaries
- Slice first 100 from the list
- Loop through through the sliced list and print insertion commands to the insert-100.sql file

# 4a
- Select the db to be used with the USE command
- Select the 3 colums required with SELECT command
- Specify the table 'readings' with FROM command
- Specify the filter with WHERE command
- Order the rows by NOx with ORDER BY command and limit the the first with LIMIT 1


# 4b
- Select the db to be used with the USE command
- Select the columns PM2.5 and VPM2.5 withe AVG command to find their mean values and the location column that they are to be grouped by with SELECT command
- Specify the date and time filters with WHERE command
- Group by location with GROUP BY

# 4c 
- Extend the query in the previous script to span from 2010 to 2019 with WHERE command.


# 5

- Create a Model
- Use pymongo to connect to the mongodb database with python
- read csv file and convert to json as before
- loop through items that have the Location AURN St Pauls' and insert them into the readings collection in the db
- To query the db you can pass in the Id to get that particular object