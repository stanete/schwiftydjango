from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist
from .models import Character, Origin
import logging

logger = logging.getLogger(__name__)


class OriginSerializer(serializers.ModelSerializer):
    """Serializer to map the Origin Model instance into JSON format."""

    class Meta:
        model = Origin
        fields = ('id', 'name')


class CharacterSerializer(serializers.ModelSerializer):
    """Serializer to map the Character Model instance into JSON format."""
    origin = OriginSerializer(read_only=True)
    origin_id = serializers.PrimaryKeyRelatedField(queryset=Origin.objects.all(), write_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Character
        fields = ('id', 'name', 'origin', 'origin_id', 'image',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

    def create(self, validated_data):
        origin_id = validated_data.pop('origin_id')
        validated_data['origin'] = origin_id
        character = Character.objects.create(**validated_data)
        return character
