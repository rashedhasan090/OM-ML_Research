module AdminStudentObjectModel
open Declaration

one sig Admin extends Class{}{
attrSet = AdminID+AdminName
id=AdminID
isAbstract = No
no parent
}

one sig AdminID extends Integer{}
one sig AdminName extends string{}

one sig Student extends Class{}{
attrSet = StudentID + StudentName
id=StudentID
isAbstract = No
no parent
}
one sig StudentID extends Integer{}
one sig StudentName extends Real{}

one sig AdminStudentAssociation extends Association{}{
src = Admin
dst = Student
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig Teacher extends Class{}{
attrSet = credentials
one parent
parent in Admin
isAbstract = No
id=AdminID
}
one sig credentials extends Integer{}

one sig TeachingAssistant extends Class{}{
attrSet = TAcred
one parent
parent in Admin
isAbstract = No
id=AdminID
}
one sig TAcred extends Integer{}


one sig Course extends Class{}{
attrSet = CourseID + CourseName
id=CourseID
isAbstract = No
no parent
}

one sig CourseID extends Integer{}
one sig CourseName extends string{}

one sig AttendenceManagementSystem extends Class{}{
attrSet = sysid + systemconifg + studentcount
id=sysid
isAbstract = No
no parent
}
one sig sysid extends Integer{}
one sig systemconifg extends string{}
one sig studentcount extends Integer{}

one sig StudentCourseAssociation extends Association{}{
src = Student
dst = Course
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig TeacherCourseAssociation extends Association{}{
src = Teacher
dst = Course
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig AdminAttendenceManagementSystemAssociation extends Association{}{
src = Admin
dst = AttendenceManagementSystem
src_multiplicity = ONE
dst_multiplicity = ONE
}



pred show{}
run show for 17
