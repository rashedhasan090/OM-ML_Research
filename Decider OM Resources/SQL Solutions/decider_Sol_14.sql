-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/decider/ImplSolution/decider_Sol_14.sql

USE decider_Sol_14;
--
-- Table structure for table RoleBindingsAssociation
--

CREATE TABLE `RoleBindingsAssociation` (
`participantID` int NOT NULL,
`roleID` int NOT NULL,
KEY `FK_RoleBindingsAssociation_participantID_idx` (`participantID`),
KEY `FK_RoleBindingsAssociation_roleID_idx` (`roleID`),
PRIMARY KEY (`participantID`,`roleID`)
);

--
-- Table structure for table Variable
--

CREATE TABLE `Variable` (
`variableName` varchar(64),
`decisionSpaceID` int,
`variableID` int NOT NULL,
KEY `FK_Variable_decisionSpaceID_idx` (`decisionSpaceID`),
PRIMARY KEY (`variableID`)
);

--
-- Table structure for table User
--

CREATE TABLE `User` (
`password` varchar(64),
`username` varchar(64),
`participantID` int NOT NULL,
KEY `FK_User_participantID_idx` (`participantID`),
PRIMARY KEY (`participantID`)
);

--
-- Table structure for table NameSpace
--

CREATE TABLE `NameSpace` (
`namespaceName` varchar(64),
`decisionSpaceID` int,
`namespaceID` int NOT NULL,
KEY `FK_NameSpace_decisionSpaceID_idx` (`decisionSpaceID`),
PRIMARY KEY (`namespaceID`)
);

--
-- Table structure for table Developer
--

CREATE TABLE `Developer` (
`department` int,
`participantID` int NOT NULL,
PRIMARY KEY (`participantID`)
);

--
-- Table structure for table Viewer
--

CREATE TABLE `Viewer` (
`period` int,
`participantID` int NOT NULL,
PRIMARY KEY (`participantID`)
);

--
-- Table structure for table Role
--

CREATE TABLE `Role` (
`roleName` varchar(64),
`roleID` int NOT NULL,
PRIMARY KEY (`roleID`)
);

--
-- Table structure for table Participant
--

CREATE TABLE `Participant` (
`participantID` int NOT NULL,
PRIMARY KEY (`participantID`)
);

--
-- Table structure for table DecisionSpace
--

CREATE TABLE `DecisionSpace` (
`decisionSpaceName` varchar(64),
`decisionSpaceID` int NOT NULL,
PRIMARY KEY (`decisionSpaceID`)
);

--
-- Table structure for table Relationship
--

CREATE TABLE `Relationship` (
`relationshipName` varchar(64),
`relationshipID` int NOT NULL,
`variableID` int,
KEY `FK_Relationship_variableID_idx` (`variableID`),
PRIMARY KEY (`relationshipID`)
);

--
-- Table structure for table descisionSpaceParticipantsAssociation
--

CREATE TABLE `descisionSpaceParticipantsAssociation` (
`participantID` int NOT NULL,
`decisionSpaceID` int NOT NULL,
KEY `FK_descisionSpaceParticipantsAssociation_participantID_idx` (`participantID`),
KEY `FK_descisionSpaceParticipantsAssociation_decisionSpaceID_idx` (`decisionSpaceID`),
PRIMARY KEY (`participantID`,`decisionSpaceID`)
);

ALTER TABLE `RoleBindingsAssociation`
  ADD CONSTRAINT `FK_RoleBindingsAssociation_participantID` FOREIGN KEY (`participantID`) REFERENCES `Participant` (`participantID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_RoleBindingsAssociation_roleID` FOREIGN KEY (`roleID`) REFERENCES `Role` (`roleID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Variable`
  ADD CONSTRAINT `FK_Variable_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `User`
  ADD CONSTRAINT `FK_User_participantID` FOREIGN KEY (`participantID`) REFERENCES `Participant` (`participantID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `NameSpace`
  ADD CONSTRAINT `FK_NameSpace_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Relationship`
  ADD CONSTRAINT `FK_Relationship_variableID` FOREIGN KEY (`variableID`) REFERENCES `Variable` (`variableID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `descisionSpaceParticipantsAssociation`
  ADD CONSTRAINT `FK_descisionSpaceParticipantsAssociation_participantID` FOREIGN KEY (`participantID`) REFERENCES `Participant` (`participantID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_descisionSpaceParticipantsAssociation_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE;
