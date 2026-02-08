"""
Simple example: Load restaurants.json into MongoDB

This is a minimal example showing the basic steps.
For a more robust version with error handling, see load_restaurants_to_mongodb.py
"""

import json
from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient('localhost', 27017)

# 2. Select database and collection
db = client['restaurants_db']
collection = db['restaurants']

# 3. Load JSON data
print("Loading restaurants from file...")
restaurants = []
with open('restaurants.json', 'r') as file:
    for line in file:
        restaurants.append(json.loads(line))

print(f"Loaded {len(restaurants)} restaurants")

# 4. Clear existing data (optional)
collection.delete_many({})

# 5. Insert data into MongoDB
result = collection.insert_many(restaurants)
print(f"Inserted {len(result.inserted_ids)} documents")

# 6. Verify insertion
total = collection.count_documents({})
print(f"Total documents in collection: {total}")

# 7. Show sample data
print("\nSample restaurant:")
sample = collection.find_one()
print(f"Name: {sample['name']}")
print(f"Cuisine: {sample['cuisine']}")
print(f"Borough: {sample['borough']}")

# 8. Close connection
client.close()
