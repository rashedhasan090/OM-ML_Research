-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/Camping/ImplSolution/Camping_Sol_28.sql

USE Camping_Sol_28;
--
-- Table structure for table CampingTripScoutAssociation
--

CREATE TABLE `CampingTripScoutAssociation` (
`TripId` int NOT NULL,
`ScoutId` int NOT NULL,
KEY `FK_CampingTripScoutAssociation_TripId_idx` (`TripId`),
KEY `FK_CampingTripScoutAssociation_ScoutId_idx` (`ScoutId`),
PRIMARY KEY (`TripId`,`ScoutId`)
);

--
-- Table structure for table BadgeSpecification
--

CREATE TABLE `BadgeSpecification` (
`BadgeName` varchar(64),
`BadgeSpecificationId` int NOT NULL,
PRIMARY KEY (`BadgeSpecificationId`)
);

--
-- Table structure for table WealthyScout
--

CREATE TABLE `WealthyScout` (
`Name` varchar(64),
`DonationDate` int,
`DonationAmount` int,
`Joined` int,
`DOB` int,
`ScoutId` int NOT NULL,
PRIMARY KEY (`ScoutId`)
);

--
-- Table structure for table CampSite
--

CREATE TABLE `CampSite` (
`Location` varchar(64),
`SiteID` int NOT NULL,
PRIMARY KEY (`SiteID`)
);

--
-- Table structure for table ScoutBadgeAwardedAssociation
--

CREATE TABLE `ScoutBadgeAwardedAssociation` (
`ScoutId` int NOT NULL,
`AwardId` int NOT NULL,
KEY `FK_ScoutBadgeAwardedAssociation_ScoutId_idx` (`ScoutId`),
KEY `FK_ScoutBadgeAwardedAssociation_AwardId_idx` (`AwardId`),
PRIMARY KEY (`ScoutId`,`AwardId`)
);

--
-- Table structure for table CampingTrip
--

CREATE TABLE `CampingTrip` (
`EndDate` int,
`StartDate` int,
`TripId` int NOT NULL,
PRIMARY KEY (`TripId`)
);

--
-- Table structure for table BadgeAwarded
--

CREATE TABLE `BadgeAwarded` (
`BadgeSpecificationId` int,
`Date` int,
`AwardId` int NOT NULL,
KEY `FK_BadgeAwarded_BadgeSpecificationId_idx` (`BadgeSpecificationId`),
PRIMARY KEY (`AwardId`)
);

--
-- Table structure for table CampingTripSiteAssociation
--

CREATE TABLE `CampingTripSiteAssociation` (
`TripId` int NOT NULL,
`SiteID` int NOT NULL,
KEY `FK_CampingTripSiteAssociation_TripId_idx` (`TripId`),
KEY `FK_CampingTripSiteAssociation_SiteID_idx` (`SiteID`),
PRIMARY KEY (`TripId`,`SiteID`)
);

--
-- Table structure for table Scout
--

CREATE TABLE `Scout` (
`Name` varchar(64),
`Joined` int,
`DOB` int,
`ScoutId` int NOT NULL,
PRIMARY KEY (`ScoutId`)
);

ALTER TABLE `CampingTripScoutAssociation`
  ADD CONSTRAINT `FK_CampingTripScoutAssociation_TripId` FOREIGN KEY (`TripId`) REFERENCES `CampingTrip` (`TripId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CampingTripScoutAssociation_ScoutId` FOREIGN KEY (`ScoutId`) REFERENCES `Scout` (`ScoutId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ScoutBadgeAwardedAssociation`
  ADD CONSTRAINT `FK_ScoutBadgeAwardedAssociation_ScoutId` FOREIGN KEY (`ScoutId`) REFERENCES `Scout` (`ScoutId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ScoutBadgeAwardedAssociation_AwardId` FOREIGN KEY (`AwardId`) REFERENCES `BadgeAwarded` (`AwardId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `BadgeAwarded`
  ADD CONSTRAINT `FK_BadgeAwarded_BadgeSpecificationId` FOREIGN KEY (`BadgeSpecificationId`) REFERENCES `BadgeSpecification` (`BadgeSpecificationId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `CampingTripSiteAssociation`
  ADD CONSTRAINT `FK_CampingTripSiteAssociation_TripId` FOREIGN KEY (`TripId`) REFERENCES `CampingTrip` (`TripId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_CampingTripSiteAssociation_SiteID` FOREIGN KEY (`SiteID`) REFERENCES `CampSite` (`SiteID`) ON DELETE CASCADE ON UPDATE CASCADE;
