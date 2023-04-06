module Store
open Declaration

one sig StoreDatabase extends Class{}{
attrSet = StoreDbId+ListOFStocks
id=StoreDbId
no parent
isAbstract = No
}

one sig StoreDbId extends Integer{}
one sig ListOFStocks extends string{}

one sig User extends Class{}{
attrSet = UserId+UserName
id=UserId
no parent
isAbstract = No
}

one sig UserId extends Integer{}
one sig UserName extends string{}

one sig Store extends Class{}{
attrSet = StoreId+NoSoldProducts+NoReservedProducts+StoreType+StoreName+TotalAmount
id=StoreId
no parent
isAbstract = No
}

one sig StoreId extends Integer{}
one sig NoSoldProducts extends Integer{}
one sig NoReservedProducts extends Integer{}
one sig StoreType extends Integer{}
one sig StoreName extends Integer{}
one sig TotalAmount extends Integer{}

one sig Stock extends Class{}{
attrSet = Type+StockItems+StockId+StockDescription
id=StockId
no parent
isAbstract = No
}

one sig Type extends string{}
one sig StockItems extends string{}
one sig StockId extends Integer{}
one sig StockDescription extends string{}

one sig Owner extends Class{}{
attrSet = ownerName
one parent
parent in User
id = UserId
isAbstract = No
}

one sig ownerName extends string{}

one sig Customer extends Class{}{
attrSet = CustomerName+CustomerId+CustomerAddress+CustomerPhone
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerName extends string{}
one sig CustomerId extends Integer{}
one sig CustomerAddress extends string{}
one sig CustomerPhone extends string{}

one sig Staff extends Class{}{
attrSet = Dept
one parent
parent in User
id = UserId
isAbstract = No
}

one sig Dept extends string{}

one sig StoreManagementSystem extends Class{}{
attrSet = TransactionId+UserType+UserName+CustomerAddress
id=TransactionId
no parent
isAbstract = No
}

one sig TransactionId extends Integer{}
one sig UserType extends string{}

one sig UserSMSAssociation extends Association{}{
src = StoreManagementSystem
dst= User
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserStockAssociation extends Association{}{
src = User
dst= Stock
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig SMSStoreAssociation extends Association{}{
src = StoreManagementSystem
dst= Store
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig SMSStockAssociation extends Association{}{
src = StoreManagementSystem
dst= Stock
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig SMSCustomerAssociation extends Association{}{
src = StoreManagementSystem
dst= Customer
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CustomerStoreDbAssociation extends Association{}{
src = Customer
dst= StoreDatabase
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CustomerStockAssociation extends Association{}{
src = Customer
dst= Stock
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig StoreStoreDbAssociation extends Association{}{
src = StoreDatabase
dst= Store
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig StockStoreDbAssociation extends Association{}{
src = StoreDatabase
dst= Stock
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserStoreAssociation extends Association{}{
src = User
dst= Store
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 44
