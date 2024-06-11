#!/usr/bin/env python3
'''Module documentation'''


def list_all(mongo_collection):
    '''Lists all documents in a collection'''
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
    return documents
