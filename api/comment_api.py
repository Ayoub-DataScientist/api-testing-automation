"""
Comment API client for managing comment endpoints.
"""

from api.base_api_client import BaseAPIClient


class CommentAPI(BaseAPIClient):
    """Client for Comment API endpoints."""

    def get_all_comments(self):
        """Get all comments."""
        return self.get("/comments")

    def get_comment(self, comment_id: int):
        """Get a comment by ID."""
        return self.get(f"/comments/{comment_id}")

    def create_comment(self, comment_data: dict):
        """Create a new comment."""
        return self.post("/comments", json=comment_data)

    def update_comment(self, comment_id: int, comment_data: dict):
        """Update an existing comment."""
        return self.put(f"/comments/{comment_id}", json=comment_data)

    def delete_comment(self, comment_id: int):
        """Delete a comment."""
        return self.delete(f"/comments/{comment_id}")

    def get_comments_by_post(self, post_id: int):
        """Get all comments for a specific post."""
        return self.get("/comments", params={"postId": post_id})

    def get_comments_by_email(self, email: str):
        """Get all comments by a specific email."""
        return self.get("/comments", params={"email": email})
