#Extract Solution Mapping Strategy of Banking Object Model
#Processing the XML files

file_name = "LibraryManagement_Sol_1.sql"
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "LibraryManagement"
om_count = 0

class1_name = "LibraryDatabase"
c1_at1 = "LibraryDbId"
c1_at1_type = "int"
c1_at2 = "ListOFBooks"
c1_at2_type = "varchar"

class2_name = "User"
c2_at1 = "UserId"
c2_at1_type = "int"
c2_at2 = "UserName"
c2_at2_type = "varchar"


class3_name = "Account"
c3_at1 = "AccountId"
c3_at1_type = "int"
c3_at2 = "NoBorrowedBooks"
c3_at2_type = "int"
c3_at3 = "NoReservedBooks"
c3_at3_type = "int"
c3_at4 = "NoReturnedBooks"
c3_at4_type = "int"
c3_at5 = "NoLostBooks"
c3_at5_type = "int"
c3_at6 = "FineAmount"
c3_at6_type = "int"


class4_name = "Book"
c4_at1 = "Title"
c4_at1_type = "varchar"
c4_at2 = "Author"
c4_at2_type = "varchar"
c4_at3 = "ISBN"
c4_at3_type = "int"
c4_at4 = "Publication"
c4_at4_type = "varchar"


class5_name = "Student"
c5_at1 = "class"
c5_at1_type = "longblob"


class6_name = "Librarian"
c6_at1 = "LibrarianName"
c6_at1_type = "varchar"
c6_at2 = "LibrarianId"
c6_at2_type = "int"
c6_at3 = "Password"
c6_at3_type = "varchar"
c6_at4 = "SearchString"
c6_at4_type = "varchar"


class7_name = "Staff"
c7_at1 = "Dept"
c7_at1_type = "varchar"
#c6_at2 = "categoryName"
#c6_at2_type = "varchar"


class8_name = "LibraryManagementSystem"
c8_at1 = "LMSId"
c8_at1_type = "int"
c8_at2 = "UserType"
c8_at2_type = "varchar"


assoc1 = "UserLMSAssociation"
assoc2 = "UserBookAssociation"
assoc3 = "LMSAccountAssociation"
assoc4 = "LMSBookAssociation"
assoc5 = "LMSLibrarianAssociation"
assoc6 = "LibrarianLibraryDbAssociation"
assoc7 = "LibrarianBookAssociation"
assoc8 = "AccountLibraryDbAssociation"
assoc9 = "BookLibraryDbAssociation"
assoc10 = "UserAccountAssociation"

src_mlpc = "ONE"
src_mlpc2 = "MANY"
dst_mlpc = "MANY"
dst_mlpc2 = "ONE"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"

assoc_str1 = "ForeignKeyEmbeddingStrategy"
assoc_str2 = "OwnAssociationTableStrategy"

#--------------------------------
OM_name_0 = "OM_name"
#om_count = 0

class1_name_0 = "class1_name"
c1_at1_0 = "c1_at1"
c1_at1_type_0 = "c1_at1_type"
c1_at2_0 = "c1_at2"
c1_at2_type_0 = "c1_at2_type"

class2_name_0 = "class2_name"
c2_at1_0 = "c2_at1"
c2_at1_type_0 = "c2_at1_type"
c2_at2_0 = "c2_at2"
c2_at2_type_0 = "c2_at2_type"


class3_name_0 = "class3_name"
c3_at1_0 = "c3_at1"
c3_at1_type_0 = "c3_at1_type"
c3_at2_0 = "c3_at2"
c3_at2_type_0 = "c3_at2_type"
c3_at3_0 = "c3_at3"
c3_at3_type_0 = "c3_at3_type"
c3_at4_0 = "c3_at4"
c3_at4_type_0 = "c3_at4_type"
c3_at5_0 = "c3_at5"
c3_at5_type_0 = "c3_at5_type"
c3_at6_0 = "c3_at6"
c3_at6_type_0 = "c3_at6_type"


