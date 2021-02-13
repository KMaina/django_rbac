import pytest
import rest_framework

pytest_plugins = (
    "django_rba.tests.fixtures.products",
    "django_rba.tests.fixtures.users"
)

@pytest.fixture(scope="function")
def client():
    from rest_framework.test import APIClient
    return APIClient()