-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/LibraryManagement/ImplSolution/LibraryManagement_Sol_4081.sql

USE LibraryManagement_Sol_4081;
--
-- Table structure for table Account
--

CREATE TABLE `Account` (
`LMSId` int,
`FineAmount` int,
`NoLostBooks` int,
`NoReturnedBooks` int,
`NoReservedBooks` int,
`NoBorrowedBooks` int,
`AccountId` int NOT NULL, 
`LibraryDbId` int,
KEY `FK_Account_LMSId_idx` (`LMSId`),
KEY `FK_Account_LibraryDbId_idx` (`LibraryDbId`),
PRIMARY KEY (`AccountId`)
);

--
-- Table structure for table LibraryDatabase
--

CREATE TABLE `LibraryDatabase` (
`ListOFBooks` varchar(64),
`LibraryDbId` int NOT NULL, 
PRIMARY KEY (`LibraryDbId`)
);

--
-- Table structure for table User
--

CREATE TABLE `User` (
`UserName` varchar(64),
`LMSId` int,
`UserId` int NOT NULL, 
KEY `FK_User_LMSId_idx` (`LMSId`),
PRIMARY KEY (`UserId`)
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
-- Table structure for table UserAccountAssociation
--

CREATE TABLE `UserAccountAssociation` (
`AccountId` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserAccountAssociation_AccountId_idx` (`AccountId`),
KEY `FK_UserAccountAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`AccountId`,`UserId`)
);

--
-- Table structure for table LibraryManagementSystem
--

CREATE TABLE `LibraryManagementSystem` (
`UserType` varchar(64),
`Password` varchar(64),
`LMSId` int NOT NULL, 
PRIMARY KEY (`LMSId`)
);

--
-- Table structure for table Student
--

CREATE TABLE `Student` (
`class` longblob,
`UserName` varchar(64),
`UserId` int NOT NULL, 
PRIMARY KEY (`UserId`)
);

--
-- Table structure for table LMSLibrarianAssociation
--

CREATE TABLE `LMSLibrarianAssociation` (
`LMSId` int NOT NULL, 
`LibrarianId` int NOT NULL, 
KEY `FK_LMSLibrarianAssociation_LMSId_idx` (`LMSId`),
KEY `FK_LMSLibrarianAssociation_LibrarianId_idx` (`LibrarianId`),
PRIMARY KEY (`LMSId`,`LibrarianId`)
);

--
-- Table structure for table LMSBookAssociation
--

CREATE TABLE `LMSBookAssociation` (
`LMSId` int NOT NULL, 
`ISBN` int NOT NULL, 
KEY `FK_LMSBookAssociation_LMSId_idx` (`LMSId`),
KEY `FK_LMSBookAssociation_ISBN_idx` (`ISBN`),
PRIMARY KEY (`LMSId`,`ISBN`)
);

--
-- Table structure for table Book
--

CREATE TABLE `Book` (
`Publication` varchar(64),
`Author` varchar(64),
`Title` varchar(64),
`LibrarianId` int,
`ISBN` int NOT NULL, 
KEY `FK_Book_LibrarianId_idx` (`LibrarianId`),
PRIMARY KEY (`ISBN`)
);

--
-- Table structure for table LibrarianLibraryDbAssociation
--

CREATE TABLE `LibrarianLibraryDbAssociation` (
`LibrarianId` int NOT NULL, 
`LibraryDbId` int NOT NULL, 
KEY `FK_LibrarianLibraryDbAssociation_LibrarianId_idx` (`LibrarianId`),
KEY `FK_LibrarianLibraryDbAssociation_LibraryDbId_idx` (`LibraryDbId`),
PRIMARY KEY (`LibrarianId`,`LibraryDbId`)
);

--
-- Table structure for table Librarian
--

CREATE TABLE `Librarian` (
`SearchString` varchar(64),
`LibrarianName` varchar(64),
`LibrarianId` int NOT NULL, 
PRIMARY KEY (`LibrarianId`)
);

--
-- Table structure for table BookLibraryDbAssociation
--

CREATE TABLE `BookLibraryDbAssociation` (
`ISBN` int NOT NULL, 
`LibraryDbId` int NOT NULL, 
KEY `FK_BookLibraryDbAssociation_ISBN_idx` (`ISBN`),
KEY `FK_BookLibraryDbAssociation_LibraryDbId_idx` (`LibraryDbId`),
PRIMARY KEY (`ISBN`,`LibraryDbId`)
);

--
-- Table structure for table UserBookAssociation
--

CREATE TABLE `UserBookAssociation` (
`ISBN` int NOT NULL, 
`UserId` int NOT NULL, 
KEY `FK_UserBookAssociation_ISBN_idx` (`ISBN`),
KEY `FK_UserBookAssociation_UserId_idx` (`UserId`),
PRIMARY KEY (`ISBN`,`UserId`)
);

ALTER TABLE `Account`
  ADD CONSTRAINT `FK_Account_LMSId` FOREIGN KEY (`LMSId`) REFERENCES `LibraryManagementSystem` (`LMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Account_LibraryDbId` FOREIGN KEY (`LibraryDbId`) REFERENCES `LibraryDatabase` (`LibraryDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `User`
  ADD CONSTRAINT `FK_User_LMSId` FOREIGN KEY (`LMSId`) REFERENCES `LibraryManagementSystem` (`LMSId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Staff`
  ADD CONSTRAINT `FK_Staff_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserAccountAssociation`
  ADD CONSTRAINT `FK_UserAccountAssociation_AccountId` FOREIGN KEY (`AccountId`) REFERENCES `Account` (`AccountId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserAccountAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `LMSLibrarianAssociation`
  ADD CONSTRAINT `FK_LMSLibrarianAssociation_LMSId` FOREIGN KEY (`LMSId`) REFERENCES `LibraryManagementSystem` (`LMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LMSLibrarianAssociation_LibrarianId` FOREIGN KEY (`LibrarianId`) REFERENCES `Librarian` (`LibrarianId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `LMSBookAssociation`
  ADD CONSTRAINT `FK_LMSBookAssociation_LMSId` FOREIGN KEY (`LMSId`) REFERENCES `LibraryManagementSystem` (`LMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LMSBookAssociation_ISBN` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Book`
  ADD CONSTRAINT `FK_Book_LibrarianId` FOREIGN KEY (`LibrarianId`) REFERENCES `Librarian` (`LibrarianId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `LibrarianLibraryDbAssociation`
  ADD CONSTRAINT `FK_LibrarianLibraryDbAssociation_LibrarianId` FOREIGN KEY (`LibrarianId`) REFERENCES `Librarian` (`LibrarianId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_LibrarianLibraryDbAssociation_LibraryDbId` FOREIGN KEY (`LibraryDbId`) REFERENCES `LibraryDatabase` (`LibraryDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `BookLibraryDbAssociation`
  ADD CONSTRAINT `FK_BookLibraryDbAssociation_ISBN` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_BookLibraryDbAssociation_LibraryDbId` FOREIGN KEY (`LibraryDbId`) REFERENCES `LibraryDatabase` (`LibraryDbId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `UserBookAssociation`
  ADD CONSTRAINT `FK_UserBookAssociation_ISBN` FOREIGN KEY (`ISBN`) REFERENCES `Book` (`ISBN`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_UserBookAssociation_UserId` FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE CASCADE;

