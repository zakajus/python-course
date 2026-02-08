"""
Example queries and operations on the restaurants collection.

This script demonstrates various MongoDB queries you can perform
on the restaurants collection after loading the data.

Prerequisites:
- MongoDB running with restaurants collection loaded
- Run load_restaurants_to_mongodb.py first to load the data
"""

from pymongo import MongoClient
from collections import Counter


def connect_to_db():
    """Connect to MongoDB and return the restaurants collection."""
    client = MongoClient('localhost', 27017)
    db = client['restaurants_db']
    collection = db['restaurants']
    return client, collection


def example_queries(collection):
    """Demonstrate various MongoDB queries."""
    
    print("=" * 60)
    print("Example MongoDB Queries on Restaurants Collection")
    print("=" * 60)
    
    # 1. Count total documents
    total = collection.count_documents({})
    print(f"\n1. Total restaurants in database: {total}")
    
    # 2. Find restaurants by borough
    manhattan_count = collection.count_documents({"borough": "Manhattan"})
    print(f"\n2. Restaurants in Manhattan: {manhattan_count}")
    
    # 3. Find restaurants by cuisine
    print("\n3. Italian restaurants (first 3):")
    for i, restaurant in enumerate(collection.find({"cuisine": "Italian"}).limit(3), 1):
        print(f"   {i}. {restaurant['name']} - {restaurant['address']['street']}")
    
    # 4. Count restaurants by borough
    print("\n4. Restaurants by borough:")
    for borough in ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"]:
        count = collection.count_documents({"borough": borough})
        print(f"   {borough}: {count}")
    
    # 5. Find restaurants with specific grade
    grade_a_count = collection.count_documents({"grades.grade": "A"})
    print(f"\n5. Restaurants with at least one 'A' grade: {grade_a_count}")
    
    # 6. Find restaurants by zipcode
    print("\n6. Restaurants in zipcode 10003 (first 3):")
    for i, restaurant in enumerate(collection.find({"address.zipcode": "10003"}).limit(3), 1):
        print(f"   {i}. {restaurant['name']} ({restaurant['cuisine']})")
    
    # 7. Most common cuisines
    print("\n7. Top 10 cuisines:")
    cuisines = [doc['cuisine'] for doc in collection.find({}, {'cuisine': 1, '_id': 0})]
    for i, (cuisine, count) in enumerate(Counter(cuisines).most_common(10), 1):
        print(f"   {i}. {cuisine}: {count} restaurants")
    
    # 8. Find restaurants with coordinates (location-based)
    print("\n8. Sample restaurant with coordinates:")
    restaurant = collection.find_one({"address.coord": {"$exists": True}})
    if restaurant:
        print(f"   Name: {restaurant['name']}")
        print(f"   Coordinates: {restaurant['address']['coord']}")
        print(f"   Location: {restaurant['address']['street']}, {restaurant['borough']}")
    
    # 9. Find restaurants by name (case-insensitive search)
    search_term = "pizza"
    print(f"\n9. Restaurants with '{search_term}' in name (first 5):")
    regex_query = {"name": {"$regex": search_term, "$options": "i"}}
    for i, restaurant in enumerate(collection.find(regex_query).limit(5), 1):
        print(f"   {i}. {restaurant['name']} - {restaurant['cuisine']}")
    
    # 10. Aggregate: Average score by cuisine (sample)
    print("\n10. Aggregation example - restaurants by cuisine (top 5):")
    pipeline = [
        {"$group": {
            "_id": "$cuisine",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}},
        {"$limit": 5}
    ]
    for i, result in enumerate(collection.aggregate(pipeline), 1):
        print(f"    {i}. {result['_id']}: {result['count']} restaurants")


def example_updates(collection):
    """Demonstrate update operations."""
    
    print("\n" + "=" * 60)
    print("Example Update Operations")
    print("=" * 60)
    
    # Example 1: Update a single document
    print("\n1. Update operation example (would update one restaurant):")
    print("   Code: collection.update_one(")
    print("       {'name': 'Restaurant Name'},")
    print("       {'$set': {'verified': True}}")
    print("   )")
    
    # Example 2: Update multiple documents
    print("\n2. Bulk update example (would add field to all Manhattan restaurants):")
    print("   Code: collection.update_many(")
    print("       {'borough': 'Manhattan'},")
    print("       {'$set': {'premium_area': True}}")
    print("   )")


def example_inserts(collection):
    """Demonstrate insert operations."""
    
    print("\n" + "=" * 60)
    print("Example Insert Operations")
    print("=" * 60)
    
    print("\n1. Insert a single restaurant:")
    print("   Code:")
    print("   new_restaurant = {")
    print("       'name': 'New Restaurant',")
    print("       'borough': 'Manhattan',")
    print("       'cuisine': 'American',")
    print("       'address': {")
    print("           'street': '123 Main St',")
    print("           'zipcode': '10001'")
    print("       }")
    print("   }")
    print("   result = collection.insert_one(new_restaurant)")


def example_deletes(collection):
    """Demonstrate delete operations."""
    
    print("\n" + "=" * 60)
    print("Example Delete Operations")
    print("=" * 60)
    
    print("\n1. Delete restaurants by criteria:")
    print("   Code: collection.delete_many({'borough': 'Test Borough'})")
    
    print("\n2. Delete a single document:")
    print("   Code: collection.delete_one({'_id': object_id})")


def main():
    """Main function."""
    try:
        client, collection = connect_to_db()
        
        # Run example queries
        example_queries(collection)
        
        # Show examples of other operations (not executed)
        example_updates(collection)
        example_inserts(collection)
        example_deletes(collection)
        
        print("\n" + "=" * 60)
        print("Examples complete!")
        print("=" * 60)
        print("\nNote: Update, insert, and delete examples are shown as code")
        print("snippets but not executed to preserve your data.")
        print("\nTo learn more about MongoDB queries, visit:")
        print("https://www.mongodb.com/docs/manual/tutorial/query-documents/")
        
        client.close()
        
    except Exception as e:
        print(f"\nError: {e}")
        print("\nMake sure MongoDB is running and data is loaded.")
        print("Run 'python load_restaurants_to_mongodb.py' first.")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
