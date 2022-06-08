from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (HTTP_201_CREATED, HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .validators import *


class SignUp(APIView):
    def post(self, request, format=None):
        user = request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if UniqueEmail(request.data):
                return Response('Email já cadastrado na base de dados', status=HTTP_400_BAD_REQUEST)
            signup_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
            signup_user.first_name = user['first_name']
            signup_user.last_name = user['last_name']

            signup_user.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Create your views here.
