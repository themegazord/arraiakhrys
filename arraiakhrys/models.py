# SIGNALS

from django.dispatch import receiver

from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models 
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class Perfil(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=31, verbose_name="first name")
    ultimo_nome = models.CharField(max_length=31, verbose_name="last name")
    email = models.EmailField(max_length=75, verbose_name="email address")

    def __str__(self):
        return self.username.username


@receiver(post_save, sender=User)
def new_profile(sender, instance, created, **kwargs):
    if created:
        user_db = User.objects.filter(username__exact=instance).first()
        p = Perfil.objects.create(
            username = instance,
            primeiro_nome = instance.first_name,
            ultimo_nome = instance.last_name,
            email = instance.email
        )
        p.save()
        print(p.primeiro_nome)
