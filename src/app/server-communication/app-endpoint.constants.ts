/* API Classes */
export interface Ticker {
    fiscalYears: FiscalYear[];
}

export interface FiscalYear {
    year: number;
    balanceSheet: BalanceSheet;
    incomeSheet: IncomeSheet;
    cashflowSheet: CashflowSheet;
}

export interface BalanceSheet {
    totalAssets1: number;
    cashEqSti: number;
    cashEq: number;
    sti: number;
    acctsRec: number;
    acctsRecNet: number;
    notesRecNet: number;
    inv: number;
    rawMat: number;
    wip: number;
    finGoods: number;
    othInv: number;
    othStAssets: number;
    derivHedgeAssets1: number;
    taxesReciev: number;
    miscStAssets: number;
    totalCurrAssets: number;
    ppeNet: number;
    ppe: number;
    accDeprec: number;
    ltiReceivables: number;
    ltInvest: number;
    othLtAssets: number;
    totalIntAssets: number;
    goodwill: number;
    othIntAssets: number;
    prepaidExp: number;
    deffTaxAssets: number;
    derivHedgeAssets2: number;
    miscAssets: number;
    totalNonCurrAssets: number;
    totalAssets2: number;
    liabAndEquity1: number;
    payablesAccruals: number;
    payables: number;
    accruedTaxes: number;
    intDivsPayables: number;
    othPayablesAccurals: number;
    stDebt: number;
    stBorrowings: number;
    stFinLeases: number;
    stOpLeases: number;
    currLtDebt: number;
    othStLiab: number;
    deffRev1: number;
    derivHedge1: number;
    miscStLiab: number;
    totalCurrLiab: number;
    ltDebt: number;
    ltBorrow: number;
    ltFinLeases: number;
    ltOpLeases: number;
    othLtLiab: number;
    accuredLiab: number;
    pensionLiab: number;
    pensions: number;
    othPostRetBen: number;
    deffRev2: number;
    defTabLiab: number;
    derivHedge: number;
    miscLtLiab: number;
    totalNonCurrLiab: number;
    totalLiab: number;
    prefEquityHybridCap: number;
    shareCapApic: number;
    commonStock: number;
    addPaidCap: number;
    treasuryStock: number;
    re: number;
    othEquity: number;
    equityBeforeMinInt: number;
    minNonControlInt: number;
    totalEquity: number;
    liabAndEquity2: number;
}

export interface IncomeSheet {
    rev: number;
    salesServRev: number;
    otherRev: number;
    costOfRev: number;
    cogs: number;
    proft: number;
    otherProfit: number;
    opExp: number;
    sgAndAdmin: number;
    sellAndMark: number;
    genAndAdmin: number;
    rAndD: number;
    depAmort: number;
    othOpExp: number;
    opIncLoss: number;
    nonOpIncLoss: number;
    netIntExp: number;
    intExp: number;
    intInc: number;
    forex: number;
    affiliates: number;
    nonOpInc: number;
    pretaxIncome: number;
    currIncTax: number;
    IncTax: number;
    contOps: number;
    netExtra1: number;
    discOps: number;
    acctChng: number;
    incomeMi: number;
    minInterest: number;
    niInc: number;
    prefDivs: number;
    othAdj: number;
    niAvailCommonGaap: number;
    niAvailCommonAdj: number;
    netAbnormal: number;
    netExtra2: number;
    basicWeightAvgShares: number;
    dilWeightAvgShares: number;
}

export interface CashflowSheet {
    niCf: number;
    depreAmort: number;
    nonCashItems: number;
    stockComp: number;
    defIntComp: number;
    othNonCashAdj: number;
    chgNonCashOp: number;
    chgAcctsRec: number;
    chgInventories: number;
    chgAcctsPayable: number;
    chgOther: number;
    netCashDiscOps1: number;
    cashOpAct: number;
    cashInvestAct1: number;
    chgFixedIntang: number;
    dispFixedIntang: number;
    dispFixedProdAssets: number;
    dispIntagAssets: number;
    acqFixedIntag: number;
    acqFixedProdAssets: number;
    acqIntagAssets: number;
    netChgLtInvest: number;
    decLtInvest: number;
    incLtInvest: number;
    netCashAcqDiv: number;
    cashDivest: number;
    cashAcqSubs: number;
    cashJvs: number;
    othInvestAct: number;
    netCashDiscOps2: number;
    cashInvestAct2: number;
    cashFinAct1: number;
    divsPaid: number;
    cashRepayDebt: number;
    cashStDebt: number;
    cashLtDebt: number;
    repayLtDebt: number;
    cashRepurchEquity: number;
    incCapitalStock: number;
    decCapitalStock: number;
    othFinAct: number;
    netCashDiscOps3: number;
    cashFinAct2: number;
    effectForexRates: number;
    netChgCash: number;
    cashPaidTaxes: number;
    cashPaidInt: number;
}

/* API calls */
export interface RegisterRequest {
    username: string;
    email: string;
    password: string;
}

export interface RegisterResponse {
    message: string;
    result: {
        email: string,
        password: string,
        username: string,
        __v: number,
        _id: string
    };
}

export interface LoginRequest {
    username: string;
    password: string;
}

export interface LoginResponse {
    token: string;
}

export interface SecuritysRequest {
    ticker: string;
}

export interface ReportedRequest {
    ticker: string;
}

export interface ReportedResponse {
    ticker: Ticker;
}
