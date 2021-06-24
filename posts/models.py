from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(null=False, max_length=255)
    content = models.TextField(null=False)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