class4_name_0 = "class4_name"
c4_at1_0 = "c4_at1"
c4_at1_type_0 = "c4_at1_type"
c4_at2_0 = "c4_at2"
c4_at2_type_0 = "c4_at2_type"
c4_at3_0 = "c4_at3"
c4_at3_type_0 = "c4_at3_type"
c4_at4_0 = "c4_at4"
c4_at4_type_0 = "c4_at4_type"




class5_name_0 = "class5_name"
c5_at1_0 = "c5_at1"
c5_at1_type_0 = "c5_at1_type"



class6_name_0 = "class6_name"
c6_at1_0 = "c6_at1_0"
c6_at1_type_0 = "c6_at1_type"
c6_at2_0 = "c6_at2"
c6_at2_type_0 = "c6_at2_type"
c6_at3_0 = "c6_at3"
c6_at3_type_0 = "c6_at3_type"
c6_at4_0 = "c6_at4"
c6_at4_type_0 = "c6_at4_type"



class7_name_0 = "class7_name"
c7_at1_0 = "c7_at1"
c7_at1_type_0 = "c7_at1_type"
#c6_at2 = "categoryName"
#c6_at2_type = "varchar"



class8_name_0 = "class8_name"
c8_at1_0 = "c8_at1"
c8_at1_type_0 = "c8_at1_type"
c8_at2_0 = "c8_at2"
c8_at2_type_0 = "c8_at2_type"



assoc1_0 = "assoc1"
assoc2_0 = "assoc2"
assoc3_0 = "assoc3"
assoc4_0 = "assoc4"
assoc5_0 = "assoc5"
assoc6_0 = "assoc6"
assoc7_0 = "assoc7"
assoc8_0 = "assoc8"
assoc9_0 = "assoc9"
assoc10_0 = "assoc10"


src_mlpc_0 = "src_mlpc"
src_mlpc2_0 = "src_mlpc2"
dst_mlpc_0 = "dst_mlpc"
dst_mlpc2_0 = "dst_mlpc2"

map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

assoc_str1_0 = "assoc_str1"
assoc_str2_0 = "assoc_str2"


file_object = open(f"LibraryManagement_Solution_Abstract_only_2.txt", 'a')



for j in range(len(mylist)):


