module AirSystem
open Declaration

one sig Aircraft extends Class{}{
attrSet = AircraftId+AircraftType
id=AircraftId
no parent
isAbstract = No
}

one sig AircraftId extends Integer{}
one sig AircraftType extends string{}

one sig CabinCrew extends Class{}{
attrSet = CabinCrewId
one parent
parent in Person
id = PersonId
isAbstract = No
}

one sig CabinCrewId extends Integer{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+CustomerAddress+CustomerPhoneNo+CustomerTicketNo
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends string{}
one sig CustomerAddress extends string{}
one sig CustomerPhoneNo extends Integer{}
one sig CustomerTicketNo extends Integer{}

one sig Equipment extends Class{}{
attrSet = EquipmentId+AcquireDate
id=EquipmentId
no parent
isAbstract = No
}

one sig EquipmentId extends Integer{}
one sig AcquireDate extends string{}

one sig Person extends Class{}{
attrSet = PersonId+CustomerId
id=PersonId
no parent
isAbstract = No
}

one sig PersonId extends Integer{}

one sig Airlines extends Class{}{
attrSet = AirlinesId+AirlinesName+AirlinesLocation
id=AirlinesId
no parent
isAbstract = No
}

one sig AirlinesId extends Integer{}
one sig AirlinesName extends string{}
one sig AirlinesLocation extends string{}

one sig Employee extends Class{}{
attrSet = EmployeeId
one parent
parent in Person
id=PersonId
isAbstract = No
}

one sig EmployeeId extends Integer{}

one sig AirlinesEquipmentAssociation extends Association{}{
src = Airlines
dst= Equipment
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig AirlinesCustomerAssociation extends Association{}{
src = Airlines
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerEquipmentAssociation extends Association{}{
src = Customer
dst= Equipment
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CustomerPersonAssociation extends Association{}{
src = Customer
dst= Person
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerAircraftAssociation extends Association{}{
src = Customer
dst= Aircraft
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
