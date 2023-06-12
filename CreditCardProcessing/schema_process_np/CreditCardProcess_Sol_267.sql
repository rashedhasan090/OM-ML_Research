-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/CreditCardProcess/ImplSolution/CreditCardProcess_Sol_267.sql

USE CreditCardProcess_Sol_267;
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
`InstructionCode` int NOT NULL, 
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
-- Table structure for table CustomerBankreqAssociation
--

CREATE TABLE `CustomerBankreqAssociation` (
`CustomerId` int NOT NULL, 
`InstructionCode` int NOT NULL, 
KEY `FK_CustomerBankreqAssociation_CustomerId_idx` (`CustomerId`),
KEY `FK_CustomerBankreqAssociation_InstructionCode_idx` (`InstructionCode`),
PRIMARY KEY (`CustomerId`,`InstructionCode`)
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
KEY `FK_CreditCardInfo_CreditCardId_idx` (`CreditCardId`),
PRIMARY KEY (`CreditCardId`)
);

--
-- Table structure for table CreditCard
--

CREATE TABLE `CreditCard` (
`CreditCardId` int NOT NULL, 
`CustomerId` int,
PRIMARY KEY (`CreditCardId`)
);

ALTER TABLE `CustomerCreditCardAssociation`
  ADD CONSTRAINT `FK_CustomerCreditCardAssociation_CreditCardId` FOREIGN KEY (`CreditCardId`) REFERENCES `CreditCard` (`CreditCardId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCreditCardAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CardMaker`
  ADD CONSTRAINT `FK_CardMaker_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `ProcessStaff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Customer`
  ADD CONSTRAINT `FK_Customer_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `ProcessStaff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerBankreqAssociation`
  ADD CONSTRAINT `FK_CustomerBankreqAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerBankreqAssociation_InstructionCode` FOREIGN KEY (`InstructionCode`) REFERENCES `Bankreq` (`InstructionCode`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CustomerCardMakerAssociation`
  ADD CONSTRAINT `FK_CustomerCardMakerAssociation_EquipmentId` FOREIGN KEY (`EquipmentId`) REFERENCES `CardMaker` (`EquipmentId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CustomerCardMakerAssociation_CustomerId` FOREIGN KEY (`CustomerId`) REFERENCES `Customer` (`CustomerId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CreditCardInfo`
  ADD CONSTRAINT `FK_CreditCardInfo_CreditCardId` FOREIGN KEY (`CreditCardId`) REFERENCES `CreditCard` (`CreditCardId`) ON DELETE CASCADE ON UPDATE CASCADE;

