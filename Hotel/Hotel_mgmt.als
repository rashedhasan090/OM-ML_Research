module Hotel_mgmt
open Declaration

one sig Menu extends Class{}{
attrSet = MenuId+ListOFCustomerTables
id=MenuId
no parent
isAbstract = No
}

one sig MenuId extends Integer{}
one sig ListOFCustomerTables extends string{}

one sig HotelManagement extends Class{}{
attrSet = HotelId+NumofEmployees
id=HotelId
no parent
isAbstract = No
}

one sig HotelId extends Integer{}
one sig NumofEmployees extends string{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+BillId+OrderId+PaymentId+ServiceId
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends Integer{}
one sig BillId extends Integer{}
one sig OrderId extends Integer{}
one sig PaymentId extends Integer{}
one sig ServiceId extends Integer{}

one sig CustomerTable extends Class{}{
attrSet = TableNumber+OccupiedStatus+ServerId+CustomerId
id=ServerId
no parent
isAbstract = No
}

one sig TableNumber extends string{}
one sig OccupiedStatus extends string{}
one sig ServerId extends Integer{}
one sig CustomerId extends string{}

one sig Employee extends Class{}{
attrSet = EmployeeID
one parent
parent in HotelManagement
id = HotelId
isAbstract = No
}

one sig EmployeeID extends string{}

one sig Payment extends Class{}{
attrSet = CustomerName+PaymentId+BillId+ServerId
id=PaymentId
no parent
isAbstract = No
}

one sig CustomerName extends string{}
one sig PaymentId extends Integer{}
one sig BillId extends string{}
one sig ServerId extends string{}

one sig Order extends Class{}{
attrSet = OrderID
one parent
parent in HotelManagement
id = HotelId
isAbstract = No
}

one sig OrderID extends string{}

one sig HotelManagementSystem extends Class{}{
attrSet = HSId+OrderStatus+NumofEmployees+BillId
id=HSId
no parent
isAbstract = No
}

one sig HSId extends Integer{}
one sig OrderStatus extends string{}

one sig HotelManagementHSAssociation extends Association{}{
src = HotelManagementSystem
dst= HotelManagement
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HotelManagementCustomerTableAssociation extends Association{}{
src = HotelManagement
dst= CustomerTable
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig HSCustomerAssociation extends Association{}{
src = HotelManagementSystem
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HSCustomerTableAssociation extends Association{}{
src = HotelManagementSystem
dst= CustomerTable
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HSPaymentAssociation extends Association{}{
src = HotelManagementSystem
dst= Payment
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig PaymentLMenuAssociation extends Association{}{
src = Payment
dst= Menu
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig PaymentCustomerTableAssociation extends Association{}{
src = Payment
dst= CustomerTable
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerMenuAssociation extends Association{}{
src = Menu
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerTableMenuAssociation extends Association{}{
src = Menu
dst= CustomerTable
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig HotelManagementCustomerAssociation extends Association{}{
src = HotelManagement
dst= Customer
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 44
