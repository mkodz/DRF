from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    after_premiere = models.BooleanField(default=False)
