-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/ecommerce/ImplSolution/ecommerce_Sol_397.sql

USE ecommerce_Sol_397;
--
-- Table structure for table Order
--

CREATE TABLE `Order` (
`orderID` int NOT NULL, 
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
`ItemID` int NOT NULL, 
KEY `FK_CartItem_ItemID_idx` (`ItemID`),
PRIMARY KEY (`ItemID`)
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

--
-- Table structure for table ShippingCart
--

CREATE TABLE `ShippingCart` (
`shippingCartID` int NOT NULL, 
`customerID` int,
KEY `FK_ShippingCart_customerID_idx` (`customerID`),
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
`shippingCartID` int,
`orderID` int,
KEY `FK_Item_shippingCartID_idx` (`shippingCartID`),
KEY `FK_Item_orderID_idx` (`orderID`),
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
`weight` decimal(20,5),
`productID` int NOT NULL, 
KEY `FK_PhysicalProduct_productID_idx` (`productID`),
PRIMARY KEY (`productID`)
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
`assetID` int NOT NULL, 
KEY `FK_Documents_assetID_idx` (`assetID`),
PRIMARY KEY (`assetID`)
);

--
-- Table structure for table OrderItem
--

CREATE TABLE `OrderItem` (
`orderItemID` int,
`status` int,
`quantity` int,
`ItemID` int NOT NULL, 
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
-- Table structure for table ProductCategoryAssociation
--

CREATE TABLE `ProductCategoryAssociation` (
`productID` int NOT NULL, 
`categoryID` int NOT NULL, 
KEY `FK_ProductCategoryAssociation_productID_idx` (`productID`),
KEY `FK_ProductCategoryAssociation_categoryID_idx` (`categoryID`),
PRIMARY KEY (`productID`,`categoryID`)
);

ALTER TABLE `Media`
  ADD CONSTRAINT `FK_Media_assetID` FOREIGN KEY (`assetID`) REFERENCES `Asset` (`assetID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Service`
  ADD CONSTRAINT `FK_Service_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CartItem`
  ADD CONSTRAINT `FK_CartItem_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerOrderAssociation`
  ADD CONSTRAINT `FK_CustomerOrderAssociation_orderID` FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerOrderAssociation_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ShippingCart`
  ADD CONSTRAINT `FK_ShippingCart_customerID` FOREIGN KEY (`customerID`) REFERENCES `Customer` (`customerID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Catalog`
  ADD CONSTRAINT `FK_Catalog_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductItemAssociation`
  ADD CONSTRAINT `FK_ProductItemAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductItemAssociation_ItemID` FOREIGN KEY (`ItemID`) REFERENCES `Item` (`ItemID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Item`
  ADD CONSTRAINT `FK_Item_shippingCartID` FOREIGN KEY (`shippingCartID`) REFERENCES `ShippingCart` (`shippingCartID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Item_orderID` FOREIGN KEY (`orderID`) REFERENCES `Order` (`orderID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `PhysicalProduct`
  ADD CONSTRAINT `FK_PhysicalProduct_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductAssetAssociation`
  ADD CONSTRAINT `FK_ProductAssetAssociation_assetID` FOREIGN KEY (`assetID`) REFERENCES `Asset` (`assetID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductAssetAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Documents`
  ADD CONSTRAINT `FK_Documents_assetID` FOREIGN KEY (`assetID`) REFERENCES `Asset` (`assetID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ProductCategoryAssociation`
  ADD CONSTRAINT `FK_ProductCategoryAssociation_productID` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ProductCategoryAssociation_categoryID` FOREIGN KEY (`categoryID`) REFERENCES `Category` (`categoryID`) ON DELETE CASCADE ON UPDATE CASCADE;

