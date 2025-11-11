from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from app.routes.routes import router
from app.core.database import health_check
from app.core.cache import get_cache
import uvicorn
import time

app = FastAPI(title="Product Catalog API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware)

app.include_router(router, prefix="/v1")

@app.get("/health")
def health():
    ok = health_check()
    return {
        "status": "healthy" if ok else "unhealthy",
        "cache_size": len(get_cache()),
        "timestamp": time.time(),
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
