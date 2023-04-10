-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/hospital_mgmt_extended/ImplSolution/hospital_mgmt_extended_Sol_11244.sql

USE hospital_mgmt_extended_Sol_11244;
--
-- Table structure for table Receptionist
--

CREATE TABLE `Receptionist` (
`ReceptionistInfo` varchar(64),
`StaffId` int NOT NULL, 
KEY `FK_Receptionist_StaffId_idx` (`StaffId`),
PRIMARY KEY (`StaffId`)
);

--
-- Table structure for table WardStaff
--

CREATE TABLE `WardStaff` (
`assignedWard` varchar(64),
`StaffId` int NOT NULL, 
KEY `FK_WardStaff_StaffId_idx` (`StaffId`),
PRIMARY KEY (`StaffId`)
);

--
-- Table structure for table HMSWardAssociation
--

CREATE TABLE `HMSWardAssociation` (
`HMSId` int NOT NULL, 
`WardNumber` int NOT NULL, 
KEY `FK_HMSWardAssociation_HMSId_idx` (`HMSId`),
KEY `FK_HMSWardAssociation_WardNumber_idx` (`WardNumber`),
PRIMARY KEY (`HMSId`,`WardNumber`)
);

--
-- Table structure for table Staff
--

CREATE TABLE `Staff` (
`StaffName` varchar(64),
`HMSId` int,
`StaffId` int NOT NULL, 
KEY `FK_Staff_HMSId_idx` (`HMSId`),
PRIMARY KEY (`StaffId`)
);

--
-- Table structure for table Patient
--

CREATE TABLE `Patient` (
`PatientMobileNo` int,
`PatientAddress` int,
`PatientGender` int,
`PatientAge` int,
`PatientName` int,
`PatientId` int NOT NULL, 
`OperationId` int,
KEY `FK_Patient_OperationId_idx` (`OperationId`),
PRIMARY KEY (`PatientId`)
);

--
-- Table structure for table Operation
--

CREATE TABLE `Operation` (
`OperationDate` varchar(64),
`OperationId` int NOT NULL, 
PRIMARY KEY (`OperationId`)
);

--
-- Table structure for table Doctor
--

CREATE TABLE `Doctor` (
`Speciality` varchar(64),
`DoctorName` varchar(64),
`DoctorId` int NOT NULL, 
PRIMARY KEY (`DoctorId`)
);

--
-- Table structure for table StaffWardAssociation
--

CREATE TABLE `StaffWardAssociation` (
`WardNumber` int NOT NULL, 
`StaffId` int NOT NULL, 
KEY `FK_StaffWardAssociation_WardNumber_idx` (`WardNumber`),
KEY `FK_StaffWardAssociation_StaffId_idx` (`StaffId`),
PRIMARY KEY (`WardNumber`,`StaffId`)
);

--
-- Table structure for table HMSDoctorAssociation
--

CREATE TABLE `HMSDoctorAssociation` (
`HMSId` int NOT NULL, 
`DoctorId` int NOT NULL, 
KEY `FK_HMSDoctorAssociation_HMSId_idx` (`HMSId`),
KEY `FK_HMSDoctorAssociation_DoctorId_idx` (`DoctorId`),
PRIMARY KEY (`HMSId`,`DoctorId`)
);

--
-- Table structure for table HMSPatientAssociation
--

CREATE TABLE `HMSPatientAssociation` (
`HMSId` int NOT NULL, 
`PatientId` int NOT NULL, 
KEY `FK_HMSPatientAssociation_HMSId_idx` (`HMSId`),
KEY `FK_HMSPatientAssociation_PatientId_idx` (`PatientId`),
PRIMARY KEY (`HMSId`,`PatientId`)
);

--
-- Table structure for table DoctorLibraryDbAssociation
--

CREATE TABLE `DoctorLibraryDbAssociation` (
`DoctorId` int NOT NULL, 
`OperationId` int NOT NULL, 
KEY `FK_DoctorLibraryDbAssociation_DoctorId_idx` (`DoctorId`),
KEY `FK_DoctorLibraryDbAssociation_OperationId_idx` (`OperationId`),
PRIMARY KEY (`DoctorId`,`OperationId`)
);

--
-- Table structure for table DoctorWardAssociation
--

CREATE TABLE `DoctorWardAssociation` (
`DoctorId` int NOT NULL, 
`WardNumber` int NOT NULL, 
KEY `FK_DoctorWardAssociation_DoctorId_idx` (`DoctorId`),
KEY `FK_DoctorWardAssociation_WardNumber_idx` (`WardNumber`),
PRIMARY KEY (`DoctorId`,`WardNumber`)
);

--
-- Table structure for table HospitalManagementSystem
--

