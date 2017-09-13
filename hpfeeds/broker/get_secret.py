import pymongo
import sys

import config

ident = sys.argv[1]
client = pymongo.MongoClient(host=config.MONGODB_HOST,
                             port=config.MONGODB_PORT)
results = client.hpfeeds.auth_key.find({'identifier': ident})
if results.count() > 0:
    print results[0]['secret']
