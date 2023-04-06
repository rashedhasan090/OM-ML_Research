module BuyerSellerObjectModel
open Declaration

one sig Buyer extends Class{}{
attrSet = BuyerID+BuyerName
id=BuyerID
isAbstract = No
no parent
}

one sig BuyerID extends Integer{}
one sig BuyerName extends string{}

one sig Seller extends Class{}{
attrSet = SellerID + SellerValue
id=SellerID
isAbstract = No
no parent
}
one sig SellerID extends Integer{}
one sig SellerValue extends Real{}

one sig BuyerSellerAssociation extends Association{}{
src = Buyer
dst = Seller
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig RegularBuyer extends Class{}{
attrSet = MembershipID
one parent
parent in Buyer
isAbstract = No
id=BuyerID
}
one sig MembershipID extends Integer{}

one sig OccassionalBuyer extends Class{}{
attrSet = discount
one parent
parent in Buyer
isAbstract = No
id=BuyerID
}
one sig discount extends Integer{}


pred show{}
run show for 16
