module Order_Process
open Declaration

one sig Inventory extends Class{}{
attrSet = ItemId+ItemType
id=ItemId
no parent
isAbstract = No
}

one sig ItemId extends Integer{}
one sig ItemType extends string{}

one sig Payment extends Class{}{
attrSet = PaymentId
one parent
parent in Customer
id = ManagementId
isAbstract = No
}

one sig PaymentId extends Integer{}

one sig Management extends Class{}{
attrSet = ManagementId+ManagementName+ManagementAddress+ManagementPhoneNo+ManagementAcctNo
id=ManagementId
no parent
isAbstract = No
}

one sig ManagementId extends Integer{}
one sig ManagementName extends string{}
one sig ManagementAddress extends string{}
one sig ManagementPhoneNo extends Integer{}
one sig ManagementAcctNo extends Integer{}

one sig Products extends Class{}{
attrSet = ProductsId+ProductsName
id=ProductsId
no parent
isAbstract = No
}

one sig ProductsId extends Integer{}
one sig ProductsName extends string{}

one sig Customer extends Class{}{
attrSet = CustomerId+ManagementId
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}

one sig Delivery extends Class{}{
attrSet = DeliveryId+AgentName+DeliveryLocation
id=DeliveryId
no parent
isAbstract = No
}

one sig DeliveryId extends Integer{}
one sig AgentName extends string{}
one sig DeliveryLocation extends string{}

one sig Order extends Class{}{
attrSet = OrderId
one parent
parent in Customer
id=ManagementId
isAbstract = No
}

one sig OrderId extends Integer{}

one sig CustomerProductsAssociation extends Association{}{
src = Customer
dst= Products
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig CustomerManagementAssociation extends Association{}{
src = Customer
dst= Management
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ManagementProductsAssociation extends Association{}{
src = Management
dst= Products
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig ManagementCustomerAssociation extends Association{}{
src = Management
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ManagementInventoryAssociation extends Association{}{
src = Management
dst= Inventory
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
