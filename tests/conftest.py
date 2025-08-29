import sys
from pathlib import Path

import pytest
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).parent.parent))

from src.main import app
from src.api.dependencies import DatabaseDep


@pytest.fixture
def mock_db():
    return AsyncMock()


@pytest.fixture
def client(mock_db):
    app.dependency_overrides[DatabaseDep] = lambda: mock_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
