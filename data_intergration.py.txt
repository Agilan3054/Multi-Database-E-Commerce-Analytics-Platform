import psycopg2
from pymongo import MongoClient

# Connect to Postgres
pg_conn = psycopg2.connect(
    dbname='ecommerce_db',
    user='user',
    password='password',
    host='localhost',
    port='5432'
)
pg_cursor = pg_conn.cursor()

# Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['ecommerce']
mongo_users = mongo_db['users']
mongo_products = mongo_db['products']

# Example function to fetch data from Postgres and insert into MongoDB
def integrate_data():
    # Fetch users from Postgres
    pg_cursor.execute("SELECT id, name, email FROM users")
    users = pg_cursor.fetchall()

    # Insert users into MongoDB
    for user in users:
        mongo_users.update_one(
            {"_id": user[0]},
            {"$set": {"name": user[1], "email": user[2]}},
            upsert=True
        )

    # Fetch products from Postgres
    pg_cursor.execute("SELECT id, name, price, stock FROM products")
    products = pg_cursor.fetchall()

    # Insert products into MongoDB
    for product in products:
        mongo_products.update_one(
            {"_id": product[0]},
            {"$set": {"name": product[1], "price": product[2], "stock": product[3]}},
            upsert=True
        )

# Run integration
integrate_data()

# Close connections
pg_cursor.close()
pg_conn.close()
mongo_client.close()
