-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/Order_Process/ImplSolution/Order_Process_Sol_7.sql

USE Order_Process_Sol_7;
--
-- Table structure for table Order
--

CREATE TABLE `Order` (
`OrderId` int,
`CustomerId` int,
`ManagementId` int NOT NULL, 
PRIMARY KEY (`ManagementId`)
);

--
-- Table structure for table ManagementCustomerAssociation
--

CREATE TABLE `ManagementCustomerAssociation` (
`CustomerId` int NOT NULL, 
`ManagementId` int NOT NULL, 
KEY `FK_ManagementCustomerAssociation_CustomerId_idx` (`CustomerId`),
KEY `FK_ManagementCustomerAssociation_ManagementId_idx` (`ManagementId`),
PRIMARY KEY (`CustomerId`,`ManagementId`)
);

--
-- Table structure for table Products
--

CREATE TABLE `Products` (
`ProductsName` varchar(64),
`CustomerId` int,
`ProductsId` int NOT NULL, 
KEY `FK_Products_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`ProductsId`)
);

--
-- Table structure for table Payment
--

CREATE TABLE `Payment` (
`CustomerId` int,
`ManagementId` int NOT NULL, 
`PaymentId` int,
PRIMARY KEY (`ManagementId`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`CustomerId` int NOT NULL, 
`ManagementId` int,
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table Management
--

CREATE TABLE `Management` (
`ManagementAddress` varchar(64),
`ManagementName` varchar(64),
`CustomerId` int,
`ManagementAcctNo` int,
`ManagementPhoneNo` int,
`ManagementId` int NOT NULL, 
KEY `FK_Management_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`ManagementId`)
);

--
-- Table structure for table Delivery
--

CREATE TABLE `Delivery` (
`DeliveryLocation` varchar(64),
`AgentName` varchar(64),
`DeliveryId` int NOT NULL, 
PRIMARY KEY (`DeliveryId`)
);

--
-- Table structure for table ManagementProductsAssociation
--

CREATE TABLE `ManagementProductsAssociation` (
`ProductsId` int NOT NULL, 
`ManagementId` int NOT NULL, 
KEY `FK_ManagementProductsAssociation_ProductsId_idx` (`ProductsId`),
KEY `FK_ManagementProductsAssociation_ManagementId_idx` (`ManagementId`),
PRIMARY KEY (`ProductsId`,`ManagementId`)
);

--
-- Table structure for table Inventory
--

CREATE TABLE `Inventory` (
`ItemType` varchar(64),
`ManagementId` int,
`ItemId` int NOT NULL, 
KEY `FK_Inventory_ManagementId_idx` (`ManagementId`),
PRIMARY KEY (`ItemId`)
);

ALTER TABLE `ManagementCustomerAssociation`
  ADD CONSTRAINT `FK_ManagementCustomerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ManagementCustomerAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Products`
  ADD CONSTRAINT `FK_Products_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Management`
  ADD CONSTRAINT `FK_Management_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ManagementProductsAssociation`
  ADD CONSTRAINT `FK_ManagementProductsAssociation_ProductsId` FOREIGN KEY (`ProductsId`) REFERENCES `Products` (`ProductsId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ManagementProductsAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Inventory`
  ADD CONSTRAINT `FK_Inventory_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;
