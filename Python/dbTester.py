import math
import sys
import pyodbc
import datetime


def myDb():
    # https://github.com/mkleehammer/pyodbc/wiki/Getting-started
    # cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=STEVE-SURFACE\\SURFACE;DATABASE=Northwind;UID=USER;PWD=PASSWORD')
    cnxn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=STEVE-SURFACE\\SURFACE;DATABASE=Northwind;Trusted_Connection=yes;')

    cursor = cnxn.cursor()

    sqlCmd = ('SELECT EmployeeID, LastName, FirstName, Title, '
              'TitleOfCourtesy, BirthDate, HireDate, Address, '
              'City, Region, PostalCode, Country, '
              'HomePhone, Extension, Notes, ReportsTo '
              'FROM [Northwind].[dbo].[Employees] (nolock) '
              'ORDER BY LastName')
    cursor.execute(sqlCmd)
    # tables = cursor.fetchall()
    # cursor.execute("SELECT WORK_ORDER.TYPE,WORK_ORDER.STATUS, WORK_ORDER.BASE_ID, WORK_ORDER.LOT_ID FROM WORK_ORDER")

    # Print entire results set
    row = cursor.fetchone()
    while row is not None:
        print(', '.join([str(c) for c in row]))
        row = cursor.fetchone()

    # Print only selected columns
    print('=' * 50)
    formatStr = '%03d:  %s %s, %s'
    for row in cursor.execute(sqlCmd):
        print(formatStr % (row.EmployeeID, row.FirstName, row.LastName, row.HomePhone))

    sqlCmd = ('SELECT TOP (100) OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, '
              'ShippedDate, ShipVia, Freight, ShipName, ShipAddress, '
              'ShipCity, ShipRegion, ShipPostalCode, ShipCountry '
              'FROM Northwind.dbo.Orders '
              ' ORDER BY OrderID ')
    cursor.execute(sqlCmd)
    formatStr = '%07d: %s %s %.2f %s'
    for row in cursor.execute(sqlCmd):
        print(
            formatStr % (row.OrderID, row.CustomerID, row.OrderDate.strftime('%d-%m-%Y'), row.Freight, row.ShipCountry))

    cnxn.close()


# Define a main() function 
def main():
    myDb()


# This is the standard boilerplate that calls main() function
if __name__ == '__main__':
    main()
