from rest_framework import viewsets
from cadastro.api import serializers
from cadastro import models

class DadosUsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DadosUsuarioSerializers
    queryset = models.DadosUsuario.objects.all()