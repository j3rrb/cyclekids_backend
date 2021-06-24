from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from posts.models import Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id']


class PostSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'
