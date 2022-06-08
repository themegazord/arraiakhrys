# SIGNALS

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()

# Create your models here.
class Perfil(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=31, verbose_name="first name")
    ultimo_nome = models.CharField(max_length=31, verbose_name="last name")
    email = models.EmailField(max_length=75, verbose_name="email address")
    valor_doado = models.FloatField(default=0)

    def __str__(self):
        return self.username.username


@receiver(post_save, sender=User)
def new_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(
            username = instance,
            email = instance.email,
        )
    else:
        if not hasattr(instance, "Perfil"):
            Perfil.objects.filter(username__exact=instance).update(
            ultimo_nome = instance.last_name,
            primeiro_nome = instance.first_name,
        )
