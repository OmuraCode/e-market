from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .models import Post, Order
from posts.permissions import IsAuthor


class OrderCreateView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.OrderUserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



