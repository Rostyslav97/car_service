from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("id", "is_active", "is_staff", "is_superuser", "last_login", "user_permissions", "groups")
        