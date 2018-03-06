import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    # avatar = models.ImageField(upload_to = 'media/', default = 'media/e/no-img.jpg')

# Category table model
class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Categories"

# Article table model
class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=3072)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField('date published')
    date_modified = models.DateTimeField('last modified')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

# Comment table model
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField('date published')
    date_modified = models.DateTimeField('last modified')
    