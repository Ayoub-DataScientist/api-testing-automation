"""
Tests for User API endpoints.
"""

import pytest
from api import UserAPI


class TestUsersAPI:
    """Test suite for User API endpoints."""

    @pytest.mark.smoke
    def test_get_all_users(self, user_api: UserAPI):
        """Test retrieving all users."""
        response = user_api.get_all_users()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    @pytest.mark.smoke
    def test_get_user_by_id(self, user_api: UserAPI):
        """Test retrieving a user by ID."""
        response = user_api.get_user(1)
        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert "name" in user
        assert "email" in user

    @pytest.mark.positive
    def test_create_user(self, user_api: UserAPI):
        """Test creating a new user."""
        user_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "username": "johndoe",
        }
        response = user_api.create_user(user_data)
        assert response.status_code == 201
        created_user = response.json()
        assert created_user["name"] == "John Doe"
        assert created_user["email"] == "john@example.com"

    @pytest.mark.positive
    def test_update_user(self, user_api: UserAPI):
        """Test updating a user."""
        user_data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
        }
        response = user_api.update_user(1, user_data)
        assert response.status_code == 200
        updated_user = response.json()
        assert updated_user["name"] == "Jane Doe"

    @pytest.mark.positive
    def test_delete_user(self, user_api: UserAPI):
        """Test deleting a user."""
        response = user_api.delete_user(1)
        assert response.status_code == 200

    @pytest.mark.negative
    def test_get_nonexistent_user(self, user_api: UserAPI):
        """Test retrieving a non-existent user."""
        response = user_api.get_user(99999)
        assert response.status_code == 404

    @pytest.mark.negative
    def test_create_user_missing_name(self, user_api: UserAPI):
        """Test creating a user without a name."""
        user_data = {
            "email": "test@example.com",
            "username": "testuser",
        }
        response = user_api.create_user(user_data)
        # API may accept this, but we validate the response
        assert response.status_code in [201, 400]

    @pytest.mark.regression
    def test_get_user_posts(self, user_api: UserAPI):
        """Test retrieving posts by a user."""
        response = user_api.get_user_posts(1)
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)

    @pytest.mark.regression
    def test_get_user_comments(self, user_api: UserAPI):
        """Test retrieving comments by a user."""
        response = user_api.get_user_comments(1)
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)

    @pytest.mark.regression
    def test_get_user_todos(self, user_api: UserAPI):
        """Test retrieving todos by a user."""
        response = user_api.get_user_todos(1)
        assert response.status_code == 200
        todos = response.json()
        assert isinstance(todos, list)

    @pytest.mark.regression
    def test_patch_user(self, user_api: UserAPI):
        """Test partially updating a user."""
        user_data = {"name": "Patched User"}
        response = user_api.patch_user(1, user_data)
        assert response.status_code == 200
        patched_user = response.json()
        assert patched_user["name"] == "Patched User"

    @pytest.mark.negative
    def test_update_nonexistent_user(self, user_api: UserAPI):
        """Test updating a non-existent user."""
        user_data = {"name": "Test"}
        response = user_api.update_user(99999, user_data)
        # JSONPlaceholder still returns 200 for non-existent resources
        assert response.status_code in [200, 404]
