from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from groups.models import Group
from groups.serializers import GroupSerializer


class CreateGroupView(CreateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        admin = request.user

        Group.objects.create(admin=admin, **request.data)

        return Response(status=200)


class UpdateGroupView(RetrieveUpdateAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated,)


class ListGroupView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class RetrieveGroupView(RetrieveAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class DestroyGroupView(DestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated,)
