"""
API client module for JSONPlaceholder API.
"""

from api.base_api_client import BaseAPIClient
from api.user_api import UserAPI
from api.post_api import PostAPI
from api.comment_api import CommentAPI

__all__ = ["BaseAPIClient", "UserAPI", "PostAPI", "CommentAPI"]
