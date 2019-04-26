from django.db import models
from PIL import Image

# Create your models here.

class InstaivoryUsuario(models.Model):

    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    sexo = models.CharField(max_length=10)
    foto = models.ImageField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.nome
