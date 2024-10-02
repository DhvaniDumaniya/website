from django.db import models # type: ignore

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name