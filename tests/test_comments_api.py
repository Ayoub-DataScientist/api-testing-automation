"""
Tests for Comment API endpoints.
"""

import pytest
from api import CommentAPI


class TestCommentsAPI:
    """Test suite for Comment API endpoints."""

    @pytest.mark.smoke
    def test_get_all_comments(self, comment_api: CommentAPI):
        """Test retrieving all comments."""
        response = comment_api.get_all_comments()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    @pytest.mark.smoke
    def test_get_comment_by_id(self, comment_api: CommentAPI):
        """Test retrieving a comment by ID."""
        response = comment_api.get_comment(1)
        assert response.status_code == 200
        comment = response.json()
        assert comment["id"] == 1
        assert "postId" in comment
        assert "name" in comment
        assert "email" in comment
        assert "body" in comment

    @pytest.mark.positive
    def test_create_comment(self, comment_api: CommentAPI):
        """Test creating a new comment."""
        comment_data = {
            "postId": 1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a test comment.",
        }
        response = comment_api.create_comment(comment_data)
        assert response.status_code == 201
        created_comment = response.json()
        assert created_comment["name"] == "Test Comment"
        assert created_comment["email"] == "test@example.com"

    @pytest.mark.positive
    def test_update_comment(self, comment_api: CommentAPI):
        """Test updating a comment."""
        comment_data = {
            "postId": 1,
            "name": "Updated Comment",
            "email": "updated@example.com",
            "body": "This is an updated comment.",
        }
        response = comment_api.update_comment(1, comment_data)
        assert response.status_code == 200
        updated_comment = response.json()
        assert updated_comment["name"] == "Updated Comment"

    @pytest.mark.positive
    def test_delete_comment(self, comment_api: CommentAPI):
        """Test deleting a comment."""
        response = comment_api.delete_comment(1)
        assert response.status_code == 200

    @pytest.mark.negative
    def test_get_nonexistent_comment(self, comment_api: CommentAPI):
        """Test retrieving a non-existent comment."""
        response = comment_api.get_comment(99999)
        assert response.status_code == 404

    @pytest.mark.regression
    def test_get_comments_by_post(self, comment_api: CommentAPI):
        """Test retrieving comments for a specific post."""
        response = comment_api.get_comments_by_post(1)
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)
        # All comments should belong to post 1
        for comment in comments:
            assert comment["postId"] == 1

    @pytest.mark.regression
    def test_get_comments_by_email(self, comment_api: CommentAPI):
        """Test retrieving comments by email."""
        response = comment_api.get_comments_by_email("Eliseo@gardner.biz")
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)

    @pytest.mark.negative
    def test_create_comment_missing_email(self, comment_api: CommentAPI):
        """Test creating a comment without an email."""
        comment_data = {
            "postId": 1,
            "name": "Test Comment",
            "body": "This is a test comment.",
        }
        response = comment_api.create_comment(comment_data)
        # API may accept this, but we validate the response
        assert response.status_code in [201, 400]

    @pytest.mark.negative
    def test_create_comment_invalid_post_id(self, comment_api: CommentAPI):
        """Test creating a comment with an invalid post ID."""
        comment_data = {
            "postId": -1,
            "name": "Test Comment",
            "email": "test@example.com",
            "body": "This is a test comment.",
        }
        response = comment_api.create_comment(comment_data)
        # API may accept this, but we validate the response
        assert response.status_code in [201, 400]

    @pytest.mark.regression
    def test_comment_response_structure(self, comment_api: CommentAPI):
        """Test that comment response has the correct structure."""
        response = comment_api.get_comment(1)
        assert response.status_code == 200
        comment = response.json()
        
        required_fields = ["postId", "id", "name", "email", "body"]
        for field in required_fields:
            assert field in comment, f"Missing field: {field}"
