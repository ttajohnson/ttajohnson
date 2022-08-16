from django.db import models

class Shurl(models.Model):
    
    long_url = models.URLField(max_length=200)

    short_url = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.long_url} - {self.short_url}'

