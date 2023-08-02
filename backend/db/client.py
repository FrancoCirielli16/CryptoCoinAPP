from pymongo import MongoClient
from keys import MONGO_DB_KEY

#Base de datos local
#db_client = MongoClient().local

#Base de datos remota
db_client = MongoClient(MONGO_DB_KEY).test
