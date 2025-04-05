from django.db import models

class statusConsulta(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'statusConsulta'

    def __str__(self):
        return self.nome
