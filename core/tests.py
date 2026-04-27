from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Cliente, Veiculo, Agendamento

class AgendamentoTestCase(TestCase):

    def setUp(self):
        self.cliente_teste = Cliente.objects.create(
            nome="Bianca Developer",
            telefone="41999999999"
        )

        self.veiculo_teste = Veiculo.objects.create(
            placa="ABC-1234",
            modelo="BMW X1",
            cor="Preto",
            cliente=self.cliente_teste
        )

        agora = timezone.now()

        self.agendamento = Agendamento.objects.create(
            veiculo=self.veiculo_teste,
            data_hora_agendamento=agora,
            previsao_entrega=agora + timedelta(hours=2),
            servico="Lavagem Completa",
            valor_total=150.00
        )

    # Teste 1: Verifica se o serviço e o valor foram salvos corretamente
    def test_dados_agendamento(self):
        self.assertEqual(self.agendamento.servico, "Lavagem Completa")
        self.assertEqual(self.agendamento.valor_total, 150.00)

    # Teste 2: Verifica se o status inicial padrão é 'AGUARDANDO'
    def test_status_padrao(self):
        self.assertEqual(self.agendamento.status, 'AGUARDANDO')

    # Teste 3: Verifica se o agendamento consegue acessar o nome do cliente
    def test_relacionamento_cliente_veiculo(self):
        self.assertEqual(self.agendamento.veiculo.cliente.nome, "Bianca Developer")

    # Teste 4: NOVO - Verifica se a previsão de entrega foi calculada para o futuro
    def test_logica_previsao_entrega(self):
        self.assertTrue(self.agendamento.previsao_entrega > self.agendamento.data_hora_agendamento)

    # Teste 5: NOVO - Verifica se o veículo foi vinculado corretamente conferindo a placa
    def test_veiculo_vinculado(self):
        self.assertEqual(self.agendamento.veiculo.placa, "ABC-1234")