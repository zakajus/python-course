"""
Script to load restaurants data from JSON file into MongoDB collection.

This script:
1. Connects to a MongoDB instance (Docker volume named "restaurants")
2. Reads the restaurants.json file
3. Creates a collection and inserts the restaurant data

Prerequisites:
- MongoDB running in Docker with volume named "restaurants"
- pymongo package installed: pip install pymongo

Usage:
    python load_restaurants_to_mongodb.py
"""

import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, BulkWriteError


def connect_to_mongodb(host='localhost', port=27017):
    """
    Connect to MongoDB instance.
    
    Args:
        host (str): MongoDB host address
        port (int): MongoDB port number
        
    Returns:
        MongoClient: MongoDB client connection
        
    Raises:
        ConnectionFailure: If unable to connect to MongoDB
    """
    try:
        client = MongoClient(host, port, serverSelectionTimeoutMS=5000)
        # Test the connection
        client.admin.command('ping')
        print(f"✓ Successfully connected to MongoDB at {host}:{port}")
        return client
    except ConnectionFailure as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        raise


def load_json_file(filepath):
    """
    Load restaurant data from JSON Lines file.
    
    Each line in the file should be a valid JSON object representing a restaurant.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of restaurant documents
    """
    restaurants = []
    print(f"\nReading data from {filepath}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    restaurant = json.loads(line.strip())
                    restaurants.append(restaurant)
                except json.JSONDecodeError as e:
                    print(f"Warning: Skipping line {line_number} due to JSON error: {e}")
                    
        print(f"✓ Successfully loaded {len(restaurants)} restaurants from file")
        return restaurants
    except FileNotFoundError:
        print(f"✗ Error: File not found: {filepath}")
        raise
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        raise


def create_collection(client, db_name='restaurants_db', collection_name='restaurants'):
    """
    Create or get a MongoDB collection.
    
    Args:
        client (MongoClient): MongoDB client connection
        db_name (str): Database name
        collection_name (str): Collection name
        
    Returns:
        Collection: MongoDB collection object
    """
    db = client[db_name]
    collection = db[collection_name]
    print(f"\n✓ Using database: '{db_name}', collection: '{collection_name}'")
    return collection


def insert_restaurants(collection, restaurants):
    """
    Insert restaurant documents into MongoDB collection.
    
    Args:
        collection (Collection): MongoDB collection
        restaurants (list): List of restaurant documents
        
    Returns:
        int: Number of documents inserted
    """
    print(f"\nInserting {len(restaurants)} restaurants into MongoDB...")
    
    try:
        # Clear existing data (optional - comment out if you want to keep existing data)
        existing_count = collection.count_documents({})
        if existing_count > 0:
            print(f"Warning: Collection already contains {existing_count} documents.")
            print("Clearing existing data...")
            collection.delete_many({})
        
        # Insert all documents
        result = collection.insert_many(restaurants)
        inserted_count = len(result.inserted_ids)
        print(f"✓ Successfully inserted {inserted_count} restaurants")
        return inserted_count
        
    except BulkWriteError as e:
        print(f"✗ Bulk write error: {e.details}")
        raise
    except Exception as e:
        print(f"✗ Error inserting documents: {e}")
        raise


def display_sample_data(collection, limit=3):
    """
    Display sample documents from the collection.
    
    Args:
        collection (Collection): MongoDB collection
        limit (int): Number of sample documents to display
    """
    print(f"\n--- Sample data (first {limit} restaurants) ---")
    for i, doc in enumerate(collection.find().limit(limit), 1):
        print(f"\n{i}. {doc.get('name', 'Unknown')}")
        print(f"   Cuisine: {doc.get('cuisine', 'N/A')}")
        print(f"   Borough: {doc.get('borough', 'N/A')}")
        print(f"   Restaurant ID: {doc.get('restaurant_id', 'N/A')}")


def main():
    """
    Main function to load restaurants data into MongoDB.
    """
    # Configuration
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    DATABASE_NAME = 'restaurants_db'
    COLLECTION_NAME = 'restaurants'
    JSON_FILE_PATH = 'restaurants.json'
    
    print("=" * 60)
    print("MongoDB Restaurant Data Loader")
    print("=" * 60)
    
    try:
        # Step 1: Connect to MongoDB
        client = connect_to_mongodb(MONGODB_HOST, MONGODB_PORT)
        
        # Step 2: Load data from JSON file
        restaurants = load_json_file(JSON_FILE_PATH)
        
        # Step 3: Create/get collection
        collection = create_collection(client, DATABASE_NAME, COLLECTION_NAME)
        
        # Step 4: Insert data
        inserted_count = insert_restaurants(collection, restaurants)
        
        # Step 5: Display sample data
        display_sample_data(collection)
        
        # Display statistics
        print("\n" + "=" * 60)
        print(f"✓ Data loading complete!")
        print(f"  Total documents in collection: {collection.count_documents({})}")
        print(f"  Database: {DATABASE_NAME}")
        print(f"  Collection: {COLLECTION_NAME}")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Script failed: {e}")
        return 1
    finally:
        # Close the connection
        if 'client' in locals():
            client.close()
            print("\n✓ MongoDB connection closed")
    
    return 0


if __name__ == "__main__":
    exit(main())
