from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'movie_id', 'movie_title', 'movie_poster', 'created_at']
        read_only_fields = ['created_at']
