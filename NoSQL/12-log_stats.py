#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    count = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{count} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    check = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{check} status check")
