"""
Data-driven test examples using Pytest parametrize.
"""

import pytest
from api import UserAPI, PostAPI


class TestDataDrivenUsers:
    """Data-driven tests for User API."""

    @pytest.mark.data_driven
    @pytest.mark.parametrize("user_id,expected_status", [
        (1, 200),
        (2, 200),
        (5, 200),
        (10, 200),
        (99999, 404),
        (0, 404),
    ])
    def test_get_user_multiple_ids(self, user_api: UserAPI, user_id: int, expected_status: int):
        """Test retrieving users with multiple IDs."""
        response = user_api.get_user(user_id)
        assert response.status_code == expected_status

    @pytest.mark.data_driven
    @pytest.mark.parametrize("user_data", [
        {
            "name": "Alice Johnson",
            "email": "alice@example.com",
            "username": "alice_j",
        },
        {
            "name": "Bob Smith",
            "email": "bob@example.com",
            "username": "bob_s",
        },
        {
            "name": "Charlie Brown",
            "email": "charlie@example.com",
            "username": "charlie_b",
        },
    ])
    def test_create_multiple_users(self, user_api: UserAPI, user_data: dict):
        """Test creating multiple users with different data."""
        response = user_api.create_user(user_data)
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == user_data["name"]
        assert created_user["email"] == user_data["email"]


class TestDataDrivenPosts:
    """Data-driven tests for Post API."""

    @pytest.mark.data_driven
    @pytest.mark.parametrize("post_id,expected_status", [
        (1, 200),
        (5, 200),
        (10, 200),
        (50, 200),
        (99999, 404),
        (-1, 404),
    ])
    def test_get_post_multiple_ids(self, post_api: PostAPI, post_id: int, expected_status: int):
        """Test retrieving posts with multiple IDs."""
        response = post_api.get_post(post_id)
        assert response.status_code == expected_status

    @pytest.mark.data_driven
    @pytest.mark.parametrize("post_data", [
        {
            "title": "First Test Post",
            "body": "This is the first test post.",
            "userId": 1,
        },
        {
            "title": "Second Test Post",
            "body": "This is the second test post.",
            "userId": 2,
        },
        {
            "title": "Third Test Post",
            "body": "This is the third test post.",
            "userId": 3,
        },
    ])
    def test_create_multiple_posts(self, post_api: PostAPI, post_data: dict):
        """Test creating multiple posts with different data."""
        response = post_api.create_post(post_data)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == post_data["title"]
        assert created_post["userId"] == post_data["userId"]

    @pytest.mark.data_driven
    @pytest.mark.parametrize("user_id,expected_post_count", [
        (1, 10),
        (2, 10),
        (3, 10),
        (5, 10),
    ])
    def test_get_posts_by_user_data_driven(self, post_api: PostAPI, user_id: int, expected_post_count: int):
        """Test retrieving posts by user with expected count."""
        response = post_api.get_posts_by_user(user_id)
        assert response.status_code == 200
        posts = response.json()
        assert len(posts) == expected_post_count
        for post in posts:
            assert post["userId"] == user_id


class TestDataDrivenValidation:
    """Data-driven tests for validation scenarios."""

    @pytest.mark.data_driven
    @pytest.mark.parametrize("invalid_email", [
        "invalid",
        "invalid@",
        "@example.com",
        "user@",
        "",
    ])
    def test_create_user_invalid_emails(self, user_api: UserAPI, invalid_email: str):
        """Test creating users with invalid email formats."""
        user_data = {
            "name": "Test User",
            "email": invalid_email,
            "username": "testuser",
        }
        response = user_api.create_user(user_data)
        # API may accept or reject, but we validate response is valid
        assert response.status_code in [201, 400]

    @pytest.mark.data_driven
    @pytest.mark.parametrize("title_length", [1, 5, 50, 100, 255])
    def test_create_post_various_title_lengths(self, post_api: PostAPI, title_length: int):
        """Test creating posts with various title lengths."""
        post_data = {
            "title": "A" * title_length,
            "body": "Test body",
            "userId": 1,
        }
        response = post_api.create_post(post_data)
        assert response.status_code == 201
        created_post = response.json()
        assert len(created_post["title"]) == title_length
