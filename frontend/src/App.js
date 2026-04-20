import React, { useState } from 'react';
import './App.css';
import FormAgendamento from './components/FormAgendamento';
import TabelaAgendamento from './components/TabelaAgendamento';

function App() {
  // O Estado agora mora aqui no App.js
  const [agendamentos, setAgendamentos] = useState([
    { id: 1, cliente: 'Matheus', veiculo: 'Peugeot 208', placa: 'ABC-1234', servico: 'Lavagem Completa', status: 'Pendente' }
  ]);

  // Função para adicionar novo agendamento
  const adicionarAgendamento = (novo) => {
    setAgendamentos([...agendamentos, { ...novo, id: Date.now(), status: 'Pendente' }]);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Lava Car - Sistema de Agendamento</h1>
      </header>

      <main className="App-main">
        <section className="coluna-esquerda">
          {/* Passamos a função de salvar para o formulário */}
          <FormAgendamento aoSalvar={adicionarAgendamento} />
        </section>
        
        <section className="coluna-direita">
          {/* Passamos a lista atualizada para a tabela */}
          <TabelaAgendamento lista={agendamentos} />
        </section>
      </main>
    </div>
  );
}

export default App;