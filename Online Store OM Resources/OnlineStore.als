module OnlineStore
open Declaration

one sig Admin extends Class{}{
attrSet = AdminId+AdminName
id=AdminId
no parent
isAbstract = No
}

one sig AdminId extends Integer{}
one sig AdminName extends string{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+Address+PhoneNo
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends string{}
one sig Address extends string{}
one sig PhoneNo extends Integer{}

one sig Payment extends Class{}{
attrSet = PaymentId+PaymentName+CardType+CardNo
id=PaymentId
no parent
isAbstract = No
}

one sig PaymentId extends Integer{}
one sig PaymentName extends string{}
one sig CardType extends string{}
one sig CardNo extends Integer{}

one sig Guest extends Class{}{
attrSet = GuestId
id=GuestId
no parent
isAbstract = No
}

one sig GuestId extends Integer{}

one sig Products extends Class{}{
attrSet = ProductsId+ProductsName+Group+Subgroup
id=ProductsId
no parent
isAbstract = No
}

one sig ProductsId extends Integer{}
one sig ProductsName extends string{}
one sig Group extends string{}
one sig Subgroup extends string{}

one sig Cart extends Class{}{
attrSet = CartId+NumOfProducts+Price+Total
id=CartId
no parent
isAbstract = No
}

one sig CartId extends Integer{}
one sig NumOfProducts extends Integer{}
one sig Price extends Integer{}
one sig Total extends Integer{}

one sig AdminProductsAssociation extends Association{}{
src = Admin
dst= Products
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerProductsAssociation extends Association{}{
src = Customer
dst= Products
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ProductsGuestAssociation extends Association{}{
src = Guest
dst= Products
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerCartAssociation extends Association{}{
src = Customer
dst= Cart
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig CustomerPaymentAssociation  extends Association{}{
src = Customer
dst= Payment
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 38
