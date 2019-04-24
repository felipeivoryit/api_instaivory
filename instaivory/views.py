from django.shortcuts import render
from rest_framework.response import Response

import base64
from django.conf import settings

from django.core.files.base import ContentFile

# Create your views here.

from rest_framework import viewsets

from .models import InstaivoryUsuario
from .serializers import InstaivoryUsuarioSerializer

class UsuarioItemViemSet(viewsets.ModelViewSet):

    serializer_class = InstaivoryUsuarioSerializer

    def get_queryset(self):
        print('Get')
        return InstaivoryUsuario.objects.all()

    def create(self, request, *args, **kwargs):


        value = request.data['foto']['value']
        filename = request.data['foto']['filename']

        print(request.data['foto'])

        #data = ContentFile(base64.b64decode(value), filename)

        # Decodificando base64 do banco de dados
        imgdata = base64.b64decode(request.data['foto']['value'])

        # Definindo caminho do arquivo
        nomeArquivo = filename

        enderecoArquivo = settings.MEDIA_ROOT

        # Salvando arquivo
        with open(enderecoArquivo + "/" + request.data['foto']['filename'], 'wb') as f:
            f.write(imgdata)



        return Response({'Olá': request.data['nome']})
