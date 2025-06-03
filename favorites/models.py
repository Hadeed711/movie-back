from django.db import models
from django.conf import settings

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # Temporary nullable
    movie_id = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    movie_poster = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie_id')  # Ensures no duplicate movies per user

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.movie_title}"