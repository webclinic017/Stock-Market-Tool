/*
 * Parses ticker data from database into a useable format.
 */
function getCleanTickerData(res) {
    const ticker = {};
    const fiscalYears = [];
    const numYears = res.YEAR_INC.length - 1;

    // Let i start at 1 to account for first index being string of field name.
    for (let i = 1; i <= numYears; i++) {
        // Do not record years containing no data.
        if (res.YEAR_INC[i] === null &&
            res.YEAR_BAL[i] === null &&
            res.YEAR_CF[i] === null) {
            continue;
        }
        fiscalYears.push(parseFiscalYear(res, i));
    }

    ticker.fiscalYears = fiscalYears;
    return ticker;
}

/*
 * Parses ticker data from database into a specific year.
 */
function parseFiscalYear(res, yearIndex) {
    const fiscalYear = {};
    if (res.YEAR_INC[yearIndex] !== null) {
        fiscalYear.incomeSheet = parseIncomeSheet(res, yearIndex);
        fiscalYear.year = res.YEAR_INC[yearIndex];
    }
    if (res.YEAR_BAL[yearIndex] !== null) {
        fiscalYear.balanceSheet = parseBalanceSheet(res, yearIndex);
        fiscalYear.year = res.YEAR_BAL[yearIndex];
    }
    if (res.YEAR_CF[yearIndex] !== null) {
        fiscalYear.cashflowSheet = parseCashflowSheet(res, yearIndex);
        fiscalYear.year = res.YEAR_CF[yearIndex];
    }
    return fiscalYear;
}

/*
 * Parses ticker data from specific year into a balance sheet.
 */
function parseBalanceSheet(res, yearIndex) {
    return {
        totalAssets1: res.TOTAL_ASSETS1[yearIndex],
        cashEqSti: res.CASH_EQ_STI[yearIndex],
        cashEq: res.CASH_EQ[yearIndex],
        sti: res.STI[yearIndex],
        acctsRec: res.ACCTS_REC[yearIndex],
        acctsRecNet: res.ACCTS_REC_NET[yearIndex],
        notesRecNet: res.NOTES_REC_NET[yearIndex],
        inv: res.INV[yearIndex],
        rawMat: res.RAW_MAT[yearIndex],
        wip: res.WIP[yearIndex],
        finGoods: res.FIN_GOODS[yearIndex],
        othInv: res.OTH_INV[yearIndex],
        othStAssets: res.OTH_ST_ASSETS[yearIndex],
        derivHedgeAssets1: res.DERIV_HEDGE_ASSETS1[yearIndex],
        taxesReciev: res.TAXES_RECIEV[yearIndex],
        miscStAssets: res.MISC_ST_ASSETS[yearIndex],
        totalCurrAssets: res.TOTAL_CURR_ASSETS[yearIndex],
        ppeNet: res.PPE_NET[yearIndex],
        ppe: res.PPE[yearIndex],
        accDeprec: res.ACC_DEPREC[yearIndex],
        ltiReceivables: res.LTI_RECEIVABLES[yearIndex],
        ltInvest: res.LT_INVEST[yearIndex],
        othLtAssets: res.OTH_LT_ASSETS[yearIndex],
        totalIntAssets: res.TOTAL_INT_ASSETS[yearIndex],
        goodwill: res.GOODWILL[yearIndex],
        othIntAssets: res.OTH_INT_ASSETS[yearIndex],
        prepaidExp: res.PREPAID_EXP[yearIndex],
        deffTaxAssets: res.DEFF_TAX_ASSETS[yearIndex],
        derivHedgeAssets2: res.DERIV_HEDGE_ASSETS2[yearIndex],
        miscAssets: res.MISC_ASSETS[yearIndex],
        totalNonCurrAssets: res.TOTAL_NON_CURR_ASSETS[yearIndex],
        totalAssets2: res.TOTAL_ASSETS2[yearIndex],
        payablesAccruals: res.PAYABLES_ACCRUALS[yearIndex],
        payables: res.PAYABLES[yearIndex],
        accruedTaxes: res.ACCRUED_TAXES[yearIndex],
        intDivsPayables: res.INT_DIVS_PAYABLES[yearIndex],
        othPayablesAccurals: res.OTH_PAYABLES_ACCURALS[yearIndex],
        stDebt: res.ST_DEBT[yearIndex],
        stBorrowings: res.ST_BORROWINGS[yearIndex],
        stFinLeases: res.ST_FIN_LEASES[yearIndex],
        stOpLeases: res.ST_OP_LEASES[yearIndex],
        currLtDebt: res.CURR_LT_DEBT[yearIndex],
        othStLiab: res.OTH_ST_LIAB[yearIndex],
        deffRev1: res.DEFF_REV_1[yearIndex],
        derivHedge1: res.DERIV_HEDGE_1[yearIndex],
        miscStLiab: res.MISC_ST_LIAB[yearIndex],
        totalCurrLiab: res.TOTAL_CURR_LIAB[yearIndex],
        ltDebt: res.LT_DEBT[yearIndex],
        ltBorrow: res.LT_BORROW[yearIndex],
        ltFinLeases: res.LT_FIN_LEASES[yearIndex],
        ltOpLeases: res.LT_OP_LEASES[yearIndex],
        othLtLiab: res.OTH_LT_LIAB[yearIndex],
        accuredLiab: res.ACCURED_LIAB[yearIndex],
        pensionLiab: res.PENSION_LIAB[yearIndex],
        pensions: res.PENSIONS[yearIndex],
        othPostRetBen: res.OTH_POST_RET_BEN[yearIndex],
        deffRev2: res.DEFF_REV_2[yearIndex],
        defTabLiab: res.DEF_TAX_LIAB[yearIndex],
        derivHedge: res.DERIV_HEDGE_2[yearIndex],
        miscLtLiab: res.MISC_LT_LIAB[yearIndex],
        totalNonCurrLiab: res.TOTAL_NON_CURR_LIAB[yearIndex],
        totalLiab: res.TOTAL_LIAB[yearIndex],
        prefEquityHybridCap: res.PREF_EQUITY_HYBRID_CAP[yearIndex],
        shareCapApic: res.SHARE_CAP_APIC[yearIndex],
        commonStock: res.COMMON_STOCK[yearIndex],
        addPaidCap: res.ADD_PAID_CAP[yearIndex],
        treasuryStock: res.TREASURY_STOCK[yearIndex],
        re: res.RE[yearIndex],
        othEquity: res.OTH_EQUITY[yearIndex],
        equityBeforeMinInt: res.EQUITY_BEFORE_MIN_INT[yearIndex],
        minNonControlInt: res.MIN_NON_CONTROL_INT[yearIndex],
        totalEquity: res.TOTAL_EQUITY[yearIndex],
        liabAndEquity: res.LIAB_AND_EQUITY[yearIndex]
    }
}

