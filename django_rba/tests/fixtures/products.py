import pytest
from django_rba.apps.products.models import Product

@pytest.fixture(scope='function')
def new_product():
    product = Product.objects.create(name="BMW", price=4000, quantity=20)
    return product

@pytest.fixture(scope='function')
def new_product2():
    product = Product.objects.create(name="Benz", price=8000, quantity=120)
    return product
