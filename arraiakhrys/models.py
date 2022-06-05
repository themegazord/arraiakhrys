from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Perfil(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, verbose_name="first name", blank=True)
    last_name = models.CharField(max_length=30, verbose_name="last name", blank=True)
    email = models.EmailField(max_length=75, verbose_name="email address", blank=True)

    def __str__(self):
        return self.username.username

# SIGNALS
def new_profile(sender, instance, created, **kwargs):
    user_db = User.objects.filter(username__exact=instance).values().first()
    if created:
        Perfil.objects.create(
            username = instance
        )
        Perfil.objects.filter(username__exact=instance).update(
            first_name = user_db['first_name'],
            last_name = user_db['last_name'],
            email = user_db['email']
        )
        
post_save.connect(new_profile, sender=User)