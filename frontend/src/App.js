import React from 'react';
import './App.css';
import FormAgendamento from './components/FormAgendamento';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Lava Car - Sistema de Agendamento</h1>
      </header>
      
      <main className="App-content">
        <div className="coluna-form">
          <FormAgendamento />
        </div>
        
      </main>
    </div>
  );
}

export default App;