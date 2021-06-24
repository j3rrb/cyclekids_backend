from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.exceptions import APIException


class RegisterView(APIView):

    @staticmethod
    def post(req: Request):
        try:
            User.objects.create_user(**req.data)

            return Response(status=HTTP_201_CREATED)
        except APIException as ex:
            return Response(status=ex.status_code)
