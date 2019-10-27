import { Component, ViewChild, OnInit, Input, AfterViewInit } from '@angular/core';
import { MatTableDataSource, MatPaginator } from '@angular/material';
import { Ticker } from 'src/app/server-communication/app-endpoint.constants';

@Component({
    selector: 'app-income-statement-table',
    template: `
        <div class="mat-elevation-z8">
            <smt-income-one *ngIf="displayTable1"></smt-income-one>
            <smt-income-two *ngIf="displayTable2"></smt-income-two>
            <smt-income-three *ngIf="displayTable3"></smt-income-three>
            <smt-income-four *ngIf="displayTable4"></smt-income-four>
            <smt-income-five *ngIf="displayTable5"></smt-income-five>
        </div>
        <button (click)="displayTable(1)" class="btn btn-primary">1999-2002</button>
        <button (click)="displayTable(2)" class="btn btn-primary">2003-2006</button>
        <button (click)="displayTable(3)" class="btn btn-primary">2007-2010</button>
        <button (click)="displayTable(4)" class="btn btn-primary">2011-2014</button>
        <button (click)="displayTable(5)" class="btn btn-primary">2015-2018</button>
    `,
    styleUrls: ['table.scss']
})
export class IncomeStatementTableComponent implements OnInit {
    // State booleans.
    displayTable1 = true;
    displayTable2 = false;
    displayTable3 = false;
    displayTable4 = false;
    displayTable5 = false;
    ngOnInit() { }

    public displayTable(table: number) {
        if (table === 1) {
            this.displayTable1 = true;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 2) {
            this.displayTable1 = false;
            this.displayTable2 = true;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 3) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = true;
            this.displayTable4 = false;
            this.displayTable5 = false;

        } if (table === 4) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = true;
            this.displayTable5 = false;

        } if (table === 5) {
            this.displayTable1 = false;
            this.displayTable2 = false;
            this.displayTable3 = false;
            this.displayTable4 = false;
            this.displayTable5 = true;
        }
    }
}

/*export interface PeriodicElement {
    metric: string;
    name: number;
    weight: number;
    symbol: number;
    value: number;
}

const ELEMENT_DATA: PeriodicElement[] = [
    {metric: 'Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Cost of Revenue', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Gross Profit', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Other Operating Income', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Operating Expenses', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Selling, General, & Admin', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Research & Development', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Other Operating Expenses', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Operating Income (Loss)', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
    {metric: 'Non-Operating (Income) Loss', name: 10101, weight: 1.0079, symbol: 30201, value: 1001},
];

@Input() tickerData: Ticker;
    displayedColumns: string[] = ['metric', 'name', 'weight', 'symbol', 'value'];
    dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);

    @ViewChild(MatPaginator) paginator: MatPaginator;

    ngOnInit() { }

    ngAfterViewInit() {
        this.dataSource.paginator = this.paginator;
    }


<div *ngIf="displayTable5" class="mat-elevation-z8">
            <table mat-table [dataSource]="dataSource">

                <!-- Metric Column -->
                <ng-container matColumnDef="metric">
                    <th mat-header-cell *matHeaderCellDef> Metric </th>
                    <td mat-cell *matCellDef="let element"> {{element.metric}} </td>
                </ng-container>

                <!-- 2015 Column -->
                <ng-container matColumnDef="name">
                    <th mat-header-cell *matHeaderCellDef> 2015 </th>
                    <td mat-cell *matCellDef="let element"> {{element.name}} </td>
                </ng-container>

                <!-- 2016 Column -->
                <ng-container matColumnDef="weight">
                    <th mat-header-cell *matHeaderCellDef> 2016 </th>
                    <td mat-cell *matCellDef="let element"> {{element.weight}} </td>
                </ng-container>

                <!-- 2017 Column -->
                <ng-container matColumnDef="symbol">
                    <th mat-header-cell *matHeaderCellDef> 2017 </th>
                    <td mat-cell *matCellDef="let element"> {{element.symbol}} </td>
                </ng-container>

                <!-- 2018 Column -->
                <ng-container matColumnDef="value">
                    <th mat-header-cell *matHeaderCellDef> 2018 </th>
                    <td mat-cell *matCellDef="let element"> {{element.value}} </td>
                </ng-container>

                <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
                <tr mat-row *matRowDef="let row; columns: displayedColumns;"></tr>
            </table>

            <mat-paginator [pageSize]="5" showFirstLastButtons></mat-paginator>
        </div>
*/
