from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer


class CreatePostView(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        author = request.user

        Post.objects.create(author=author, **request.data)

        return Response(status=200)


class UpdatePostView(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)


class ListPostView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    permission_classes = (IsAuthenticated,)


class RetrievePostView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    permission_classes = (IsAuthenticated,)


class DestroyPostView(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)
