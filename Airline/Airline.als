module Reservation
open Declaration

one sig Crews extends Class{}{
attrSet = CrewsId+CrewsName+CrewsAge+Crewscontactnum
id=CrewsId
no parent
isAbstract = No
}

one sig CrewsId extends Integer{}
one sig CrewsName extends string{}
one sig CrewsAge extends string{}
one sig Crewscontactnum extends string{}

one sig Transaction extends Class{}{
attrSet = TransactionId+details+listofdish+date
id = TransactionId
no parent
isAbstract = No
}

one sig TransactionId extends Integer{}
one sig details extends Integer{}
one sig listofdish extends Integer{}
one sig date extends Integer{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+CustomerAddress+CustomerReservations+CustomerDetails
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends string{}
one sig CustomerAddress extends string{}
one sig CustomerReservations extends Integer{}
one sig CustomerDetails extends Integer{}

one sig AirlineTicket extends Class{}{
attrSet = AirlineTicketId+AirlineTicketName+AirlineDetails+AirlinePrice
id=AirlineTicketId
no parent
isAbstract = No
}

one sig AirlineTicketId extends Integer{}
one sig AirlineTicketName extends string{}
one sig AirlineDetails extends string{}
one sig AirlinePrice extends string{}



one sig Reservation extends Class{}{
attrSet = ReservationId+ReservationDetails+ticketnumber+date
id=ReservationId
no parent
isAbstract = No
}

one sig ReservationId extends Integer{}
one sig ReservationDetails extends string{}
one sig ticketnumber extends string{}
one sig date extends string{}

one sig Payment extends Class{}{
attrSet = PaymentId+Paymentamount+Paymentdate
id=PaymentId
no parent
isAbstract = No
}

one sig PaymentId extends Integer{}
one sig Paymentamount extends Integer{}
one sig Paymentdate extends Integer{}

one sig ReservationAirlineTicketAssociation extends Association{}{
src = Reservation
dst= AirlineTicket
src_multiplicity = ONE
dst_multiplicity = ONE
}


one sig ReservationCustomerAssociation extends Association{}{
src = Reservation
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TransactionAirlineTicketAssociation extends Association{}{
src = Transaction
dst= AirlineTicket
src_multiplicity = ONE
dst_multiplicity = ONE
}



pred show{}
run show for 38