/*
 * Parses ticker data from specific year into an income sheet.
 */
function parseIncomeSheet(res, yearIndex) {
    return {
        rev: res.REV[yearIndex],
        salesServRev: res.SALES_SERV_REV[yearIndex],
        otherRev: res.OTHER_REV[yearIndex],
        costOfRev: res.COST_OF_REV[yearIndex],
        cogs: res.COGS[yearIndex],
        proft: res.PROFIT[yearIndex],
        otherProfit: res.OTH_PROFIT[yearIndex],
        opExp: res.OP_EXP[yearIndex],
        sgAndAdmin: res.SG_AND_ADMIN[yearIndex],
        sellAndMark: res.SELL_AND_MARK[yearIndex],
        genAndAdmin: res.GEN_AND_ADMIN[yearIndex],
        rAndD: res.R_AND_D[yearIndex],
        depAmort: res.DEP_AMORT[yearIndex],
        othOpExp: res.OTH_OP_EXP[yearIndex],
        opIncLoss: res.OP_INC_LOSS[yearIndex],
        nonOpIncLoss: res.NON_OP_INC_LOSS[yearIndex],
        netIntExp: res.NET_INT_EXP[yearIndex],
        intExp: res.INT_EXP[yearIndex],
        intInc: res.INT_INC[yearIndex],
        forex: res.FOREX[yearIndex],
        affiliates: res.AFFILIATES[yearIndex],
        nonOpInc: res.NON_OP_INC[yearIndex],
        pretaxIncome: res.PRETAX_INCOME[yearIndex],
        currIncTax: res.CURR_INC_TAX[yearIndex],
        IncTax: res.DEFF_INC_TAX[yearIndex],
        contOps: res.CONT_OPS[yearIndex],
        netExtra1: res.NET_EXTRA1[yearIndex],
        discOps: res.DISC_OPS[yearIndex],
        acctChng: res.ACCT_CHNG[yearIndex],
        incomeMi: res.INCOME_MI[yearIndex],
        minInterest: res.MIN_INTEREST[yearIndex],
        niInc: res.NI_INC[yearIndex],
        prefDivs: res.PREF_DIVS[yearIndex],
        othAdj: res.OTH_ADJ[yearIndex],
        niAvailCommonGaap: res.NI_AVAIL_COMMON_GAAP[yearIndex],
        niAvailCommonAdj: res.NI_AVAIL_COMMON_ADJ[yearIndex],
        netAbnormal: res.NET_ABNORMAL[yearIndex],
        netExtra2: res.NET_EXTRA2[yearIndex],
        basicWeightAvgShares: res.BASIC_WEIGHT_AVG_SHARES[yearIndex],
        dilWeightAvgShares: res.DIL_WEIGHT_AVG_SHARES[yearIndex]
    }
}

