from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import TokenObtainPairSerializer


class TokenObtainPairViewSet(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
