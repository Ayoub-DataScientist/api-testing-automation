"""
Base API Client with common methods for all API endpoints.
"""

import requests
from config import get_config
import logging

logger = logging.getLogger(__name__)


class BaseAPIClient:
    """Base class for all API clients."""

    def __init__(self, config=None):
        """Initialize the API client with configuration."""
        self.config = config or get_config()
        self.base_url = self.config.BASE_URL
        self.timeout = self.config.TIMEOUT
        self.verify_ssl = self.config.VERIFY_SSL
        self.session = requests.Session()

    def get(self, endpoint: str, params: dict = None, headers: dict = None):
        """Perform a GET request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        return self.session.get(
            url,
            params=params,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def post(self, endpoint: str, json: dict = None, data: dict = None, headers: dict = None):
        """Perform a POST request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        return self.session.post(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def put(self, endpoint: str, json: dict = None, data: dict = None, headers: dict = None):
        """Perform a PUT request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        return self.session.put(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def patch(self, endpoint: str, json: dict = None, data: dict = None, headers: dict = None):
        """Perform a PATCH request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        return self.session.patch(
            url,
            json=json,
            data=data,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def delete(self, endpoint: str, headers: dict = None):
        """Perform a DELETE request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        return self.session.delete(
            url,
            headers=headers,
            timeout=self.timeout,
            verify=self.verify_ssl,
        )

    def close(self):
        """Close the session."""
        self.session.close()
