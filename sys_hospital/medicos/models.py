from django.db import models

from django.db import models
from enderecos.models import Endereco
from especializacoes.models import Especializacao

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    crm = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)  
    especializacao = models.ForeignKey(Especializacao, on_delete=models.CASCADE)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'medicos'

    def __str__(self):
        return f"{self.nome} - {self.crm}"
