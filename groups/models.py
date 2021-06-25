from django.contrib.auth.models import User
from django.db import models

from posts.models import Post


class Group(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(default="")
    admin = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='admin', null=False)
    is_public = models.BooleanField(default=False)
    members = models.ManyToManyField(User, related_name='members')
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'groups'
