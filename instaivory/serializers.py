from rest_framework import serializers

from .models import InstaivoryUsuario

class InstaivoryUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstaivoryUsuario
        fields = '__all__'
