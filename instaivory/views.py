from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .models import InstaivoryUsuario
from .serializers import InstaivoryUsuarioSerializer

class UsuarioItemViemSet(viewsets.ModelViewSet):

    serializer_class = InstaivoryUsuarioSerializer
    queryset = InstaivoryUsuario.objects.all()
