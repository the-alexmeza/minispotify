from django.db import models

# Create your models here.

class TestField(models.Model):
    test = models.CharField(max_length=320, null=True, blank=True)

    def __str__(self):
        return self.id
