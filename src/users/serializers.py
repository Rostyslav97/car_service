from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("id", "is_active", "is_staff", "is_superuser", "last_login", "user_permissions", "groups", "sex")