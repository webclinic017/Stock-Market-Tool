const express = require("express");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Security = require("../models/security");
const Reported = require("../models/reported");
const checkAuth = require("../middleware/check-auth");
const tickerDataService = require("../services/tickerDataService");
const router = express.Router();

router.get("/dashboard", checkAuth, (req, res, next) => {
    Security.findOne({ ticker: req.query.ticker })
        .then(security => {
            if(!security) {
                return res.status(401).json({
                    message: "Security not found in database!"
                });
            }
            res.status(200).json({
                ticker: security.ticker,
                CAE: security.CAE,
                STA: security.STA,
                LTA: security.LTA,
                DCF: security.DCF,
                IV: security.IV,
                DC: security.DTCR,
                DE: security.DE,
                ICR: security.ICR,
                DCL: security.DCL,
                DOL: security.DOL,
                DFL: security.DFL,
                PE: security.PE,
                EY: security.EY,
                AbsolutePE: security.AbsolutePE,
                RelativePE: security.RelativePE,
                ROE: security.ROE,
                ROIC: security.ROIC,
                RetentionRatio: security.RetentionRatio,
                SGR: security.SGR,
                ROA: security.ROA,
                PB: security.PB
            });
        })
        .catch(err => {
            return res.status(401).json({
                message: "Security lookup failed!"
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
        res.status(200).json(reportedTicker);
        /*const reportedResponse = {};
        reportedResponse.ticker = reportedTicker
        res.status(200).json(reportedResponse);*/
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
