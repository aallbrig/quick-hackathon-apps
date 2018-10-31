const express = require('express');
const router = express.Router();
const Database = require('../Database');
const db = new Database();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.setHeader('Content-Type', 'application/json');
  res.send(db.healthCheck());
});

module.exports = router;
