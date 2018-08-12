#!/usr/bin/env python3

import argparse
import json
from pymongo import MongoClient

parser = argparse.ArgumentParser(description='Insert JSON object from file into a named Mongo database and collection.')
parser.add_argument('-s', '--server', nargs=1, help='Mongo server URL')
parser.add_argument('database', nargs=1, help='database name')
parser.add_argument('collection', nargs=1, help='collection name')
parser.add_argument('datafile', nargs=1, help='datafile name - this file must contains a JSON map')

args = parser.parse_args()

if args.server is None:
    client = MongoClient()
else:
    client = MongoClient(args.server)

database = client[args.database[0]]

with open(args.datafile[0]) as data_file:
    data = json.load(data_file)

    collection = database[args.collection[0]]
    inserted_id = collection.insert_one(data).inserted_id
    print('Inserted data and got id {}'.format(inserted_id))
