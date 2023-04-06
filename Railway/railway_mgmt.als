module railway_mgmt
open Declaration

one sig Administration extends Class{}{
attrSet = AdministrationID
id=AdministrationID
isAbstract = No
no parent
}

one sig AdministrationID extends Integer{}


one sig Reservation extends Class{}{
attrSet = ReservationID
id=ReservationID
isAbstract = No
no parent
}

one sig ReservationID extends Integer{}


one sig AdministrationReservationAssociation extends Association{}{
src = Administration
dst = Reservation
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig SearchTrain extends Class{}{
attrSet = train_no
id=train_no
isAbstract = No
no parent
}

one sig train_no extends Integer{}


one sig AdministrationSearchTrainAssociation extends Association{}{
src = Administration
dst = SearchTrain
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig Passanger extends Class{}{
attrSet = PassangerID+PassangerName
id=PassangerID
isAbstract = No
no parent
}

one sig PassangerID extends Integer{}
one sig PassangerName extends Integer{}

one sig Ticket extends Class{}{
attrSet = TicketNo
one parent
id=PassangerID
isAbstract = No
parent in Passanger
}

one sig TicketNo extends Integer{}


one sig SearchTrainPassangerAssociation extends Association{}{
src = SearchTrain
dst = Passanger
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ReservationPassanger extends Class{}{
attrSet = ReservationPassangerID+status
one parent
id=PassangerID
isAbstract = No
parent in Passanger
}

one sig status extends Integer{}
one sig ReservationPassangerID extends Integer{}


one sig ReservationPassangerAssociation extends Association{}{
src = Reservation
dst = Passanger
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Super_fast_train extends Class{}{
attrSet = trainNo+trainName
id=trainNo
isAbstract = No
no parent
}

one sig trainNo extends Integer{}
one sig trainName extends string{}


one sig Train extends Class{}{
attrSet = TrainID+TrainName+no_of_coach+departure_time
id=TrainID
isAbstract = No
no parent
}


one sig TrainID extends Integer{}
one sig TrainName extends string{}
one sig no_of_coach extends string{}
one sig departure_time extends Real{}


one sig TrainSuper_fast_trainAssociation extends Association{}{
src = Train
dst = Super_fast_train
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig Rajdhani_Express extends Class{}{
attrSet = trainNo
id=trainNo
isAbstract = No
no parent
}

one sig trainNo extends Integer{}



one sig TrainRajdhani_ExpressAssociation extends Association{}{
src = Train
dst = Rajdhani_Express
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig TrainPassangerAssociation extends Association{}{
src = Train
dst = Passanger
src_multiplicity = MANY
dst_multiplicity = MANY
}


one sig CargoTrain extends Class{}{
attrSet = weight+availability
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig weight extends Real{}
one sig availability extends Bool{}


one sig ElectronicTrain extends Class{}{
attrSet = size
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig size extends string{}

one sig Traincar extends Class{}{
attrSet = schedule
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig schedule extends string{}

one sig Zone extends Class{}{
attrSet = ZoneID+ZoneName+Zonelength
id = ZoneID
isAbstract = No
no parent
}

one sig ZoneID extends Integer{}
one sig ZoneName extends string{}
one sig Zonelength extends string{}

one sig TrainZoneAssociation extends Association{}{
src = Train
dst = Zone
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CentralZone extends Class{}{
attrSet = CentralZoneroute
one parent
id = ZoneID
isAbstract = No
parent in Zone
}

one sig CentralZoneroute extends Integer{}

one sig WesternZone extends Class{}{
attrSet = WesternZoneroute
one parent
id = ZoneID
isAbstract = No
parent in Zone
}

one sig WesternZoneroute extends string{}


pred show{}
run show for 48
