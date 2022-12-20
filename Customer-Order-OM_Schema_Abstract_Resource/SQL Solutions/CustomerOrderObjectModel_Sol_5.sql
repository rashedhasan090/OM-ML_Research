-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/customerOrderObjectModel/ImplSolution/customerOrderObjectModel_Sol_5.sql

USE customerOrderObjectModel_Sol_5;
--
-- Table structure for table Order
--

CREATE TABLE `Order` (
`orderValue` decimal(20,5),
`orderID` int NOT NULL,
PRIMARY KEY (`orderID`)
);

--
-- Table structure for table PreferredCustomer
--

CREATE TABLE `PreferredCustomer` (
`customerName` varchar(64),
`discount` int,
`customerID` int NOT NULL,
PRIMARY KEY (`customerID`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`customerName` varchar(64),
`customerID` int NOT NULL,
PRIMARY KEY (`customerID`)
);

--
-- Table structure for table CustomerOrderAssociation
--

CREATE TABLE `CustomerOrderAssociation` (
`orderID` int NOT NULL,
`customerID` int NOT NULL,
KEY `FK_CustomerOrderAssociation_orderID_idx` (`orderID`),
KEY `FK_CustomerOrderAssociation_customerID_idx` (`customerID`),
PRIMARY KEY (`orderID`,`customerID`)
);

ALTER TABLE `CustomerOrderAssociation`
  ADD CONSTRAINT `FK_CustomerOrderAssociation_orderID` FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerOrderAssociation_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;
