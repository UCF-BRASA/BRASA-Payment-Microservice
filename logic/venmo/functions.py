
# general imports
import pymongo
from venmo_api import Client

# project imports
from util.constants import Keys


def load_client() -> Client:
    # loads the client with access token (DO NOT LOG OUT, UNLESS EXPLICITLY SAID TO)
    return Client(Keys.ACCESS_TOKEN)


def auth_user() -> bool:
    try:
        load_client()
        return True
    except:
        return False


def get_db_collection(collection_name):
    db_client = pymongo.MongoClient(
        Keys.DB_URI, connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1)
    db = db_client[Keys.DB_NAME]
    collection = db[collection_name]

    return collection


def get_most_recent_transaction(collection_name):
    return get_db_collection(collection_name).find().sort('$natural', -1).next()


def insert_venmo_trasactions(transactions):
    collection = get_db_collection(Keys.VENMO_COLECT)

    try:
        collection.insert_many(transactions)
        return True
    except:
        return False


def DELETE_ALL_VENMO_DB_INFO():
    collection = get_db_collection(Keys.VENMO_COLECT)
    collection.delete_many({})
