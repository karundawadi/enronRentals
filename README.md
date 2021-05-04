# Enrol Rental System

Enron rental system is a GUI application that is created using Tkinter. It manages a fictional company called Enron Rentals. Inside the application, an end-user will be able to make changes to the database; they will be able to add new users, update the existing records, and perform various other tasks. 

## Authors
[Dawadi, Karun](https://github.com/karundawadi)
[Fabbro, Robert](https://github.com/peppernaut)
[Gonzalez, Paola](https://github.com/peppernaut)
[Rana, Prajwal](https://github.com/PrajRana)

## Installation

 1. Install the latest version of [python](https://www.python.org/downloads/). 

2. Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install tkinter.

```bash
pip3 install tkinter
```
3. Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install mysql.connector.

```bash
pip3 install mysql.connector
```
4. Load the database correctly into MySQL from [Project 2](https://github.com/karundawadi/teambearcats/tree/master/project2)

5. Run the following SQL to create a vRentalInfo view :
```sql
USE project2;

-- DROP VIEW vRentalInfo;

CREATE VIEW vRentalInfo
AS SELECT OrderDate, StartDate, ReturnDate,
(Qty * RentalType) as 'TotalDays', 
VechicleID AS 'VIN', Description AS 'Vehicle', 
(CASE Type  
	WHEN 1 THEN "Compact"
	WHEN 2 THEN "Medium"
	WHEN 3 THEN "Large"
	WHEN 4 THEN "SUV"
	WHEN 5 THEN "Truck"
	WHEN 6 THEN "VAN"
END) AS 'Type',
(CASE Category
	WHEN 0 THEN "Basic"
	WHEN 1 THEN "Luxury"
END) AS 'Category', 
CustID AS 'CusomterID', 
Name AS 'CustomerName', 
TotalAmount AS 'OrderAmount', 
(CASE WHEN PaymentDate IS NULL THEN TotalAmount ELSE 0
END) AS 'BalanceDue'
FROM Rental
NATURAL JOIN Customer
NATURAL JOIN Vehicle
NATURAL JOIN RATE;

SELECT * FROM vRentalInfo;
```
6. Change the password_database variable on enron.py to the user's root password. 

7. Navigate to the directory and run the application by using the following command: 
```python 
python3 enron.py
```
You will be greeted with a GUI to Enron Systems. 
