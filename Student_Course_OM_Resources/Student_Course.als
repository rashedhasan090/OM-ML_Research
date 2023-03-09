module Student_Course
open Declaration

one sig Registration extends Class{}{
attrSet = AwardId+Fee
id=AwardId
no parent
isAbstract = No
}

one sig AwardId extends Integer{}
one sig Fee extends Integer{}

one sig Payment extends Class{}{
attrSet = PaymentID+amount
id=PaymentID
no parent
isAbstract = No
}

one sig PaymentID extends Integer{}
one sig amount extends string{}

one sig Transaction extends Class{}{
attrSet = TransactionId+TransactionName
id=TransactionId
no parent
isAbstract = No
}

one sig TransactionId extends Integer{}
one sig TransactionName extends string{}

one sig Student extends Class{}{
attrSet = StudentId+Name+Age+gender
id=StudentId
no parent
isAbstract = No
}

one sig StudentId extends Integer{}
one sig Name extends string{}
one sig Age extends Integer{}
one sig gender extends Integer{}

one sig Requirements extends Class{}{
attrSet = content+date
one parent
parent in Student
id = StudentId
isAbstract = No
}

one sig content extends Integer{}
one sig date extends Integer{}

one sig Courses extends Class{}{
attrSet = CourseId+CourseName+Description
id=CourseId
no parent
isAbstract = No
}

one sig CourseId extends Integer{}
one sig CourseName extends Integer{}
one sig Description extends Integer{}

one sig CoursesStudentAssociation extends Association{}{
src = Courses
dst= Student
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CoursesSiteAssociation extends Association{}{
src = Payment
dst= Courses
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig StudentRegistrationAssociation extends Association{}{
src = Student
dst= Registration
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig RegistrationSpecificationAssociation extends Association{}{
src = Transaction
dst= Registration
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 211
