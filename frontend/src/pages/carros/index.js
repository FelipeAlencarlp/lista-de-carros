import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from '../../components/Header'
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import api from '../../services/api';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';

import './carros.css';

const Lists = () => {
  const [token] = useState(localStorage.getItem('token'));
  const [carrosList, setCarrosList] = useState([]);
  const history = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('token');
    api.get('/api/cars', {
      headers: {
        Authorization: `Bearer ${token}`,
      }
    }).then(response => {
      if (response.data.status && response.data.status === (401 || 498)) {
        localStorage.clear();
        history('/');
      } else {
        setCarrosList(response.data);
      }
    }).catch(error => {
      if (error.response) {
        console.error("Erro de resposta:", error.response.data);
        console.error("Status do erro:", error.response.status);
        console.error("Cabeçalhos da resposta:", error.response.headers);
      } else if (error.request) {
        console.error("Erro de solicitação:", error.request);
      } else {
        console.error("Erro geral:", error.message);
      }
      console.error("Configuração da solicitação:", error.config);
    });
  }, [token, history]);
  
  return (
    <React.Fragment>
      <Header />

      <Container maxWidth="xl">
        <Grid container spacing={2}>
          {carrosList && carrosList.length > 0 ? carrosList.map((list) => 
            ( 
              <Grid item xs={3} key={list.id}>
                <Card sx={{ maxWidth: 345 }}>
                  <CardMedia
                    sx={{ height: 240 }}
                    image={list.foto}
                    title="green iguana"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h6" component="div">
                      {list.nome}
                    </Typography>
                    {(list.ano || list.km || list.cidade) && (
                      <Typography variant="body2" color="text.secondary">
                        {`${list.ano} ${list.km} ${list.cidade}`}
                      </Typography>
                    )}
                    {list.valor &&
                    <Typography gutterBottom variant="h5" component="div" color="#304ffe">
                      R$ {list.valor}
                    </Typography>
                    }
                  </CardContent>
                </Card>
              </Grid>
            )) : null 
          }
        </Grid>
      </Container>
    </React.Fragment>
  );

}

export default Lists;