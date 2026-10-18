# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating routes, handling HTTP requests, and validating input for a small application.

## 📝 Tasks

### 🛠️ Create a FastAPI application

#### Description
Set up a basic FastAPI project and create a working web API that responds to HTTP requests.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app instance.
- Create a health check endpoint such as `GET /health`.
- Return a JSON response like `{"status": "ok"}`.
- Run the app locally using a development server.

### 🛠️ Add CRUD endpoints

#### Description
Build a small API for managing items such as tasks, books, or products.

#### Requirements
Completed program should:

- Create a list of sample items in memory.
- Add a `GET /items` endpoint to return all items.
- Add a `POST /items` endpoint to create a new item.
- Add a `GET /items/{item_id}` endpoint to fetch one item.
- Add a `PUT /items/{item_id}` endpoint to update an item.
- Add a `DELETE /items/{item_id}` endpoint to remove an item.

### 🛠️ Validate input and handle errors

#### Description
Improve the API by validating incoming data and returning clear responses when something goes wrong.

#### Requirements
Completed program should:

- Use Pydantic models to define the expected request data.
- Ensure required fields are present and values match the expected type.
- Return a 404 response when an item does not exist.
- Return appropriate validation errors for invalid input.
- Keep the API responses consistent and easy to understand.

Example request:

```python
{
  "name": "Write API notes",
  "completed": false
}
```

Example response:

```json
{
  "id": 1,
  "name": "Write API notes",
  "completed": false
}
```
