const express = require('express');
const app = express();
require('dotenv').config();

const port = process.env.PORT || 3000;

// Middleware to process JSON
app.use(express.json());

// POST text
app.post('/receive-text', (req, res) => {
    const { text } = req.body; // Desestruturando o texto enviado no JSON
    if (!text) {
        return res.status(400).json({ message: 'Texto não fornecido!' });
    }
    console.log(`Texto recebido: ${text}`);
    res.json({ message: 'Texto recebido com sucesso!', text });
});

// GET text
app.get('/send-text', (req, res) => {
    const text = 'Este é um exemplo de texto retornado.';
    res.json({ text });
});

// Init server
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
