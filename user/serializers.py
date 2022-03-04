# 3rd party
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# django
from django.db.models import Q
from django.contrib.auth import get_user_model

# retrieve the user object
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for retrieving Custom User data
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
    """
        Serializer for creating Custom User
    """

    class Meta:
        model = User
        fields = (
            'email',
            'secret_code',
            'password',
        )


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    """
        Custom Token pair creating serializer from email and password
    """
    default_error_messages = {'no_userprofile': 'User credentials does not exist.Please sign up'}
    username_field = 'email'

    def validate(self, attrs):
        data = attrs
        user_obj = User.objects.get(Q(email__iexact=attrs.get('email')))
        password = attrs.get('password')
        if user_obj is not None:
            credentials = {
                'username': user_obj.email,
                'password': password
            }
            if all(credentials.values()):
                try:
                    # Validate the credentials and return the user on success.
                    if user_obj.check_password(password):
                        refresh = RefreshToken.for_user(user_obj)
                        data['refresh'] = str(refresh)
                        data['token'] = str(refresh.access_token)
                        data.pop('password')
                        return data
                except Exception as e:
                    raise e
        self.fail('no_userprofile')
