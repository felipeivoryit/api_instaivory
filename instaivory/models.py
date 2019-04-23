from django.db import models

# Create your models here.

class InstaivoryUsuario(models.Model):

    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
