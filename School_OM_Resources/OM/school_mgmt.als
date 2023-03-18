module school
open Declaration


one sig Registrar extends Class{}{
attrSet = RegistrarID+RegistrarName
id=RegistrarID
isAbstract = No
no parent
}

one sig RegistrarID extends Integer{}
one sig RegistrarName extends string{}


one sig Instructors extends Class{}{
attrSet = InstructorsID+InstructorsName
id=InstructorsID
isAbstract = No
no parent
}

one sig InstructorsID extends Integer{}
one sig InstructorsName extends string{}



one sig Transactions extends Class{}{
attrSet = TransactionsID+TransactionsName
id=TransactionsID
isAbstract = No
no parent
}

one sig TransactionsID extends Integer{}
one sig TransactionsName extends string{}


one sig InstructorsTransactionsAssociation extends Association{}{
src = Instructors
dst = Transactions
src_multiplicity = ONE
dst_multiplicity = MANY
}



one sig Students extends Class{}{
attrSet = StudentsID+StudentsName
id=StudentsID
isAbstract = No
no parent
}

one sig StudentsID extends Integer{}
one sig StudentsName extends string{}


one sig Subjects extends Class{}{
attrSet = SubjectsID+SubjectsName
id=SubjectsID
isAbstract = No
no parent
}

one sig SubjectsID extends Integer{}
one sig SubjectsName extends string{}



one sig StudentsBindingsAssociation extends Association{}{
src = Course
dst = Students
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig Course extends Class{}{
attrSet=CourseID
id=CourseID
isAbstract = No
no parent
}
one sig CourseID extends Integer{}

one sig SubjectsCoursesAssociation extends Association{}{
src = Subjects
dst = Course
src_multiplicity = MANY
dst_multiplicity = MANY
}


one sig SubjectsInstructorsAssociation extends Association{}{
src = Subjects
dst = Instructors
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig User extends Class{}{
attrSet = username+password
id=CourseID
one parent
parent in Course
isAbstract = No
}

one sig username extends string{}
one sig password extends string{}

one sig Viewer extends Class{}{
attrSet = period
id=CourseID
one parent
parent in Course
isAbstract = No
}

one sig period extends Integer{}


one sig Enrollment extends Class{}{
attrSet = department
id=CourseID
one parent
parent in Course
isAbstract = No
}

one sig department extends Integer{}

one sig SubjectsRegistrarAssociation  extends Association{}{
src = Subjects
dst = Registrar
src_multiplicity = ONE
dst_multiplicity = MANY
}


pred show{}
run show for 55
