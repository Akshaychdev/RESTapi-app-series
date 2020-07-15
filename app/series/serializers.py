from rest_framework import serializers

from core.models import Tag, Character


# Creating a ModelSerializer and link to Tag MODEL, pull in ID and name values
class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for Tag objects
    """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer for Character objects
    """

    class Meta:
        model = Character
        fields = ('id', 'name')
        read_only_fields = ('id',)
