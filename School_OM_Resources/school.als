module school
open Declaration


one sig Registrar extends Class{}{
attrSet = RegistrarID+RegistrarName+RegistrarAge+RegistrarContactnum+RegistrarUsername+RegistrarPassword
id=RegistrarID
isAbstract = No
no parent
}

one sig RegistrarID extends Integer{}
one sig RegistrarName extends string{}
one sig RegistrarAge extends string{}
one sig RegistrarContactnum extends string{}
one sig RegistrarUsername extends string{}
one sig RegistrarPassword extends string{}


one sig Instructors extends Class{}{
attrSet = credentials
id=RegistrarID
one parent
parent in Registrar
isAbstract = No
}

one sig credentials extends string{}


one sig Transactions extends Class{}{
attrSet = TransactionID+Details+Date
id=RegistrarID
one parent
parent in Registrar
isAbstract = No
}

one sig TransactionID extends Integer{}
one sig Details extends string{}
one sig Date extends string{}

one sig Students extends Class{}{
attrSet = course
id=RegistrarID
one parent
parent in Registrar
isAbstract = No
}

one sig course extends string{}



one sig Subjects extends Class{}{
attrSet = SubjectID+SubjectName+SubjectDescription+SubjectInstructor+SubjectSchedule
id=SubjectID
no parent
isAbstract = No
}


one sig SubjectID extends Integer{}
one sig SubjectName extends string{}
one sig SubjectDescription extends string{}
one sig SubjectInstructor extends string{}
one sig SubjectSchedule extends string{}


one sig Course extends Class{}{
attrSet = CourseID+CourseDescriptions+CourseDate+yearlevel
id=TransactionID
one parent
parent in Transactions
isAbstract = No
}

one sig CourseID extends Integer{}
one sig CourseDescriptions extends string{}
one sig CourseDate extends string{}
one sig yearlevel extends string{}




one sig Enrollment extends Class{}{
attrSet = EnrollmentID+details+requirements+date
id=EnrollmentID
no parent
isAbstract = No
}


one sig EnrollmentID extends Integer{}
one sig details extends string{}
one sig requirements extends string{}
one sig date extends string{}




one sig InstructorsSubjectsAssociation extends Association{}{
src = Instructors
dst = Subjects
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig SubjectsInstructorsAssociation extends Association{}{
src = Subjects
dst = Instructors
src_multiplicity = ONE
dst_multiplicity = ONE
}


one sig SubjectsCourseAssociation extends Association{}{
src = Subjects
dst = Course
src_multiplicity = MANY
dst_multiplicity = ONE
}

one sig CourseSubjectsAssociation extends Association{}{
src = Course
dst = Subjects
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig EnrollmentCourseAssociation extends Association{}{
src = Enrollment
dst = Course
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig StudentsEnrollmentAssociation extends Association{}{
src = Students
dst = Enrollment
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig EnrollmentStudentsAssociation extends Association{}{
src = Enrollment
dst = Students
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 55
