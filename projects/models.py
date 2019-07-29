from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="img")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    createdTime = models.DateTimeField(default=timezone.now)
    updatedTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

