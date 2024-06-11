#!/usr/bin/env python3
'''Module documentation'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a school document'''
    result = mongo_collection.update(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return result
