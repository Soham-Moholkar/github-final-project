"""Configuration and failure-response regression tests."""
import importlib
import os
from unittest import TestCase
from unittest.mock import patch
from service import app, config
from service.common.error_handlers import internal_server_error


class TestCommon(TestCase):
    """Check environment configuration and safe server-error responses."""

    def test_database_configuration(self):
        """It should build a PostgreSQL URL from the deployment environment"""
        settings = {"DATABASE_USER": "test", "DATABASE_PASSWORD": "example",
                    "DATABASE_HOST": "postgres", "DATABASE_NAME": "accounts"}
        with patch.dict(os.environ, settings, clear=True):
            importlib.reload(config)
            self.assertEqual(config.DATABASE_URI, "postgresql://test:example@postgres:5432/accounts")
        importlib.reload(config)

    def test_internal_error(self):
        """It should return a structured 500 response"""
        with app.app_context():
            response, code = internal_server_error("An unexpected error occurred")
        self.assertEqual(code, 500)
        self.assertEqual(response.get_json()["error"], "Internal Server Error")
