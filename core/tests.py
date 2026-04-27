from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from .models import Cliente, Veiculo, Agendamento

class AgendamentoTestCase(TestCase):

    def setUp(self):
        # 1. Primeiro criamos um Cliente real no banco de testes
        self.cliente_teste = Cliente.objects.create(
            nome="Bianca Developer",
            telefone="41999999999"
        )

        # 2. Depois criamos um Veículo e ligamos ele ao Cliente acima
        self.veiculo_teste = Veiculo.objects.create(
            placa="ABC-1234",
            modelo="BMW X1",
            cor="Preto",
            cliente=self.cliente_teste  # Ligação da Chave Estrangeira
        )

        # 3. Pegamos a hora atual para o agendamento
        agora = timezone.now()

        # 4. Finalmente, criamos o Agendamento com todos os campos obrigatórios
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

    # Teste 3: Verifica se o agendamento consegue acessar o nome do cliente através do veículo
    def test_relacionamento_cliente_veiculo(self):
        self.assertEqual(self.agendamento.veiculo.cliente.nome, "Bianca Developer")

    # Teste 4: Verifica a formatação em texto (__str__) do Agendamento
    def test_representacao_string_agendamento(self):
        data_formatada = self.agendamento.data_hora_agendamento.strftime('%d/%m/%Y %H:%M')
        esperado = f"Agendamento: {self.veiculo_teste} - {data_formatada}"
        self.assertEqual(str(self.agendamento), esperado)

    # Teste 5: Verifica se a página inicial está no ar (Status 200)
    def test_acesso_pagina_home(self):
        url = reverse('home') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)