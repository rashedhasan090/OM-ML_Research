-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/OnlineStore/ImplSolution/OnlineStore_Sol_3.sql

USE OnlineStore_Sol_3;
--
-- Table structure for table AdminProductsAssociation
--

CREATE TABLE `AdminProductsAssociation` (
`ProductsId` int NOT NULL,
`AdminId` int NOT NULL,
KEY `FK_AdminProductsAssociation_ProductsId_idx` (`ProductsId`),
KEY `FK_AdminProductsAssociation_AdminId_idx` (`AdminId`),
PRIMARY KEY (`ProductsId`,`AdminId`)
);

--
-- Table structure for table Products
--

CREATE TABLE `Products` (
`Subgroup` varchar(64),
`Group` varchar(64),
`ProductsName` varchar(64),
`ProductsId` int NOT NULL,
`GuestId` int,
`CustomerId` int,
KEY `FK_Products_GuestId_idx` (`GuestId`),
KEY `FK_Products_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`ProductsId`)
);

--
-- Table structure for table Payment
--

CREATE TABLE `Payment` (
`CardType` varchar(64),
`PaymentName` varchar(64),
`CardNo` int,
`PaymentId` int NOT NULL,
PRIMARY KEY (`PaymentId`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`Address` varchar(64),
`CustomerName` varchar(64),
`PhoneNo` int,
`CustomerId` int NOT NULL,
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table Guest
--

CREATE TABLE `Guest` (
`GuestId` int NOT NULL,
PRIMARY KEY (`GuestId`)
);

--
-- Table structure for table Admin
--

CREATE TABLE `Admin` (
`AdminName` varchar(64),
`AdminId` int NOT NULL,
PRIMARY KEY (`AdminId`)
);

--
-- Table structure for table CustomerPaymentAssociation
--

CREATE TABLE `CustomerPaymentAssociation` (
`PaymentId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_CustomerPaymentAssociation_PaymentId_idx` (`PaymentId`),
KEY `FK_CustomerPaymentAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`PaymentId`,`CustomerId`)
);

--
-- Table structure for table CustomerCartAssociation
--

CREATE TABLE `CustomerCartAssociation` (
`CartId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_CustomerCartAssociation_CartId_idx` (`CartId`),
KEY `FK_CustomerCartAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`CartId`,`CustomerId`)
);

--
-- Table structure for table Cart
--

CREATE TABLE `Cart` (
`Total` int,
`Price` int,
`NumOfProducts` int,
`CartId` int NOT NULL,
PRIMARY KEY (`CartId`)
);

ALTER TABLE `AdminProductsAssociation`
  ADD CONSTRAINT `FK_AdminProductsAssociation_ProductsId` FOREIGN KEY (`ProductsId`) REFERENCES `Products` (`ProductsId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_AdminProductsAssociation_AdminId` FOREIGN KEY (`AdminId`) REFERENCES `Admin` (`AdminId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Products`
  ADD CONSTRAINT `FK_Products_GuestId` FOREIGN KEY (`GuestId`) REFERENCES `Guest` (`GuestId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Products_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerPaymentAssociation`
  ADD CONSTRAINT `FK_CustomerPaymentAssociation_PaymentId` FOREIGN KEY (`PaymentId`) REFERENCES `Payment` (`PaymentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerPaymentAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerCartAssociation`
  ADD CONSTRAINT `FK_CustomerCartAssociation_CartId` FOREIGN KEY (`CartId`) REFERENCES `Cart` (`CartId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCartAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;
