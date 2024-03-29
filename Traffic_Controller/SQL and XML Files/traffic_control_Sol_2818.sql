-- CREATE DATABASE FOR /home/centos/orm_synthesizer/models/traffic_control/ImplSolution/traffic_control_Sol_2818.sql

USE traffic_control_Sol_2818;
--
-- Table structure for table Traffic_ControllerInsurance_CompanyAssociation
--

CREATE TABLE `Traffic_ControllerInsurance_CompanyAssociation` (
`Policy_No` int NOT NULL, 
`EmployeeId` int NOT NULL, 
KEY `FK_Traffic_ControllerInsurance_CompanyAssociation_Policy_No_idx` (`Policy_No`),
KEY `FK_Traffic_ControllerInsurance_CompanyAssociation_EmployeeId_idx` (`EmployeeId`),
PRIMARY KEY (`Policy_No`,`EmployeeId`)
);

--
-- Table structure for table Report
--

CREATE TABLE `Report` (
`TARS_NO` int,
`FineAmount` int,
`Location` int,
`caseid` int,
`Reporting_Officer` int,
`Incident_No` int,
`ReportId` int NOT NULL, 
KEY `FK_Report_TARS_NO_idx` (`TARS_NO`),
PRIMARY KEY (`ReportId`)
);

--
-- Table structure for table Driver
--

CREATE TABLE `Driver` (
`LicDuration` varchar(64),
`Insurance_company` varchar(64),
`DriverName` varchar(64),
`DriverLNo` int NOT NULL, 
PRIMARY KEY (`DriverLNo`)
);

--
-- Table structure for table TARS
--

CREATE TABLE `TARS` (
`TARS_NAME` varchar(64),
`Insurance_company` varchar(64),
`Duty_Officer` varchar(64),
`TARS_NO` int NOT NULL, 
PRIMARY KEY (`TARS_NO`)
);

--
-- Table structure for table Traffic_ControllerReportAssociation
--

CREATE TABLE `Traffic_ControllerReportAssociation` (
`ReportId` int NOT NULL, 
`EmployeeId` int NOT NULL, 
KEY `FK_Traffic_ControllerReportAssociation_ReportId_idx` (`ReportId`),
KEY `FK_Traffic_ControllerReportAssociation_EmployeeId_idx` (`EmployeeId`),
PRIMARY KEY (`ReportId`,`EmployeeId`)
);

--
-- Table structure for table VehicleDetails
--

