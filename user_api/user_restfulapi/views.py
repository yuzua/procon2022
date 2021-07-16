from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils.auth import NormalAuthentication


class Login(APIView):

    authentication_classes = [NormalAuthentication,]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})