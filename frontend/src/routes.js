import React from 'react';
import { BrowserRouter, Route, Routes as Rout } from 'react-router-dom';
import Carros from './pages/carros';
import Login from './pages/login';
import Register from './pages/register';
import Painel from './pages/painel';

export default function Routes() {
  return (
    <BrowserRouter>
      <Rout>
        <Route path="/" exact element={<Carros/>} />
        <Route path="/login" exact element={<Login/>} />
        <Route path="/register" exact element={<Register/>} />
        <Route path="/painel" exact element={<Painel/>} />
        <Route path="/logout" exact element={<Painel/>} />
      </Rout>
    </BrowserRouter>
  );
}