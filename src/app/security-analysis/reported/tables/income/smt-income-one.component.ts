import { Component, OnInit, Input, ViewChild } from '@angular/core';
import { IncomeSheet } from '../../../../server-communication/app-endpoint.constants';
import { MatTableDataSource, MatPaginator } from '@angular/material';

@Component({
    selector: 'smt-income-one',
    template: `
        <table mat-table [dataSource]="dataSource">

            <!-- Metric Column -->
            <ng-container matColumnDef="metric">
                <th mat-header-cell *matHeaderCellDef> Metric </th>
                <td mat-cell *matCellDef="let element"> {{element.metric}} </td>
            </ng-container>

            <!-- _1999 Column -->
            <ng-container matColumnDef="_1999">
                <th mat-header-cell *matHeaderCellDef> 1999 </th>
                <td mat-cell *matCellDef="let element"> {{element._1999}} </td>
            </ng-container>

            <!-- _2000 Column -->
            <ng-container matColumnDef="_2000">
                <th mat-header-cell *matHeaderCellDef> 2000 </th>
                <td mat-cell *matCellDef="let element"> {{element._2000}} </td>
            </ng-container>

            <!-- _2001 Column -->
            <ng-container matColumnDef="_2001">
                <th mat-header-cell *matHeaderCellDef> 2001 </th>
                <td mat-cell *matCellDef="let element"> {{element._2001}} </td>
            </ng-container>

            <!-- _2002 Column -->
            <ng-container matColumnDef="_2002">
                <th mat-header-cell *matHeaderCellDef> 2002 </th>
                <td mat-cell *matCellDef="let element"> {{element._2002}} </td>
            </ng-container>

            <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
            <tr mat-row *matRowDef="let row; columns: displayedColumns;"></tr>
        </table>

        <mat-paginator [pageSize]="5" showFirstLastButtons></mat-paginator>
    `,
    styleUrls: ['../table.scss']
})
export class SmtIncomeOneComponent implements OnInit {
    @Input() public incomeSheet;
    public INCOME_SHEET;
    public displayedColumns: string[] = ['metric', '_1999', '_2000', '_2001', '_2002'];
    public dataSource;

    @ViewChild(MatPaginator) paginator: MatPaginator;

    ngAfterViewInit() {
        this.dataSource.paginator = this.paginator;
    }

    constructor() { }

