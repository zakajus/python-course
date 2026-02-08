# MongoDB Restaurants Data Loader

This directory contains a Python script to load restaurant data from `restaurants.json` into a MongoDB collection.

## Files

- `restaurants.json` - Restaurant data in JSON Lines format (one JSON object per line)
- `load_restaurants_to_mongodb.py` - Python script to load data into MongoDB
- `README.md` - This file

## Prerequisites

### 1. Install Python Dependencies

```bash
pip install pymongo
```

### 2. Set up MongoDB with Docker

If you don't have MongoDB running yet, you can start it with Docker:

```bash
# Create a Docker volume named "restaurants"
docker volume create restaurants

# Run MongoDB container with the volume
docker run -d \
  --name mongodb \
  -p 27017:27017 \
  -v restaurants:/data/db \
  mongo:latest
```

To verify MongoDB is running:
```bash
docker ps | grep mongodb
```

## Usage

### Basic Usage

Navigate to this directory and run the script:

```bash
cd nd/2
python load_restaurants_to_mongodb.py
```

The script will:
1. Connect to MongoDB at `localhost:27017`
2. Read all restaurants from `restaurants.json`
3. Create a database named `restaurants_db` (if it doesn't exist)
4. Create a collection named `restaurants` (if it doesn't exist)
5. Insert all restaurant documents into the collection
6. Display a sample of the inserted data

### Configuration

You can modify these variables in the script's `main()` function:

- `MONGODB_HOST` - MongoDB server address (default: `localhost`)
- `MONGODB_PORT` - MongoDB port (default: `27017`)
- `DATABASE_NAME` - Name of the database (default: `restaurants_db`)
- `COLLECTION_NAME` - Name of the collection (default: `restaurants`)
- `JSON_FILE_PATH` - Path to the JSON file (default: `restaurants.json`)

### Example: Different MongoDB Host

If your MongoDB is running on a different host or port:

```python
MONGODB_HOST = '192.168.1.100'
MONGODB_PORT = 27018
```

## Data Format

The `restaurants.json` file contains restaurant data in JSON Lines format. Each line is a separate JSON object with this structure:

```json
{
  "address": {
    "building": "1007",
    "coord": [-73.856077, 40.848447],
    "street": "Morris Park Ave",
    "zipcode": "10462"
  },
  "borough": "Bronx",
  "cuisine": "Bakery",
  "grades": [
    {"date": {"$date": 1393804800000}, "grade": "A", "score": 2}
  ],
  "name": "Morris Park Bake Shop",
  "restaurant_id": "30075445"
}
```

## Querying the Data

After loading the data, you can query it using MongoDB shell or Python:

### MongoDB Shell

```bash
# Connect to MongoDB
docker exec -it mongodb mongosh

# Switch to database
use restaurants_db

# Count documents
db.restaurants.countDocuments()

# Find restaurants in Manhattan
db.restaurants.find({"borough": "Manhattan"}).limit(5)

# Find Italian restaurants
db.restaurants.find({"cuisine": "Italian"})
```

### Python

```python
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['restaurants_db']
collection = db['restaurants']

# Find all restaurants in Brooklyn
brooklyn_restaurants = collection.find({"borough": "Brooklyn"})

# Find restaurants with grade A
grade_a_restaurants = collection.find({"grades.grade": "A"})

# Count restaurants by cuisine
from collections import Counter
cuisines = [doc['cuisine'] for doc in collection.find({}, {'cuisine': 1})]
print(Counter(cuisines).most_common(10))
```

## Troubleshooting

### Cannot connect to MongoDB

**Error:** `Failed to connect to MongoDB`

**Solution:** 
- Ensure MongoDB is running: `docker ps | grep mongodb`
- Check if port 27017 is accessible: `telnet localhost 27017`
- Verify MongoDB is listening on the correct port

### File not found error

**Error:** `File not found: restaurants.json`

**Solution:**
- Ensure you're running the script from the `nd/2` directory
- Or provide the full path to the JSON file in the configuration

### JSON decode error

**Error:** `JSON decode error`

**Solution:**
- The file may be corrupted
- Ensure the file is in JSON Lines format (one JSON object per line)

## Docker Commands Reference

```bash
# Stop MongoDB
docker stop mongodb

# Start MongoDB
docker start mongodb

# Remove MongoDB container
docker rm mongodb

# Remove volume (WARNING: This deletes all data)
docker volume rm restaurants

# View MongoDB logs
docker logs mongodb

# Access MongoDB shell
docker exec -it mongodb mongosh
```

## Notes

- The script clears existing data in the collection before inserting new data. Comment out the `collection.delete_many({})` line if you want to keep existing data.
- Large files may take some time to load. The script displays progress information.
- Make sure you have sufficient disk space for the MongoDB volume.
