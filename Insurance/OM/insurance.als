module Insurance
open Declaration

one sig InsuranceProfile extends Class{}{
attrSet = InsuranceId+ListOFCar_Insurances
id=InsuranceId
no parent
isAbstract = No
}

one sig InsuranceId extends Integer{}
one sig ListOFCar_Insurances extends string{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerDetails
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerDetails extends string{}

one sig Policy extends Class{}{
attrSet = PolicyId+PolicyName+Conditions+Coverage+Claims+CustomerId
id=PolicyId
no parent
isAbstract = No
}

one sig PolicyId extends Integer{}
one sig PolicyName extends Integer{}
one sig Conditions extends Integer{}
one sig Coverage extends Integer{}
one sig Claims extends Integer{}
one sig CustomerId extends Integer{}

one sig Car_Insurance extends Class{}{
attrSet = PolicyNo+terms+VIN+Coverage
id=VIN
no parent
isAbstract = No
}

one sig PolicyNo extends string{}
one sig terms extends string{}
one sig VIN extends Integer{}
one sig Coverage extends string{}

one sig Person extends Class{}{
attrSet = FileNo
one parent
parent in Customer
id = CustomerId
isAbstract = No
}

one sig FileNo extends string{}

one sig Damage_File extends Class{}{
attrSet = Status+Assessment+History+Claim
id=Assessment
no parent
isAbstract = No
}

one sig Status extends string{}
one sig Assessment extends Integer{}
one sig History extends string{}
one sig Claim extends string{}

one sig Company extends Class{}{
attrSet = Claims+Policies
one parent
parent in Customer
id = CustomerId
isAbstract = No
}

one sig Claims extends string{}
one sig Policies extends string{}

one sig InsuranceEnumerationSystem extends Class{}{
attrSet = ReqId+status+CustomerDetails+History
id=ReqId
no parent
isAbstract = No
}

one sig ReqId extends Integer{}
one sig status extends string{}

one sig CustomerInsuranceEnumerationSystemAssociation extends Association{}{
src = InsuranceEnumerationSystem
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerCar_InsuranceAssociation extends Association{}{
src = Customer
dst= Car_Insurance
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig InsuranceEnumerationSystemPolicyAssociation extends Association{}{
src = InsuranceEnumerationSystem
dst= Policy
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig InsuranceEnumerationSystemCar_InsuranceAssociation extends Association{}{
src = InsuranceEnumerationSystem
dst= Car_Insurance
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig InsuranceEnumerationSystemDamage_FileAssociation extends Association{}{
src = InsuranceEnumerationSystem
dst= Damage_File
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig Damage_FileLibraryDbAssociation extends Association{}{
src = Damage_File
dst= InsuranceProfile
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig Damage_FileCar_InsuranceAssociation extends Association{}{
src = Damage_File
dst= Car_Insurance
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig PolicyLibraryDbAssociation extends Association{}{
src = InsuranceProfile
dst= Policy
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Car_InsuranceLibraryDbAssociation extends Association{}{
src = InsuranceProfile
dst= Car_Insurance
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerPolicyAssociation extends Association{}{
src = Customer
dst= Policy
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 32
