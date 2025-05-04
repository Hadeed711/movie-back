from django.db import models
from django.contrib.auth import get_user_model

class Favorite(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    movie_id = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    movie_poster = models.URLField(max_length=500)  # Add this field
    created_at = models.DateTimeField(auto_now_add=True)  # Track when added

    def __str__(self):
        return f"{self.movie_title} (ID: {self.movie_id})"