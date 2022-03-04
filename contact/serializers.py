# 3ed-party
from rest_framework import serializers

# local
from user.serializers import UserSerializer
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
        Serializer for viewing the contacts
    """
    user = UserSerializer(required=False)

    class Meta:
        model = Contact
        fields = (
            'uid',
            'user',
            'name',
            'email',
            'phone_number',
        )


class ContactCreateSerializer(serializers.ModelSerializer):
    """
        Serializer for creating a contact
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),)

    class Meta:
        model = Contact
        fields = (
            'uid',
            'user',
            'name',
            'email',
            'phone_number',
        )
