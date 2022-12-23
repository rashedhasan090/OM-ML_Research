-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/Bank/ImplSolution/Bank_Sol_59.sql

USE Bank_Sol_59;
--
-- Table structure for table Account
--

CREATE TABLE `Account` (
`AccountId` int NOT NULL,
`CustomerId` int,
PRIMARY KEY (`AccountId`)
);

--
-- Table structure for table Savings
--

CREATE TABLE `Savings` (
`SavingsId` int,
`AccountId` int,
`CustomerId` int NOT NULL,
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table Bank
--

CREATE TABLE `Bank` (
`BankLocation` varchar(64),
`BankName` varchar(64),
`BankId` int NOT NULL,
PRIMARY KEY (`BankId`)
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
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`CustomerAddress` varchar(64),
`CustomerName` varchar(64),
`CustomerAcctNo` int,
`CustomerPhoneNo` int,
`CustomerId` int NOT NULL,
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table CustomerLoanAssociation
--

CREATE TABLE `CustomerLoanAssociation` (
`CustomerId` int NOT NULL,
`LoanId` int NOT NULL,
KEY `FK_CustomerLoanAssociation_CustomerId_idx` (`CustomerId`),
KEY `FK_CustomerLoanAssociation_LoanId_idx` (`LoanId`),
PRIMARY KEY (`CustomerId`,`LoanId`)
);

--
-- Table structure for table Teller
--

CREATE TABLE `Teller` (
`TellerName` varchar(64),
`TellerId` int NOT NULL,
PRIMARY KEY (`TellerId`)
);

--
-- Table structure for table BankCustomerAssociation
--

CREATE TABLE `BankCustomerAssociation` (
`BankId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_BankCustomerAssociation_BankId_idx` (`BankId`),
KEY `FK_BankCustomerAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`BankId`,`CustomerId`)
);

--
-- Table structure for table CustomerTellerAssociation
--

CREATE TABLE `CustomerTellerAssociation` (
`TellerId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_CustomerTellerAssociation_TellerId_idx` (`TellerId`),
KEY `FK_CustomerTellerAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`TellerId`,`CustomerId`)
);

--
-- Table structure for table CustomerAccountAssociation
--

CREATE TABLE `CustomerAccountAssociation` (
`AccountId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_CustomerAccountAssociation_AccountId_idx` (`AccountId`),
KEY `FK_CustomerAccountAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`AccountId`,`CustomerId`)
);

--
-- Table structure for table BankTellerAssociation
--

CREATE TABLE `BankTellerAssociation` (
`BankId` int NOT NULL,
`TellerId` int NOT NULL,
KEY `FK_BankTellerAssociation_BankId_idx` (`BankId`),
KEY `FK_BankTellerAssociation_TellerId_idx` (`TellerId`),
PRIMARY KEY (`BankId`,`TellerId`)
);

--
-- Table structure for table Checking
--

CREATE TABLE `Checking` (
`AccountId` int,
`CustomerId` int NOT NULL,
`CheckingId` int,
PRIMARY KEY (`CustomerId`)
);

ALTER TABLE `CustomerLoanAssociation`
  ADD CONSTRAINT `FK_CustomerLoanAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerLoanAssociation_LoanId` FOREIGN KEY (`LoanId`) REFERENCES `Loan` (`LoanId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `BankCustomerAssociation`
  ADD CONSTRAINT `FK_BankCustomerAssociation_BankId` FOREIGN KEY (`BankId`) REFERENCES `Bank` (`BankId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BankCustomerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerTellerAssociation`
  ADD CONSTRAINT `FK_CustomerTellerAssociation_TellerId` FOREIGN KEY (`TellerId`) REFERENCES `Teller` (`TellerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerTellerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerAccountAssociation`
  ADD CONSTRAINT `FK_CustomerAccountAssociation_AccountId` FOREIGN KEY (`AccountId`) REFERENCES `Account` (`AccountId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerAccountAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `BankTellerAssociation`
  ADD CONSTRAINT `FK_BankTellerAssociation_BankId` FOREIGN KEY (`BankId`) REFERENCES `Bank` (`BankId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BankTellerAssociation_TellerId` FOREIGN KEY (`TellerId`) REFERENCES `Teller` (`TellerId`) ON DELETE CASCADE ON UPDATE CASCADE;
