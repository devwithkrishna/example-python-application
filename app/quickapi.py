from fastapi import FastAPI
from app.logging_config import setup_logging
from app.data_model import UserColorEntry

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
# In-memory database (for demonstration purposes)
user_colour = []

@app.get("/")
async def root():
    """Default end point.Serves welcome message for the API"""
    logger.info("Root endpoint accessed")
    logger.info("Root endpoint was accessed!")

    return {"message": "Hello World"}

@app.get("/healthcheck")
async def healthcheck():
    """
    Healthcheck endpoint to verify if the service is running.
    """
    logger.info("Healthcheck endpoint accessed")
    return {"status": "ok"}

# Create an user_colour mapping
@app.post("/usercolour/", response_model=UserColorEntry)
async def create_item(item: UserColorEntry):
    """Create an item with a username and users favourite colour and return it."""
    user_colour.append(item)
    print(user_colour)
    # Sanitize log message to prevent log injection
    logger.info("New user-color entry added: username=%s, color=%s", item.username, item.color)
    return item

# List all user_colour mappings
@app.get("/allusercolour/")
async def get_all_user_colour():
    """Get all user_colour mappings."""
    logger.info("All user_colour mappings accessed")
    logger.info(user_colour)
    return user_colour
