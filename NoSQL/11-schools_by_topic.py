#!/usr/bin/env python3
'''Module documentation'''


def schools_by_topic(mongo_collection, topic):
    '''Returns a list of school having specific topic'''
    result = mongo_collection.find(
        {'topics': topic}
    )
    return list(result)
