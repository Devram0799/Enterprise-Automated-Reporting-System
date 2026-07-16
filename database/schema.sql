CREATE DATABASE EnterpriseReportingDB;
GO

USE EnterpriseReportingDB;
GO

SELECT DB_NAME() AS CurrentDatabase;


CREATE TABLE Customers
(
    CustomerID INT IDENTITY(1,1) PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Phone NVARCHAR(15),
    City NVARCHAR(50),
    State NVARCHAR(50),
    CreatedDate DATETIME DEFAULT GETDATE()
);

SELECT * FROM Customers;


INSERT INTO Customers
(FirstName, LastName, Email, Phone, City, State)
VALUES
('Rahul','Sharma','rahul.sharma@email.com','9876543210','Mumbai','Maharashtra'),
('Priya','Patel','priya.patel@email.com','9876543211','Ahmedabad','Gujarat'),
('Amit','Verma','amit.verma@email.com','9876543212','Delhi','Delhi'),
('Sneha','Rao','sneha.rao@email.com','9876543213','Bengaluru','Karnataka'),
('Arjun','Singh','arjun.singh@email.com','9876543214','Jaipur','Rajasthan');

SELECT * FROM Customers;


