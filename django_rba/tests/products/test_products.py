import pytest, json
from django.urls import reverse
from rest_framework import status


class TestProducts():

    @pytest.mark.django_db
    def test_get_all_products(self, client, new_product, new_product2):
        """This tests that you can get all products"""
        new_product.save()
        new_product2.save()
        url = reverse('products:article_view')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_create_product(self, client):
        """This tests that you can create a new product"""
        product = {
            "name": "Lambo",
            "price": 4500,
            "quantity": 49
        }
        url = reverse('products:article_view')
        response = client.post(url, data=json.dumps(product), content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED
    
    @pytest.mark.django_db
    def test_attendant_can_update_a_single_product_successfully(self, client, new_product, get_or_create_attendant_token):
        """This tests that an attendant can successfully update a product"""
        new_product.save()
        product = {
            "name": "BMW",
            "price": 4000,
            "quantity": 49
        }
        token = get_or_create_attendant_token
        url = reverse('products:single_article', kwargs={'pk':new_product.id})
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.put(url, data=product)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_customer_cant_update_a_single_product(self, client, new_product, get_or_create_customer_token):
        """This tests that a customer can't update a product"""
        new_product.save()
        product = {
            "name": "BMW",
            "price": 4000,
            "quantity": 49
        }
        token = get_or_create_customer_token
        url = reverse('products:single_article', kwargs={'pk':new_product.id})
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.put(url, data=product)
        assert response.status_code == status.HTTP_403_FORBIDDEN