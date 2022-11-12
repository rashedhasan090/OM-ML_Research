-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/OnlineStore/ImplSolution/OnlineStore_Sol_12.sql

USE OnlineStore_Sol_12;
--
-- Table structure for table ProductsGuestAssociation
--

CREATE TABLE `ProductsGuestAssociation` (
`ProductsId` int NOT NULL,
`GuestId` int NOT NULL,
KEY `FK_ProductsGuestAssociation_ProductsId_idx` (`ProductsId`),
KEY `FK_ProductsGuestAssociation_GuestId_idx` (`GuestId`),
PRIMARY KEY (`ProductsId`,`GuestId`)
);

--
-- Table structure for table Products
--

CREATE TABLE `Products` (
`Subgroup` varchar(64),
`Group` varchar(64),
`ProductsName` varchar(64),
`ProductsId` int NOT NULL,
`AdminId` int,
KEY `FK_Products_AdminId_idx` (`AdminId`),
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
-- Table structure for table CustomerProductsAssociation
--

CREATE TABLE `CustomerProductsAssociation` (
`ProductsId` int NOT NULL,
`CustomerId` int NOT NULL,
KEY `FK_CustomerProductsAssociation_ProductsId_idx` (`ProductsId`),
KEY `FK_CustomerProductsAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`ProductsId`,`CustomerId`)
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
-- Table structure for table Cart
--

CREATE TABLE `Cart` (
`Total` int,
`Price` int,
`NumOfProducts` int,
`CartId` int NOT NULL,
PRIMARY KEY (`CartId`)
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

ALTER TABLE `ProductsGuestAssociation`
  ADD CONSTRAINT `FK_ProductsGuestAssociation_ProductsId` FOREIGN KEY (`ProductsId`) REFERENCES `Products` (`ProductsId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductsGuestAssociation_GuestId` FOREIGN KEY (`GuestId`) REFERENCES `Guest` (`GuestId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Products`
  ADD CONSTRAINT `FK_Products_AdminId` FOREIGN KEY (`AdminId`) REFERENCES `Admin` (`AdminId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerProductsAssociation`
  ADD CONSTRAINT `FK_CustomerProductsAssociation_ProductsId` FOREIGN KEY (`ProductsId`) REFERENCES `Products` (`ProductsId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerProductsAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerPaymentAssociation`
  ADD CONSTRAINT `FK_CustomerPaymentAssociation_PaymentId` FOREIGN KEY (`PaymentId`) REFERENCES `Payment` (`PaymentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerPaymentAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerCartAssociation`
  ADD CONSTRAINT `FK_CustomerCartAssociation_CartId` FOREIGN KEY (`CartId`) REFERENCES `Cart` (`CartId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCartAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;
