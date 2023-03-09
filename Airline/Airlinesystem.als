module AirlineSystem
open Declaration

one sig AirlineTicket extends Class{}{
attrSet = AirlineTicketID+AirlineTicketName
id=AirlineTicketID
isAbstract = No
no parent
}

one sig AirlineTicketID extends Integer{}
one sig AirlineTicketName extends string{}

one sig Customer extends Class{}{
attrSet = CustomerID + CustomerName
id=CustomerID
isAbstract = No
no parent
}
one sig CustomerID extends Integer{}
one sig CustomerName extends Real{}

one sig CustomerAirlineTicketAssociation extends Association{}{
src = Customer
dst = AirlineTicket
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Transaction extends Class{}{
attrSet = TransactionID
one parent
parent in AirlineTicket
isAbstract = No
id=AirlineTicketID
}
one sig TransactionID extends Integer{}

one sig Payment extends Class{}{
attrSet = amount
one parent
parent in AirlineTicket
isAbstract = No
id=AirlineTicketID
}
one sig amount extends Integer{}


pred show{}
run show for 16
