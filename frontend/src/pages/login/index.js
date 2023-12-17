import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FiChevronsRight } from 'react-icons/fi';

import api from '../../services/api';

import './login.css';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const history = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();

    try {
      const response = await api.post('/api/auth/login', { email, password });
      localStorage.setItem('token', response.data.token);

      history('/');
    } catch (err) {
      alert('Erro ao tentar efetuar login, tente novamente.');
    }
  }

  return (
    <div className="login-container">
      <section className="form">

        <form onSubmit={handleLogin}>
          <input 

            placeholder="E-mail"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />
          <input 
            placeholder="Senha"
            type="password"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />

          <button className="button" type="submit">Entrar</button>

          <Link className="back-link" to="/register">
            <FiChevronsRight size={18} color="#3498db" />
            Cadastre-se
          </Link>
        </form>
      </section>
    </div>
  );
}