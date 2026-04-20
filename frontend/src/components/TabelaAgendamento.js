import React, { Component } from 'react';
import './TabelaAgendamento.css';

class TabelaAgendamento extends Component {
  render() {
    // Agora os dados não vêm mais do 'this.state', mas sim do 'this.props.lista'
    const { lista } = this.props;

    return (
      <div className="tabela-container">
        <h3>📋 Agendamentos do Dia</h3>
        <table>
          <thead>
            <tr>
              <th>Cliente</th>
              <th>Veículo (Placa)</th>
              <th>Serviço</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {/* ESTE É O MAP QUE VOCÊ PROCURAVA: */}
            {lista && lista.map(item => (
              <tr key={item.id}>
                <td>{item.cliente}</td>
                <td>{item.veiculo} ({item.placa})</td>
                <td>{item.servico}</td>
                <td>
                  <span className={`badge ${item.status.toLowerCase()}`}>
                    {item.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default TabelaAgendamento;