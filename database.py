from pymongo import MongoClient
import certifi

mongo_uri= "mongodb://localhost:27017/tienda_simple2334430586"

ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(mongo_uri, tlsCAFile=ca)
        db = client["tienda_simple"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
