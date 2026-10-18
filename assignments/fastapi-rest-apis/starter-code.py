from fastapi import FastAPI

app = FastAPI(title="Task API")

# In-memory storage for tasks
items = [
    {"id": 1, "name": "Learn FastAPI", "completed": False},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add CRUD endpoints for reading, creating, updating, and deleting items.
# TODO: Add request validation using Pydantic models.
# TODO: Return helpful errors for missing items.
