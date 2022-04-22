from django.db import models


class Post(models.Model):
    image = models.ImageField()
    descriptions = models.TextField()


class Comments(models.Model):
    username = models.CharField(max_length=20)
    text = models.CharField(max_length=100)