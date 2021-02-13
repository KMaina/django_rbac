import pytest, json
from django.urls import reverse
from django_rba.apps.authentication.models import User

@pytest.fixture(scope='function')
def admin():
    admin = User.objects.create_superuser(email='admin@me.com', username='admin', password='1234')
    return admin


@pytest.fixture
def get_or_create_admin_token(db, client, admin):
    admin.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "admin@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def attendant():
    attendant = User.objects.create_attendant(email='att1@me.com', username='att1', password='1234')
    return attendant

@pytest.fixture
def get_or_create_attendant_token(db, client, attendant):
    attendant.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "att1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token

@pytest.fixture(scope='function')
def customer():
    customer = User.objects.create_user(email='cust1@me.com', username='cust1', password='1234')
    return customer

@pytest.fixture
def get_or_create_customer_token(db, client, customer):
    customer.save()
    url = reverse('authentication:token_obtain_pair')
    my_data =  {
        "email": "cust1@me.com",
        "password": "1234"
	}
    response = client.post(url,data=json.dumps(my_data),
                                   content_type='application/json')
    token =  response.data['access']
    return token
