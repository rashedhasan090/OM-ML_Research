-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/Order_Process/ImplSolution/Order_Process_Sol_51.sql

USE Order_Process_Sol_51;
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
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table ManagementInventoryAssociation
--

CREATE TABLE `ManagementInventoryAssociation` (
`ManagementId` int NOT NULL, 
`ItemId` int NOT NULL, 
KEY `FK_ManagementInventoryAssociation_ManagementId_idx` (`ManagementId`),
KEY `FK_ManagementInventoryAssociation_ItemId_idx` (`ItemId`),
PRIMARY KEY (`ManagementId`,`ItemId`)
);

--
-- Table structure for table Management
--

CREATE TABLE `Management` (
`ManagementAddress` varchar(64),
`ManagementName` varchar(64),
`ManagementAcctNo` int,
`ManagementPhoneNo` int,
`ManagementId` int NOT NULL, 
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
`ItemId` int NOT NULL, 
PRIMARY KEY (`ItemId`)
);

--
-- Table structure for table CustomerManagementAssociation
--

CREATE TABLE `CustomerManagementAssociation` (
`CustomerId` int NOT NULL, 
`ManagementId` int NOT NULL, 
KEY `FK_CustomerManagementAssociation_CustomerId_idx` (`CustomerId`),
KEY `FK_CustomerManagementAssociation_ManagementId_idx` (`ManagementId`),
PRIMARY KEY (`CustomerId`,`ManagementId`)
);

ALTER TABLE `ManagementCustomerAssociation`
  ADD CONSTRAINT `FK_ManagementCustomerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ManagementCustomerAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Products`
  ADD CONSTRAINT `FK_Products_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ManagementInventoryAssociation`
  ADD CONSTRAINT `FK_ManagementInventoryAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ManagementInventoryAssociation_ItemId` FOREIGN KEY (`ItemId`) REFERENCES `Inventory` (`ItemId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ManagementProductsAssociation`
  ADD CONSTRAINT `FK_ManagementProductsAssociation_ProductsId` FOREIGN KEY (`ProductsId`) REFERENCES `Products` (`ProductsId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ManagementProductsAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerManagementAssociation`
  ADD CONSTRAINT `FK_CustomerManagementAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerManagementAssociation_ManagementId` FOREIGN KEY (`ManagementId`) REFERENCES `Management` (`ManagementId`) ON DELETE CASCADE ON UPDATE CASCADE;
