-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/store/ImplSolution/store_Sol_1222.sql

USE store_Sol_1222;
--
-- Table structure for table Owner
--

CREATE TABLE `Owner` (
`ownerName` varchar(64),
`UserId` int NOT NULL, 
KEY `FK_Owner_UserId_idx` (`UserId`),
PRIMARY KEY (`UserId`)
);

--
-- Table structure for table User
--

CREATE TABLE `User` (
`UserId` int NOT NULL, 
PRIMARY KEY (`UserId`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`CustomerPhone` varchar(64),
`CustomerAddress` varchar(64),
`CustomerName` varchar(64),
`CustomerId` int NOT NULL, 
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table StoreDatabase
--

CREATE TABLE `StoreDatabase` (
`ListOFStocks` varchar(64),
`StoreDbId` int NOT NULL, 
PRIMARY KEY (`StoreDbId`)
);

--
-- Table structure for table Staff
--

CREATE TABLE `Staff` (
`Dept` varchar(64),
`UserId` int NOT NULL, 
KEY `FK_Staff_UserId_idx` (`UserId`),
PRIMARY KEY (`UserId`)
);

--
-- Table structure for table Store
--

CREATE TABLE `Store` (
`TransactionId` int,
`TotalAmount` int,
`StoreName` int,
`StoreType` int,
`NoReservedProducts` int,
`NoSoldProducts` int,
`StoreId` int NOT NULL, 
`StoreDbId` int,
KEY `FK_Store_TransactionId_idx` (`TransactionId`),
KEY `FK_Store_StoreDbId_idx` (`StoreDbId`),
PRIMARY KEY (`StoreId`)
);

--
-- Table structure for table UserStockAssociation
--

CREATE TABLE `UserStockAssociation` (
`StockId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserStockAssociation_StockId_idx` (`StockId`),
KEY `FK_UserStockAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`StockId`,`UserId`)
);

--
-- Table structure for table UserSMSAssociation
--

CREATE TABLE `UserSMSAssociation` (
`TransactionId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserSMSAssociation_TransactionId_idx` (`TransactionId`),
KEY `FK_UserSMSAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`TransactionId`,`UserId`)
);

--
-- Table structure for table CustomerStoreDbAssociation
--

CREATE TABLE `CustomerStoreDbAssociation` (
`CustomerId` int NOT NULL, 
`StoreDbId` int NOT NULL, 
KEY `FK_CustomerStoreDbAssociation_CustomerId_idx` (`CustomerId`),
KEY `FK_CustomerStoreDbAssociation_StoreDbId_idx` (`StoreDbId`),
PRIMARY KEY (`CustomerId`,`StoreDbId`)
);

--
-- Table structure for table UserStoreAssociation
--

CREATE TABLE `UserStoreAssociation` (
`StoreId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserStoreAssociation_StoreId_idx` (`StoreId`),
KEY `FK_UserStoreAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`StoreId`,`UserId`)
);

--
-- Table structure for table SMSCustomerAssociation
--

CREATE TABLE `SMSCustomerAssociation` (
`TransactionId` int NOT NULL, 
`CustomerId` int NOT NULL, 
KEY `FK_SMSCustomerAssociation_TransactionId_idx` (`TransactionId`),
KEY `FK_SMSCustomerAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`TransactionId`,`CustomerId`)
);

--
-- Table structure for table Stock
--

CREATE TABLE `Stock` (
`StockDescription` varchar(64),
`StockItems` varchar(64),
`Type` varchar(64),
`TransactionId` int,
`CustomerId` int,
`StockId` int NOT NULL, 
KEY `FK_Stock_TransactionId_idx` (`TransactionId`),
KEY `FK_Stock_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`StockId`)
);

--
-- Table structure for table StockStoreDbAssociation
--

CREATE TABLE `StockStoreDbAssociation` (
`StockId` int NOT NULL, 
`StoreDbId` int NOT NULL, 
KEY `FK_StockStoreDbAssociation_StockId_idx` (`StockId`),
KEY `FK_StockStoreDbAssociation_StoreDbId_idx` (`StoreDbId`),
PRIMARY KEY (`StockId`,`StoreDbId`)
);

--
-- Table structure for table StoreManagementSystem
--

CREATE TABLE `StoreManagementSystem` (
`UserType` varchar(64),
`CustomerAddress` varchar(64),
`UserName` varchar(64),
`TransactionId` int NOT NULL, 
PRIMARY KEY (`TransactionId`)
);

ALTER TABLE `Owner`
  ADD CONSTRAINT `FK_Owner_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Staff`
  ADD CONSTRAINT `FK_Staff_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Store`
  ADD CONSTRAINT `FK_Store_TransactionId` FOREIGN KEY (`TransactionId`) REFERENCES `StoreManagementSystem` (`TransactionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Store_StoreDbId` FOREIGN KEY (`StoreDbId`) REFERENCES `StoreDatabase` (`StoreDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserStockAssociation`
  ADD CONSTRAINT `FK_UserStockAssociation_StockId` FOREIGN KEY (`StockId`) REFERENCES `Stock` (`StockId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserStockAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserSMSAssociation`
  ADD CONSTRAINT `FK_UserSMSAssociation_TransactionId` FOREIGN KEY (`TransactionId`) REFERENCES `StoreManagementSystem` (`TransactionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserSMSAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerStoreDbAssociation`
  ADD CONSTRAINT `FK_CustomerStoreDbAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerStoreDbAssociation_StoreDbId` FOREIGN KEY (`StoreDbId`) REFERENCES `StoreDatabase` (`StoreDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserStoreAssociation`
  ADD CONSTRAINT `FK_UserStoreAssociation_StoreId` FOREIGN KEY (`StoreId`) REFERENCES `Store` (`StoreId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserStoreAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `SMSCustomerAssociation`
  ADD CONSTRAINT `FK_SMSCustomerAssociation_TransactionId` FOREIGN KEY (`TransactionId`) REFERENCES `StoreManagementSystem` (`TransactionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_SMSCustomerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Stock`
  ADD CONSTRAINT `FK_Stock_TransactionId` FOREIGN KEY (`TransactionId`) REFERENCES `StoreManagementSystem` (`TransactionId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Stock_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `StockStoreDbAssociation`
  ADD CONSTRAINT `FK_StockStoreDbAssociation_StockId` FOREIGN KEY (`StockId`) REFERENCES `Stock` (`StockId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_StockStoreDbAssociation_StoreDbId` FOREIGN KEY (`StoreDbId`) REFERENCES `StoreDatabase` (`StoreDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

