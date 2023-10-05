from pymongo import errors, MongoClient
from constants import MONGO_URL, DATABASE_NAME, COLLECTION_NAME

print("Attempting to Connect:", MONGO_URL)
try:
    client = MongoClient(MONGO_URL)
    print("Connected to MongoDB successfully!")

    database = client[DATABASE_NAME]
    collection = database[COLLECTION_NAME]
    documents = collection.find({}, {}).sort("orderFromSun", 1)  # 1 for ascending order
    planets = []
    for document in documents:
        planets.append(document)

    print(planets)

except errors.ConnectionFailure as e:
    print("Could not connect to MongoDB:", e)
    exit(1)




