module DonorProcess
open Declaration

one sig BloodBankreq extends Class{}{
attrSet = InstructionCode+Info
id=InstructionCode
no parent
isAbstract = No
}

one sig InstructionCode extends Integer{}
one sig Info extends string{}

one sig Recepients extends Class{}{
attrSet = RecepientId
one parent
parent in Donor
id = DonorId
isAbstract = No
}

one sig RecepientId extends Integer{}

one sig BloodBank extends Class{}{
attrSet = SpecimenId+BloodGroup+Collections+PlasmaId+DonorId
id=SpecimenId
no parent
isAbstract = No
}

one sig SpecimenId extends Integer{}
one sig BloodGroup extends string{}
one sig Collections extends string{}
one sig PlasmaId extends Integer{}
one sig DonorId extends Integer{}

one sig BloodRequest extends Class{}{
attrSet = RequestId+RequestDate
id=RequestId
no parent
isAbstract = No
}

one sig RequestId extends Integer{}
one sig RequestDate extends string{}

one sig Donor extends Class{}{
attrSet = DonorId+SpecimenId
id=DonorId
no parent
isAbstract = No
}

one sig DonorId extends Integer{}

one sig ProcessStaff extends Class{}{
attrSet = StaffId+StaffName+ClientList
id=StaffId
no parent
isAbstract = No
}

one sig StaffId extends Integer{}
one sig StaffName extends string{}
one sig ClientList extends string{}

one sig DonationCard extends Class{}{
attrSet = DonationInfo
one parent
parent in Donor
id=DonorId
isAbstract = No
}

one sig DonationInfo extends Integer{}

one sig ProcessStaffBloodRequestAssociation extends Association{}{
src = ProcessStaff
dst= BloodRequest
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig ProcessStaffBloodBankAssociation extends Association{}{
src = ProcessStaff
dst= BloodBank
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig BloodBankBloodRequestAssociation extends Association{}{
src = BloodBank
dst= BloodRequest
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig BloodBankDonorAssociation extends Association{}{
src = BloodBank
dst= Donor
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig BloodBankBloodBankreqAssociation extends Association{}{
src = BloodBank
dst= BloodBankreq
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
