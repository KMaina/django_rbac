from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

app_name = "authentication"
urlpatterns = [
    path('auth/customer_registration/', CustomerRegistration.as_view(), name='customer_registration'),
    path('auth/attendant_registration/', AttendantRegistration.as_view(), name='attendant_registration'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]