from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PokemonUser(models.Model):
    pokemon_id = models.IntegerField(null=True)

class userBase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(PokemonUser, on_delete=models.SET_NULL, null=True)
