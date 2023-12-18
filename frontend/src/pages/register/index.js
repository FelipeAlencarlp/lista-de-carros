import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FiChevronsLeft } from 'react-icons/fi';

import api from '../../services/api';
import './register.css';

export default function Register() {
  const [username, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const history = useNavigate();

  async function handleRegister(e) {
    e.preventDefault();

    const data = {
      username,
      email,
      password,
      "confirm_password":confirmPassword,
    };
    
    try {
      api.post('/api/register', data)
      .then(async (res) =>{
        if(res.data.status){
          const responseLogin = await api.post('/api/login', { email, password });
          localStorage.setItem('token', responseLogin.data.token);
          history('/login');
        }
      return history('/login');
      });
    } catch (err) {
      alert('Erro no cadastro, tente novamente.');
    }
  }

  return (
    <div className="register-container">
      <div className="content">
        <section>
          <h1>Cadastre-se Agora!</h1>
          <p>Desfrute de todas as funcionalidades da nossa plataforma registrando-se hoje mesmo. Adicione facilmente os detalhes dos seus carros e usufrua de uma experiência completa para gerenciar sua frota de veículos. Estamos ansiosos para ter você a bordo!</p>

          <Link className="back-link" to="/login">
            <FiChevronsLeft size={18} color="#3498db" />
            Já tenho cadastro
          </Link>
        </section>

        <form onSubmit={handleRegister}>
          <input 
            placeholder="Nome"
            value={username}
            onChange={e => setName(e.target.value)}
          />

          <input 
            type="email" 
            placeholder="Digite seu e-mail"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />

          <input 
            placeholder="Digite sua senha"
            value={password}
            type="password"
            onChange={e => setPassword(e.target.value)}
          />

          <input 
            placeholder="Confirme sua senha"
            value={confirmPassword}
            type="password"
            onChange={e => setConfirmPassword(e.target.value)}
          />

          <button className="button" type="submit">Cadastrar</button>
        </form>
      </div>
    </div>
  );
}