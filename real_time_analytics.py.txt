from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['ecommerce']
mongo_orders = mongo_db['orders']

# Query data
pipeline = [
    {"$group": {"_id": "$product_id", "total_sales": {"$sum": "$quantity"}}},
    {"$sort": {"total_sales": -1}}
]
sales_data = mongo_orders.aggregate(pipeline)

# Convert to DataFrame for plotting
df = pd.DataFrame(list(sales_data))
df.set_index('_id', inplace=True)
df.plot(kind='bar', legend=False)
plt.title('Real-Time Sales Analysis')
plt.xlabel('Product ID')
plt.ylabel('Total Sales')
plt.show()

# Close connection
mongo_client.close()
