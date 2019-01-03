from django.conf import settings
from django.db import models
from django.utils import timezone


# from datetime import date
# from PIL import Image


# Create your models here.
class Game(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True)
    release_date = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = models.CharField(max_length=200)
    cat_image = models.ImageField(null=True)

    def __str__(self):
        return self.cat_name
