from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local

#Base de datos remota
db_client = MongoClient("mongodb+srv://FrancoCirielli16:Franco2002@usercryptoscoin.gxkjmvk.mongodb.net/?retryWrites=true&w=majority").test
