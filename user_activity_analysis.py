# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['ecommerce']
mongo_activity = mongo_db['user_activity']

# Aggregate user activities
pipeline = [
    {"$group": {"_id": "$user_id", "activity_count": {"$sum": 1}}},
    {"$sort": {"activity_count": -1}}
]
activity_data = mongo_activity.aggregate(pipeline)

# Print results
for record in activity_data:
    print(f"User ID: {record['_id']}, Activity Count: {record['activity_count']}")

# Close connection
mongo_client.close()
