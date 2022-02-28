# 3rd party
from rest_framework import serializers

# django
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
        Customer User serializer
    """
    class Meta:
        model = User
        fields = (
            'uid',
            'email',
            'username',
            'secret_code',
            'date_joined',
        )


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'secret_code',
        )