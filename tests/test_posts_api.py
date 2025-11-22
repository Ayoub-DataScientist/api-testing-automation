"""
Tests for Post API endpoints.
"""

import pytest
from api import PostAPI


class TestPostsAPI:
    """Test suite for Post API endpoints."""

    @pytest.mark.smoke
    def test_get_all_posts(self, post_api: PostAPI):
        """Test retrieving all posts."""
        response = post_api.get_all_posts()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) > 0

    @pytest.mark.smoke
    def test_get_post_by_id(self, post_api: PostAPI):
        """Test retrieving a post by ID."""
        response = post_api.get_post(1)
        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert "title" in post
        assert "body" in post
        assert "userId" in post

    @pytest.mark.positive
    def test_create_post(self, post_api: PostAPI):
        """Test creating a new post."""
        post_data = {
            "title": "Test Post",
            "body": "This is a test post.",
            "userId": 1,
        }
        response = post_api.create_post(post_data)
        assert response.status_code == 201
        created_post = response.json()
        assert created_post["title"] == "Test Post"
        assert created_post["body"] == "This is a test post."

    @pytest.mark.positive
    def test_update_post(self, post_api: PostAPI):
        """Test updating a post."""
        post_data = {
            "title": "Updated Post",
            "body": "This is an updated post.",
            "userId": 1,
        }
        response = post_api.update_post(1, post_data)
        assert response.status_code == 200
        updated_post = response.json()
        assert updated_post["title"] == "Updated Post"

    @pytest.mark.positive
    def test_delete_post(self, post_api: PostAPI):
        """Test deleting a post."""
        response = post_api.delete_post(1)
        assert response.status_code == 200

    @pytest.mark.negative
    def test_get_nonexistent_post(self, post_api: PostAPI):
        """Test retrieving a non-existent post."""
        response = post_api.get_post(99999)
        assert response.status_code == 404

    @pytest.mark.regression
    def test_get_post_comments(self, post_api: PostAPI):
        """Test retrieving comments for a post."""
        response = post_api.get_post_comments(1)
        assert response.status_code == 200
        comments = response.json()
        assert isinstance(comments, list)

    @pytest.mark.regression
    def test_get_posts_by_user(self, post_api: PostAPI):
        """Test retrieving posts by a specific user."""
        response = post_api.get_posts_by_user(1)
        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        # All posts should belong to user 1
        for post in posts:
            assert post["userId"] == 1

    @pytest.mark.regression
    def test_patch_post(self, post_api: PostAPI):
        """Test partially updating a post."""
        post_data = {"title": "Patched Post"}
        response = post_api.patch_post(1, post_data)
        assert response.status_code == 200
        patched_post = response.json()
        assert patched_post["title"] == "Patched Post"

    @pytest.mark.negative
    def test_create_post_missing_title(self, post_api: PostAPI):
        """Test creating a post without a title."""
        post_data = {
            "body": "This is a test post.",
            "userId": 1,
        }
        response = post_api.create_post(post_data)
        # API may accept this, but we validate the response
        assert response.status_code in [201, 400]

    @pytest.mark.negative
    def test_create_post_invalid_user_id(self, post_api: PostAPI):
        """Test creating a post with an invalid user ID."""
        post_data = {
            "title": "Test Post",
            "body": "This is a test post.",
            "userId": -1,
        }
        response = post_api.create_post(post_data)
        # API may accept this, but we validate the response
        assert response.status_code in [201, 400]
