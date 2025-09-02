"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Comunidade Plone Brasil"],
            ["plone.email_from_name", "Comunidade Plone Brasil"],
            ["plone.smtp_host", "localhost"],
            ["plone.smtp_port", 25],
            ["plone.default_language", "pt-br"],
            ["plone.available_languages", ["pt-br"]],
        ],
    )
    def test_setting(self, portal, key: str, expected: str | int | list[str]):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected