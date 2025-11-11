import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "product_catalog")
    CACHE_TTL: int = int(os.getenv("CACHE_TTL", 300))
    PORT: int = int(os.getenv("PORT", 8080))

settings = Settings()
