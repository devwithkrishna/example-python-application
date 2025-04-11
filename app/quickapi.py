from fastapi import FastAPI
# from pylogs import get_logger
from logging_config import setup_logging

# Setup logging
logger = setup_logging()

# Initialize logger
# logger = get_logger("myapp")
logger.info("Logger initialized successfully")

# Fast API app initialization
app = FastAPI(
    title="Favorite Colors API",
    description="Submit your name and favorite color",
    version="1.0.0"
)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    # logger = logging.getLogger("myapp")
    logger.info("Root endpoint was accessed!")

    return {"message": "Hello World"}

@app.get("/healthcheck")
async def healthcheck():
    """
    Healthcheck endpoint to verify if the service is running.
    """
    logger.info("Healthcheck endpoint accessed")
    return {"status": "ok"}

# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     logger = logging.getLogger("myapp")
#     logger.info(f"Received request: {request.method} {request.url}")
#     response = await call_next(request)
#     logger.info(f"Response status: {response.status_code}")
#     return response


