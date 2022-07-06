from django.db import models

class GroceryItem(models.Model):

    description = models.CharField(max_length=255)

    date_created = models.DateTimeField(verbose_name= 'created', auto_now_add=True)

    date_completed = models.DateTimeField(verbose_name= 'completed', null=True, blank=True)

    is_done = models.BooleanField(verbose_name= 'is complete', default=False)

    def __str__(self):
        return self.description

