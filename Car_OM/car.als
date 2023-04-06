module Library
open Declaration

one sig CarModel extends Class{}{
attrSet = VINNo+state
id=VINNo
no parent
isAbstract = No
}

one sig VINNo extends Integer{}
one sig state extends string{}

one sig Car extends Class{}{
attrSet = registrationNum+licenseNum
id=registrationNum
no parent
isAbstract = No
}

one sig registrationNum extends Integer{}
one sig licenseNum extends string{}

one sig Engine extends Class{}{
attrSet = EngineId+Manufacturer+capacity+HP+Buildyear+model
id=EngineId
no parent
isAbstract = No
}

one sig EngineId extends Integer{}
one sig Manufacturer extends Integer{}
one sig capacity extends Integer{}
one sig HP extends Integer{}
one sig Buildyear extends Integer{}
one sig model extends Integer{}

one sig CarBody extends Class{}{
attrSet = Type+color+num_of_doors+manufacturer
id=num_of_doors
no parent
isAbstract = No
}

one sig Type extends string{}
one sig color extends string{}
one sig num_of_doors extends Integer{}
one sig manufacturer extends string{}

one sig GearBox extends Class{}{
attrSet = currentGear
one parent
parent in Car
id = registrationNum
isAbstract = No
}

one sig currentGear extends string{}

one sig suspension extends Class{}{
attrSet = manufacturer+ComponentId+functionalities+springRate
id=ComponentId
no parent
isAbstract = No
}

one sig manufacturer extends string{}
one sig ComponentId extends Integer{}
one sig functionalities extends string{}
one sig springRate extends string{}

one sig GearBoxType extends Class{}{
attrSet = Name
one parent
parent in Car
id = registrationNum
isAbstract = No
}

one sig Name extends string{}

one sig CarCPU extends Class{}{
attrSet = CPUID+Manufacturer+licenseNum+functionalities
id=CPUID
no parent
isAbstract = No
}

one sig CPUID extends Integer{}
one sig Manufacturer extends string{}

one sig CarCarCPUAssociation extends Association{}{
src = CarCPU
dst= Car
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarCarBodyAssociation extends Association{}{
src = Car
dst= CarBody
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarCPUEngineAssociation extends Association{}{
src = CarCPU
dst= Engine
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarCPUCarBodyAssociation extends Association{}{
src = CarCPU
dst= CarBody
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarCPUCarAssociation extends Association{}{
src = CarCPU
dst= Car
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarCarModelAssociation extends Association{}{
src = Car
dst= CarModel
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig EngineCarCPUAssociation extends Association{}{
src = Engine
dst= CarCPU
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig EngineLibraryDbAssociation extends Association{}{
src = CarModel
dst= Engine
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CarEngineAssociation extends Association{}{
src = Car
dst= Engine
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 43
