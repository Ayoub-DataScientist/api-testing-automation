"""
Pytest configuration and fixtures for API tests.
"""

import pytest
import logging
from api import UserAPI, PostAPI, CommentAPI
from config import get_config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    """Add custom command-line options."""
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against: dev, staging, or prod",
    )


@pytest.fixture(scope="session")
def config(request):
    """Provide configuration based on environment."""
    env = request.config.getoption("--env")
    return get_config(env)


@pytest.fixture
def user_api(config):
    """Provide a UserAPI instance."""
    api = UserAPI(config)
    yield api
    api.close()


@pytest.fixture
def post_api(config):
    """Provide a PostAPI instance."""
    api = PostAPI(config)
    yield api
    api.close()


@pytest.fixture
def comment_api(config):
    """Provide a CommentAPI instance."""
    api = CommentAPI(config)
    yield api
    api.close()


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "smoke: Smoke tests for critical paths")
    config.addinivalue_line("markers", "regression: Full regression test suite")
    config.addinivalue_line("markers", "positive: Positive test cases")
    config.addinivalue_line("markers", "negative: Negative test cases")
    config.addinivalue_line("markers", "data_driven: Data-driven test cases")
