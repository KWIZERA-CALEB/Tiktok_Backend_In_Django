from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    hashtags = models.CharField(max_length=255, null=True)
    # owner
    def __str__(self):
        return self.title
