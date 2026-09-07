import pytest
from fastapi.testclient import TestClient
from main import app, get_db


# 1. Define your safe, isolated test dependency
def get_test_db():
    # db = SetupTestDatabase()
    db = "DB Connection"
    try:
        yield db
    finally:
        # db.cleanup()
        print("Closing DB")


# 2. Use a Pytest fixture to manage the override lifecycle
@pytest.fixture
def client():
    # Setup: Apply the override
    app.dependency_overrides[get_db] = get_test_db

    # Pause and hand the TestClient to the specific test
    yield TestClient(app)

    # Teardown: This is GUARANTEED to run after the test finishes.
    # We completely wipe the dictionary to prevent state leaks.
    app.dependency_overrides = {}
