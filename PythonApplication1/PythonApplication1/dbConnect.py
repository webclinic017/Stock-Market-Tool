

#The standard URI connection string includes the following components:
#mongodb://					#A required prefix to identify that this is a string in the standard connection format.
#username:password@			#Optional. Authentication credentials. If specified, the client will attempt to log in to the specific database using these credentials after connecting. If the username or password includes the at sign @, colon :, slash /, or the percent sign % character, use percent encoding.
#host[:port]				#The host (and optional port number) where the mongod instance (or mongos instance for a sharded cluster) is running. the default port is 27017
#/database					#Optional. The name of the database to authenticate if the connection string includes authentication credentials in the form of username:password@. If /database is not specified and the connection string includes credentials, the driver will authenticate to the admin database.
#?<options>					#Optional. A query string that specifies connection specific options as <name>=<value> pairs.


from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


prefix = "mongodb://"
username = "JimSeeber"
password = "&4TOe3uH8Nu#"
port = "27017"
hostname = "cluster0-988hr.mongodb.net[:"+ port +"]"
hostname2 = "cluster0-988hr.mongodb.net:"+ port +""
db = "test"
db = "securities"
collection = "testCollection"
url = hostname+"/"+db+"."+collection
url2 = hostname2+"/"+db+"."+collection
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(url)
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)




#print(url2)

#client = pymongo.MongoClient(prefix + url2)			
#with client:
#	db = client.test
#	print(db.collection_names())



#from pymongo import MongoClient
## pprint library is used to make the output look more pretty
#from pprint import pprint

#mongodb://[JimSeeber:&4TOe3uH8Nu#@]host1[:port1][,...hostN[:portN]][/[database][?options]]

## connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
#db=client.admin
## Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)











#client = pymongo.MongoClient("localhost", 27017)
#db = client.test
#db.name
#u'test'
#db.my_collection
#Collection(Database(MongoClient('localhost', 27017), u'test'), u'my_collection')
#db.my_collection.insert_one({"x": 10}).inserted_id
#ObjectId('4aba15ebe23f6b53b0000000')
#db.my_collection.insert_one({"x": 8}).inserted_id
#ObjectId('4aba160ee23f6b543e000000')
#db.my_collection.insert_one({"x": 11}).inserted_id
#ObjectId('4aba160ee23f6b543e000002')
#db.my_collection.find_one()
#{u'x': 10, u'_id': ObjectId('4aba15ebe23f6b53b0000000')}
#for item in db.my_collection.find():
#    print(item["x"])

#10
#8
#11
#db.my_collection.create_index("x")
#u'x_1'
#for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
#    print(item["x"])

#8
#10
#11
#[item["x"] for item in db.my_collection.find().limit(2).skip(1)]
#[8, 11]
