module Library
open Declaration

one sig LibraryDatabase extends Class{}{
attrSet = LibraryDbId+ListOFBooks
id=LibraryDbId
no parent
isAbstract = No
}

one sig LibraryDbId extends Integer{}
one sig ListOFBooks extends string{}

one sig User extends Class{}{
attrSet = UserId+UserName
id=UserId
no parent
isAbstract = No
}

one sig UserId extends Integer{}
one sig UserName extends string{}

one sig Account extends Class{}{
attrSet = AccountId+NoBorrowedBooks+NoReservedBooks+NoReturnedBooks+NoLostBooks+FineAmount
id=AccountId
no parent
isAbstract = No
}

one sig AccountId extends Integer{}
one sig NoBorrowedBooks extends Integer{}
one sig NoReservedBooks extends Integer{}
one sig NoReturnedBooks extends Integer{}
one sig NoLostBooks extends Integer{}
one sig FineAmount extends Integer{}

one sig Book extends Class{}{
attrSet = Title+Author+ISBN+Publication
id=ISBN
no parent
isAbstract = No
}

one sig Title extends string{}
one sig Author extends string{}
one sig ISBN extends Integer{}
one sig Publication extends string{}

one sig Student extends Class{}{
attrSet = class
one parent
parent in User
id = UserId
isAbstract = No
}

one sig class extends string{}

one sig Librarian extends Class{}{
attrSet = LibrarianName+LibrarianId+Password+SearchString
id=LibrarianId
no parent
isAbstract = No
}

one sig LibrarianName extends string{}
one sig LibrarianId extends Integer{}
one sig Password extends string{}
one sig SearchString extends string{}

one sig Staff extends Class{}{
attrSet = Dept
one parent
parent in User
id = UserId
isAbstract = No
}

one sig Dept extends string{}

one sig LibraryManagementSystem extends Class{}{
attrSet = LMSId+UserType+UserName+Password
id=LMSId
no parent
isAbstract = No
}

one sig LMSId extends Integer{}
one sig UserType extends string{}

one sig UserLMSAssociation extends Association{}{
src = LibraryManagementSystem
dst= User
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserBookAssociation extends Association{}{
src = User
dst= Book
src_multiplicity = MANY
dst_multiplicity = MANY
}

one sig LMSAccountAssociation extends Association{}{
src = LibraryManagementSystem
dst= Account
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig LMSBookAssociation extends Association{}{
src = LibraryManagementSystem
dst= Book
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig LMSLibrarianAssociation extends Association{}{
src = LibraryManagementSystem
dst= Librarian
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig LibrarianLibraryDbAssociation extends Association{}{
src = Librarian
dst= LibraryDatabase
src_multiplicity = ONE
dst_multiplicity = ONE
}

one sig LibrarianBookAssociation extends Association{}{
src = Librarian
dst= Book
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig AccountLibraryDbAssociation extends Association{}{
src = LibraryDatabase
dst= Account
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig BookLibraryDbAssociation extends Association{}{
src = LibraryDatabase
dst= Book
src_multiplicity = ONE
dst_multiplicity = MANY
}

one sig UserAccountAssociation extends Association{}{
src = User
dst= Account
src_multiplicity = ONE
dst_multiplicity = ONE
}

pred show{}
run show for 44
