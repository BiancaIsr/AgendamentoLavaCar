from django.test import TestCase
from django.urls import reverse
from .models import Agendamento 
class AgendamentoTestCase(TestCase):

    def setUp(self):
        """
        Este método cria um objeto de teste inicial antes de cada teste abaixo rodar.
        """
        self.veiculo_teste = Veiculo.objects.create(
            # Coloque aqui os campos que o seu Veiculo exige. Exemplo:
            marca="VW",
            modelo="Fusca" 
        )
        self.agendamento = Agendamento.objects.create(

            cliente="Bianca",
            veiculo=self.veiculo_teste,
            placa="ABC-1234",
            servico="Lavagem Completa"
        )

    # Teste 1: Verifica se os dados do cliente e veículo foram gravados com sucesso
    def test_criacao_agendamento(self):
        self.assertEqual(self.agendamento.cliente, "Bianca Developer")
        self.assertEqual(self.agendamento.veiculo, "Carro de Teste")

    # Teste 2: Verifica se a placa foi salva exatamente como o esperado
    def test_validacao_placa(self):
        self.assertEqual(self.agendamento.placa, "ABC-1234")

    # Teste 3: Verifica se o serviço cadastrado é o correto (lógica de negócio)
    def test_tipo_servico(self):
        self.assertEqual(self.agendamento.servico, "Lavagem Completa")

    # Teste 4: Verifica a representação em string do modelo (método __str__)
    def test_representacao_string(self):
        esperado = f"{self.agendamento.cliente} - {self.agendamento.veiculo}"
        self.assertEqual(str(self.agendamento), esperado)

    # Teste 5: Verifica se a página inicial do sistema está carregando (Status 200)
    def test_acesso_pagina_home(self):
        # Substitua 'home' pelo 'name' que você deu para a rota da sua página principal no urls.py
        url = reverse('home') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)