from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=2000, null=True, default="No description", blank=True)
    def __str__(self):
        return self.name