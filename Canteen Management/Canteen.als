module Canteen
open Declaration

one sig Payment extends Class{}{
attrSet = PaymentId+ProductDetails
id=PaymentId
no parent
isAbstract = No
}

one sig PaymentId extends Integer{}
one sig ProductDetails extends string{}

one sig User extends Class{}{
attrSet = UserId+IntructionType
id=UserId
no parent
isAbstract = No
}

one sig UserId extends Integer{}
one sig IntructionType extends string{}

one sig Product extends Class{}{
attrSet = ProductId+NoOfSoldProducts+NoTotalProducts+NoInventoryProducts+ProductType+Description
id=ProductId
no parent
isAbstract = No
}

one sig ProductId extends Integer{}
one sig NoOfSoldProducts extends Integer{}
one sig NoTotalProducts extends Integer{}
one sig NoInventoryProducts extends Integer{}
one sig ProductType extends Integer{}
one sig Description extends Integer{}

one sig Food extends Class{}{
attrSet = FoodCategory+FoodType+ItemId+Price
id=ItemId
no parent
isAbstract = No
}

one sig FoodCategory extends string{}
one sig FoodType extends string{}
one sig ItemId extends Integer{}
one sig Price extends string{}

one sig Salesman extends Class{}{
attrSet = TotalItemsSold
one parent
parent in User
id = UserId
isAbstract = No
}

one sig TotalItemsSold extends string{}

one sig Orders extends Class{}{
attrSet = OrdersName+OrdersId+OrderNumber+Customer_Info
id=OrdersId
no parent
isAbstract = No
}

one sig OrdersName extends string{}
one sig OrdersId extends Integer{}
one sig OrderNumber extends string{}
one sig Customer_Info extends string{}

one sig Manager extends Class{}{
attrSet = ResponsibilityLog
one parent
parent in User
id = UserId
isAbstract = No
}

one sig ResponsibilityLog extends string{}

one sig Canteen extends Class{}{
attrSet = CanteenId+UserType+IntructionType+OrderNumber
id=CanteenId
no parent
isAbstract = No
}

one sig CanteenId extends Integer{}
one sig UserType extends string{}

one sig UserCanteenAssociation extends Association{}{
src = Canteen
dst= User
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserFoodAssociation extends Association{}{
src = User
dst= Food
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CanteenProductAssociation extends Association{}{
src = Canteen
dst= Product
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CanteenFoodAssociation extends Association{}{
src = Canteen
dst= Food
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CanteenOrdersAssociation extends Association{}{
src = Canteen
dst= Orders
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig OrdersLibraryDbAssociation extends Association{}{
src = Orders
dst= Payment
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig OrdersFoodAssociation extends Association{}{
src = Orders
dst= Food
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ProductLibraryDbAssociation extends Association{}{
src = Payment
dst= Product
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig FoodLibraryDbAssociation extends Association{}{
src = Payment
dst= Food
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserProductAssociation extends Association{}{
src = User
dst= Product
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 41
