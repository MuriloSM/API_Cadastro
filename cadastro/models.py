from django.db import models

# Modelos de cadastro de usuarios para o banco de dados:

class DadosUsuario(models.Model):
    login = models.CharField(max_length= 30, unique=True, )  # Login unico, utilizando "unique=True".
    nome = models.CharField(max_length= 100)
    sobrenome = models.CharField(max_length= 100)
    data_nascimento = models.DateField()  
    email = models.EmailField(unique=True)  # Email unico, utilizando "unique=True".
    cadastro_criado_em = models.DateField(auto_now_add=True, editable=False) #Data de quando foi cadastrado o usuario, esse campo nao é editavel para o usuario.
    




