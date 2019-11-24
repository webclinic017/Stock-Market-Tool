const express = require("express");
var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const Security = require("../models/security");
const Reported = require("../models/reported");
const Scorecard = require("../models/scorecard");
const Rating = require("../models/rating");
const checkAuth = require("../middleware/check-auth");
const tickerDataService = require("../services/tickerDataService");
const jsonifyBadJsonService = require("../services/jsonifyBadJsonService")
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

router.post("/scorecard", (req, res, next) => {
    Scorecard.findOne({ symbol: req.body.ticker })
    .then(scorecard => {
        if(!scorecard) {
            return res.status(401).json({
                message: "Scorecard for security not found in database!"
            });
        }
        Rating.findOne({ symbol: req.body.ticker })
        .then(rating => {
            if(!rating) {
                return res.status(401).json({
                    message: "Rating Data for security not found in database!"
                });
            }
            res.status(200).json({
                Solvency: {
                    CashRatio: scorecard["CASH_RATIO"][1],
                    CashRatioRating: rating["CASH_RATIO"][1],
                    CashAndShortTermInvestments: scorecard["CASH_STI_RATIO"][1],
                    CashAndShortTermInvestmentsRating: rating["CASH_STI_RATIO"][1],
                    CashServiceRatio: scorecard["CASH_SERVICE_RATIO"][1],
                    CashServiceRatioRating: rating["CASH_SERVICE_RATIO"][1],
                    InterestServiceRatio: scorecard["INT_SERVICE_RATIO"][1],
                    InterestServiceRatioRating: rating["INT_SERVICE_RATIO"][1],
                    DebtServiceRatio: scorecard["DEBT_SERVICE_RATIO"][1],
                    DebtServiceRatioRating: rating["DEBT_SERVICE_RATIO"][1],
                    CashToShortTermDebtRatio: scorecard["CASH_ST_DEBT_RATIO"][1],
                    CashToShortTermDebtRatioRating: rating["CASH_ST_DEBT_RATIO"][1],
                    AcidTestRatio: scorecard["ACID_TEST"][1],
                    AcidTestRatioRating: rating["ACID_TEST"][1],
                    QuickRatioDef1: scorecard["QUICK_RATIO"][1],
                    QuickRatioDef1Rating: rating["QUICK_RATIO"][1],
                    QuickRatioDef2: scorecard["QUICK_RATIO_2"][1],
                    QuickRatioDef2Rating: rating["QUICK_RATIO_2"][1],
                    CurrentRatio: scorecard["CURRENT_RATIO"][1],
                    CurrentRatioRating: rating["CURRENT_RATIO"][1],
                    NetWorkingCapitalToAssets: scorecard["NWC_TO_TA"][1],
                    NetWorkingCapitalToAssetsRating: rating["NWC_TO_TA"][1]
                },
                CapitalStructure: {
                    ChangeInShortTermDebt: scorecard["CHG_ST_DEBT"][1],
                    ChangeInShortTermDebtRating: rating["CHG_ST_DEBT"][1],
                    ChangeInLongTermDebt: scorecard["CHG_LT_DEBT"][1],
                    ChangeInLongTermDebtRating: rating["CHG_LT_DEBT"][1],
                    ChangeInNetDebt: scorecard["CHG_NET_DEBT"][1],
                    ChangeInNetDebtRating: rating["CHG_NET_DEBT"][1],
                    NetDebt: scorecard["NET_DEBT"][1],
                    NetDebtRating: rating["NET_DEBT"][1],
                    ShortTermObligationsRatio: scorecard["TOTAL_CURR_LIAB_RATIO"][1],
                    ShortTermObligationsRatioRating: rating["TOTAL_CURR_LIAB_RATIO"][1],
                    LongTermDebtRatio: scorecard["LT_DEBT_RATIO"][1],
                    LongTermDebtRatioRating: rating["LT_DEBT_RATIO"][1],
                    DebtRatio: scorecard["DEBT_RATIO"][1],
                    DebtRatioRating: rating["DEBT_RATIO"][1],
                    DebtEquityRatio: scorecard["DEBT_EQ_RATIO"][1],
                    DebtEquityRatioRating: rating["DEBT_EQ_RATIO"][1],
                    FixedCoverageChargeRatio: scorecard["FIXED_CHARGE_COVERAGE"][1],
                    FixedCoverageChargeRatioRating: rating["FIXED_CHARGE_COVERAGE"][1],
                    DegreeOfCombinedLeverage: scorecard["DEGREE_COMBINED_LEV"][1],
                    DegreeOfCombinedLeverageRating: rating["DEGREE_COMBINED_LEV"][1],
                    DegreeOfOperatingLeverage: scorecard["DEGREE_OPERATING_LEV"][1],
                    DegreeOfOperatingLeverageRating: rating["DEGREE_OPERATING_LEV"][1],
                    DegreeOfFinancialLeverage: scorecard["DEGREE_FINANCIAL_LEV"][1],
                    DegreeOfFinancialLeverageRating: rating["DEGREE_FINANCIAL_LEV"][1],
                    DegreeOfFinancialLeverageRatio: scorecard["DFL_RATIO"][1],
                    DegreeOfFinancialLeverageRatioRating:  rating["DFL_RATIO"][1],
                    FinancialLeverageRatio: scorecard["FINANCIAL_LEVERAGE"][1],
                    FinancialLeverageRatioRating: rating["FINANCIAL_LEVERAGE"][1],
                    EquityRatio: scorecard["EQUITY_RATIO"][1],
                    EquityRatioRating: rating["EQUITY_RATIO"][1],
                    EquityMultiplierDef1: scorecard["EQUITY_MULTIPLIER_RATIO_1"][1],
                    EquityMultiplierDef1Rating: rating["EQUITY_MULTIPLIER_RATIO_1"][1],
                    EquityMultiplierDef2: scorecard["EQUITY_MULTIPLIER_RATIO_2"][1],
                    EquityMultiplierDef2Rating: rating["EQUITY_MULTIPLIER_RATIO_2"][1],
                    NetAssetValue: scorecard["NAV"][1],
                    NetAssetValueRating: rating["NAV"][1],
                    EffectiveInterestRate: scorecard["EFFECTIVE_INT_RATE"][1],
                    EffectiveInterestRateRating: rating["EFFECTIVE_INT_RATE"][1],
                    DebtCostOfCapital: scorecard["DEBT_COST_CAP"][1],
                    DebtCostOfCapitalRating: rating["DEBT_COST_CAP"][1],
                    EquityCostOfCapital: scorecard["FAIR_RETURN_RATE"][1],
                    EquityCostOfCapitalRating: rating["FAIR_RETURN_RATE"][1],
                    WeightAvgCostOfCapital: scorecard["WACC"][1],
                    WeightAvgCostOfCapitalRating: rating["WACC"][1]
                },
                AssetActivity: {
                    SalesTurnover: scorecard["SALES_TURNOVER"][1],
                    SalesTurnoverRating: rating["SALES_TURNOVER"][1],
                    DaysSalesOutstanding: scorecard["DSO"][1],
                    DaysSalesOutstandingRating: rating["DSO"][1],
                    InventorySalesTurnover: scorecard["INV_SALES_TURNOVER"][1],
                    InventorySalesTurnoverRating: rating["INV_SALES_TURNOVER"][1],
                    DaysSalesInventory: scorecard["DSI"][1],
                    DaysSalesInventoryRating: rating["DSI"][1],
                    InventoryTurnoverCOGS: scorecard["INV_COGS_TURNOVER"][1],
                    InventoryTurnoverCOGSRating: rating["INV_COGS_TURNOVER"][1],
                    DaysInventoryOutstanding: scorecard["DIO"][1],
                    DaysInventoryOutstandingRating: rating["DIO"][1],
                    CreditorsTurnover: scorecard["CREDITORS_TURNOVER"][1],
                    CreditorsTurnoverRating: rating["CREDITORS_TURNOVER"][1],
                    CreditorsDaysOutstanding: scorecard["CDO"][1],
                    CreditorsDaysOutstandingRating: rating["CDO"][1],
                    AccountsReceivablesTurnover: scorecard["RECEIVABLES_ACCTS_TURNOVER"][1],
                    AccountsReceivablesTurnoverRating: rating["RECEIVABLES_ACCTS_TURNOVER"][1],
                    DaysReceivablesOutstanding: scorecard["DRO"][1],
                    DaysReceivablesOutstandingRating: rating["DRO"][1],
                    WorkingCapitalTurnover: scorecard["WORKING_CAP_TURNOVER"][1],
                    WorkingCapitalTurnoverRating: rating["WORKING_CAP_TURNOVER"][1],
                    DaysWorkingCapital: scorecard["DWC"][1],
                    DaysWorkingCapitalRating: rating["DWC"][1],
                    AssetTurnover: scorecard["ASSET_TURNOVER"][1],
                    AssetTurnoverRating: rating["ASSET_TURNOVER"][1],
                    AssetTurnRate: scorecard["ASSET_TURN_RATE"][1],
                    AssetTurnRateRating: rating["ASSET_TURN_RATE"][1],
                    LongTermAssetTurnover: scorecard["LT_ASSET_TURNOVER"][1], 
                    LongTermAssetTurnoverRating: rating["LT_ASSET_TURNOVER"][1],  
                    LongTermAssetRate: scorecard["LT_ASSET_TURN_RATE"][1],
                    LongTermAssetRateRating: rating["LT_ASSET_TURN_RATE"][1],
                    CashConversionCycle: scorecard["CCC"][1],
                    CashConversionCycleRating: rating["CCC"][1],
                    ReturnOnInvestments: scorecard["ROI_INVESTMENTS"][1],
                    ReturnOnInvestmentsRating: rating["ROI_INVESTMENTS"][1]
                },
                LiabilityActivity: {
                    PayablesTurnoverCOGS: scorecard["PAYABLES_TURNOVER_COGS"][1],
                    PayablesTurnoverCOGSRating: rating["PAYABLES_TURNOVER_COGS"][1],
                    COGSDaysPayablesOutstanding: scorecard["DPO_COGS"][1],
                    COGSDaysPayablesOutstandingRating: rating["DPO_COGS"][1],
                    COSPayablesTurnover: scorecard["PAYABLES_TURNOVER_COS"][1],
                    COSPayablesTurnoverRating: rating["PAYABLES_TURNOVER_COS"][1],
                    COSDaysPayablesOutstanding: scorecard["DPO_COS"][1],
                    COSDaysPayablesOutstandingRating: rating["DPO_COS"][1],
                    LiabilitiesTurnover: scorecard["LIAB_TURNOVER"][1],
                    LiabilitiesTurnoverRating: rating["LIAB_TURNOVER"][1],  
                    LiabilitiesTurnoverRate: scorecard["LIAB_TURN_RATE"][1],
                    LiabilitiesTurnoverRateRating: rating["LIAB_TURN_RATE"][1],
                    ChangeInDebtObligations: scorecard["CHG_DEBT_REPAYMENT_REQ"][1],
                    ChangeInDebtObligationsRating: rating["CHG_DEBT_REPAYMENT_REQ"][1],
                    DebtorsPaybackPeriod: scorecard["DEBTORS_PAYBACK_PERIOD"][1],  
                    DebtorsPaybackPeriodRating: rating["DEBTORS_PAYBACK_PERIOD"][1],   
                    BurnRate: scorecard["BURN_RATE"][1],
                    BurnRateRating: rating["BURN_RATE"][1]
                },
                ProfitabilityAndDividends: {
                    Earnings: scorecard["EPS_DILUTED_NI"][1], 
                    EarningsRating: rating["EPS_DILUTED_NI"][1],
                    EBITCashflow: scorecard["EPS_DILUTED_EBIT"][1], 
                    EBITCashflowRating: rating["EPS_DILUTED_EBIT"][1],
                    ReturnOnSales: scorecard["ROS"][1],
                    ReturnOnSalesRating: rating["ROS"][1],
                    ReturnOnEquity: scorecard["ROE"][1],
                    ReturnOnEquityRating: rating["ROE"][1], 
                    DupontROE: scorecard["DUPONT_SYSTEM_1"][1],    
                    DupontROERating: rating["DUPONT_SYSTEM_1"][1],
                    ReturnOnAssets: scorecard["ROA"][1],
                    ReturnOnAssetsRating: rating["ROA"][1],
                    NIReturnOnCapitalEmployed: scorecard["ROCE_NI"][1],
                    NIReturnOnCapitalEmployedRating: rating["ROCE_NI"][1], 
                    EBITReturnOnCapitalEmployed: scorecard["ROCE_EBIT"][1],
                    EBITReturnOnCapitalEmployedRating: rating["ROCE_EBIT"][1], 
                    PERatio: scorecard["PE"][1],    
                    PERatioRating: rating["PE"][1],           
                    ThreeYearPERatioAverage: scorecard["PE_REL_3"][1],  
                    ThreeYearPERatioAverageRating: rating["PE_REL_3"][1],      
                    FiveYearPERatioAverage: scorecard["PE_REL_5"][1],  
                    FiveYearPERatioAverageRating: rating["PE_REL_5"][1],      
                    EarningsPower: scorecard["EARNINGS_POWER"][1],    
                    EarningsPowerRating: rating["EARNINGS_POWER"][1],
                    GrossProfitMargin: scorecard["GROSS_MARGIN"][1],  
                    GrossProfitMarginRating: rating["GROSS_MARGIN"][1],  
                    NetOperatingProfitAfterTax: scorecard["NOPAT_EBIT"][1], 
                    NetOperatingProfitAfterTaxRating: rating["NOPAT_EBIT"][1],
                    ReturnOnInvestedCapital: scorecard["ROIC"][1], 
                    ReturnOnInvestedCapitalRating: rating["ROIC"][1],
                    OperatingExpensesRatio: scorecard["OPERATING_RATIO"][1], 
                    OperatingExpensesRatioRating: rating["OPERATING_RATIO"][1],
                    OperatingProfitRatio: scorecard["OP_PROFIT_MARGIN"][1], 
                    OperatingProfitRatioRating: rating["OP_PROFIT_MARGIN"][1],
                    RetentionRatio: scorecard["RETENTION_RATIO"][1], 
                    RetentionRatioRating: rating["RETENTION_RATIO"][1],
                    DividendPayoutRatio: scorecard["DIV_PAYOUT_RATIO"][1], 
                    DividendPayoutRatioRating: rating["DIV_PAYOUT_RATIO"][1],
                    EarningsYield: scorecard["EARNINGS_YIELD"][1], 
                    EarningsYieldRating: rating["EARNINGS_YIELD"][1],
                    DividendYield: scorecard["DIVS_YIELD"][1],
                    DividendYieldRating: rating["DIVS_YIELD"][1],        
                    SustainableGrowthRate: scorecard["SGR"][1],
                    SustainableGrowthRateRating: rating["SGR"][1]
                },
                Valuation: {
                    MarketValue: scorecard["MV"][1],
                    MarketValueRating: rating["MV"][1], 
                    CashAndEquivalentsToPrice: scorecard["CASH_PRICE_RATIO"][1],
                    CashAndEquivalentsToPriceRating: rating["CASH_PRICE_RATIO"][1], 
                    NetAssetValueToPrice: scorecard["PRICE_NAV"][1],
                    NetAssetValueToPriceRating: rating["PRICE_NAV"][1], 
                    EBITCashFlowToPrice: scorecard["MV_EBIT_RATIO"][1],
                    EBITCashFlowToPriceRating: rating["MV_EBIT_RATIO"][1], 
                    FreeCashFlowToPrice: scorecard["PRICE_FCF"][1],
                    FreeCashFlowToPriceRating: rating["PRICE_FCF"][1], 
                    UnleveredFreeCashFlowToPrice: scorecard["PRICE_UN_FCF"][1],
                    UnleveredFreeCashFlowToPriceRating: rating["PRICE_UN_FCF"][1], 
                    SalesToPrice: scorecard["PRICE_SALES"][1],
                    SalesToPriceRating: rating["PRICE_SALES"][1], 
                    BookValueToPrice: scorecard["PRICE_BOOK"][1],
                    BookValueToPriceRating: rating["PRICE_BOOK"][1], 
                    OriginalGrahamValuation: scorecard["ORIG_GRAHAM"][1],
                    OriginalGrahamValuationRating: rating["ORIG_GRAHAM"][1], 
                    RevisedGrahamValuation: scorecard["REVISED_GRAHAM"][1],
                    RevisedGrahamValuationRating: rating["REVISED_GRAHAM"][1], 
                    DCFValuation: scorecard["INTRINSIC_VALUE_NI"][1],
                    DCFValuationRating: rating["INTRINSIC_VALUE_NI"][1], 
                    MarginOfSafety: scorecard["MARGIN_OF_SAFETY_NI"][1],
                    MarginOfSafetyRating: rating["MARGIN_OF_SAFETY_NI"][1], 
                    DCFValuation: scorecard["INTRINSIC_VALUE_EBIT"][1],
                    DCFValuationRating: rating["INTRINSIC_VALUE_EBIT"][1], 
                    MarginOfSafety: scorecard["MARGIN_OF_SAFETY_EBIT"][1],
                    MarginOfSafetyRating: rating["MARGIN_OF_SAFETY_EBIT"][1], 
                    DCFValuation: scorecard["INTRINSIC_VALUE_FCF"][1],
                    DCFValuationRating: rating["INTRINSIC_VALUE_FCF"][1], 
                    MarginOfSafety: scorecard["MARGIN_OF_SAFETY_FCF"][1],
                    MarginOfSafetyRating: rating["MARGIN_OF_SAFETY_FCF"][1], 
                    EnterpriseValuation: scorecard["EV"][1],
                    EnterpriseValuationRating: rating["EV"][1], 
                    NetIncomeToEnterpriseValuation: scorecard["EV_NI"][1],
                    NetIncomeToEnterpriseValuationRating: rating["EV_NI"][1], 
                    EBITToEnterpriseValuation: scorecard["EV_EBIT"][1],
                    EBITToEnterpriseValuationRating: rating["EV_EBIT"][1], 
                    BookValue: scorecard["BV"][1],
                    BookValueRating: rating["BV"][1], 
                    BookValuePerShare: scorecard["BV_PER_SHARE"][1],
                    BookValuePerShareRating: rating["BV_PER_SHARE"][1], 
                    NetIncomeToBookValue: scorecard["BV_NI"][1],
                    NetIncomeToBookValueRating: rating["BV_NI"][1], 
                    EBITToBookValue: scorecard["BV_EBIT"][1],
                    EBITToBookValueRating: rating["BV_EBIT"][1]
                }
            });
        })
        .catch(err => {
            return res.status(401).json({
                message: "Rating lookup failed!"
            });
        });
    })
    .catch(err => {
        return res.status(401).json({
            message: "Scorecard lookup failed!"
        });
    });
});

