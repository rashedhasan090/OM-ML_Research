CREATE DATABASE FOR /home/centos/orm_synthesizer/models/customerOrderObjectModel/ImplSolution/customerOrderObjectModel_Sol_1.sql

USE customerOrderObjectModel_Sol_1;
--
-- Table structure for table Order
--

CREATE TABLE `Order` (
`orderValue` decimal(20,5),
`orderID` int NOT NULL,
`customerID` int,
KEY `FK_Order_customerID_idx` (`customerID`),
PRIMARY KEY (`orderID`)
);

--
-- Table structure for table PreferredCustomer
--

CREATE TABLE `PreferredCustomer` (
`discount` int,
`customerID` int NOT NULL,
KEY `FK_PreferredCustomer_customerID_idx` (`customerID`),
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

ALTER TABLE `Order`
  ADD CONSTRAINT `FK_Order_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `PreferredCustomer`
  ADD CONSTRAINT `FK_PreferredCustomer_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;
