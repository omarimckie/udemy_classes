__author__ = 'naptime'

import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod   #not going to use self, going to always use this info
    def initialize():
        client = pymongo.MongoClient(Database.URI)   # enter the address into the mongoclient
        Database.DATABASE = client['fullstack']      # go to fullstack database

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
