import logging
import time

from fastapi import FastAPI, HTTPException, Request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from starlette.responses import Response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="DevOps Monitoring Project")

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint", "status_code"]
)

REQUEST_LATENCY = Histogram(
    "app_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "endpoint"]
)


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()
    endpoint = request.url.path

    response = await call_next(request)

    duration = time.time() - start_time

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint,
        status_code=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=endpoint
    ).observe(duration)

    logger.info(
        f"{request.method} {endpoint} - {response.status_code} - {duration:.4f}s"
    )
    return response


@app.get("/")
def read_root():
    return {"message": "DevOps monitoring project is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/error")
def error():
    raise HTTPException(status_code=500, detail="Simulated error")


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)