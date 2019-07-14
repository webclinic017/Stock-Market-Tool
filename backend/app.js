const express = require("express");
const bodyParser = require("body-parser");
const mongoose = require("mongoose");

const userRoutes = require("./routes/users");
const securityRoutes = require("./routes/securitys");

const User = require("./models/user");
const Security = require("./models/security");

const app = express();
mongoose.connect("mongodb+srv://DanielCanas:WSgnHp2IM8zOmqov@cluster0-988hr.mongodb.net/market-predictor?retryWrites=true&w=majority")
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

//app.use("/home", (req, res, next) => {
  //res.status(201).json({
    //message: 'Welcome to the server!'
  //});
//});

app.use("/api/user", userRoutes);
app.use("/api/security", securityRoutes);

module.exports = app;
