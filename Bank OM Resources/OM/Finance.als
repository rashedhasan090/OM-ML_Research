module Bank
open Declaration

one sig Loan extends Class{}{
attrSet = LoanId+LoanType
id=LoanId
no parent
isAbstract = No
}

one sig LoanId extends Integer{}
one sig LoanType extends string{}

one sig Checking extends Class{}{
attrSet = CheckingId
one parent
parent in Account
id = CustomerId
isAbstract = No
}

one sig CheckingId extends Integer{}

one sig Customer extends Class{}{
attrSet = CustomerId+CustomerName+CustomerAddress+CustomerPhoneNo+CustomerAcctNo
id=CustomerId
no parent
isAbstract = No
}

one sig CustomerId extends Integer{}
one sig CustomerName extends string{}
one sig CustomerAddress extends string{}
one sig CustomerPhoneNo extends Integer{}
one sig CustomerAcctNo extends Integer{}

one sig Teller extends Class{}{
attrSet = TellerId+TellerName
id=TellerId
no parent
isAbstract = No
}

one sig TellerId extends Integer{}
one sig TellerName extends string{}

one sig Account extends Class{}{
attrSet = AccountId+CustomerId
id=AccountId
no parent
isAbstract = No
}

one sig AccountId extends Integer{}

one sig Bank extends Class{}{
attrSet = BankId+BankName+BankLocation
id=BankId
no parent
isAbstract = No
}

one sig BankId extends Integer{}
one sig BankName extends string{}
one sig BankLocation extends string{}

one sig Savings extends Class{}{
attrSet = SavingsId
one parent
parent in Account
id=CustomerId
isAbstract = No
}

one sig SavingsId extends Integer{}

one sig BankTellerAssociation extends Association{}{
src = Bank
dst= Teller
src_multiplicity = ONE
dst_multiplicity = MANY
}


one sig BankCustomerAssociation extends Association{}{
src = Bank
dst= Customer
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerTellerAssociation extends Association{}{
src = Customer
dst= Teller
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig CustomerAccountAssociation extends Association{}{
src = Customer
dst= Account
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig CustomerLoanAssociation extends Association{}{
src = Customer
dst= Loan
src_multiplicity = ONE
dst_multiplicity = MANY
}

pred show{}
run show for 38
