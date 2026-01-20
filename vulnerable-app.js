const express = require('express');
const mysql = require('mysql2');
const app = express();

// Database connection
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'testdb'
});

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// VULNERABILITY 1: SQL Injection in login endpoint
app.post('/login', (req, res) => {
  const { username, password } = req.body;
  
  // Direct string concatenation - SQL injection vulnerability
  const query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
  
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
      return;
    }
    
    if (results.length > 0) {
      res.json({ success: true, user: results[0] });
    } else {
      res.status(401).json({ error: 'Invalid credentials' });
    }
  });
});

// VULNERABILITY 2: SQL Injection in search endpoint
app.get('/search', (req, res) => {
  const searchTerm = req.query.q;
  
  // Template literal with user input - SQL injection vulnerability
  const query = `SELECT * FROM products WHERE name LIKE '%${searchTerm}%' OR description LIKE '%${searchTerm}%'`;
  
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
      return;
    }
    res.json(results);
  });
});

// VULNERABILITY 3: SQL Injection in user profile endpoint
app.get('/user/:id', (req, res) => {
  const userId = req.params.id;
  
  // No input validation and direct concatenation
  const query = "SELECT id, username, email, created_at FROM users WHERE id = " + userId;
  
  connection.query(query, (error, results) => {
    if (error) {
      res.status(500).json({ error: 'Database error' });
      return;
    }
    res.json(results[0]);
  });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});