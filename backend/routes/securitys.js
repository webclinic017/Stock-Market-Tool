const express = require("express");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Security = require("../models/security");
const Reported = require("../models/reported");
const checkAuth = require("../middleware/check-auth");
const tickerDataService = require("../services/tickerDataService");
const router = express.Router();

function getCurrentPrice(ticker, callback) {
    const Http = new XMLHttpRequest();
    const url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + ticker + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
    Http.open("GET", url, true);
    Http.send();

    Http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var myObj = JSON.parse(this.responseText);
          if(myObj.hasOwnProperty('Error Message')) {
              callback.apply(-1);
              return;
          }
          callback.apply(parseFloat(myObj["Global Quote"]["05. price"]));
        }
    };
}

router.get("/scorecard", (req, res, next) => {
    Reported.findOne({ symbol: req.query.ticker })
    .then(reported => {
        if(!reported) {
            return res.status(401).json({
                message: "Reported security not found in database!"
            });  
        }
        getCurrentPrice(req.query.ticker, function(){
            var price = this;
            //var spawn = require("child_process").spawn;
            var spawn = require("child_process");
            var process = spawn.spawnSync('python', ["././financial-logic/test.py", reported, price.toString()]);
            console.log(process.stdout.toString());
            return res.send(process.stdout.toString());
            //return res.send(process.stdout.toString());
            //console.log("We start here!");
            //process.stdout.on('data', function(data) { 
                //console.log("We are finally in here!");
                //return res.send(data.toString());
            //})
            //console.log("Now we are here!");
        });
    })
    .catch(err => {
        return res.status(401).json({
            message: "Reported security lookup failed!"
        });
    });
});

router.post("/getReportedTicker", /*checkAuth,*/ (req, res, next) => { // TODO: Put back auth once ML no longer needs to hit this.
    Reported.findOne({ symbol: req.body.ticker })
    .then(reported => {
        if(!reported) {
            return res.status(401).json({
                message: "Reported security not found in database!"
            });
        }
        const reportedTicker = tickerDataService.getCleanTickerData(reported);
        const reportedResponse = {};
        reportedResponse.ticker = reportedTicker
        res.status(200).json(reportedResponse);
    })
    .catch(err => {
        return res.status(401).json({
            message: "Reported security lookup failed!"
        });
    });
});

router.get("/currentPrice", (req, res, next) => {
    const Http = new XMLHttpRequest();
    const url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + req.query.ticker + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
    Http.open("GET", url, true);
    Http.send();

    Http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var myObj = JSON.parse(this.responseText);
          if(myObj.hasOwnProperty('Error Message')) {
              return res.status(401).json({
                message: "Error obtaning price data from API!"
              });
          }
          res.status(200).json(myObj["Global Quote"]["05. price"]);
        }
    };
});

router.get("/searchTicker", (req, res, next) => {
    const Http = new XMLHttpRequest();
    const url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + req.query.keywords + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
    Http.open("GET", url, true);
    Http.send();

    Http.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          var myObj = JSON.parse(this.responseText);
          console.log(myObj);
          if(myObj.hasOwnProperty('Error Message')) {
              return res.status(401).json({
                message: "Error searching for ticker!"
              });
          }
          res.status(200).json(myObj);
        }
    };
});

module.exports = router;
