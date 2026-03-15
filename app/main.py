import logging
from fastapi import FastAPI, Request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

request_count = 0

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

@app.get("/")
def read_root():
    global request_count
    request_count += 1
    logger.info("Root endpoint accessed")
    return {"message": "DevOps monitoring project is running"}

@app.get("/health")
def health_check():
    global request_count
    request_count += 1
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}

@app.get("/metrics")
def metrics():
    logger.info("Metrics endpoint accessed")
    return {"requests_total": request_count}