from rest_framework import serializers
from core.models import Defect


class DefectSerializer(serializers.ModelSerializer):
    city=serializers.SlugRelatedField(slug_field="name", read_only=True)
    class Meta:
        model = Defect
        exclude = ("id", "status")


class DefectCreateSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Defect
        exclude = ("id", "status")