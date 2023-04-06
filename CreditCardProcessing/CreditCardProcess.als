module CreditCardProcess
open Declaration

one sig Bankreq extends Class{}{
attrSet = InstructionCode+Info
id=InstructionCode
no parent
isAbstract = No
}

one sig InstructionCode extends Integer{}
one sig Info extends string{}

one sig CreditCardSys extends Class{}{
attrSet = SysId
one parent
parent in CreditCard
id = CreditCardId
isAbstract = No
}

one sig SysId extends Integer{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+CustomerAddress+CustomerPhoneNo+TaxpayerId
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends string{}
one sig CustomerAddress extends string{}
one sig CustomerPhoneNo extends Integer{}
one sig TaxpayerId extends Integer{}

one sig CardMaker extends Class{}{
attrSet = EquipmentId+AcquireDate
id=EquipmentId
no parent
isAbstract = No
}

one sig EquipmentId extends Integer{}
one sig AcquireDate extends string{}

one sig CreditCard extends Class{}{
attrSet = CreditCardId+CustomerId
id=CreditCardId
no parent
isAbstract = No
}

one sig CreditCardId extends Integer{}

one sig ProcessStaff extends Class{}{
attrSet = StaffId+StaffName+ClientList
id=StaffId
no parent
isAbstract = No
}

one sig StaffId extends Integer{}
one sig StaffName extends string{}
one sig ClientList extends string{}

one sig CreditCardInfo extends Class{}{
attrSet = CustomerCredentials
one parent
parent in CreditCard
id=CreditCardId
isAbstract = No
}

one sig CustomerCredentials extends Integer{}

one sig ProcessStaffCardMakerAssociation extends Association{}{
src = ProcessStaff
dst= CardMaker
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig ProcessStaffCustomerAssociation extends Association{}{
src = ProcessStaff
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerCardMakerAssociation extends Association{}{
src = Customer
dst= CardMaker
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CustomerCreditCardAssociation extends Association{}{
src = Customer
dst= CreditCard
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerBankreqAssociation extends Association{}{
src = Customer
dst= Bankreq
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
