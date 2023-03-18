module Camping
open Declaration

one sig BadgeAwarded extends Class{}{
attrSet = AwardId+Date
id=AwardId
no parent
isAbstract = No
}

one sig AwardId extends Integer{}
one sig Date extends Integer{}

one sig CampSite extends Class{}{
attrSet = SiteID+Location
id=SiteID
no parent
isAbstract = No
}

one sig SiteID extends Integer{}
one sig Location extends string{}

one sig BadgeSpecification extends Class{}{
attrSet = BadgeSpecificationId+BadgeName
id=BadgeSpecificationId
no parent
isAbstract = No
}

one sig BadgeSpecificationId extends Integer{}
one sig BadgeName extends string{}

one sig Scout extends Class{}{
attrSet = ScoutId+Name+DOB+Joined
id=ScoutId
no parent
isAbstract = No
}

one sig ScoutId extends Integer{}
one sig Name extends string{}
one sig DOB extends Integer{}
one sig Joined extends Integer{}

one sig WealthyScout extends Class{}{
attrSet = DonationAmount+DonationDate
one parent
parent in Scout
id = ScoutId
isAbstract = No
}

one sig DonationAmount extends Integer{}
one sig DonationDate extends Integer{}

one sig CampingTrip extends Class{}{
attrSet = TripId+StartDate+EndDate
id=TripId
no parent
isAbstract = No
}

one sig TripId extends Integer{}
one sig StartDate extends Integer{}
one sig EndDate extends Integer{}

one sig CampingTripScoutAssociation extends Association{}{
src = CampingTrip
dst= Scout
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CampingTripSiteAssociation extends Association{}{
src = CampSite
dst= CampingTrip
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig ScoutBadgeAwardedAssociation extends Association{}{
src = Scout
dst= BadgeAwarded
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig BadgeAwardedSpecificationAssociation extends Association{}{
src = BadgeSpecification
dst= BadgeAwarded
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 30
