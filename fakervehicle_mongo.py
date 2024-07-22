#pip install pymongo faker

import time
import signal
import sys
from faker import Faker
from faker_vehicle import VehicleProvider
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import random


# Initialize Faker and MongoDB client
fake = Faker()
fake.add_provider(VehicleProvider)

#client = MongoClient('localhost', 27017)  # Adjust the host and port as needed

client = MongoClient(
            host='localhost',
            port=27017,
            username='admin',
            password='admin123'            
        )
db = client['test']  # Adjust the database name as needed
collection = db['vehicle']  # Adjust the collection name as needed

# Function to handle interrupt signal
def signal_handler(sig, frame):
    print('Interrupt received, stopping the script...')
    sys.exit(0)

# Register the interrupt signal handler
signal.signal(signal.SIGINT, signal_handler)

# Function to generate fake data
def generate_fake_data():
    return {
        'vehicle_number':''.join(random.choice('01234ABCD') for i in range(8)),
        'makeYear':fake.vehicle_year(),
        'model':fake.vehicle_model(),
        'make':fake.vehicle_make(),
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'text': fake.text(),
        'created_at': fake.date_time()
    }

# Main loop to generate and insert data
while True:
    try:
        # Generate fake data
        data = generate_fake_data()
        print(f"Inserting data: {data}")
        
        # Insert the data into MongoDB
        collection.insert_one(data)
        
        # Sleep for 5 seconds
        time.sleep(5)
    except ConnectionFailure:
        print("Failed to connect to MongoDB, please check your connection.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")



