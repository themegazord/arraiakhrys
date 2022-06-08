from django.contrib.auth.models import User
from rest_framework import serializers

from arraiakhrys.models import Perfil


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        field = ['username', 'primeiro_nome', 'ultimo_nome', 'email', 'cpf']
