const dbCredentials = require('./dbCredentials');

const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const userRoutes = require("./routes/users");
const securityRoutes = require("./routes/securitys");
const pytonCommunicationRoutes = require("./routes/pythonCommunication");

const User = require("./models/user");
const Security = require("./models/security");

const dbUsername = dbCredentials.username;
const dbPassword = dbCredentials.password;

const app = express();
mongoose.connect(`mongodb+srv://${dbUsername}:${dbPassword}@cluster0-988hr.mongodb.net/market-predictor?retryWrites=true&w=majority`)
  .then(() => {
    console.log("Connection with database established!");
  })
  .catch(() => {
    console.log("Could not establish connection with the database!");
  });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use((req, res, next) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS");
  next();
});

/*app.options("/*", function(req, res, next) {
        res.header('Access-Control-Allow-Origin', '*');
        res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
        res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');
        res.send(200);
    });*/

app.use("/api/user", userRoutes);
app.use("/api/security", securityRoutes);
app.use("/api/communications", pytonCommunicationRoutes);

module.exports = app;
