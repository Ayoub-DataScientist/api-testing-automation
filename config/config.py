"""
Configuration management for API tests.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Base configuration class."""

    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    TIMEOUT = int(os.getenv("TIMEOUT", "5"))
    VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class DevelopmentConfig(Config):
    """Development environment configuration."""

    DEBUG = True
    BASE_URL = os.getenv("DEV_BASE_URL", "https://jsonplaceholder.typicode.com")


class StagingConfig(Config):
    """Staging environment configuration."""

    DEBUG = False
    BASE_URL = os.getenv("STAGING_BASE_URL", "https://jsonplaceholder.typicode.com")


class ProductionConfig(Config):
    """Production environment configuration."""

    DEBUG = False
    VERIFY_SSL = True
    BASE_URL = os.getenv("PROD_BASE_URL", "https://jsonplaceholder.typicode.com")


def get_config(env: str = "dev") -> Config:
    """Get configuration for the specified environment."""
    configs = {
        "dev": DevelopmentConfig,
        "staging": StagingConfig,
        "prod": ProductionConfig,
    }
    return configs.get(env, DevelopmentConfig)()
