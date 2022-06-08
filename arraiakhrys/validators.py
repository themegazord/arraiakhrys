#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

def UniqueEmail(data):
    user_api = data
    query = User.objects.filter(email__exact=user_api['email']).first()
    if not isinstance(query, type(None)):
        return True
    else:
        return False

