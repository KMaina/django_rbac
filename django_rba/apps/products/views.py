from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

from .models import Product
from .serializer import ProductSerializer
from django_rba.utility.permissions import IsAdminOrAttendant

class CreateListProductsView(APIView):
    """API View to create and list product items"""
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        post:
        Creates a new product item
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        """
        get:
        Returns all products
        """
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductsView(APIView):
    """
    APIView that allows CRUD operations for Products
    """

    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrAttendant,)

    def put(self, request, pk):
        """
        put:
        Update a single product instance
        Args:
            pk: the pk of the product
        """
        product = get_object_or_404(Product.objects.all(), pk=pk)
        data = request.data
        serializer = ProductSerializer(instance=product, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            updated_product = serializer.save()
        return Response({"success": f"Product {updated_product.name} saved successfully"})
    
    def delete(self, request, pk):
        """
        delete:
        Delete a single product instance
        Args:
            pk: the pk of the product
        """
        product = get_object_or_404(Product.objects.all(), pk=pk)
        product.delete()
        return Response({"message": f"Article with id {pk} has been deleted"}, status=204)