-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/customerOrderObjectModel/ImplSolution/customerOrderObjectModel_Sol_9.sql

USE customerOrderObjectModel_Sol_9;
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
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`DType` varchar(64),
`customerName` varchar(64),
`discount` int,
`customerID` int NOT NULL,
PRIMARY KEY (`customerID`)
);

ALTER TABLE `Order`
  ADD CONSTRAINT `FK_Order_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;
