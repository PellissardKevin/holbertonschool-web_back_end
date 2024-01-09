#!/usr/bin/env python3
"""Script to changes all topics of a document"""


def update_topics(mongo_collection, name, topics):
    """Method to change topics in document"""

    return mongo_collection.update_many({"name": name},
    {"$set": {"name": topics}})
