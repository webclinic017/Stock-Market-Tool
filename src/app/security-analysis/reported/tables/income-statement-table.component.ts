import { Component, ViewChild, OnInit } from '@angular/core';
import { MatTableDataSource, MatPaginator } from '@angular/material';

@Component({
    selector: 'app-income-statement-table',
    template: `
        <div class="mat-elevation-z8">
            <table mat-table [dataSource]="dataSource">

                <!-- 2015 Column -->
                <ng-container matColumnDef="metric">
                    <th mat-header-cell *matHeaderCellDef> Metric </th>
                    <td mat-cell *matCellDef="let element"> {{element.metric}} </td>
                </ng-container>

                <!-- 2016 Column -->
                <ng-container matColumnDef="name">
                    <th mat-header-cell *matHeaderCellDef> 2015 </th>
                    <td mat-cell *matCellDef="let element"> {{element.name}} </td>
                </ng-container>

                <!-- 2017 Column -->
                <ng-container matColumnDef="weight">
                    <th mat-header-cell *matHeaderCellDef> 2016 </th>
                    <td mat-cell *matCellDef="let element"> {{element.weight}} </td>
                </ng-container>

                <!-- 2018 Column -->
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
    `,
    styleUrls: ['table.scss']
})
export class IncomeStatementTableComponent implements OnInit {
    displayedColumns: string[] = ['metric', 'name', 'weight', 'symbol', 'value'];
    dataSource = new MatTableDataSource<PeriodicElement>(ELEMENT_DATA);

    @ViewChild(MatPaginator) paginator: MatPaginator;

    ngOnInit() {
        this.dataSource.paginator = this.paginator;
    }
}

export interface PeriodicElement {
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
