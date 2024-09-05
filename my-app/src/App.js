// src/App.js
import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Box, Paper } from '@mui/material';

function App() {
  const [projectName, setProjectName] = useState('');
  const [department, setDepartment] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handlePredict = async () => {
    const response = await fetch('http://localhost:3000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        project_name: projectName,
        department: department,
      }),
    });

    const data = await response.json();
    setPrediction(data);
  };

  return (
    <Container maxWidth="sm">
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 5 }}>
        <Typography variant="h4" gutterBottom>
          Projektprognose
        </Typography>
        <TextField
          label="Projektname"
          variant="outlined"
          fullWidth
          margin="normal"
          value={projectName}
          onChange={(e) => setProjectName(e.target.value)}
        />
        <TextField
          label="Department"
          variant="outlined"
          fullWidth
          margin="normal"
          value={department}
          onChange={(e) => setDepartment(e.target.value)}
        />
        <Button variant="contained" color="primary" onClick={handlePredict} fullWidth sx={{ mt: 3 }}>
          Prognose abrufen
        </Button>

        {prediction && (
          <Paper elevation={3} sx={{ padding: 3, mt: 3, width: '100%' }}>
            <Typography variant="h6">Prognose:</Typography>
            <Typography>Länge des Projekts: {prediction.project_length}</Typography>
            <Typography>Kosten des Projekts: {prediction.project_cost}</Typography>
          </Paper>
        )}
      </Box>
    </Container>
  );
}

export default App;
