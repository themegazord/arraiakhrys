from django.contrib.auth.models import User
from .models import *

def UniqueEmail(data):
    user = data
    query_user = User.objects.filter(email__exact=user['email']).first()
    if not isinstance(query_user, type(None)):
        return True
    else:
        return False

