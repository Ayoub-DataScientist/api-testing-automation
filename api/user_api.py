"""
User API client for managing user endpoints.
"""

from api.base_api_client import BaseAPIClient


class UserAPI(BaseAPIClient):
    """Client for User API endpoints."""

    def get_all_users(self):
        """Get all users."""
        return self.get("/users")

    def get_user(self, user_id: int):
        """Get a user by ID."""
        return self.get(f"/users/{user_id}")

    def create_user(self, user_data: dict):
        """Create a new user."""
        return self.post("/users", json=user_data)

    def update_user(self, user_id: int, user_data: dict):
        """Update an existing user."""
        return self.put(f"/users/{user_id}", json=user_data)

    def patch_user(self, user_id: int, user_data: dict):
        """Partially update a user."""
        return self.patch(f"/users/{user_id}", json=user_data)

    def delete_user(self, user_id: int):
        """Delete a user."""
        return self.delete(f"/users/{user_id}")

    def get_user_posts(self, user_id: int):
        """Get all posts by a user."""
        return self.get(f"/users/{user_id}/posts")

    def get_user_comments(self, user_id: int):
        """Get all comments by a user."""
        return self.get(f"/users/{user_id}/comments")

    def get_user_todos(self, user_id: int):
        """Get all todos by a user."""
        return self.get(f"/users/{user_id}/todos")
