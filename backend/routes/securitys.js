const express = require("express");
const Security = require("../models/security");

const router = express.Router();

router.get("/info", (req, res, next) => {
    Security.findOne({ ticker: req.query.ticker})
    .then(security => {
        if(!security)
        {
            return res.status(401).json({
                message: 'Security not found in database!'
            });
        }
        res.status(200).json({
            ticker: security.ticker,
            PE: security.PE,
            EY: security.EY,
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

module.exports = router;
