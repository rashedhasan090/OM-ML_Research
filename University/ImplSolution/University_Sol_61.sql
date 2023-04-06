-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/University/ImplSolution/University_Sol_61.sql

USE University_Sol_61;
--
-- Table structure for table UniversityHRAssociation
--

CREATE TABLE `UniversityHRAssociation` (
`UniversityId` int NOT NULL, 
`HRId` int NOT NULL, 
KEY `FK_UniversityHRAssociation_UniversityId_idx` (`UniversityId`),
KEY `FK_UniversityHRAssociation_HRId_idx` (`HRId`),
PRIMARY KEY (`UniversityId`,`HRId`)
);

--
-- Table structure for table Salary
--

CREATE TABLE `Salary` (
`SalaryId` int NOT NULL, 
PRIMARY KEY (`SalaryId`)
);

--
-- Table structure for table EmployeeSalaryAssociation
--

CREATE TABLE `EmployeeSalaryAssociation` (
`SalaryId` int NOT NULL, 
`EmployeeId` int NOT NULL, 
KEY `FK_EmployeeSalaryAssociation_SalaryId_idx` (`SalaryId`),
KEY `FK_EmployeeSalaryAssociation_EmployeeId_idx` (`EmployeeId`),
PRIMARY KEY (`SalaryId`,`EmployeeId`)
);

--
-- Table structure for table Savings
--

CREATE TABLE `Savings` (
`SavingsId` int,
`SalaryId` int,
`EmployeeId` int NOT NULL, 
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table EmployeeLoanAssociation
--

CREATE TABLE `EmployeeLoanAssociation` (
`EmployeeId` int NOT NULL, 
`LoanId` int NOT NULL, 
KEY `FK_EmployeeLoanAssociation_EmployeeId_idx` (`EmployeeId`),
KEY `FK_EmployeeLoanAssociation_LoanId_idx` (`LoanId`),
PRIMARY KEY (`EmployeeId`,`LoanId`)
);

--
-- Table structure for table MonthlySalary
--

CREATE TABLE `MonthlySalary` (
`SalaryId` int,
`EmployeeId` int NOT NULL, 
`MonthlySalaryId` int,
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table Employee
--

CREATE TABLE `Employee` (
`EmployeeAddress` varchar(64),
`EmployeeName` varchar(64),
`EmployeeAcctNo` int,
`EmployeePhoneNo` int,
`EmployeeId` int NOT NULL, 
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table Loan
--

CREATE TABLE `Loan` (
`LoanType` varchar(64),
`LoanId` int NOT NULL, 
PRIMARY KEY (`LoanId`)
);

--
-- Table structure for table University
--

CREATE TABLE `University` (
`UniversityLocation` varchar(64),
`UniversityName` varchar(64),
`UniversityId` int NOT NULL, 
PRIMARY KEY (`UniversityId`)
);

--
-- Table structure for table HR
--

CREATE TABLE `HR` (
`HRName` varchar(64),
`HRId` int NOT NULL, 
PRIMARY KEY (`HRId`)
);

--
-- Table structure for table UniversityEmployeeAssociation
--

CREATE TABLE `UniversityEmployeeAssociation` (
`UniversityId` int NOT NULL, 
`EmployeeId` int NOT NULL, 
KEY `FK_UniversityEmployeeAssociation_UniversityId_idx` (`UniversityId`),
KEY `FK_UniversityEmployeeAssociation_EmployeeId_idx` (`EmployeeId`),
PRIMARY KEY (`UniversityId`,`EmployeeId`)
);

--
-- Table structure for table EmployeeHRAssociation
--

CREATE TABLE `EmployeeHRAssociation` (
`HRId` int NOT NULL, 
`EmployeeId` int NOT NULL, 
KEY `FK_EmployeeHRAssociation_HRId_idx` (`HRId`),
KEY `FK_EmployeeHRAssociation_EmployeeId_idx` (`EmployeeId`),
PRIMARY KEY (`HRId`,`EmployeeId`)
);

ALTER TABLE `UniversityHRAssociation`
  ADD CONSTRAINT `FK_UniversityHRAssociation_UniversityId` FOREIGN KEY (`UniversityId`) REFERENCES `University` (`UniversityId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UniversityHRAssociation_HRId` FOREIGN KEY (`HRId`) REFERENCES `HR` (`HRId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `EmployeeSalaryAssociation`
  ADD CONSTRAINT `FK_EmployeeSalaryAssociation_SalaryId` FOREIGN KEY (`SalaryId`) REFERENCES `Salary` (`SalaryId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_EmployeeSalaryAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Employee` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `EmployeeLoanAssociation`
  ADD CONSTRAINT `FK_EmployeeLoanAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Employee` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_EmployeeLoanAssociation_LoanId` FOREIGN KEY (`LoanId`) REFERENCES `Loan` (`LoanId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UniversityEmployeeAssociation`
  ADD CONSTRAINT `FK_UniversityEmployeeAssociation_UniversityId` FOREIGN KEY (`UniversityId`) REFERENCES `University` (`UniversityId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UniversityEmployeeAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Employee` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `EmployeeHRAssociation`
  ADD CONSTRAINT `FK_EmployeeHRAssociation_HRId` FOREIGN KEY (`HRId`) REFERENCES `HR` (`HRId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_EmployeeHRAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Employee` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE;

