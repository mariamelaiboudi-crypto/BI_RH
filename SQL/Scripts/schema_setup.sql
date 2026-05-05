-- SQL Schema for HR Business Intelligence MVP
-- This script defines the Star Schema structure.

-- Dimension Table: Employee
CREATE TABLE Dim_Employee (
    EmployeeID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(20)
);

-- Dimension Table: Department
CREATE TABLE Dim_Department (
    DeptID INT PRIMARY KEY,
    Department VARCHAR(50),
    JobRole VARCHAR(50)
);

-- Dimension Table: Date
CREATE TABLE Dim_Date (
    Date DATE PRIMARY KEY,
    Year INT,
    Month INT,
    Quarter INT,
    Day INT,
    Weekday VARCHAR(20)
);

-- Fact Table: Employee Records
CREATE TABLE Fact_EmployeeRecords (
    RecordID SERIAL PRIMARY KEY,
    EmployeeID VARCHAR(50) REFERENCES Dim_Employee(EmployeeID),
    DeptID INT REFERENCES Dim_Department(DeptID),
    HireDate DATE,
    ExitDate VARCHAR(20), -- 'Active' or Date
    Salary INT,
    PerformanceRating INT,
    TenureDays INT,
    IsActive INT
);

-- Example View: Attrition Analysis
CREATE VIEW View_AttritionSummary AS
SELECT 
    d.Department,
    COUNT(f.EmployeeID) as TotalEmployees,
    SUM(CASE WHEN f.IsActive = 0 THEN 1 ELSE 0 END) as TotalExited,
    CAST(SUM(CASE WHEN f.IsActive = 0 THEN 1 ELSE 0 END) AS FLOAT) / COUNT(f.EmployeeID) * 100 as AttritionRate
FROM Fact_EmployeeRecords f
JOIN Dim_Department d ON f.DeptID = d.DeptID
GROUP BY d.Department;
