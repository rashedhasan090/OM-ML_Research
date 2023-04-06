module EventManagement
open Declaration

one sig Event extends Class{}{
attrSet = EventId+Price
id=EventId
no parent
isAbstract = No
}

one sig EventId extends Integer{}
one sig Price extends string{}

one sig Crew extends Class{}{
attrSet = CrewId
one parent
parent in User
id = UserId
isAbstract = No
}

one sig CrewId extends Integer{}

one sig Client extends Class{}{
attrSet = ClientId+ClientName+ClientAddress+ClientPhoneNo+ClientOrderId
id=ClientId
no parent
isAbstract = No
}

one sig ClientId extends Integer{}
one sig ClientName extends string{}
one sig ClientAddress extends string{}
one sig ClientPhoneNo extends Integer{}
one sig ClientOrderId extends Integer{}

one sig Price extends Class{}{
attrSet = PriceId+EventDescription
id=PriceId
no parent
isAbstract = No
}

one sig PriceId extends Integer{}
one sig EventDescription extends string{}

one sig User extends Class{}{
attrSet = UserId+ClientId
id=UserId
no parent
isAbstract = No
}

one sig UserId extends Integer{}

one sig Reports extends Class{}{
attrSet = ReportId+description+CrewList
id=ReportId
no parent
isAbstract = No
}

one sig ReportId extends Integer{}
one sig description extends string{}
one sig CrewList extends string{}

one sig Admin extends Class{}{
attrSet = AdminId
one parent
parent in User
id=UserId
isAbstract = No
}

one sig AdminId extends Integer{}

one sig ReportsPriceAssociation extends Association{}{
src = Reports
dst= Price
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig ReportsClientAssociation extends Association{}{
src = Reports
dst= Client
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ClientPriceAssociation extends Association{}{
src = Client
dst= Price
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig ClientUserAssociation extends Association{}{
src = Client
dst= User
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ClientEventAssociation extends Association{}{
src = Client
dst= Event
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
