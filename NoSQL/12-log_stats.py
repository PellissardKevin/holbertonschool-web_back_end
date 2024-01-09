#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['logs']
collection = db['nginx']
collection = client.logs.nginx
count = collection.count_documents({})
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(f"{count} logs")

# Count documents for method
print("Methods:")
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")


# Count documents with method=GET and path=/status
count_status = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count_status} status check")

# Close MongoDB connection
client.close()