CREATE TABLE `HospitalManagementSystem` (
`StaffType` varchar(64),
`Qualification` varchar(64),
`HMSId` int NOT NULL, 
PRIMARY KEY (`HMSId`)
);

--
-- Table structure for table Ward
--

CREATE TABLE `Ward` (
`status` varchar(64),
`WardName` varchar(64),
`WardId` varchar(64),
`WardNumber` int NOT NULL, 
`OperationId` int,
KEY `FK_Ward_OperationId_idx` (`OperationId`),
PRIMARY KEY (`WardNumber`)
);

--
-- Table structure for table StaffPatientAssociation
--

CREATE TABLE `StaffPatientAssociation` (
`PatientId` int NOT NULL, 
`StaffId` int NOT NULL, 
KEY `FK_StaffPatientAssociation_PatientId_idx` (`PatientId`),
KEY `FK_StaffPatientAssociation_StaffId_idx` (`StaffId`),
PRIMARY KEY (`PatientId`,`StaffId`)
);

--
-- Table structure for table Pharmacist
--

CREATE TABLE `Pharmacist` (
`PharmacistInfo` varchar(64),
`StaffId` int NOT NULL, 
KEY `FK_Pharmacist_StaffId_idx` (`StaffId`),
PRIMARY KEY (`StaffId`)
);

--
-- Table structure for table LabAssistant
--

CREATE TABLE `LabAssistant` (
`LabAssistantInfo` varchar(64),
`StaffName` varchar(64),
`StaffId` int NOT NULL, 
PRIMARY KEY (`StaffId`)
);

ALTER TABLE `Receptionist`
  ADD CONSTRAINT `FK_Receptionist_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `Staff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `WardStaff`
  ADD CONSTRAINT `FK_WardStaff_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `Staff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `HMSWardAssociation`
  ADD CONSTRAINT `FK_HMSWardAssociation_HMSId` FOREIGN KEY (`HMSId`) REFERENCES `HospitalManagementSystem` (`HMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_HMSWardAssociation_WardNumber` FOREIGN KEY (`WardNumber`) REFERENCES `Ward` (`WardNumber`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Staff`
  ADD CONSTRAINT `FK_Staff_HMSId` FOREIGN KEY (`HMSId`) REFERENCES `HospitalManagementSystem` (`HMSId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Patient`
  ADD CONSTRAINT `FK_Patient_OperationId` FOREIGN KEY (`OperationId`) REFERENCES `Operation` (`OperationId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `StaffWardAssociation`
  ADD CONSTRAINT `FK_StaffWardAssociation_WardNumber` FOREIGN KEY (`WardNumber`) REFERENCES `Ward` (`WardNumber`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_StaffWardAssociation_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `Staff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `HMSDoctorAssociation`
  ADD CONSTRAINT `FK_HMSDoctorAssociation_HMSId` FOREIGN KEY (`HMSId`) REFERENCES `HospitalManagementSystem` (`HMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_HMSDoctorAssociation_DoctorId` FOREIGN KEY (`DoctorId`) REFERENCES `Doctor` (`DoctorId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `HMSPatientAssociation`
  ADD CONSTRAINT `FK_HMSPatientAssociation_HMSId` FOREIGN KEY (`HMSId`) REFERENCES `HospitalManagementSystem` (`HMSId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_HMSPatientAssociation_PatientId` FOREIGN KEY (`PatientId`) REFERENCES `Patient` (`PatientId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `DoctorLibraryDbAssociation`
  ADD CONSTRAINT `FK_DoctorLibraryDbAssociation_DoctorId` FOREIGN KEY (`DoctorId`) REFERENCES `Doctor` (`DoctorId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DoctorLibraryDbAssociation_OperationId` FOREIGN KEY (`OperationId`) REFERENCES `Operation` (`OperationId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `DoctorWardAssociation`
  ADD CONSTRAINT `FK_DoctorWardAssociation_DoctorId` FOREIGN KEY (`DoctorId`) REFERENCES `Doctor` (`DoctorId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DoctorWardAssociation_WardNumber` FOREIGN KEY (`WardNumber`) REFERENCES `Ward` (`WardNumber`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Ward`
  ADD CONSTRAINT `FK_Ward_OperationId` FOREIGN KEY (`OperationId`) REFERENCES `Operation` (`OperationId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `StaffPatientAssociation`
  ADD CONSTRAINT `FK_StaffPatientAssociation_PatientId` FOREIGN KEY (`PatientId`) REFERENCES `Patient` (`PatientId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_StaffPatientAssociation_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `Staff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Pharmacist`
  ADD CONSTRAINT `FK_Pharmacist_StaffId` FOREIGN KEY (`StaffId`) REFERENCES `Staff` (`StaffId`) ON DELETE CASCADE ON UPDATE CASCADE;