CREATE TABLE `VehicleDetails` (
`VIN_NVMC` varchar(64),
`Duty_Officer` varchar(64),
`EmployeeId` int NOT NULL, 
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table Traffic_Controller
--

CREATE TABLE `Traffic_Controller` (
`TARS_NO` int,
`EmployeeId` int NOT NULL, 
KEY `FK_Traffic_Controller_TARS_NO_idx` (`TARS_NO`),
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table GIS
--

CREATE TABLE `GIS` (
`SATLocation` varchar(64),
`GISRoute` int NOT NULL, 
PRIMARY KEY (`GISRoute`)
);

--
-- Table structure for table ReportGISAssociation
--

CREATE TABLE `ReportGISAssociation` (
`ReportId` int NOT NULL, 
`GISRoute` int NOT NULL, 
KEY `FK_ReportGISAssociation_ReportId_idx` (`ReportId`),
KEY `FK_ReportGISAssociation_GISRoute_idx` (`GISRoute`),
PRIMARY KEY (`ReportId`,`GISRoute`)
);

--
-- Table structure for table DriverGISAssociation
--

CREATE TABLE `DriverGISAssociation` (
`DriverLNo` int NOT NULL, 
`GISRoute` int NOT NULL, 
KEY `FK_DriverGISAssociation_DriverLNo_idx` (`DriverLNo`),
KEY `FK_DriverGISAssociation_GISRoute_idx` (`GISRoute`),
PRIMARY KEY (`DriverLNo`,`GISRoute`)
);

--
-- Table structure for table Insurance_Company
--

CREATE TABLE `Insurance_Company` (
`Policy_Date` varchar(64),
`IC_Address` varchar(64),
`IC_Name` varchar(64),
`TARS_NO` int,
`DriverLNo` int,
`Policy_No` int NOT NULL, 
`GISRoute` int,
KEY `FK_Insurance_Company_TARS_NO_idx` (`TARS_NO`),
KEY `FK_Insurance_Company_DriverLNo_idx` (`DriverLNo`),
KEY `FK_Insurance_Company_GISRoute_idx` (`GISRoute`),
PRIMARY KEY (`Policy_No`)
);

--
-- Table structure for table Insurance
--

CREATE TABLE `Insurance` (
`Insurancedetails` varchar(64),
`Duty_Officer` varchar(64),
`EmployeeId` int NOT NULL, 
PRIMARY KEY (`EmployeeId`)
);

--
-- Table structure for table TARSDriverAssociation
--

CREATE TABLE `TARSDriverAssociation` (
`TARS_NO` int NOT NULL, 
`DriverLNo` int NOT NULL, 
KEY `FK_TARSDriverAssociation_TARS_NO_idx` (`TARS_NO`),
KEY `FK_TARSDriverAssociation_DriverLNo_idx` (`DriverLNo`),
PRIMARY KEY (`TARS_NO`,`DriverLNo`)
);

ALTER TABLE `Traffic_ControllerInsurance_CompanyAssociation`
  ADD CONSTRAINT `FK_Traffic_ControllerInsurance_CompanyAssociation_Policy_No` FOREIGN KEY (`Policy_No`) REFERENCES `Insurance_Company` (`Policy_No`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Traffic_ControllerInsurance_CompanyAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Traffic_Controller` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Report`
  ADD CONSTRAINT `FK_Report_TARS_NO` FOREIGN KEY (`TARS_NO`) REFERENCES `TARS` (`TARS_NO`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Traffic_ControllerReportAssociation`
  ADD CONSTRAINT `FK_Traffic_ControllerReportAssociation_ReportId` FOREIGN KEY (`ReportId`) REFERENCES `Report` (`ReportId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Traffic_ControllerReportAssociation_EmployeeId` FOREIGN KEY (`EmployeeId`) REFERENCES `Traffic_Controller` (`EmployeeId`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Traffic_Controller`
  ADD CONSTRAINT `FK_Traffic_Controller_TARS_NO` FOREIGN KEY (`TARS_NO`) REFERENCES `TARS` (`TARS_NO`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `ReportGISAssociation`
  ADD CONSTRAINT `FK_ReportGISAssociation_ReportId` FOREIGN KEY (`ReportId`) REFERENCES `Report` (`ReportId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_ReportGISAssociation_GISRoute` FOREIGN KEY (`GISRoute`) REFERENCES `GIS` (`GISRoute`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `DriverGISAssociation`
  ADD CONSTRAINT `FK_DriverGISAssociation_DriverLNo` FOREIGN KEY (`DriverLNo`) REFERENCES `Driver` (`DriverLNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_DriverGISAssociation_GISRoute` FOREIGN KEY (`GISRoute`) REFERENCES `GIS` (`GISRoute`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `Insurance_Company`
  ADD CONSTRAINT `FK_Insurance_Company_TARS_NO` FOREIGN KEY (`TARS_NO`) REFERENCES `TARS` (`TARS_NO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Insurance_Company_DriverLNo` FOREIGN KEY (`DriverLNo`) REFERENCES `Driver` (`DriverLNo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_Insurance_Company_GISRoute` FOREIGN KEY (`GISRoute`) REFERENCES `GIS` (`GISRoute`) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE `TARSDriverAssociation`
  ADD CONSTRAINT `FK_TARSDriverAssociation_TARS_NO` FOREIGN KEY (`TARS_NO`) REFERENCES `TARS` (`TARS_NO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `FK_TARSDriverAssociation_DriverLNo` FOREIGN KEY (`DriverLNo`) REFERENCES `Driver` (`DriverLNo`) ON DELETE CASCADE ON UPDATE CASCADE;

