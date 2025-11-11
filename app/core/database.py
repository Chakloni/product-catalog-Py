from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.DB_NAME]
collection = db["products"]

def health_check():
    try:
        client.admin.command("ping")
        return True
    except Exception:
        return False
