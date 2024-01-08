#!/usr/bin/env python3
"""script to list all documents in fonction"""


def list_all(mongo_collection):
    """Method to list all"""
    dic = []
    if mongo_collection.find_one():
        dic.append(mongo_collection.find_one())

    return dic
