-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/attendence_mgmt_extended/ImplSolution/attendence_mgmt_extended_Sol_12.sql

USE attendence_mgmt_extended_Sol_12;
--
-- Table structure for table AdminAttendenceManagementSystemAssociation
--

CREATE TABLE `AdminAttendenceManagementSystemAssociation` (
`sysid` int NOT NULL, 
`AdminID` int NOT NULL, 
KEY `FK_AdminAttendenceManagementSystemAssociation_sysid_idx` (`sysid`),
KEY `FK_AdminAttendenceManagementSystemAssociation_AdminID_idx` (`AdminID`),
PRIMARY KEY (`sysid`,`AdminID`)
);

--
-- Table structure for table AttendenceManagementSystem
--

CREATE TABLE `AttendenceManagementSystem` (
`systemconifg` varchar(64),
`studentcount` int,
`sysid` int NOT NULL, 
PRIMARY KEY (`sysid`)
);

--
-- Table structure for table AdminStudentAssociation
--

CREATE TABLE `AdminStudentAssociation` (
`StudentID` int NOT NULL, 
`AdminID` int NOT NULL, 
KEY `FK_AdminStudentAssociation_StudentID_idx` (`StudentID`),
KEY `FK_AdminStudentAssociation_AdminID_idx` (`AdminID`),
PRIMARY KEY (`StudentID`,`AdminID`)
);

--
-- Table structure for table Admin
--

CREATE TABLE `Admin` (
`DType` varchar(64),
`AdminName` varchar(64),
`TAcred` int,
`credentials` int,
`AdminID` int NOT NULL, 
PRIMARY KEY (`AdminID`)
);

--
-- Table structure for table Student
--

CREATE TABLE `Student` (
`StudentName` decimal(20,5),
`StudentID` int NOT NULL, 
PRIMARY KEY (`StudentID`)
);

--
-- Table structure for table StudentCourseAssociation
--

CREATE TABLE `StudentCourseAssociation` (
`CourseID` int NOT NULL, 
`StudentID` int NOT NULL, 
KEY `FK_StudentCourseAssociation_CourseID_idx` (`CourseID`),
KEY `FK_StudentCourseAssociation_StudentID_idx` (`StudentID`),
PRIMARY KEY (`CourseID`,`StudentID`)
);

--
-- Table structure for table Course
--

CREATE TABLE `Course` (
`CourseName` varchar(64),
`CourseID` int NOT NULL, 
`AdminID` int,
KEY `FK_Course_AdminID_idx` (`AdminID`),
PRIMARY KEY (`CourseID`)
);

ALTER TABLE `AdminAttendenceManagementSystemAssociation`
  ADD CONSTRAINT `FK_AdminAttendenceManagementSystemAssociation_sysid` FOREIGN KEY (`sysid`) REFERENCES `AttendenceManagementSystem` (`sysid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_AdminAttendenceManagementSystemAssociation_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `AdminStudentAssociation`
  ADD CONSTRAINT `FK_AdminStudentAssociation_StudentID` FOREIGN KEY (`StudentID`) REFERENCES `Student` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_AdminStudentAssociation_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `StudentCourseAssociation`
  ADD CONSTRAINT `FK_StudentCourseAssociation_CourseID` FOREIGN KEY (`CourseID`) REFERENCES `Course` (`CourseID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_StudentCourseAssociation_StudentID` FOREIGN KEY (`StudentID`) REFERENCES `Student` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Course`
  ADD CONSTRAINT `FK_Course_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;
