#!/usr/bin/env python3

import argparse
import json
from pymongo import MongoClient

parser = argparse.ArgumentParser(description='Insert JSON object from file into a named Mongo database and collection.')
parser.add_argument('-s', '--server', nargs=1, help='Mongo server URL')
parser.add_argument('database', nargs=1, help='database name')
parser.add_argument('collection', nargs=1, help='collection name')

args = parser.parse_args()

if args.server is None:
    client = MongoClient()
else:
    client = MongoClient(args.server)

database = client[args.database[0]]

collection = database[args.collection[0]]
collection.delete_many({"name": "Dave Donaghy"})
