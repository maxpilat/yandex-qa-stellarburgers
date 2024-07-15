import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_db():
    return Mock()