/*
 * Parses ticker data from specific year into a cashflow sheet.
 */
function parseCashflowSheet(res, yearIndex) {
    return {
        niCf: res.NI_CF[yearIndex],
        depreAmort: res.DEPRE_AMORT[yearIndex],
        nonCashItems: res.NON_CASH_ITEMS[yearIndex],
        stockComp: res.STOCK_COMP[yearIndex],
        defIntComp: res.DEF_INT_COMP[yearIndex],
        othNonCashAdj: res.OTH_NON_CASH_ADJ[yearIndex],
        chgNonCashOp: res.CHG_NON_CASH_OP[yearIndex],
        chgAcctsRec: res.CHG_ACCTS_REC[yearIndex],
        chgInventories: res.CHG_INVENTORIES[yearIndex],
        chgAcctsPayable: res.CHG_ACCTS_PAYABLE[yearIndex],
        chgOther: res.CHG_OTHER[yearIndex],
        netCashDiscOps1: res.NET_CASH_DISC_OPS1[yearIndex],
        cashOpAct: res.CASH_OP_ACT[yearIndex],
        cashInvestAct1: res.CASH_INVEST_ACT1[yearIndex],
        chgFixedIntang: res.CHG_FIXED_INTANG[yearIndex],
        dispFixedIntang: res.DISP_FIXED_INTANG[yearIndex],
        dispFixedProdAssets: res.DISP_FIXED_PROD_ASSETS[yearIndex],
        dispIntagAssets: res.DISP_INTAG_ASSETS[yearIndex],
        acqFixedIntag: res.ACQ_FIXED_INTAG[yearIndex],
        acqFixedProdAssets: res.ACQ_FIXED_PROD_ASSETS[yearIndex],
        acqIntagAssets: res.ACQ_INTAG_ASSETS[yearIndex],
        netChgLtInvest: res.NET_CHG_LT_INVEST[yearIndex],
        decLtInvest: res.DEC_LT_INVEST[yearIndex],
        incLtInvest: res.INC_LT_INVEST[yearIndex],
        netCashAcqDiv: res.NET_CASH_ACQ_DIV[yearIndex],
        cashDivest: res.CASH_DIVEST[yearIndex],
        cashAcqSubs: res.CASH_ACQ_SUBS[yearIndex],
        cashJvs: res.CASH_JVS[yearIndex],
        othInvestAct: res.OTH_INVEST_ACT[yearIndex],
        netCashDiscOps2: res.NET_CASH_DISC_OPS2[yearIndex],
        cashInvestAct2: res.CASH_INVEST_ACT2[yearIndex],
        cashFinAct1: res.CASH_FIN_ACT1[yearIndex],
        divsPaid: res.DIVS_PAID[yearIndex],
        cashRepayDebt: res.CASH_REPAY_DEBT[yearIndex],
        cashStDebt: res.CASH_ST_DEBT[yearIndex],
        cashLtDebt: res.CASH_LT_DEBT[yearIndex],
        repayLtDebt: res.REPAY_LT_DEBT[yearIndex],
        cashRepurchEquity: res.CASH_REPURCH_EQUITY[yearIndex],
        incCapitalStock: res.INC_CAPITAL_STOCK[yearIndex],
        decCapitalStock: res.DEC_CAPITAL_STOCK[yearIndex],
        othFinAct: res.OTH_FIN_ACT[yearIndex],
        netCashDiscOps3: res.NET_CASH_DISC_OPS3[yearIndex],
        cashFinAct2: res.CASH_FIN_ACT2[yearIndex],
        effectForexRates: res.EFFECT_FOREX_RATES[yearIndex],
        netChgCash: res.NET_CHG_CASH[yearIndex],
        cashPaidTaxes: res.CASH_PAID_TAXES[yearIndex],
        cashPaidInt: res.CASH_PAID_INT[yearIndex]
    }
}

module.exports.getCleanTickerData = getCleanTickerData;
