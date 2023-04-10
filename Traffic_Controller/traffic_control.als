module traffic_control
open Declaration

one sig GIS extends Class{}{
attrSet = GISRoute+SATLocation
id=GISRoute
no parent
isAbstract = No
}

one sig GISRoute extends Integer{}
one sig SATLocation extends string{}

one sig Traffic_Controller extends Class{}{
attrSet = EmployeeId+Duty_Officer
id=EmployeeId
no parent
isAbstract = No
}

one sig EmployeeId extends Integer{}
one sig Duty_Officer extends string{}

one sig Report extends Class{}{
attrSet = ReportId+Incident_No+Reporting_Officer+caseid+Location+FineAmount
id=ReportId
no parent
isAbstract = No
}

one sig ReportId extends Integer{}
one sig Incident_No extends Integer{}
one sig Reporting_Officer extends Integer{}
one sig caseid extends Integer{}
one sig Location extends Integer{}
one sig FineAmount extends Integer{}

one sig Insurance_Company extends Class{}{
attrSet = IC_Name+IC_Address+Policy_No+Policy_Date
id=Policy_No
no parent
isAbstract = No
}

one sig IC_Name extends string{}
one sig IC_Address extends string{}
one sig Policy_No extends Integer{}
one sig Policy_Date extends string{}

one sig Insurance extends Class{}{
attrSet = Insurancedetails
one parent
parent in Traffic_Controller
id = EmployeeId
isAbstract = No
}

one sig Insurancedetails extends string{}

one sig Driver extends Class{}{
attrSet = DriverName+DriverLNo+Insurance_company+LicDuration
id=DriverLNo
no parent
isAbstract = No
}

one sig DriverName extends string{}
one sig DriverLNo extends Integer{}
one sig Insurance_company extends string{}
one sig LicDuration extends string{}

one sig VehicleDetails extends Class{}{
attrSet = VIN_NVMC
one parent
parent in Traffic_Controller
id = EmployeeId
isAbstract = No
}

one sig VIN_NVMC extends string{}

one sig TARS extends Class{}{
attrSet = TARS_NO+TARS_NAME+Duty_Officer+Insurance_company
id=TARS_NO
no parent
isAbstract = No
}

one sig TARS_NO extends Integer{}
one sig TARS_NAME extends string{}

one sig Traffic_ControllerTARSAssociation extends Association{}{
src = TARS
dst= Traffic_Controller
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Traffic_ControllerInsurance_CompanyAssociation extends Association{}{
src = Traffic_Controller
dst= Insurance_Company
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig TARSReportAssociation extends Association{}{
src = TARS
dst= Report
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TARSInsurance_CompanyAssociation extends Association{}{
src = TARS
dst= Insurance_Company
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TARSDriverAssociation extends Association{}{
src = TARS
dst= Driver
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig DriverGISAssociation extends Association{}{
src = Driver
dst= GIS
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig DriverInsurance_CompanyAssociation extends Association{}{
src = Driver
dst= Insurance_Company
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ReportGISAssociation extends Association{}{
src = GIS
dst= Report
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Insurance_CompanyGISAssociation extends Association{}{
src = GIS
dst= Insurance_Company
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Traffic_ControllerReportAssociation extends Association{}{
src = Traffic_Controller
dst= Report
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 21
