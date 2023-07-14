CREATE DATABASE BFGS; --Barely_functional_game_shop

--Customer table
----Customer ID (INT auto increment) *
----First Name (VARCHAR(30)) *
----Last Name (VARCHAR(30)) *
----Email
----Phone Number (INT)
CREATE TABLE Customers(
Customer_ID INT AUTO_INCREMENT,
cust_First_Name VARCHAR(30) NOT NULL,
cust_Last_Name VARCHAR(30) NOT NULL,
cust_Email VARCHAR(60),
cust_Phone_number INT,
PRIMARY KEY(Customer_ID)
);

--Transaction Table
----Transaction ID
----GameID
----CustomerID
----Date_time 
CREATE TABLE Transaction(
Transaction_ID INT AUTO_INCREMENT,
Date_time DATETIME,
FK_Customer_ID INT NOT NULL,
FK_Employee_ID INT NOT NULL,
FK_Game_ID INT NOT NULL,
PRIMARY KEY (Transaction_ID),
FOREIGN KEY (FK_Customer_ID) REFERENCES Customers(Customer_ID),
FOREIGN KEY (FK_Game_ID) REFERENCES Games(Game_ID),
FOREIGN KEY (FK_Employee_ID) REFERENCES Employee(Employee_ID)
);

--Games Table
----Game_ID (INT auto increment) *
----Game_genre (VARCHAR(30)) 
----Game_Name *
----Game_Price (Float) Not Null
----No_of_sales (INT) Default 0
----Stock (INT)
----Rating (INT) 

----Supplier ID
CREATE TABLE Games(
Game_ID INT AUTO_INCREMENT,
Game_genre VARCHAR(30),
Game_Name VARCHAR(50) NOT NULL,
Game_Price FLOAT NOT NULL,
No_of_sales INT DEFAULT 0,
Stock INT DEFAULT 0,
RATING FLOAT,
FK_Supplier_ID INT NOT NULL,
PRIMARY KEY (Game_ID),
FOREIGN KEY (FK_Supplier_ID) REFERENCES Supplier(Supplier_ID)
);

--Employee Table
----EmployeeID (INT auto increment)
----First_Name (VARCHAR(30))
----Last_Name (VARCHAR(30))
----Salary (INT)
----Email 
----Phone_number (INT)
----Hours_per_week
CREATE TABLE Employee(
Employee_ID INT AUTO_INCREMENT,
Emp_First_Name VARCHAR(30) NOT NULL,
Emp_Last_Name VARCHAR(30) NOT NULL,
SALARY INT NOT NULL,
Emp_EMAIL VARCHAR(60) NOT NULL,
Emp_Phone_number INT NOT NULL,
PRIMARY KEY(Employee_ID)
);

--Inventory/Supplier Table
----Supplier ID (INT autoincrement)
----Supplier_name (VARCHAR(30))
----Phone_number (INT)
----Email
CREATE TABLE Supplier(
Supplier_ID INT AUTO_INCREMENT,
Supplier_name VARCHAR(50) NOT NULL,
Sup_Phone_number INT,
Sup_Email VARCHAR(60),
PRIMARY KEY(Supplier_ID)
);