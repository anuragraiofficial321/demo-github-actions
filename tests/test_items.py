import sys
import os
import pytest_asyncio

# Add the root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

import pytest
from httpx import AsyncClient
from app.main import app  # Import your FastAPI app

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8000") as ac:
        yield ac

# Test cases
@pytest.mark.asyncio
async def test_create_item(client: AsyncClient):
    # Test creating a new item
    response = await client.post(
        "/api/v1/items/",
        json={
  "name": "string",
  "description": "string",
  "id": "string",
  "llm_response": "string"
}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Anurag"
    assert data["description"] == "A test item"