#---------------------------------------------------------------------


    if f'USE' in mylist[j]:
        mylist[j] = (f"USE {OM_name_0}:{om_count};")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'CREATE DATABASE FOR' in mylist[j]:
        mylist[j] = (f"")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'Table structure for' in mylist[j]:
        mylist[j] = (f"")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("")

 #-------------------------------------------------------------------------


    if f'CREATE TABLE `{class3_name}` (' in mylist[j]:
        mylist[j] = (f"CREATE TABLE `{class3_name_0}` (")
        a280 = mylist[j]
        file_object.write(a280)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c8_at1}` {c8_at1_type},' in mylist[j]:
        mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0},")
        a281 = mylist[j]
        file_object.write(a281)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at6}` {c3_at6_type},' in mylist[j]:
        mylist[j] = (f"`{c3_at6_0}` {c3_at6_type_0},")
        a282 = mylist[j]
        file_object.write(a282)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at5}` {c3_at5_type},' in mylist[j]:
        mylist[j] = (f"`{c3_at5_0}` {c3_at5_type_0},")
        a283 = mylist[j]
        file_object.write(a283)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at4}` {c3_at4_type},' in mylist[j]:
        mylist[j] = (f"`{c3_at4_0}` {c3_at4_type_0},")
        a284 = mylist[j]
        file_object.write(a284)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at3}` {c3_at3_type},' in mylist[j]:
        mylist[j] = (f"`{c3_at3_0}` {c3_at3_type_0},")
        a285 = mylist[j]
        file_object.write(a285)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at2}` {c3_at2_type},' in mylist[j]:
        mylist[j] = (f"`{c3_at2_0}` {c3_at2_type_0},")
        a286 = mylist[j]
        file_object.write(a286)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c3_at1}` {c3_at1_type} NOT NULL,' in mylist[j]:
        mylist[j] = (f"`{c3_at1_0}` {c3_at1_type_0} NOT NULL,")
        a287 = mylist[j]
        file_object.write(a287)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
        mylist[j] = (f"`{c1_at1_0}` {c1_at1_type},")
        a288 = mylist[j]
        file_object.write(a288)
        file_object.write("\n")
        print(mylist[j])
        print("")



    if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
        mylist[j] = (f"`{c1_at1_0}` {c1_at1_type},")
        a289 = mylist[j]
        file_object.write(a289)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'KEY `FK_{class3_name}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
        mylist[j] = (f"KEY `FK_{class3_name_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
        a290 = mylist[j]
        file_object.write(a290)
        file_object.write("\n")
        print(mylist[j])
        print("")



    if f'KEY `FK_{class3_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
        mylist[j] = (f"KEY `FK_{class3_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
        a291 = mylist[j]
        file_object.write(a291)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:
        mylist[j] = (f"PRIMARY KEY (`{c3_at1_0}`)")
        a292 = mylist[j]
        file_object.write(a292)
        file_object.write("\n")
        print(mylist[j])
        print("")

  #-------------------------------------------------------------------------------


    if f'CREATE TABLE `{class1_name}` (' in mylist[j]:
        mylist[j] = (f"CREATE TABLE `{class1_name_0}` (")
        a293 = mylist[j]
        file_object.write(a293)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c1_at2}` {c1_at2_type}(64),' in mylist[j]:
        mylist[j] = (f"`{c1_at2_0}` {c1_at2_type_0}(64),")
        a294 = mylist[j]
        file_object.write(a294)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c1_at1}` {c1_at1_type} NOT NULL,' in mylist[j]:
        mylist[j] = (f"`{c1_at1_0}` {c1_at1_type_0} NOT NULL,")
        a295 = mylist[j]
        file_object.write(a295)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'PRIMARY KEY (`{c1_at1}`)' in mylist[j]:
        mylist[j] = (f"PRIMARY KEY (`{c1_at1_0}`)")
        a296 = mylist[j]
        file_object.write(a296)
        file_object.write("\n")
        print(mylist[j])
        print("")


   #----------------------------------------------------------------


    if f'CREATE TABLE `{class2_name}` (' in mylist[j]:
        mylist[j] = (f"CREATE TABLE `{class2_name_0}` (")
        a297 = mylist[j]
        file_object.write(a297)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c2_at2}` {c2_at2_type}(64),' in mylist[j]:
        mylist[j] = (f"`{c2_at2_0}` {c2_at2_type_0}(64),")
        a298 = mylist[j]
        file_object.write(a298)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'`{c8_at1}` {c8_at1_type},' in mylist[j]:
        mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0},")
        a299 = mylist[j]
        file_object.write(a299)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
        mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
        a300 = mylist[j]
        file_object.write(a300)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'KEY `FK_{class2_name}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
        mylist[j] = (f"KEY `FK_{class2_name_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
        a301 = mylist[j]
        file_object.write(a301)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
        mylist[j] = (f"PRIMARY KEY (`{c2_at1_0}`)")
        a302 = mylist[j]
        file_object.write(a302)
        file_object.write("\n")
        print(mylist[j])
        print("")


#---------------------------------------------------------



    if f'CREATE TABLE `{class7_name}` (' in mylist[j]:
        mylist[j] = (f"CREATE TABLE `{class7_name_0}` (")
        a303 = mylist[j]
        file_object.write(a303)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c7_at1}` {c7_at1_type}(64),' in mylist[j]:
        mylist[j] = (f"`{c7_at1_0}` {c7_at1_type_0}(64),")
        a304 = mylist[j]
        file_object.write(a304)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
        mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
        a305 = mylist[j]
        file_object.write(a305)
        file_object.write("\n")
        print(mylist[j])
        print("")



    if f'KEY `FK_{class7_name}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        mylist[j] = (f"KEY `FK_{class7_name_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
        a306 = mylist[j]
        file_object.write(a306)
        file_object.write("\n")
        print(mylist[j])
        print("")

#----------------------------------------------------------------



    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="LibraryManagement/Account"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str1_0}")
        a100 = mylist[j]
        file_object.write(a100)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="LibraryManagement/Account"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str2_0}")
        a100 = mylist[j]
        file_object.write(a100)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="LibraryManagement/Account"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str3_0}")
        a100 = mylist[j]
        file_object.write(a100)
        file_object.write("\n")
        print(mylist[j])
        print("")


