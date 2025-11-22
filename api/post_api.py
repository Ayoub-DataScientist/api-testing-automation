"""
Post API client for managing post endpoints.
"""

from api.base_api_client import BaseAPIClient


class PostAPI(BaseAPIClient):
    """Client for Post API endpoints."""

    def get_all_posts(self):
        """Get all posts."""
        return self.get("/posts")

    def get_post(self, post_id: int):
        """Get a post by ID."""
        return self.get(f"/posts/{post_id}")

    def create_post(self, post_data: dict):
        """Create a new post."""
        return self.post("/posts", json=post_data)

    def update_post(self, post_id: int, post_data: dict):
        """Update an existing post."""
        return self.put(f"/posts/{post_id}", json=post_data)

    def patch_post(self, post_id: int, post_data: dict):
        """Partially update a post."""
        return self.patch(f"/posts/{post_id}", json=post_data)

    def delete_post(self, post_id: int):
        """Delete a post."""
        return self.delete(f"/posts/{post_id}")

    def get_post_comments(self, post_id: int):
        """Get all comments for a post."""
        return self.get(f"/posts/{post_id}/comments")

    def get_posts_by_user(self, user_id: int):
        """Get all posts by a specific user."""
        return self.get("/posts", params={"userId": user_id})
