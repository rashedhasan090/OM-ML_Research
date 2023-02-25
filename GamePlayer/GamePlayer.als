module GamePlayer
open Declaration

one sig GamePlayer extends Class{}{
attrSet = playerID+Name+club+battingAverage+bowlingAverage
no parent
id=playerID
isAbstract = No
}

one sig playerID extends Integer{}
one sig Name extends string{}
one sig club extends string{}
one sig battingAverage extends string{}
one sig bowlingAverage extends string{}


one sig Footballer extends Class{}{
attrSet = club 
one parent
parent in GamePlayer
id=playerID
isAbstract = No
}

one sig club extends string{}

one sig Cricketer extends Class{}{
attrSet = cricketerID+battingAverage+bowlingAverage
one parent
parent in GamePlayer
id=playerID
isAbstract = No
}  

one sig cricketerID extends Integer{}
one sig battingAverage extends Integer{}
one sig bowlingAverage extends Integer{}

one sig Bowler extends Class{}{
attrSet = Average
one parent
parent in Cricketer 
id=cricketerID
isAbstract = No
} 

one sig Average extends Integer{}



one sig GamePlayerFootballerAssociation extends Association{}{
src = GamePlayer
dst= Footballer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig GamePlayerFootballerAssociation extends Association{}{
src = GamePlayer
dst= Cricketer
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig CricketerBowlerAssociation extends Association{}{
src = Cricketer
dst= Bowler
src_multiplicity = MANY
dst_multiplicity = MANY
}


pred show{}
run show for 38

