import logging
import socket
from fastapi import FastAPI, Response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello from ECS Fargate. Checking the deployment pipeline test",
        "host": socket.gethostname()
    }

@app.get("/error", status_code=500)
def error():
    logger.error("simulated failure")
    return Response(
        content="boom",
        status_code=500,
        media_type="text/plain",
    )

@app.get("/health")
def health():
    return {"status": "healthy"}
