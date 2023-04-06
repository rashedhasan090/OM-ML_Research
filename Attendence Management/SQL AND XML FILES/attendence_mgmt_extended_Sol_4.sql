-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/attendence_mgmt_extended/ImplSolution/attendence_mgmt_extended_Sol_4.sql

USE attendence_mgmt_extended_Sol_4;
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
`AdminID` int,
KEY `FK_Student_AdminID_idx` (`AdminID`),
PRIMARY KEY (`StudentID`)
);

--
-- Table structure for table Course
--

CREATE TABLE `Course` (
`CourseName` varchar(64),
`CourseID` int NOT NULL, 
`StudentID` int,
KEY `FK_Course_StudentID_idx` (`StudentID`),
PRIMARY KEY (`CourseID`)
);

--
-- Table structure for table TeacherCourseAssociation
--

CREATE TABLE `TeacherCourseAssociation` (
`CourseID` int NOT NULL, 
`AdminID` int NOT NULL, 
KEY `FK_TeacherCourseAssociation_CourseID_idx` (`CourseID`),
KEY `FK_TeacherCourseAssociation_AdminID_idx` (`AdminID`),
PRIMARY KEY (`CourseID`,`AdminID`)
);

ALTER TABLE `AdminAttendenceManagementSystemAssociation`
  ADD CONSTRAINT `FK_AdminAttendenceManagementSystemAssociation_sysid` FOREIGN KEY (`sysid`) REFERENCES `AttendenceManagementSystem` (`sysid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_AdminAttendenceManagementSystemAssociation_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Student`
  ADD CONSTRAINT `FK_Student_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Course`
  ADD CONSTRAINT `FK_Course_StudentID` FOREIGN KEY (`StudentID`) REFERENCES `Student` (`StudentID`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `TeacherCourseAssociation`
  ADD CONSTRAINT `FK_TeacherCourseAssociation_CourseID` FOREIGN KEY (`CourseID`) REFERENCES `Course` (`CourseID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_TeacherCourseAssociation_AdminID` FOREIGN KEY (`AdminID`) REFERENCES `Admin` (`AdminID`) ON DELETE CASCADE ON UPDATE CASCADE;

