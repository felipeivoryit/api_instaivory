from django.shortcuts import render
from rest_framework.response import Response

import base64
from django.conf import settings

from django.core.files.base import ContentFile

# Create your views here.

from rest_framework import viewsets

from .models import InstaivoryUsuario
from .serializers import InstaivoryUsuarioSerializer

import random
import string

class UsuarioItemViemSet(viewsets.ModelViewSet):

    serializer_class = InstaivoryUsuarioSerializer

    def get_queryset(self):
        print('Get')
        usuario = InstaivoryUsuario.objects.all()
        print(usuario)
        return usuario

    def salvarImagem(self, image_data):

        format, imgstr = image_data.split(';base64,')
        # Decodificando base64 do banco de dados
        imgdata = base64.b64decode(imgstr)

        # Extensão do arquivos
        ext = format.split('/')

        # Criar nome para a imagem
        letters = string.ascii_lowercase
        nome_random = ''.join(random.choice(letters) for i in range(30))

        # Definindo caminho do arquivo
        nomeArquivo = nome_random +'.' + ext[1]

        enderecoArquivo = settings.MEDIA_ROOT

        # Salvando arquivo
        with open(enderecoArquivo + "/" + nomeArquivo, 'wb') as f:
            f.write(imgdata)

        return nomeArquivo

    def create(self, request, *args, **kwargs):

        nome_imagem = None

        image_data = request.data['foto']

        if image_data != None:
            nome_imagem = self.salvarImagem(image_data)

        # Salvar dados no banco de dados
        usuario = InstaivoryUsuario.objects.create( foto=nome_imagem, nome= request.data['nome'],
                                                    email= request.data['email'], sexo= request.data['sexo'])

        print(usuario)

        return usuario
