-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/CreditCardProcess/ImplSolution/CreditCardProcess_Sol_15.sql

USE CreditCardProcess_Sol_15;
--
-- Table structure for table CustomerCreditCardAssociation
--

CREATE TABLE `CustomerCreditCardAssociation` (
`CreditCardId` int NOT NULL, 
`CustomerId` int NOT NULL, 
KEY `FK_CustomerCreditCardAssociation_CreditCardId_idx` (`CreditCardId`),
KEY `FK_CustomerCreditCardAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`CreditCardId`,`CustomerId`)
);

--
-- Table structure for table Bankreq
--

CREATE TABLE `Bankreq` (
`Info` varchar(64),
`CustomerId` int,
`InstructionCode` int NOT NULL, 
KEY `FK_Bankreq_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`InstructionCode`)
);

--
-- Table structure for table CreditCardSys
--

CREATE TABLE `CreditCardSys` (
`CreditCardId` int NOT NULL, 
`CustomerId` int,
`SysId` int,
PRIMARY KEY (`CreditCardId`)
);

--
-- Table structure for table ProcessStaff
--

CREATE TABLE `ProcessStaff` (
`ClientList` varchar(64),
`StaffName` varchar(64),
`StaffId` int NOT NULL, 
PRIMARY KEY (`StaffId`)
);

--
-- Table structure for table CardMaker
--

CREATE TABLE `CardMaker` (
`AcquireDate` varchar(64),
`StaffId` int,
`EquipmentId` int NOT NULL, 
KEY `FK_CardMaker_StaffId_idx` (`StaffId`),
PRIMARY KEY (`EquipmentId`)
);

--
-- Table structure for table Customer
--

CREATE TABLE `Customer` (
`CustomerAddress` varchar(64),
`CustomerName` varchar(64),
`StaffId` int,
`TaxpayerId` int,
`CustomerPhoneNo` int,
`CustomerId` int NOT NULL, 
KEY `FK_Customer_StaffId_idx` (`StaffId`),
PRIMARY KEY (`CustomerId`)
);

--
-- Table structure for table CustomerCardMakerAssociation
--

CREATE TABLE `CustomerCardMakerAssociation` (
`EquipmentId` int NOT NULL, 
`CustomerId` int NOT NULL, 
KEY `FK_CustomerCardMakerAssociation_EquipmentId_idx` (`EquipmentId`),
KEY `FK_CustomerCardMakerAssociation_CustomerId_idx` (`CustomerId`),
PRIMARY KEY (`EquipmentId`,`CustomerId`)
);

--
-- Table structure for table CreditCardInfo
--

CREATE TABLE `CreditCardInfo` (
`CustomerCredentials` int,
`CreditCardId` int NOT NULL, 
`CustomerId` int,
PRIMARY KEY (`CreditCardId`)
);

--
-- Table structure for table CreditCard
--

CREATE TABLE `CreditCard` (
`CreditCardId` int NOT NULL, 
PRIMARY KEY (`CreditCardId`)
);

ALTER TABLE `CustomerCreditCardAssociation`
  ADD CONSTRAINT `FK_CustomerCreditCardAssociation_CreditCardId` FOREIGN KEY (`CreditCardId`) REFERENCES `CreditCard` (`CreditCardId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCreditCardAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Bankreq`
  ADD CONSTRAINT `FK_Bankreq_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CardMaker`
  ADD CONSTRAINT `FK_CardMaker_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `ProcessStaff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Customer`
  ADD CONSTRAINT `FK_Customer_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `ProcessStaff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerCardMakerAssociation`
  ADD CONSTRAINT `FK_CustomerCardMakerAssociation_EquipmentId` FOREIGN KEY (`EquipmentId`) REFERENCES `CardMaker` (`EquipmentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCardMakerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;
