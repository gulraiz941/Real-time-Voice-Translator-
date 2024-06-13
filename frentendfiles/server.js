// index.js
const express = require('express');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient();
const app = express();

app.use(express.json());
app.use(cookieParser());
app.use(session({
  secret: 'your-secret-key',
  resave: false,
  saveUninitialized: true,
}));

// Prisma schema (prisma/schema.prisma)
// ... (same as mentioned in the previous response)

// Routes
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  const user = await prisma.user.findUnique({
    where: { username },
  });

  if (user && user.password === password) {
    req.session.userId = user.id;
    res.json({ success: true, message: 'Login successful' });
  } else {
    res.json({ success: false, message: 'Invalid credentials' });
  }
});

app.post('/logout', (req, res) => {
  req.session.destroy(() => {
    res.json({ success: true, message: 'Logout successful' });
  });
});

// Server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});