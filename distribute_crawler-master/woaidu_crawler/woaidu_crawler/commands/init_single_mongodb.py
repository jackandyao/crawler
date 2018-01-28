#!/usr/bin/python
#-*-coding:utf-8-*-


import pymongo
import types


DATABASE_NAME = "books_fs"
client = None
DATABASE_HOST = "localhost"
DATABASE_PORT = 27017
INDEX = {\
            #collection
            'book_detail':\
                {\
                    (('book_name',pymongo.ASCENDING),('author',pymongo.ASCENDING)):{'name':'book_name_author','unique':True},
                    'book_name':{'name':'book_name'},
                    'author':{'name':'author'},
                    'alias_name':{'name':'alias_name'},
                }\
        }

def drop_database(name_or_database):
    if name_or_database and client:
        client.drop_database(name_or_database)

def create_index():

    for k,v in INDEX.items():
        for key,kwargs in v.items():
            client[DATABASE_NAME][k].ensure_index(list(key) if type(key)==types.TupleType else key,**kwargs)

if __name__ == "__main__":
    client = pymongo.MongoClient(DATABASE_HOST,DATABASE_PORT)
    drop_database(DATABASE_NAME)
    create_index() 
