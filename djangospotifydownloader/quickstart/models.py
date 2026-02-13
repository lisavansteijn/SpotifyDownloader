from django.db import models

# Create your models here.
class SpotifyLink(models.Model):
    link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    songs = models.JSONField(default=list)
    
    class Meta:
        verbose_name = 'Spotify Link'
        verbose_name_plural = 'Spotify Links'
    