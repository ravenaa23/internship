import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# creating a table
mydb = client['Employee']

information = mydb.employeeinformation
records={
    "fname":"Ravenaa",
    "lname":"sri",
    "age":21
}
information.insert_one(records)