import pytest
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient
from datetime import datetime
from src.main import app
from src.api.dependencies import DatabaseDep


@pytest.fixture
def mock_db():
    db = AsyncMock()
    db.questions = AsyncMock()
    db.commit = AsyncMock()
    return db


@pytest.fixture
def client(mock_db):
    app.dependency_overrides[DatabaseDep] = lambda: mock_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


TEST_QUESTION_DATA = {"text": "Test question text"}
TEST_QUESTION_ID = 1
TEST_QUESTION = {
    "id": TEST_QUESTION_ID,
    "text": "Test question",
    "created_at": datetime.now().isoformat(),
}


class TestQuestionsAPI:
    @pytest.mark.asyncio
    async def test_create_question_validation_error(self, client):
        """Тест ошибки валидации при создании вопроса"""
        # Act
        response = client.post("/questions/", json={"invalid_field": "test"})

        # Assert
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_get_question_by_id_invalid_id(self, client):
        """Тест получения вопроса с невалидным ID"""
        # Act
        response = client.get("/questions/invalid_id")

        # Assert
        assert response.status_code == 422

    @pytest.mark.asyncio
    async def test_delete_question_invalid_id(self, client):
        """Тест удаления вопроса с невалидным ID"""
        # Act
        response = client.delete("/questions/invalid_id")

        # Assert
        assert response.status_code == 422
