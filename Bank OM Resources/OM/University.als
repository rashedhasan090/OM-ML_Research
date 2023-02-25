module University
open Declaration

one sig Loan extends Class{}{
attrSet = LoanId+LoanType
id=LoanId
no parent
isAbstract = No
}

one sig LoanId extends Integer{}
one sig LoanType extends string{}

one sig MonthlySalary extends Class{}{
attrSet = MonthlySalaryId
one parent
parent in Salary
id = EmployeeId
isAbstract = No
}

one sig MonthlySalaryId extends Integer{}

one sig Employee extends Class{}{
attrSet = EmployeeId+EmployeeName+EmployeeAddress+EmployeePhoneNo+EmployeeAcctNo
id=EmployeeId
no parent
isAbstract = No
}

one sig EmployeeId extends Integer{}
one sig EmployeeName extends string{}
one sig EmployeeAddress extends string{}
one sig EmployeePhoneNo extends Integer{}
one sig EmployeeAcctNo extends Integer{}

one sig HR extends Class{}{
attrSet = HRId+HRName
id=HRId
no parent
isAbstract = No
}

one sig HRId extends Integer{}
one sig HRName extends string{}

one sig Salary extends Class{}{
attrSet = SalaryId+EmployeeId
id=SalaryId
no parent
isAbstract = No
}

one sig SalaryId extends Integer{}

one sig University extends Class{}{
attrSet = UniversityId+UniversityName+UniversityLocation
id=UniversityId
no parent
isAbstract = No
}

one sig UniversityId extends Integer{}
one sig UniversityName extends string{}
one sig UniversityLocation extends string{}

one sig Savings extends Class{}{
attrSet = SavingsId
one parent
parent in Salary
id=EmployeeId
isAbstract = No
}

one sig SavingsId extends Integer{}

one sig UniversityHRAssociation extends Association{}{
src = University
dst= HR
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig UniversityEmployeeAssociation extends Association{}{
src = University
dst= Employee
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig EmployeeHRAssociation extends Association{}{
src = Employee
dst= HR
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig EmployeeSalaryAssociation extends Association{}{
src = Employee
dst= Salary
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig EmployeeLoanAssociation extends Association{}{
src = Employee
dst= Loan
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
