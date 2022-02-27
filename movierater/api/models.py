from django.db import models


class ExtraInfo(models.Model):
    KIND = {
        (0, 'Not Known'),
        (1, 'Drama'),
        (2, 'Comedy'),
        (3, 'Thriller'),
        (4, 'Horror')
    }
    time = models.IntegerField()
    kind = models.IntegerField(choices=KIND, default=0)

    def __str__(self):
        return f'{self.time}mins - {self.kind}'


class Film(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    after_premiere = models.BooleanField(default=False)
    premiere = models.DateField(null=True, blank=True)
    year = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2,
                                      null=True, blank=True)
    kind = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE,
                                null=True, blank=True)

    def __str__(self):
        return f'{self.title} ({self.year})'


