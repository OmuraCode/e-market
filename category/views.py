from rest_framework import generics, permissions
from . import serializers
from .models import Category

# from django.views.decorators.cache import cache_page


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser)

    # @cache_page(60 * 15)
    def get_permissions(self):
        if self.request.method == 'GET':
            return permissions.AllowAny(),
        return permissions.IsAdminUser(),


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    # @cache_page(60 * 15)
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny(), ]
        return [permissions.IsAdminUser(), ]