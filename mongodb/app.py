
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

from pymongo import MongoClient

uri = "mongodb+srv://syedmikadaniel:KEJloCWtkXZ3CXAN@cluster0.zr2yo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
cluster = MongoClient(uri)
collection=cluster['test']
# Send a ping to confirm a successful connection
col1 = {"_id":0, "Name": "Kazuha", "Level":90}
col2 = {"_id":1, "Name": "Venti", "Level":60}
col3 = {"_id":2, "Name": "Zhong Li", "Level":90}
col4 = {"_id":3, "Name": "Raiden", "Level":90}

collection.insert_many(col1,col2,col3,col4)
results = collection.delete_one({ "Name":"Raiden"})
