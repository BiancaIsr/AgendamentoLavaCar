from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_lenght=20, unique=True)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(mas_length=40)
    cliente = models.FireignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('AGUARDANDO', 'Aguardando'),
        ('LAVANDO', 'Lavando'),
        ('CONCLUIDO', 'Concluído'),
        ('FINALIZADO', 'Finalizado'),
        ('CANCELADO', 'Cancelado'),
    ]

    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_hora_agendamento = models.DateTimeField()
    previsao_entrega = models.DateTimeField()
    servico = models.CharField(max_length=100) # Ex: Lavagem Completa
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGUARDANDO')
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

def __str__(self):
    data_formatada = self.data_hora_agendamento.strftime('%d/%m/%Y %H:%M')
    return f"Agendamento: {self.veiculo} - {data_formatada}"