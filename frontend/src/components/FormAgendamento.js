import React, { Component } from 'react';
import './FormAgendamento.css';

class FormAgendamento extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cliente: '',
      veiculo: '',
      placa: '',
      servico: 'lavagem-simples',
      dataHora: ''
    };
  }

  // Função para capturar o que o usuário digita (Igual ao Login!)
  handleChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  }

  handleSubmit = (e) => {
    e.preventDefault();
    console.log("Dados salvos no State:", this.state);
    alert(`Agendamento de ${this.state.veiculo} para o cliente ${this.state.cliente} realizado!`);
    // Aqui no futuro chamaremos a API do Django usando Axios
  }

  render() {
    return (
      <div className="form-agendamento">
        <h3>🚗 Novo Agendamento</h3>
        <form onSubmit={this.handleSubmit}>
          <div className="campo">
            <label>Nome do Cliente</label>
            <input type="text" name="cliente" placeholder="Ex: Matheus" onChange={this.handleChange} required />
          </div>

          <div className="campo">
            <label>Veículo / Modelo</label>
            <input type="text" name="veiculo" placeholder="Ex: Fiat Argo" onChange={this.handleChange} required />
          </div>

          <div className="campo">
            <label>Placa</label>
            <input type="text" name="placa" placeholder="ABC-1234" onChange={this.handleChange} required />
          </div>

          <div className="campo">
            <label>Tipo de Serviço</label>
            <select name="servico" onChange={this.handleChange}>
              <option value="lavagem-simples">Lavagem Simples</option>
              <option value="lavagem-completa">Lavagem Completa</option>
              <option value="polimento">Polimento</option>
              <option value="higienizacao">Higienização Interna</option>
            </select>
          </div>

          <div className="campo">
            <label>Data e Hora</label>
            <input type="datetime-local" name="dataHora" onChange={this.handleChange} required />
          </div>

          <button type="submit" className="botao-agendar">Confirmar Agendamento</button>
        </form>
      </div>
    );
  }
}

export default FormAgendamento;