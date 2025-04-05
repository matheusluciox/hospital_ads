from django.db import models

class Consultas(models.Model):
    id = models.AutoField(primary_key=True)
    data_hora = models.DateTimeField()
    medico = models.ForeignKey('medicos.Medico', on_delete=models.CASCADE)
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    doenca = models.ForeignKey('doencas.Doencas', on_delete=models.CASCADE)
    endereco = models.ForeignKey('enderecos.Endereco', on_delete=models.CASCADE)
    enfermeiro = models.ForeignKey('enfermeiros.Enfermeiro', on_delete=models.CASCADE)

    class Meta:
        db_table = 'consultas'

    def __str__(self):
        return f"Consulta {self.id} - {self.paciente} - {self.data_hora}"