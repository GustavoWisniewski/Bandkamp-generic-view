from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    
    class Meta:
        model = Song
        fields = ["id", "title", "duration", "album_id"]

        extra_kwargs = {
            "id": {"read_only": True},
            "title": {"max_length": 255},
            "duration": {"max_length": 255},
            "album_id": {"read_only": True},
        }