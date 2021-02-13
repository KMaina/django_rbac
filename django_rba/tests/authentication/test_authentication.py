import pytest, json
from django.urls import reverse
from rest_framework import status


class TestAuthentication():
    """Class to Test creation of users"""
    @pytest.mark.django_db
    def test_admin_can_create_attendants(self, client, admin, get_or_create_admin_token):
        """Test that an admin can create a new attendant"""
        new_attendant = {
            "email": "attendant@me.com",
            "username": "attendant",
            "password": "1234"
        }
        token = get_or_create_admin_token
        url = reverse('authentication:attendant_registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_attendant)
        assert response.status_code == status.HTTP_201_CREATED

    @pytest.mark.django_db
    def test_customer_cant_create_attendants(self, client, customer, get_or_create_customer_token):
        """Test that a customer can't create a new attendant"""
        new_attendant = {
            "email": "attendant@me.com",
            "username": "attendant",
            "password": "1234"
        }
        token = get_or_create_customer_token
        url = reverse('authentication:attendant_registration')
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.post(url, new_attendant)
        assert response.status_code == status.HTTP_403_FORBIDDEN
