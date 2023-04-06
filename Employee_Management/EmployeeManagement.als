module EmployeeManagement
open Declaration


one sig Deductions extends Class{}{
attrSet = DeductionsID+payeedetails
id=DeductionsID
isAbstract = No
no parent
}

one sig DeductionsID extends Integer{}
one sig payeedetails extends string{}


one sig Benefits extends Class{}{
attrSet = BenefitsID+Requirements
id=BenefitsID
isAbstract = No
no parent
}

one sig BenefitsID extends Integer{}
one sig Requirements extends string{}



one sig Tax extends Class{}{
attrSet = TaxID+TaxFile
id=TaxID
isAbstract = No
no parent
}

one sig TaxID extends Integer{}
one sig TaxFile extends string{}


one sig BenefitsTaxAssociation extends Association{}{
src = Benefits
dst = Tax
src_multiplicity = ONE
dst_multiplicity = MANY
}



one sig JobDepartment extends Class{}{
attrSet = JobDepartmentID+JobDepartmentName
id=JobDepartmentID
isAbstract = No
no parent
}

one sig JobDepartmentID extends Integer{}
one sig JobDepartmentName extends string{}


one sig Absences extends Class{}{
attrSet = EmployeeID+EmployeeName
id=EmployeeID
isAbstract = No
no parent
}

one sig EmployeeID extends Integer{}
one sig EmployeeName extends string{}



one sig JobDepartmentEmployeeAssociation extends Association{}{
src = Employee
dst = JobDepartment
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig Employee extends Class{}{
attrSet=EmployeeID
id=EmployeeID
isAbstract = No
no parent
}
one sig EmployeeID extends Integer{}

one sig AbsencesEmployeesAssociation extends Association{}{
src = Absences
dst = Employee
src_multiplicity = MANY
dst_multiplicity = MANY
}


one sig AbsencesBenefitssAssociation extends Association{}{
src = Absences
dst = Benefits
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig Salary extends Class{}{
attrSet = Workhours+total
id=EmployeeID
one parent
parent in Employee
isAbstract = No
}

one sig Workhours extends string{}
one sig total extends string{}

one sig Manager extends Class{}{
attrSet = salary
id=EmployeeID
one parent
parent in Employee
isAbstract = No
}

one sig salary extends Integer{}


one sig ChiefExecutive extends Class{}{
attrSet = department
id=EmployeeID
one parent
parent in Employee
isAbstract = No
}

one sig department extends Integer{}

one sig AbsencesDeductionsAssociation  extends Association{}{
src = Absences
dst = Deductions
src_multiplicity = ONE
dst_multiplicity = MANY
}


pred show{}
run show for 55
