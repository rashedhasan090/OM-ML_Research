-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/Canteen/ImplSolution/Canteen_Sol_275.sql

USE Canteen_Sol_275;
--
-- Table structure for table Orders
--

CREATE TABLE `Orders` (
`Customer_Info` varchar(64),
`OrderNumber` varchar(64),
`OrdersName` varchar(64),
`OrdersId` int NOT NULL, 
PRIMARY KEY (`OrdersId`)
);

--
-- Table structure for table Canteen
--

CREATE TABLE `Canteen` (
`UserType` varchar(64),
`OrderNumber` varchar(64),
`CanteenId` int NOT NULL, 
PRIMARY KEY (`CanteenId`)
);

--
-- Table structure for table User
--

CREATE TABLE `User` (
`DType` varchar(64),
`ResponsibilityLog` varchar(64),
`TotalItemsSold` varchar(64),
`IntructionType` varchar(64),
`UserId` int NOT NULL, 
PRIMARY KEY (`UserId`)
);

--
-- Table structure for table Product
--

CREATE TABLE `Product` (
`Description` int,
`ProductType` int,
`NoInventoryProducts` int,
`NoTotalProducts` int,
`NoOfSoldProducts` int,
`ProductId` int NOT NULL, 
`PaymentId` int,
KEY `FK_Product_PaymentId_idx` (`PaymentId`),
PRIMARY KEY (`ProductId`)
);

--
-- Table structure for table CanteenProductAssociation
--

CREATE TABLE `CanteenProductAssociation` (
`CanteenId` int NOT NULL, 
`ProductId` int NOT NULL, 
KEY `FK_CanteenProductAssociation_CanteenId_idx` (`CanteenId`),
KEY `FK_CanteenProductAssociation_ProductId_idx` (`ProductId`),
PRIMARY KEY (`CanteenId`,`ProductId`)
);

--
-- Table structure for table Payment
--

CREATE TABLE `Payment` (
`ProductDetails` varchar(64),
`PaymentId` int NOT NULL, 
PRIMARY KEY (`PaymentId`)
);

--
-- Table structure for table OrdersLibraryDbAssociation
--

CREATE TABLE `OrdersLibraryDbAssociation` (
`OrdersId` int NOT NULL, 
`PaymentId` int NOT NULL, 
KEY `FK_OrdersLibraryDbAssociation_OrdersId_idx` (`OrdersId`),
KEY `FK_OrdersLibraryDbAssociation_PaymentId_idx` (`PaymentId`),
PRIMARY KEY (`OrdersId`,`PaymentId`)
);

--
-- Table structure for table UserCanteenAssociation
--

CREATE TABLE `UserCanteenAssociation` (
`CanteenId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserCanteenAssociation_CanteenId_idx` (`CanteenId`),
KEY `FK_UserCanteenAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`CanteenId`,`UserId`)
);

--
-- Table structure for table CanteenFoodAssociation
--

CREATE TABLE `CanteenFoodAssociation` (
`CanteenId` int NOT NULL, 
`ItemId` int NOT NULL, 
KEY `FK_CanteenFoodAssociation_CanteenId_idx` (`CanteenId`),
KEY `FK_CanteenFoodAssociation_ItemId_idx` (`ItemId`),
PRIMARY KEY (`CanteenId`,`ItemId`)
);

--
-- Table structure for table CanteenOrdersAssociation
--

CREATE TABLE `CanteenOrdersAssociation` (
`CanteenId` int NOT NULL, 
`OrdersId` int NOT NULL, 
KEY `FK_CanteenOrdersAssociation_CanteenId_idx` (`CanteenId`),
KEY `FK_CanteenOrdersAssociation_OrdersId_idx` (`OrdersId`),
PRIMARY KEY (`CanteenId`,`OrdersId`)
);

--
-- Table structure for table UserFoodAssociation
--

CREATE TABLE `UserFoodAssociation` (
`ItemId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserFoodAssociation_ItemId_idx` (`ItemId`),
KEY `FK_UserFoodAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`ItemId`,`UserId`)
);

--
-- Table structure for table UserProductAssociation
--

CREATE TABLE `UserProductAssociation` (
`ProductId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserProductAssociation_ProductId_idx` (`ProductId`),
KEY `FK_UserProductAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`ProductId`,`UserId`)
);

--
-- Table structure for table Food
--

CREATE TABLE `Food` (
`Price` varchar(64),
`FoodType` varchar(64),
`FoodCategory` varchar(64),
`OrdersId` int,
`ItemId` int NOT NULL, 
`PaymentId` int,
KEY `FK_Food_OrdersId_idx` (`OrdersId`),
KEY `FK_Food_PaymentId_idx` (`PaymentId`),
PRIMARY KEY (`ItemId`)
);

ALTER TABLE `Product`
  ADD CONSTRAINT `FK_Product_PaymentId` FOREIGN KEY (`PaymentId`) REFERENCES `Payment` (`PaymentId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CanteenProductAssociation`
  ADD CONSTRAINT `FK_CanteenProductAssociation_CanteenId` FOREIGN KEY (`CanteenId`) REFERENCES `Canteen` (`CanteenId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CanteenProductAssociation_ProductId` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `OrdersLibraryDbAssociation`
  ADD CONSTRAINT `FK_OrdersLibraryDbAssociation_OrdersId` FOREIGN KEY (`OrdersId`) REFERENCES `Orders` (`OrdersId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_OrdersLibraryDbAssociation_PaymentId` FOREIGN KEY (`PaymentId`) REFERENCES `Payment` (`PaymentId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserCanteenAssociation`
  ADD CONSTRAINT `FK_UserCanteenAssociation_CanteenId` FOREIGN KEY (`CanteenId`) REFERENCES `Canteen` (`CanteenId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserCanteenAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CanteenFoodAssociation`
  ADD CONSTRAINT `FK_CanteenFoodAssociation_CanteenId` FOREIGN KEY (`CanteenId`) REFERENCES `Canteen` (`CanteenId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CanteenFoodAssociation_ItemId` FOREIGN KEY (`ItemId`) REFERENCES `Food` (`ItemId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CanteenOrdersAssociation`
  ADD CONSTRAINT `FK_CanteenOrdersAssociation_CanteenId` FOREIGN KEY (`CanteenId`) REFERENCES `Canteen` (`CanteenId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CanteenOrdersAssociation_OrdersId` FOREIGN KEY (`OrdersId`) REFERENCES `Orders` (`OrdersId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserFoodAssociation`
  ADD CONSTRAINT `FK_UserFoodAssociation_ItemId` FOREIGN KEY (`ItemId`) REFERENCES `Food` (`ItemId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserFoodAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserProductAssociation`
  ADD CONSTRAINT `FK_UserProductAssociation_ProductId` FOREIGN KEY (`ProductId`) REFERENCES `Product` (`ProductId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserProductAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Food`
  ADD CONSTRAINT `FK_Food_OrdersId` FOREIGN KEY (`OrdersId`) REFERENCES `Orders` (`OrdersId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Food_PaymentId` FOREIGN KEY (`PaymentId`) REFERENCES `Payment` (`PaymentId`) ON DELETE CASCADE ON UPDATE CASCADE;