#-----------------------------------------------------------------------------




    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="LibraryManagement/User"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str1_0}")
        a101 = mylist[j]
        file_object.write(a101)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="LibraryManagement/User"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str2_0}")
        a101 = mylist[j]
        file_object.write(a101)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="LibraryManagement/User"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str3_0}")
        a101 = mylist[j]
        file_object.write(a101)
        file_object.write("\n")
        print(mylist[j])
        print("")


#--------------------------------------------------------------

#from ecommerce/ElectronicProduct



#---------------------------------------------------------------------

#-------------------------------------------------------------------------- ------------------


#------------------------ ------------------------- -------------------------------- -------------

    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/UserLMSAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str1_0}")
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/UserLMSAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str2_0}")
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n")
        print(mylist[j])
        print("")

        #---------------------------------------------------------------------------

    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/CustomerShippingCartAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str1_0}")
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/CustomerShippingCartAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str2_0}")
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n")
        print(mylist[j])
        print("")

      #-------------------------------------------------------------------------------

    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/LMSAccountAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str1_0}")
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/LMSAccountAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str2_0}")
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")
        print(mylist[j])
        print("")


    #-----------------------------------------------------------------------------

    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/LMSBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str2_0}")
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/LMSBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str1_0}")
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
        print(mylist[j])
        print("")

     #-------------------------------------------------------------------------

    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/LibrarianLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str2_0}")
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/LibrarianLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str1_0}")
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()

  #----------------------------------------------------------------------------

#From ecommerce/ProductCategoryAssociation
#<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductCatalogAssociation"/> </tuple>
#<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductCategoryAssociation"/> </tuple>
#<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductItemAssociation"/> </tuple>
#<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductAssetAssociation"/> </tuple>


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/LMSLibrarianAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str2_0}")
        a36 = mylist[j]
        file_object.write(a36)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/LMSLibrarianAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str1_0}")
        a36 = mylist[j]
        file_object.write(a36)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()


#-----------------------------------------------------------------------------


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/LibrarianBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str2_0}")
        a37 = mylist[j]
        file_object.write(a37)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/LibrarianBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str1_0}")
        a37 = mylist[j]
        file_object.write(a37)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()


#-----------------------------------------------------------------------


    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/AccountLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str2_0}")
        a38 = mylist[j]
        file_object.write(a38)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/AccountLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str1_0}")
        a38 = mylist[j]
        file_object.write(a38)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()



#-----------------------------------------------------------------



    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/BookLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str2_0}")
        a39 = mylist[j]
        file_object.write(a39)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/BookLibraryDbAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str1_0}")
        a39 = mylist[j]
        file_object.write(a39)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()



#-----------------------------------------------------------------------



    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="LibraryManagement/UserBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str2_0}")
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="LibraryManagement/UserBookAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str1_0}")
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")
        print(mylist[j])
        print("")
        #file_object.close()


#ecommerce_Sol_58.xml
#LibraryManagement_Sol_ .xml
