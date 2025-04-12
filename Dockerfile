# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration files to the container
COPY pyproject.toml  /app/

# Copy the README.md file to the container
COPY README.md /app/

# Install Poetry
RUN pip install poetry

# Install the application dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Copy the application code to the container
COPY app /app/app

# Expose the port that the FastAPI application will run on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "app.quickapi:app", "--host", "0.0.0.0", "--port", "8000"]