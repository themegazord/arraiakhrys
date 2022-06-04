from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class SignUp(APIView):
    def post(self, request, format=None):
        user = request.data
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            #print(user['username'], user['password'], user['email'], user['last_name'], user['first_name'])
            signup_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
            signup_user.first_name = user['first_name']
            signup_user.last_name = user['last_name']

            signup_user.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# Create your views here.
