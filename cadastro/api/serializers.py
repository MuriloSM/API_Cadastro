from rest_framework import serializers
from cadastro import models

class DadosUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.DadosUsuario
        fields = '__all__'
