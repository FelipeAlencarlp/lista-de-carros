import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FiPower } from 'react-icons/fi';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';

export default function Header() {
  const [token] = useState(localStorage.getItem('token'));
  const navigate = useNavigate();

  function handleLogout() {
    localStorage.clear();
    window.location.reload(false);
    navigate('/');
  }

  return (
    <div className="header">
      <AppBar className="menu" position="static">
        <Toolbar>
          <Link to="/" className="menuTitle">
            <h1>Carros a venda (vitrine)</h1>
          </Link>

          {token ? (
            <div>
              <Link to="/" className="menuButton">
                Página inicial
              </Link>
              <Link to="/painel" className="menuButton">
                Painel
              </Link>
              <button
                className="logoutButton"
                onClick={handleLogout}
                title="Sair"
                type="button"
              >
                <FiPower size={18} color="#1f7fc0" />
              </button>
            </div>
          ) : (
            <Link to="/login" className="menuButton">
              Login
            </Link>
          )}
        </Toolbar>
      </AppBar>
    </div>
  );
}
