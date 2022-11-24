-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/decider/ImplSolution/decider_Sol_36.sql

USE decider_Sol_36;
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
`variableID` int NOT NULL,
PRIMARY KEY (`variableID`)
);

--
-- Table structure for table DSNNamespaceAssociation
--

CREATE TABLE `DSNNamespaceAssociation` (
`decisionSpaceID` int NOT NULL,
`namespaceID` int NOT NULL,
KEY `FK_DSNNamespaceAssociation_decisionSpaceID_idx` (`decisionSpaceID`),
KEY `FK_DSNNamespaceAssociation_namespaceID_idx` (`namespaceID`),
PRIMARY KEY (`decisionSpaceID`,`namespaceID`)
);

--
-- Table structure for table NameSpace
--

CREATE TABLE `NameSpace` (
`namespaceName` varchar(64),
`namespaceID` int NOT NULL,
PRIMARY KEY (`namespaceID`)
);

--
-- Table structure for table VarAssociation
--

CREATE TABLE `VarAssociation` (
`relationshipID` int NOT NULL,
`variableID` int NOT NULL,
KEY `FK_VarAssociation_relationshipID_idx` (`relationshipID`),
KEY `FK_VarAssociation_variableID_idx` (`variableID`),
PRIMARY KEY (`relationshipID`,`variableID`)
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
`DType` varchar(64),
`password` varchar(64),
`username` varchar(64),
`department` int,
`period` int,
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
PRIMARY KEY (`relationshipID`)
);

--
-- Table structure for table descisionSpaceVariablesAssociation
--

CREATE TABLE `descisionSpaceVariablesAssociation` (
`decisionSpaceID` int NOT NULL,
`variableID` int NOT NULL,
KEY `FK_descisionSpaceVariablesAssociation_decisionSpaceID_idx` (`decisionSpaceID`),
KEY `FK_descisionSpaceVariablesAssociation_variableID_idx` (`variableID`),
PRIMARY KEY (`decisionSpaceID`,`variableID`)
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

ALTER TABLE `DSNNamespaceAssociation`
  ADD CONSTRAINT `FK_DSNNamespaceAssociation_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DSNNamespaceAssociation_namespaceID` FOREIGN KEY (`namespaceID`) REFERENCES `NameSpace` (`namespaceID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `VarAssociation`
  ADD CONSTRAINT `FK_VarAssociation_relationshipID` FOREIGN KEY (`relationshipID`) REFERENCES `Relationship` (`relationshipID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_VarAssociation_variableID` FOREIGN KEY (`variableID`) REFERENCES `Variable` (`variableID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `descisionSpaceVariablesAssociation`
  ADD CONSTRAINT `FK_descisionSpaceVariablesAssociation_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_descisionSpaceVariablesAssociation_variableID` FOREIGN KEY (`variableID`) REFERENCES `Variable` (`variableID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `descisionSpaceParticipantsAssociation`
  ADD CONSTRAINT `FK_descisionSpaceParticipantsAssociation_participantID` FOREIGN KEY (`participantID`) REFERENCES `Participant` (`participantID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_descisionSpaceParticipantsAssociation_decisionSpaceID` FOREIGN KEY (`decisionSpaceID`) REFERENCES `DecisionSpace` (`decisionSpaceID`) ON DELETE CASCADE ON UPDATE CASCADE;
