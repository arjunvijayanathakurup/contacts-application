# django
from django.shortcuts import render

# 3rd party
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# local
from .models import Contact
from .serializers import (
    ContactSerializer,
    ContactCreateSerializer
)


class ContactViewSet(viewsets.ModelViewSet):
    """
        Contacts Viewset for managing the Contacts
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return ContactCreateSerializer
        return ContactSerializer
