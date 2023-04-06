-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/ecommerce/ImplSolution/ecommerce_Sol_6163.sql

USE ecommerce_Sol_6163;
--
-- Table structure for table Order
--

CREATE TABLE `Order` (
`orderID` int NOT NULL, 
`customerID` int,
KEY `FK_Order_customerID_idx` (`customerID`),
PRIMARY KEY (`orderID`)
);

--
-- Table structure for table Category
--

CREATE TABLE `Category` (
`categoryName` varchar(64),
`categoryID` int NOT NULL, 
PRIMARY KEY (`categoryID`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`customerID` int NOT NULL, 
PRIMARY KEY (`customerID`)
);

--
-- Table structure for table ShippingCartItemAssociation
--

CREATE TABLE `ShippingCartItemAssociation` (
`ItemID` int NOT NULL, 
`shippingCartID` int NOT NULL, 
KEY `FK_ShippingCartItemAssociation_ItemID_idx` (`ItemID`),
KEY `FK_ShippingCartItemAssociation_shippingCartID_idx` (`shippingCartID`),
PRIMARY KEY (`ItemID`,`shippingCartID`)
);

--
-- Table structure for table Media
--

CREATE TABLE `Media` (
`mediaType` int,
`assetID` int NOT NULL, 
KEY `FK_Media_assetID_idx` (`assetID`),
PRIMARY KEY (`assetID`)
);

--
-- Table structure for table Product
--

CREATE TABLE `Product` (
`description` varchar(64),
`productName` varchar(64),
`price` decimal(20,5),
`productID` int NOT NULL, 
PRIMARY KEY (`productID`)
);

--
-- Table structure for table Service
--

CREATE TABLE `Service` (
`schedule` varchar(64),
`productID` int NOT NULL, 
KEY `FK_Service_productID_idx` (`productID`),
PRIMARY KEY (`productID`)
);

--
-- Table structure for table CartItem
--

CREATE TABLE `CartItem` (
`cartItemID` int,
`quantity` int,
`ItemID` int NOT NULL, 
PRIMARY KEY (`ItemID`)
);

--
-- Table structure for table ShippingCart
--

CREATE TABLE `ShippingCart` (
`shippingCartID` int NOT NULL, 
PRIMARY KEY (`shippingCartID`)
);

--
-- Table structure for table Catalog
--

CREATE TABLE `Catalog` (
`CatalogID` int NOT NULL, 
`productID` int,
KEY `FK_Catalog_productID_idx` (`productID`),
PRIMARY KEY (`CatalogID`)
);

--
-- Table structure for table ProductItemAssociation
--

CREATE TABLE `ProductItemAssociation` (
`productID` int NOT NULL, 
`ItemID` int NOT NULL, 
KEY `FK_ProductItemAssociation_productID_idx` (`productID`),
KEY `FK_ProductItemAssociation_ItemID_idx` (`ItemID`),
PRIMARY KEY (`productID`,`ItemID`)
);

--
-- Table structure for table Item
--

CREATE TABLE `Item` (
`quantity` int,
`ItemID` int NOT NULL, 
PRIMARY KEY (`ItemID`)
);

--
-- Table structure for table ElectronicProduct
--

CREATE TABLE `ElectronicProduct` (
`size` varchar(64),
`description` varchar(64),
`productName` varchar(64),
`price` decimal(20,5),
`productID` int NOT NULL, 
PRIMARY KEY (`productID`)
);

--
-- Table structure for table PhysicalProduct
--

CREATE TABLE `PhysicalProduct` (
`availability` boolean,
`description` varchar(64),
`productName` varchar(64),
`weight` decimal(20,5),
`price` decimal(20,5),
`productID` int NOT NULL, 
PRIMARY KEY (`productID`)
);

--
-- Table structure for table CustomerShippingCartAssociation
--

CREATE TABLE `CustomerShippingCartAssociation` (
`shippingCartID` int NOT NULL, 
`customerID` int NOT NULL, 
KEY `FK_CustomerShippingCartAssociation_shippingCartID_idx` (`shippingCartID`),
KEY `FK_CustomerShippingCartAssociation_customerID_idx` (`customerID`),
PRIMARY KEY (`shippingCartID`,`customerID`)
);

--
-- Table structure for table ProductAssetAssociation
--

CREATE TABLE `ProductAssetAssociation` (
`assetID` int NOT NULL, 
`productID` int NOT NULL, 
KEY `FK_ProductAssetAssociation_assetID_idx` (`assetID`),
KEY `FK_ProductAssetAssociation_productID_idx` (`productID`),
PRIMARY KEY (`assetID`,`productID`)
);

--
-- Table structure for table Documents
--

CREATE TABLE `Documents` (
`excerpt` varchar(64),
`fileURI` varchar(64),
`assetName` varchar(64),
`assetID` int NOT NULL, 
PRIMARY KEY (`assetID`)
);

--
-- Table structure for table OrderItem
--

CREATE TABLE `OrderItem` (
`orderItemID` int,
`status` int,
`ItemID` int NOT NULL, 
KEY `FK_OrderItem_ItemID_idx` (`ItemID`),
PRIMARY KEY (`ItemID`)
);

--
-- Table structure for table Asset
--

CREATE TABLE `Asset` (
`fileURI` varchar(64),
`assetName` varchar(64),
`assetID` int NOT NULL, 
PRIMARY KEY (`assetID`)
);

--
-- Table structure for table OrderItemAssociation
--

CREATE TABLE `OrderItemAssociation` (
`ItemID` int NOT NULL, 
`orderID` int NOT NULL, 
KEY `FK_OrderItemAssociation_ItemID_idx` (`ItemID`),
KEY `FK_OrderItemAssociation_orderID_idx` (`orderID`),
PRIMARY KEY (`ItemID`,`orderID`)
);

--
-- Table structure for table ProductCategoryAssociation
--

CREATE TABLE `ProductCategoryAssociation` (
`productID` int NOT NULL, 
`categoryID` int NOT NULL, 
KEY `FK_ProductCategoryAssociation_productID_idx` (`productID`),
KEY `FK_ProductCategoryAssociation_categoryID_idx` (`categoryID`),
PRIMARY KEY (`productID`,`categoryID`)
);

ALTER TABLE `Order`
  ADD CONSTRAINT `FK_Order_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ShippingCartItemAssociation`
  ADD CONSTRAINT `FK_ShippingCartItemAssociation_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ShippingCartItemAssociation_shippingCartID` FOREIGN KEY (`shippingCartID`) REFERENCES `ShippingCart` (`shippingCartID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Media`
  ADD CONSTRAINT `FK_Media_assetID` FOREIGN KEY (`assetID`) REFERENCES `Asset` (`assetID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Service`
  ADD CONSTRAINT `FK_Service_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Catalog`
  ADD CONSTRAINT `FK_Catalog_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductItemAssociation`
  ADD CONSTRAINT `FK_ProductItemAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductItemAssociation_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerShippingCartAssociation`
  ADD CONSTRAINT `FK_CustomerShippingCartAssociation_shippingCartID` FOREIGN KEY (`shippingCartID`) REFERENCES `ShippingCart` (`shippingCartID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerShippingCartAssociation_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductAssetAssociation`
  ADD CONSTRAINT `FK_ProductAssetAssociation_assetID` FOREIGN KEY (`assetID`) REFERENCES `Asset` (`assetID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductAssetAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `OrderItem`
  ADD CONSTRAINT `FK_OrderItem_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `OrderItemAssociation`
  ADD CONSTRAINT `FK_OrderItemAssociation_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_OrderItemAssociation_orderID` FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductCategoryAssociation`
  ADD CONSTRAINT `FK_ProductCategoryAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductCategoryAssociation_categoryID` FOREIGN KEY (`categoryID`) REFERENCES `Category` (`categoryID`) ON DELETE CASCADE ON UPDATE CASCADE;

