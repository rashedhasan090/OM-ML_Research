module Attendence
open Declaration

one sig Admin extends Class{}{
attrSet = AdminId+AdminName
id=AdminId
no parent
isAbstract = No
}

one sig AdminId extends Integer{}
one sig AdminName extends string{}

one sig Teacher extends Class{}{
attrSet = TeacherId+TeacherName+Email+Password
id=TeacherId
no parent
isAbstract = No
}

one sig TeacherId extends Integer{}
one sig TeacherName extends string{}
one sig Email extends string{}
one sig Password extends Integer{}

one sig Student extends Class{}{
attrSet = StudentId+StudentName+Password+Email
id=StudentId
no parent
isAbstract = No
}

one sig StudentId extends Integer{}
one sig StudentName extends string{}
one sig Password extends string{}
one sig Email extends Integer{}

one sig RegularStudent extends Class{}{
attrSet = Attendence_Count
id=Attendence_Count
no parent
isAbstract = No
}

one sig Attendence_Count extends Integer{}

one sig Course extends Class{}{
attrSet = CourseId+CourseName+CourseTeacher+EnrolledStudents
id=CourseId
no parent
isAbstract = No
}

one sig CourseId extends Integer{}
one sig CourseName extends string{}
one sig CourseTeacher extends string{}
one sig EnrolledStudents extends string{}

one sig IrregularStudent extends Class{}{
attrSet = IrregularStudentId+NumOfCourse+status+count
id=IrregularStudentId
no parent
isAbstract = No
}

one sig IrregularStudentId extends Integer{}
one sig NumOfCourse extends Integer{}
one sig status extends Integer{}
one sig count extends Integer{}

one sig AdminCourseAssociation extends Association{}{
src = Admin
dst= Course
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TeacherCourseAssociation extends Association{}{
src = Teacher
dst= Course
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CourseRegularStudentAssociation extends Association{}{
src = RegularStudent
dst= Course
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TeacherIrregularStudentAssociation extends Association{}{
src = Teacher
dst= IrregularStudent
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TeacherStudentAssociation  extends Association{}{
src = Teacher
dst= Student
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 12
