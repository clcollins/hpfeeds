#!/usr/bin/python

import pymongo

import config


client = pymongo.MongoClient(host=config.MONGODB_HOST,
                             port=config.MONGODB_PORT)
for doc in client.hpfeeds.auth_key.find():
    print doc