router.post("/getIntrinsicValue", /*checkAuth,*/ (req, res, next) => { 
    Reported.findOne({ symbol: req.body.ticker })
    .then(reported => {
        if(!reported) {
            return res.status(401).json({
                message: "Reported security not found in database!"
            });
        }
        const cleanTicker = tickerDataService.getCleanTickerData(reported);
        const corporateAAA = 3.04;
        const corporateAAAOld = 4.4;
        const PEValue = 20.037027;
        const gCoefficient = -10.682356;
        const bias = 26.22732;
        var dilWeightAvgShares = cleanTicker["fiscalYears"][0]["incomeSheet"]["dilWeightAvgShares"];
        var niAvailCommonGaap = cleanTicker["fiscalYears"][0]["incomeSheet"]["niAvailCommonGaap"];
        var EPS = niAvailCommonGaap / dilWeightAvgShares;
        var priorDilWeightAvgShares = cleanTicker["fiscalYears"][1]["incomeSheet"]["dilWeightAvgShares"];
        var priorNiAvailCommonGaap = cleanTicker["fiscalYears"][1]["incomeSheet"]["niAvailCommonGaap"];
        var priorEPS = priorNiAvailCommonGaap / priorDilWeightAvgShares;
        var growthRate = (EPS - priorEPS)/priorEPS;
        var intrinsicValue = ((EPS * (PEValue + gCoefficient * growthRate) * corporateAAAOld) / corporateAAA) + bias;
        getCurrentPrice(req.body.ticker, function(){
            var price = this;
            var shouldRecommend = intrinsicValue / price > 1.5;
            if(shouldRecommend) {
                return res.status(200).json({
                    recommend: true,
                    currentPrice: price,
                    intrinsicValue: intrinsicValue
                });
            }
            else {
                return res.status(200).json({
                    recommend: false,
                    currentPrice: price,
                    intrinsicValue: intrinsicValue
                });
            }
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
        res.status(200).json(reported);
    })
    .catch(err => {
        return res.status(401).json({
            message: "Reported security lookup failed!"
        });
    });
});

router.get("/currentPrice", (req, res, next) => {
    const Http = new XMLHttpRequest();
    const url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + req.body.ticker + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
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
    const url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + req.body.keywords + '&apikey=OjdkMzliY2VkOWVlYTZjYjNlYzg2NDkxZDBmMzVjZTdi';
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
