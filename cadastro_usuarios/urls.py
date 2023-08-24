from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cadastro.api import viewsets as dadosviewset

#Criando rota para API

route = routers.DefaultRouter()
route.register(r'cadastro', dadosviewset.DadosUsuarioViewSet, basename = 'Cadastro')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),

]
