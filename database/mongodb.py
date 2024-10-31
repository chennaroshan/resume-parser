from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("mongodb://localhost:27017/jobx")  # e.g., "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGODB_URL)
db = client.your_database_name  # Replace with your database name

async def get_collection(collection_name):
    return db[collection_name]
