from django.urls import path

from .views import *

app_name="products"
urlpatterns = [
    path('products/', CreateListProductsView.as_view(), name="article_view"),
    path('products/<int:pk>/', ProductsView.as_view(), name='single_article')
]