"""
Creating insert and fetch functions for mongo testing
"""

import os
from pymongo import MongoClient
import arrow

# Setting up mongo client
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "test_inputs"
db = client.test_inputs
# Using collection "test_lists"
collection = db.test_lists

TIME1 = "2023-07-01T00:00"


def insert_attempt(begin_time, brevet_dist, rows):

    output = collection.insert_one({
        "begin_time": begin_time,
        "brevet_dist": brevet_dist,
        "rows": rows
        })

    _id = output.inserted_id
    return str(_id)

def fetch_attempt():
    inputs = collection.find().sort("_id", -1).limit(1)

    for value in inputs:
        return value["begin_time"], value['brevet_dist'], value['rows']


