'use strict';

const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const twilio = require('twilio');

const twilioClient = new twilio(
  process.env.TWILIO_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true  }));

app.post('/send_text', function(req, res){
  console.log(req.body);

  const message = twilioClient.messages.create({
    body: req.body.sms_text,
    to: req.body.phone_number,
    from: process.env.TWILIO_FROM_NUMBER
  });

  message.then(function(message) {
    console.log(message);
    res.redirect('/thank-you.html');
  });

  message.catch(function(error) {
    console.log(error);
    res.send("there was an error in sending SMS");
  });

  console.log(message);
  // res.send("recieved your request!");
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
