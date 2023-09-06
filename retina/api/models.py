from django.db import models
from datetime import datetime
from django.utils import timezone

class VideoModel(models.Model):
    video = models.FileField()

    def __str__(self):
        return self.video.name()
