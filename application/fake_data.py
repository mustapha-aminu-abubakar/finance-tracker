import pymongo
import random
from faker import Faker # type: ignore
uri = "mongodb://localhost:27017"

mongodb_client = pymongo.MongoClient(uri)
db = mongodb_client.fundamental

def add_fake_data(size = 8):
    fake = Faker()


    data = [{
                "amount": round(fake.random.uniform(5, 5000),2),
                "description": fake.paragraph(),
                "type": random.choice(["income", "expense"]),
                "source": fake.name(),
                "beneficiary": random.choice([fake.name(), fake.company()]),
                "date": fake.date_time_this_year()
            }
            for _ in range(size)]
    print(data)
    db.finances.insert_many(data)

add_fake_data()
