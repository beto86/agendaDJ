from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)  #charFild tipo de campo para string
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True) #pega a data atual
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE) #modo CASCADE deleta tudo que tem relação com usuario

    class Meta:
        db_table = 'evento' #faz no banco de dados com este nome evento