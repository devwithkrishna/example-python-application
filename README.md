# Example Python Application

This is a sample Python application built using **FastAPI**. The application allows users to submit their name and favorite color, and provides endpoints to retrieve the submitted data. It also includes logging functionality with JSON formatting.

## Features

- **FastAPI** for building RESTful APIs.
- **Pydantic** for data validation and serialization.
- **Logging** with JSON formatting using `python-json-logger`.
- In-memory storage for demonstration purposes.

## Endpoints

### Root Endpoint
- **GET** `/`
  - Returns a welcome message.

### Healthcheck
- **GET** `/healthcheck`
  - Verifies if the service is running.

### Submit User Color
- **POST** `/usercolour/`
  - Accepts a user's name and favorite color.
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "favorite_color": "Blue"
    }
    ```
  - **Response**:
    ```json
    {
      "name": "John Doe",
      "favorite_color": "Blue"
    }
    ```

### Get All User Colors
- **GET** `/allusercolour/`
  - Returns all submitted user-color mappings.

## Installation

* Clone the repository:
   ```bash
   git clone https://github.com/githubofkrishnadhas/example-python-application.git
   cd example-python-application
  ```
   
* Install dependencies using Poetry:

```
poetry install
```

Run the application:

```    
poetry run uvicorn app.quickapi:app --reload
```
Access the API documentation at http://127.0.0.1:8000/docs.

## Project Structure
```yaml
example-python-application/
├── app/
│   ├── data_model.py         # Defines the Pydantic models
│   ├── logging_config.py     # Configures logging for the application
│   ├── quickapi.py           # Main FastAPI application
├── README.md                 # Project documentation
├── pyproject.toml            # Poetry configuration
```

## Dependencies
* Python: 3.11+
* FastAPI: For building APIs.
* Uvicorn: ASGI server for running the application.
* Pydantic: Data validation and settings management.
* python-json-logger: JSON formatting for logs.