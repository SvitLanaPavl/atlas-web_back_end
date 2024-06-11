#!/usr/bin/env python3
'''Module documentation'''
from pymongo import MongoClient


def log_stats():
    '''Stats about Nginx logs stored in MongoDB'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.Nginx
    total_logs = collection.count({})
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')
    for method in methods:
        count = collection.count({'method': method})
        print(f'method {method}: {count}')
    status_check = collection.count({'method': 'GET', 'path': '/status'})
    print(f'{status_check} status check')
