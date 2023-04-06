module railway
open Declaration

one sig Passanger extends Class{}{
attrSet = PassangerID+PassangerName
id=PassangerID
isAbstract = No
no parent
}

one sig PassangerID extends Integer{}
one sig PassangerName extends string{}

one sig Reservation extends Class{}{
attrSet = ReservationID+status
id=ReservationID
isAbstract = No
no parent
}

one sig ReservationID extends Integer{}
one sig status extends string{}

one sig PassangerReservationAssociation extends Association{}{
src = Passanger
dst = Reservation
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig PaymentPortal extends Class{}{
attrSet = PaymentPortalID
id=PaymentPortalID
isAbstract = No
no parent
}

one sig PaymentPortalID extends Integer{}


one sig PassangerPaymentPortalAssociation extends Association{}{
src = Passanger
dst = PaymentPortal
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig SearchTrain extends Class{}{
attrSet = SearchTrainID+trainname
id=SearchTrainID
isAbstract = No
no parent
}

one sig SearchTrainID extends Integer{}
one sig trainname extends Integer{}

one sig Kiosk extends Class{}{
attrSet = KioskID
one parent
id=SearchTrainID
isAbstract = No
parent in SearchTrain
}

one sig KioskID extends Integer{}

one sig Website extends Class{}{
attrSet = WebAddress
one parent
id=SearchTrainID
isAbstract = No
parent in SearchTrain
}

one sig WebAddress extends string{}


one sig PaymentPortalSearchTrainAssociation extends Association{}{
src = PaymentPortal
dst = SearchTrain
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ReservationSearchTrain extends Class{}{
attrSet = ReservationSearchTrainID+status
one parent
id=SearchTrainID
isAbstract = No
parent in SearchTrain
}

one sig status extends Integer{}
one sig ReservationSearchTrainID extends Integer{}


one sig ReservationSearchTrainAssociation extends Association{}{
src = Reservation
dst = SearchTrain
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Administration extends Class{}{
attrSet = AdministrationID+AdministrationName
id=AdministrationID
isAbstract = No
no parent
}

one sig AdministrationID extends Integer{}
one sig AdministrationName extends string{}


one sig Train extends Class{}{
attrSet = TrainID+TrainName+arrival_time+departure_time
id=TrainID
isAbstract = No
no parent
}


one sig TrainID extends Integer{}
one sig TrainName extends string{}
one sig arrival_time extends string{}
one sig departure_time extends Real{}


one sig TrainAdministrationAssociation extends Association{}{
src = Train
dst = Administration
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig Zone extends Class{}{
attrSet = ZoneID
id=ZoneID
isAbstract = No
no parent
}

one sig ZoneID extends Integer{}



one sig TrainZoneAssociation extends Association{}{
src = Train
dst = Zone
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig TrainSearchTrainAssociation extends Association{}{
src = Train
dst = SearchTrain
src_multiplicity = MANY
dst_multiplicity = MANY
}


one sig Super-fast-train extends Class{}{
attrSet = station
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig station extends string{}



one sig RajdhaniExpress extends Class{}{
attrSet = station
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig station extends string{}

one sig ShatabdiExpress extends Class{}{
attrSet = station
one parent
id=TrainID
isAbstract = No
parent in Train
}

one sig station extends string{}

one sig ReservedZone extends Class{}{
attrSet = ReservedZoneID+ReservedZoneName+Zoneroute
id = ReservedZoneID
isAbstract = No
no parent
}

one sig ReservedZoneID extends Integer{}
one sig ReservedZoneName extends string{}
one sig Zoneroute extends string{}

one sig TrainReservedZoneAssociation extends Association{}{
src = Train
dst = ReservedZone
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CentralZone extends Class{}{
attrSet = CentralZoneRoute
one parent
id = ReservedZoneID
isAbstract = No
parent in ReservedZone
}

one sig CentralZoneRoute extends Integer{}

one sig EasternZone extends Class{}{
attrSet = EasternZoneRoute
one parent
id = ReservedZoneID
isAbstract = No
parent in ReservedZone
}

one sig EasternZoneRoute extends string{}

one sig WesternZone extends Class{}{
attrSet = WesternZoneRoute
one parent
id = ReservedZoneID
isAbstract = No
parent in ReservedZone
}

one sig WesternZoneRoute extends string{}

one sig SouthernZone extends Class{}{
attrSet = SouthernZoneRoute
one parent
id = ReservedZoneID
isAbstract = No
parent in ReservedZone
}

one sig SouthernZoneRoute extends string{}


pred show{}
run show for 48
