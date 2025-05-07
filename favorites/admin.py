from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'movie_id', 'created_at') 
    search_fields = ('movie_title', 'movie_id')
    list_filter = ('created_at',)