    ngOnInit() {
        this.INCOME_SHEET = [
            // tslint:disable-next-line: max-line-length
            {metric: 'Income Tax', '_1999': this.incomeSheet.IncTax, '_2000': this.incomeSheet.IncTax, '_2001': this.incomeSheet.IncTax, '_2002': this.incomeSheet.IncTax},
            // tslint:disable-next-line: max-line-length
            {metric: 'X0 & Accounting Changes', '_1999': this.incomeSheet.acctChng, '_2000': this.incomeSheet.acctChng, '_2001': this.incomeSheet.acctChng, '_2002': this.incomeSheet.acctChng},
            // tslint:disable-next-line: max-line-length
            {metric: '(Income) Loss from Affiliates', '_1999': this.incomeSheet.affiliates, '_2000': this.incomeSheet.affiliates, '_2001': this.incomeSheet.affiliates, '_2002': this.incomeSheet.affiliates},
            // tslint:disable-next-line: max-line-length
            {metric: 'Basic Weighted Avg Shares', '_1999': this.incomeSheet.basicWeightAvgShares, '_2000': this.incomeSheet.basicWeightAvgShares, '_2001': this.incomeSheet.basicWeightAvgShares, '_2002': this.incomeSheet.basicWeightAvgShares},
            // tslint:disable-next-line: max-line-length
            {metric: 'Cost of Goods & Services', '_1999': this.incomeSheet.cogs, '_2000': this.incomeSheet.cogs, '_2001': this.incomeSheet.cogs, '_2002': this.incomeSheet.cogs},
            // tslint:disable-next-line: max-line-length
            {metric: 'Income (Loss) from Cont Ops', '_1999': this.incomeSheet.contOps, '_2000': this.incomeSheet.contOps, '_2001': this.incomeSheet.contOps, '_2002': this.incomeSheet.contOps},
            // tslint:disable-next-line: max-line-length
            {metric: 'Cost of Revenue', '_1999': this.incomeSheet.costOfRev, '_2000': this.incomeSheet.costOfRev, '_2001': this.incomeSheet.costOfRev, '_2002': this.incomeSheet.costOfRev},
            // tslint:disable-next-line: max-line-length
            {metric: 'Current Income Tax', '_1999': this.incomeSheet.currIncTax, '_2000': this.incomeSheet.currIncTax, '_2001': this.incomeSheet.currIncTax, '_2002': this.incomeSheet.currIncTax},
            // tslint:disable-next-line: max-line-length
            {metric: 'Diluted Weighted Avg Shares', '_1999': this.incomeSheet.dilWeightAvgShares, '_2000': this.incomeSheet.dilWeightAvgShares, '_2001': this.incomeSheet.dilWeightAvgShares, '_2002': this.incomeSheet.dilWeightAvgShares},
            // tslint:disable-next-line: max-line-length
            {metric: 'Discontinued Operations', '_1999': this.incomeSheet.discOps, '_2000': this.incomeSheet.discOps, '_2001': this.incomeSheet.discOps, '_2002': this.incomeSheet.discOps},
            // tslint:disable-next-line: max-line-length
            {metric: 'Foreign Exch (Gain) Loss', '_1999': this.incomeSheet.forex, '_2000': this.incomeSheet.forex, '_2001': this.incomeSheet.forex, '_2002': this.incomeSheet.forex},
            // tslint:disable-next-line: max-line-length
            {metric: 'Income (Loss) Incl. MI', '_1999': this.incomeSheet.incomeMi, '_2000': this.incomeSheet.incomeMi, '_2001': this.incomeSheet.incomeMi, '_2002': this.incomeSheet.incomeMi},
            // tslint:disable-next-line: max-line-length
            {metric: 'Interest Expense', '_1999': this.incomeSheet.intExp, '_2000': this.incomeSheet.intExp, '_2001': this.incomeSheet.intExp, '_2002': this.incomeSheet.intExp},
            // tslint:disable-next-line: max-line-length
            {metric: 'Minority Interest', '_1999': this.incomeSheet.minInterest, '_2000': this.incomeSheet.minInterest, '_2001': this.incomeSheet.minInterest, '_2002': this.incomeSheet.minInterest},
            // tslint:disable-next-line: max-line-length
            {metric: 'Net Abnormal Losses (Gains)', '_1999': this.incomeSheet.netAbnormal, '_2000': this.incomeSheet.netAbnormal, '_2001': this.incomeSheet.netAbnormal, '_2002': this.incomeSheet.netAbnormal},
            // tslint:disable-next-line: max-line-length
            {metric: 'Net Extraordinary Losses (Gains)', '_1999': this.incomeSheet.netExtra1, '_2000': this.incomeSheet.netExtra1, '_2001': this.incomeSheet.netExtra1, '_2002': this.incomeSheet.netExtra1},
            // tslint:disable-next-line: max-line-length
            {metric: 'Interest Expense, Net', '_1999': this.incomeSheet.netIntExp, '_2000': this.incomeSheet.netIntExp, '_2001': this.incomeSheet.netIntExp, '_2002': this.incomeSheet.netIntExp},
            // tslint:disable-next-line: max-line-length
            {metric: 'Net Income Avail to Common, Adj', '_1999': this.incomeSheet.niAvailCommonAdj, '_2000': this.incomeSheet.niAvailCommonAdj, '_2001': this.incomeSheet.niAvailCommonAdj, '_2002': this.incomeSheet.niAvailCommonAdj},
            // tslint:disable-next-line: max-line-length
            {metric: 'Net Income Avail to Common, GAAP', '_1999': this.incomeSheet.niAvailCommonGaap, '_2000': this.incomeSheet.niAvailCommonGaap, '_2001': this.incomeSheet.niAvailCommonGaap, '_2002': this.incomeSheet.niAvailCommonGaap},
            // tslint:disable-next-line: max-line-length
            {metric: 'Net Income, GAAP', '_1999': this.incomeSheet.niInc, '_2000': this.incomeSheet.niInc, '_2001': this.incomeSheet.niInc, '_2002': this.incomeSheet.niInc},
            // tslint:disable-next-line: max-line-length
            {metric: 'Other Non-Op (Income) Loss', '_1999': this.incomeSheet.nonOpInc, '_2000': this.incomeSheet.nonOpInc, '_2001': this.incomeSheet.nonOpInc, '_2002': this.incomeSheet.nonOpInc},
            // tslint:disable-next-line: max-line-length
            {metric: 'Non-Operating (Income) Loss', '_1999': this.incomeSheet.nonOpIncLoss, '_2000': this.incomeSheet.nonOpIncLoss, '_2001': this.incomeSheet.nonOpIncLoss, '_2002': this.incomeSheet.nonOpIncLoss},
            // tslint:disable-next-line: max-line-length
            {metric: 'Operating Expenses', '_1999': this.incomeSheet.opExp, '_2000': this.incomeSheet.opExp, '_2001': this.incomeSheet.opExp, '_2002': this.incomeSheet.opExp},
            // tslint:disable-next-line: max-line-length
            {metric: 'Other Adjustments', '_1999': this.incomeSheet.othAdj, '_2000': this.incomeSheet.othAdj, '_2001': this.incomeSheet.othAdj, '_2002': this.incomeSheet.othAdj},
            // tslint:disable-next-line: max-line-length
            {metric: 'Other Operating Expense', '_1999': this.incomeSheet.othOpExp, '_2000': this.incomeSheet.othOpExp, '_2001': this.incomeSheet.othOpExp, '_2002': this.incomeSheet.othOpExp},
            // tslint:disable-next-line: max-line-length
            {metric: 'Other Operating Income', '_1999': this.incomeSheet.otherProfit, '_2000': this.incomeSheet.otherProfit, '_2001': this.incomeSheet.otherProfit, '_2002': this.incomeSheet.otherProfit},
            // tslint:disable-next-line: max-line-length
            {metric: 'Other Revenue', '_1999': this.incomeSheet.otherRev, '_2000': this.incomeSheet.otherRev, '_2001': this.incomeSheet.otherRev, '_2002': this.incomeSheet.otherRev},
            // tslint:disable-next-line: max-line-length
            {metric: 'Preferred Dividends', '_1999': this.incomeSheet.prefDivs, '_2000': this.incomeSheet.prefDivs, '_2001': this.incomeSheet.prefDivs, '_2002': this.incomeSheet.prefDivs},
            // tslint:disable-next-line: max-line-length
            {metric: 'Pretax Income', '_1999': this.incomeSheet.pretaxIncome, '_2000': this.incomeSheet.pretaxIncome, '_2001': this.incomeSheet.pretaxIncome, '_2002': this.incomeSheet.pretaxIncome},
            // tslint:disable-next-line: max-line-length
            {metric: 'Gross Profit', '_1999': this.incomeSheet.proft, '_2000': this.incomeSheet.profit, '_2001': this.incomeSheet.profit, '_2002': this.incomeSheet.profit},
            // tslint:disable-next-line: max-line-length
            {metric: 'Revenue', '_1999': this.incomeSheet.rev, '_2000': this.incomeSheet.rev, '_2001': this.incomeSheet.rev, '_2002': this.incomeSheet.rev},
            // tslint:disable-next-line: max-line-length
            {metric: 'Sales & Services Revenue', '_1999': this.incomeSheet.salesServRev, '_2000': this.incomeSheet.salesServRev, '_2001': this.incomeSheet.salesServRev, '_2002': this.incomeSheet.salesServRev},
            // tslint:disable-next-line: max-line-length
            {metric: 'Selling, General & Admin', '_1999': this.incomeSheet.sgAndAdmin, '_2000': this.incomeSheet.sgAndAdmin, '_2001': this.incomeSheet.sgAndAdmin, '_2002': this.incomeSheet.sgAndAdmin},
            // tslint:disable-next-line: max-line-length
            {metric: 'Discontinued Operations', '_1999': this.incomeSheet.discOps, '_2000': this.incomeSheet.discOps, '_2001': this.incomeSheet.discOps, '_2002': this.incomeSheet.discOps},
            // tslint:disable-next-line: max-line-length
            {metric: 'Foreign Exch (Gain) Loss', '_1999': this.incomeSheet.forex, '_2000': this.incomeSheet.forex, '_2001': this.incomeSheet.forex, '_2002': this.incomeSheet.forex}
        ];
        this.dataSource = new MatTableDataSource(this.INCOME_SHEET);
    }

}
