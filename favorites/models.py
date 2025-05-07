# favorites/models.py
from django.db import models
from django.utils import timezone

class Favorite(models.Model):
    movie_id = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    movie_poster = models.CharField(max_length=255, null=True, blank=True)  # Added this field
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('movie_id',)  # Ensures no duplicate movies in favorites

    def __str__(self):
        return f"{self.movie_title} (ID: {self.movie_id})"