module HospitalManagement
open Declaration

one sig Operation extends Class{}{
attrSet = OperationId+OperationDate
id=OperationId
no parent
isAbstract = No
}

one sig OperationId extends Integer{}
one sig OperationDate extends string{}

one sig Staff extends Class{}{
attrSet = StaffId+StaffName
id=StaffId
no parent
isAbstract = No
}

one sig StaffId extends Integer{}
one sig StaffName extends string{}

one sig Patient extends Class{}{
attrSet = PatientId+PatientName+PatientAge+PatientGender+PatientAddress+PatientMobileNo
id=PatientId
no parent
isAbstract = No
}

one sig PatientId extends Integer{}
one sig PatientName extends Integer{}
one sig PatientAge extends Integer{}
one sig PatientGender extends Integer{}
one sig PatientAddress extends Integer{}
one sig PatientMobileNo extends Integer{}

one sig Ward extends Class{}{
attrSet = WardId+WardName+WardNumber+status
id=WardNumber
no parent
isAbstract = No
}

one sig WardId extends string{}
one sig WardName extends string{}
one sig WardNumber extends Integer{}
one sig status extends string{}

one sig WardStaff extends Class{}{
attrSet = assignedWard
one parent
parent in Staff
id = StaffId
isAbstract = No
}

one sig assignedWard extends string{}

one sig Doctor extends Class{}{
attrSet = DoctorName+DoctorId+Qualification+Speciality
id=DoctorId
no parent
isAbstract = No
}

one sig DoctorName extends string{}
one sig DoctorId extends Integer{}
one sig Qualification extends string{}
one sig Speciality extends string{}

one sig Receptionist extends Class{}{
attrSet = ReceptionistInfo
one parent
parent in Staff
id = StaffId
isAbstract = No
}

one sig ReceptionistInfo extends string{}

one sig LabAssistant extends Class{}{
attrSet = LabAssistantInfo
one parent
parent in Staff
id = StaffId
isAbstract = No
}

one sig LabAssistantInfo extends string{}


one sig Pharmacist extends Class{}{
attrSet = PharmacistInfo
one parent
parent in Staff
id = StaffId
isAbstract = No
}

one sig PharmacistInfo extends string{}

one sig HospitalManagementSystem extends Class{}{
attrSet = HMSId+StaffType+StaffName+Qualification
id=HMSId
no parent
isAbstract = No
}

one sig HMSId extends Integer{}
one sig StaffType extends string{}

one sig StaffHMSAssociation extends Association{}{
src = HospitalManagementSystem
dst= Staff
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig StaffWardAssociation extends Association{}{
src = Staff
dst= Ward
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig HMSPatientAssociation extends Association{}{
src = HospitalManagementSystem
dst= Patient
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HMSWardAssociation extends Association{}{
src = HospitalManagementSystem
dst= Ward
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HMSDoctorAssociation extends Association{}{
src = HospitalManagementSystem
dst= Doctor
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig DoctorLibraryDbAssociation extends Association{}{
src = Doctor
dst= Operation
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig DoctorWardAssociation extends Association{}{
src = Doctor
dst= Ward
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig PatientLibraryDbAssociation extends Association{}{
src = Operation
dst= Patient
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig WardLibraryDbAssociation extends Association{}{
src = Operation
dst= Ward
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig StaffPatientAssociation extends Association{}{
src = Staff
dst= Patient
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 44
