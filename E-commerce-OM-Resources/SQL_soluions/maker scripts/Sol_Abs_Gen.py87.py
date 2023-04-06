
#print(mylist)


file_name = "ecommerce_Sol_301.sql"
file_read = open(file_name, "r")
mylist = file_read.readlines()

# file_name = input("Enter The File's Name: ")
# file_read = open(file_name, "r")
# mylist = file_read.readlines()


OM_name = "ecommerce"
om_count = 0

class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "int"

class01_name = "Order"
c01_at1 = "orderID"
c01_at1_type = "int"


class2_name = "ShippingCart"
c2_at1 = "shippingCartID"
c2_at1_type = "int"


class3_name = "Item"
c3_at1 = "ItemID"
c3_at1_type = "int"
c3_at2 = "quantity"
c3_at2_type = "int"




class4_name = "CartItem"
c4_at1 = "cartItemID"
c4_at1_type = "int"



class5_name = "OrderItem"
c5_at1 = "orderItemID"
c5_at1_type = "int"
c5_at2 = "status"
c5_at2_type = "int"



class6_name = "Category"
c6_at1 = "categoryID"
c6_at1_type = "int"
c6_at2 = "categoryName"
c6_at2_type = "varchar"





class7_name = "Product"
c7_at1 = "productID"
c7_at1_type = "int"
c7_at2 = "productName"
c7_at2_type = "varchar"
c7_at3 = "description"
c7_at3_type = "varchar"
c7_at4 = "price"
c7_at4_type = "decimal"


class8_name = "Catalog"
c8_at1 = "CatalogID"
c8_at1_type = "int"


class9_name = "PhysicalProduct"
c9_at1 = "weight"
c9_at1_type = "decimal"
c9_at2 = "availability"
c9_at2_type = "boolean"



class10_name = "ElectronicProduct"
c10_at1 = "size"
c10_at1_type = "varchar"


class11_name = "Service"
c11_at1 = "schedule"
c11_at1_type = "varchar"

class12_name = "Asset"
c12_at1 = "assetID"
c12_at1_type = "int"
c12_at2 = "assetName"
c12_at2_type = "varchar"
c12_at3 = "fileURI"
c12_at3_type = "varchar"



class13_name = "Media"
c13_at1 = "mediaType"
c13_at1_type = "int"


class14_name = "Documents"
c14_at1 = "excerpt"
c14_at1_type = "varchar"



assoc1 = "CustomerOrderAssociation"
assoc2 = "CustomerShippingCartAssociation"
assoc3 = "ShippingCartItemAssociation"
assoc4 = "OrderItemAssociation"
assoc5 = "ProductCategoryAssociation"
assoc6 = "ProductCatalogAssociation"
assoc7 = "ProductItemAssociation"
assoc8 = "ProductAssetAssociation"


src_mlpc = "ONE"
src_mlpc2 = "MANY"
dst_mlpc = "MANY"
dst_mlpc2 = "ONE"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"

OM_name_0 = "OM_name"
#om_count = 0

class1_name_0 = "class1_name"
c1_at1_0 = "c1_at1"
c1_at1_type_0 = "c1_at1_type"

class01_name_0 = "class01_name"
c01_at1_0 = "c01_at1"
c01_at1_type_0 = "c01_at1_type"


class2_name_0 = "class2_name"
c2_at1_0 = "c2_at1"
c2_at1_type_0 = "c2_at1_type"





class3_name_0 = "class3_name"
c3_at1_0 = "c3_at1"
c3_at1_type_0 = "c3_at1_type"
c3_at2_0 = "c3_at2"
c3_at2_type_0 = "c3_at2_type"




class4_name_0 = "class4_name"
c4_at1_0 = "c4_at1"
c4_at1_type_0 = "c4_at1_type"



class5_name_0 = "class5_name"
c5_at1_0 = "c5_at1"
c5_at1_type_0 = "c5_at1_type"
c5_at2_0 = "c5_at2"
c5_at2_type_0 = "c5_at2_type"




class6_name_0 = "class6_name"
c6_at1_0 = "c6_at1"
c6_at1_type_0 = "c6_at1_type"
c6_at2_0 = "c6_at2"
c6_at2_type_0 = "c6_at2_type"



class7_name_0 = "class7_name"
c7_at1_0 = "c7_at1"
c7_at1_type_0 = "c7_at1_type"
c7_at2_0 = "c7_at2"
c7_at2_type_0 = "c7_at2_type"
c7_at3_0 = "c7_at3"
c7_at3_type_0 = "c7_at3_type"
c7_at4_0 = "c7_at4"
c7_at4_type_0 = "c7_at4_type"



class8_name_0 = "class8_name"
c8_at1_0 = "c8_at1"
c8_at1_type_0 = "c8_at1_type"



class9_name_0 = "class9_name"
c9_at1_0 = "c9_at1"
c9_at1_type_0 = "c9_at1_type"
c9_at2_0 = "c10_at2"
c9_at2_type_0 = "c10_at2_type"


class10_name_0 = "class10_name"
c10_at1_0 = "c10_at1"
c10_at1_type_0 = "c10_at1_type"



class11_name_0 = "class11_name"
c11_at1_0 = "c11_at1"
c11_at1_type_0 = "c11_at1_type"

class12_name_0 = "class12_name"
c12_at1_0 = "c12_at1"
c12_at1_type_0 = "c12_at1_type"
c12_at2_0 = "c12_at2"
c12_at2_type_0 = "c12_at2_type"
c12_at3_0 = "c12_at3"
c12_at3_type_0 = "c12_at3_type"



class13_name_0 = "class13_name"
c13_at1_0 = "c13_at1"
c13_at1_type_0 = "c13_at1_type"


class14_name_0 = "class14_name"
c14_at1_0 = "c14_at1"
c14_at1_type_0 = "c14_at1_type"




assoc1_0 = "assoc1"
assoc2_0 = "assoc2"
assoc3_0 = "assoc3"
assoc4_0 = "assoc4"
assoc5_0 = "assoc5"
assoc6_0 = "assoc6"
assoc7_0 = "assoc7"
assoc8_0 = "assoc8"


src_mlpc_0 = "src_mlpc"
dst_mlpc_0 = "dst_mlpc"
src_mlpc2_0 = "src_mlpc2"
dst_mlpc2_0 = "dst_mlpc2"


map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

file_object = open(f'sol_301.txt', 'a')


for j in range(len(mylist)):


    if f"Table structure for" in mylist[j]:
        mylist[j] = (f"")
        a00 = mylist[j]
        file_object.write(a00)
        file_object.write("\n")



    if f"CREATE DATABASE FOR" in mylist[j]:
        mylist[j] = (f"")
        a000 = mylist[j]
        file_object.write(a000)
        file_object.write("\n")


    if f"--" in mylist[j]:
        mylist[j] = (f"")
        a0000 = mylist[j]
        file_object.write(a0000)
        file_object.write("\n")



    if f"USE {OM_name}" in mylist[j]:
        mylist[j] = (f"USE {OM_name_0}_{om_count}")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        om_count += 1


    #--------------------------------------------------------------------

    if f'CREATE TABLE `{class01_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class01_name_0}` (')
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")


    if f'`{c01_at1}` {c01_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f"`{c01_at1_0}` {c01_at1_type_0} NOT NULL,")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")

    if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0},')
        a3 = mylist[j]
        file_object.write(a3)
        file_object.write("\n")



    if f'KEY `FK_{class01_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class01_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c01_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c01_at1_0}`),')
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")


#-----------------------------------------------------------------------------------


#--------------------------------------------------------------------

    if f'CREATE TABLE `{class6_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class6_name_0}` (')
        a8 = mylist[j]
        file_object.write(a8)
        file_object.write("\n")


    if f'`{c6_at2}` {c6_at2_type}(64),' in mylist[j]:

        mylist[j] = (f"`{c7_at1_0}` {c7_at1_type_0}(64)")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")

    if f'`{c6_at1}` {c6_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c6_at1_0}` {c6_at1_type_0} NOT NULL')
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c6_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c6_at1_0}`),')
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")


  #-----------------------------------------------------------------------------------
    if f'CREATE TABLE `{class1_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class1_name_0}` (')
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")


    if f'`{c1_at1}` {c1_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f"`{c1_at1_0}` {c1_at1_type_0} NOT NULL")
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")

    if f'PRIMARY KEY (`{c1_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c1_at1_0}`),')
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")


 #--------------------------------------------------------------

    if f'CREATE TABLE `{class13_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class13_name_0}` (')
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")


    if f'`{c13_at1}` {c13_at1_type},' in mylist[j]:

        mylist[j] = (f"`{c13_at1_0}` {c13_at1_type_0}(64)")
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")

    if f'`{c12_at1}` {c12_at1_type} NOT NULL' in mylist[j]:

        mylist[j] = (f'`{c12_at1_0}` {c12_at1_type_0} NOT NULL')
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")



    if f'KEY `FK_{class13_name}_{c12_at1}_idx` (`{c12_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class13_name_0}_{c12_at1_0}_idx` (`{c12_at1_0}`)')
        a023 = mylist[j]
        file_object.write(a023)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c13_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c13_at1_0}`),')
        a24 = mylist[j]
        file_object.write(a24)
        file_object.write("\n")

#----------------------------------------------------------------


 #----------------------------------------------------------


    if f'CREATE TABLE `{class7_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class7_name_0}` (')
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")


    if f'`{c7_at3}` {c7_at3_type}(64),' in mylist[j]:

        mylist[j] = (f"`{c7_at3_0}` {c7_at3_type_0}(64)")
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")

    if f'`{c7_at2}` {c7_at2_type}(64),' in mylist[j]:

        mylist[j] = (f'`{c7_at2_0}` {c7_at2_type_0}')
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")


    if f'`{c7_at4}` {c7_at4_type}(20,5),' in mylist[j]:

        mylist[j] = (f'`{c7_at4_0}` {c7_at4_type_0}(20,5)')
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")


    if f'`{c7_at1}` {c7_at1_type} NOT NULL' in mylist[j]:

        mylist[j] = (f'`{c7_at1_0}` {c7_at1_type_0} NOT NULL')
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c7_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c7_at1_0}`),')
        a30 = mylist[j]
        file_object.write(a30)
        file_object.write("\n")






 #------------------------------------------------------------

    if f'CREATE TABLE `{class11_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class11_name_0}` (')
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")


    if f'`{c11_at1}` {c11_at1_type}(64),' in mylist[j]:

        mylist[j] = (f"`{c11_at1_0}` {c11_at1_type_0}(64)")
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")



    if f'KEY `FK_{class11_name}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class11_name_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a035 = mylist[j]
        file_object.write(a035)
        file_object.write("\n")





#------------------------------------------------------------------------

    if f'CREATE TABLE `{class4_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class4_name_0}` (')
        a37 = mylist[j]
        file_object.write(a37)
        file_object.write("\n")



    if f'`{c4_at1}` {c4_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c4_at1_0}` {c4_at1_type_0},')
        a037 = mylist[j]
        file_object.write(a037)
        file_object.write("\n")


    if f'`{c3_at1}` {c3_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f"`{c3_at1_0}` {c3_at1_type_0} NOT NULL")
        a38 = mylist[j]
        file_object.write(a38)
        file_object.write("\n")

    if f'KEY `FK_{class4_name}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class4_name_0}_{c3_at1_0}_idx` (`{c3_at1_0}`),')
        a39 = mylist[j]
        file_object.write(a39)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c3_at1}`),')
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")



 #Table shipping cart from here
#-------------------------------------------------------------------


    if f'CREATE TABLE `{class2_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class2_name_0}` (')
        a37 = mylist[j]
        file_object.write(a37)
        file_object.write("\n")




    if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c2_at1_0}` {c2_at1_type_0} NOT NULL')
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")




    if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0},')
        a140 = mylist[j]
        file_object.write(a140)
        file_object.write("\n")






    if f'KEY `FK_{class2_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class2_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a141 = mylist[j]
        file_object.write(a141)
        file_object.write("\n")







    if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c2_at1_0}`),')
        a142 = mylist[j]
        file_object.write(a142)
        file_object.write("\n")

#------------------------------------------------------------------------

    if f'CREATE TABLE `{class8_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class8_name_0}` (')
        a143 = mylist[j]
        file_object.write(a143)
        file_object.write("\n")


    if f'`{c7_at1}` {c7_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c7_at1_0}` {c7_at1_type_0}')
        a0143 = mylist[j]
        file_object.write(a0143)
        file_object.write("\n")


    if f'`{c8_at1}` {c8_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c8_at1_0}` {c8_at1_type_0} NOT NULL')
        a144 = mylist[j]
        file_object.write(a144)
        file_object.write("\n")




    if f'KEY `FK_{class8_name}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class8_name_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a145 = mylist[j]
        file_object.write(a145)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c8_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c8_at1_0}`),')
        a145 = mylist[j]
        file_object.write(a145)
        file_object.write("\n")




#-------------------------------------------------------------------------



    if f'CREATE TABLE `{assoc7}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc7_0}` (')
        a146 = mylist[j]
        file_object.write(a146)
        file_object.write("\n")


    if f'`{c3_at1}` {c3_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c3_at1_0}` {c3_at1_type_0} NOT NULL')
        a147 = mylist[j]
        file_object.write(a147)
        file_object.write("\n")




    if f'KEY `FK_{assoc7}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc7_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a148 = mylist[j]
        file_object.write(a148)
        file_object.write("\n")


    if f'KEY `FK_{assoc7}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc7_0}_{c3_at1_0}_idx` (`{c3_at1_0}`)')
        a149 = mylist[j]
        file_object.write(a149)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c7_at1}`,`{c3_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c7_at1_0}`,`{c3_at1_0}`),')
        a150 = mylist[j]
        file_object.write(a150)
        file_object.write("\n")


#----------------------------------------------------------------------------
#From table item

    if f'CREATE TABLE `{class3_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class3_name_0}` (')
        a151 = mylist[j]
        file_object.write(a151)
        file_object.write("\n")

    if f'`{c3_at2}` {c3_at2_type},' in mylist[j]:

        mylist[j] = (f'`{c3_at2_0}` {c3_at2_type_0}')
        a152 = mylist[j]
        file_object.write(a152)
        file_object.write("\n")



    if f'`{c2_at1}` {c2_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c2_at1_0}` {c2_at1_type_0}')
        a153 = mylist[j]
        file_object.write(a153)
        file_object.write("\n")



    if f'`{c01_at1}` {c01_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c01_at1_0}` {c01_at1_type_0}')
        a154 = mylist[j]
        file_object.write(a154)
        file_object.write("\n")







    if f'KEY `FK_{class3_name}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class3_name_0}_{c2_at1_0}_idx` (`{c2_at1_0}`)')
        a155 = mylist[j]
        file_object.write(a155)
        file_object.write("\n")


    if f'KEY `FK_{class3_name}_{c01_at1}_idx` (`{c01_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class3_name_0}_{c01_at1_0}_idx` (`{c01_at1_0}`)')
        a156 = mylist[j]
        file_object.write(a156)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c3_at1_0}`),')
        a157 = mylist[j]
        file_object.write(a157)
        file_object.write("\n")


#--------------------------------------------- --------------------------- ------------------


#from table ElectronicProduct

    if f'CREATE TABLE `{class10_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class10_name_0}` (')
        a158 = mylist[j]
        file_object.write(a158)
        file_object.write("\n")

    if f'`{c10_at1}` {c10_at1_type}(64),' in mylist[j]:

        mylist[j] = (f'`{c10_at1_0}` {c10_at1_type_0}(64)')
        a159 = mylist[j]
        file_object.write(a159)
        file_object.write("\n")





    if f'KEY `FK_{class10_name}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class10_name_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a160 = mylist[j]
        file_object.write(a160)
        file_object.write("\n")



    if f'PRIMARY KEY (`{c7_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c7_at1_0}`),')
        a161 = mylist[j]
        file_object.write(a161)
        file_object.write("\n")



#---------------------------------------------------------------------------------- ------------ ---------------



    if f'CREATE TABLE `{class9_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class9_name_0}` (')
        a162 = mylist[j]
        file_object.write(a162)
        file_object.write("\n")

    if f'`{c9_at2}` {c9_at2_type},' in mylist[j]:

        mylist[j] = (f'`{c9_at2_0}` {c9_at2_type_0},')
        a163 = mylist[j]
        file_object.write(a163)
        file_object.write("\n")

    if f'`{c9_at1}` {c9_at1_type}(20,5),' in mylist[j]:

        mylist[j] = (f'`{c9_at1_0}` {c9_at1_type_0}(20,5),')
        a164 = mylist[j]
        file_object.write(a164)
        file_object.write("\n")



    if f'KEY `FK_{class9_name}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class9_name_0}_{c7_at1_0}_idx` (`{c7_at1_0}`),')
        a165 = mylist[j]
        file_object.write(a165)
        file_object.write("\n")




#------------------------------------------------------------------------- --------------------- -------------



    if f'CREATE TABLE `{class5_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class5_name_0}` (')
        a166 = mylist[j]
        file_object.write(a166)
        file_object.write("\n")

    if f'`{c5_at1}` {c5_at1_type},' in mylist[j]:

        mylist[j] = (f'`{c5_at1_0}` {c5_at1_type_0},')
        a167 = mylist[j]
        file_object.write(a167)
        file_object.write("\n")

    if f'`{c5_at2}` {c5_at2_type},' in mylist[j]:

        mylist[j] = (f'`{c5_at2_0}` {c5_at2_type_0},')
        a168 = mylist[j]
        file_object.write(a168)
        file_object.write("\n")



    if f'KEY `FK_{class5_name}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class5_name_0}_{c3_at1_0}_idx` (`{c3_at1_0}`)')
        a169 = mylist[j]
        file_object.write(a169)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c3_at1_0}`),')
        a170 = mylist[j]
        file_object.write(a170)
        file_object.write("\n")




#------------------------------------------------------------ ------------------------------- -----------------

    if f'CREATE TABLE `{assoc8}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc8_0}` (')
        a171 = mylist[j]
        file_object.write(a171)
        file_object.write("\n")





    if f'`{c12_at1}` {c12_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c12_at1}` {c12_at1_type} NOT NULL')
        a172 = mylist[j]
        file_object.write(a172)
        file_object.write("\n")





    if f'KEY `FK_{assoc8}_{c12_at1}_idx` (`{c12_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc8_0}_{c12_at1_0}_idx` (`{c12_at1_0}`)')
        a173 = mylist[j]
        file_object.write(a173)
        file_object.write("\n")


    if f'KEY `FK_{assoc8}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc8_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a174 = mylist[j]
        file_object.write(a174)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c12_at1}`,`{c7_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c12_at1_0}`,`{c7_at1_0}`),')
        a175 = mylist[j]
        file_object.write(a175)
        file_object.write("\n")



#------------------------ ------------------------------- ---------------------------- --------------------------

    if f'CREATE TABLE `{class14_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class14_name_0}` (')
        a176 = mylist[j]
        file_object.write(a176)
        file_object.write("\n")


    if f'`{c14_at1}` {c14_at1_type}(64),' in mylist[j]:

        mylist[j] = (f'`{c14_at1_0}` {c14_at1_type_0}(64)')
        a177 = mylist[j]
        file_object.write(a177)
        file_object.write("\n")


    if f'KEY `FK_{class14_name}_{c12_at1}_idx` (`{c12_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{class14_name_0}_{c12_at1_0}_idx` (`{c12_at1_0}`)')
        a178 = mylist[j]
        file_object.write(a178)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c12_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c12_at1_0}`),')
        a179 = mylist[j]
        file_object.write(a179)
        file_object.write("\n")


#---------------------------- -------------------------------- --------------------- ----------------------- ------



    if f'CREATE TABLE `{class12_name}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{class12_name_0}` (')
        a180 = mylist[j]
        file_object.write(a180)
        file_object.write("\n")


    if f'`{c12_at3}` {c12_at3_type}(64),' in mylist[j]:

        mylist[j] = (f'`{c12_at3_0}` {c12_at3_type_0}(64)')
        a181 = mylist[j]
        file_object.write(a181)
        file_object.write("\n")


    if f'`{c12_at2}` {c12_at2_type}(64),' in mylist[j]:

        mylist[j] = (f'`{c12_at2_0}` {c12_at2_type_0}(64)')
        a182 = mylist[j]
        file_object.write(a182)
        file_object.write("\n")



    if f'`{c12_at1}` {c12_at1_type} NOT NULL,' in mylist[j]:

        mylist[j] = (f'`{c12_at1_0}` {c12_at1_type_0} NOT NULL')
        a183 = mylist[j]
        file_object.write(a183)
        file_object.write("\n")



    if f'PRIMARY KEY (`{c12_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c12_at1_0}`),')
        a184 = mylist[j]
        file_object.write(a184)
        file_object.write("\n")


#--------------------------------- ------------------------------------------ ------------------------ -------

    if f'CREATE TABLE `{assoc5}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc5_0}` (')
        a185 = mylist[j]
        file_object.write(a185)
        file_object.write("\n")



    if f'KEY `FK_{assoc5}_{c7_at1}_idx` (`{c7_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc5_0}_{c7_at1_0}_idx` (`{c7_at1_0}`)')
        a186 = mylist[j]
        file_object.write(a186)
        file_object.write("\n")



    if f'KEY `FK_{assoc5}_{c6_at1}_idx` (`{c6_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc5_0}_{c6_at1_0}_idx` (`{c6_at1_0}`)')
        a187 = mylist[j]
        file_object.write(a187)
        file_object.write("\n")



    if f'PRIMARY KEY (`{c7_at1}`,`{c6_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c7_at1_0}`,`{c6_at1_0}`),')
        a188 = mylist[j]
        file_object.write(a188)
        file_object.write("\n")




#-------------------- ---------------------------- --------------------------------------- -------------------------

    if f'ALTER TABLE `{class01_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class01_name_0}`')
        a189 = mylist[j]
        file_object.write(a189)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class01_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class01_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a190 = mylist[j]
        file_object.write(a190)
        file_object.write("\n")



    if f'ALTER TABLE `{class13_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class13_name_0}`')
        a191 = mylist[j]
        file_object.write(a191)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class13_name}_{c12_at1}` FOREIGN KEY (`{c12_at1}`) REFERENCES `{class12_name}` (`{c12_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class13_name_0}_{c12_at1_0}` FOREIGN KEY (`{c12_at1_0}`) REFERENCES `{class12_name_0}` (`{c12_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a192 = mylist[j]
        file_object.write(a192)
        file_object.write("\n")




    if f'ALTER TABLE `{class11_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class11_name_0}`')
        a193 = mylist[j]
        file_object.write(a193)
        file_object.write("\n")





    if f'ADD CONSTRAINT `FK_{class11_name}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class11_name_0}_{c7_at1_0}` FOREIGN KEY (`{c12_at1_0}`) REFERENCES `{class12_name_0}` (`{c12_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a194 = mylist[j]
        file_object.write(a194)
        file_object.write("\n")

        #from alter table cart item





#----------------------------------------------------------------------------
    if f'ALTER TABLE `{class4_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class4_name_0}`')
        a195 = mylist[j]
        file_object.write(a195)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class4_name}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class4_name_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a196 = mylist[j]
        file_object.write(a196)
        file_object.write("\n")


#-----------------------------------------------------------------------------
    if f'ALTER TABLE `{class2_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class2_name_0}`')
        a197 = mylist[j]
        file_object.write(a197)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class2_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class2_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a198 = mylist[j]
        file_object.write(a198)
        file_object.write("\n")

#-------------------------------------------------------------------------------

    if f'ALTER TABLE `{class8_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class8_name_0}`')
        a199 = mylist[j]
        file_object.write(a199)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class8_name}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class8_name_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a200 = mylist[j]
        file_object.write(a200)
        file_object.write("\n")



#---------------------------------------------------------------------------------

    if f'ALTER TABLE `{assoc7}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc7_0}`')
        a201 = mylist[j]
        file_object.write(a201)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{assoc7}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc7_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a202 = mylist[j]
        file_object.write(a202)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{assoc7}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc7_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a203 = mylist[j]
        file_object.write(a203)
        file_object.write("\n")


#-----------------------------------------------------------------------------

  #from table item


    if f'ALTER TABLE `{class3_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class3_name_0}`')
        a204 = mylist[j]
        file_object.write(a204)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class3_name}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class3_name_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a205 = mylist[j]
        file_object.write(a205)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class3_name}_{c01_at1}` FOREIGN KEY (`{c01_at1}`) REFERENCES `{class01_name}` (`{c01_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class3_name_0}_{c01_at1_0}` FOREIGN KEY (`{c01_at1_0}`) REFERENCES `{class01_name_0}` (`{c01_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a206 = mylist[j]
        file_object.write(a206)
        file_object.write("\n")

#------------------------------------------ ------------------------------------ ----------------



    if f'ALTER TABLE `{class10_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class10_name_0}`')
        a207 = mylist[j]
        file_object.write(a207)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{class10_name}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class10_name_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a208 = mylist[j]
        file_object.write(a208)
        file_object.write("\n")


   #----------------------------------------------- ---------------------------- ------------------------------


    if f'ALTER TABLE `{class9_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class9_name_0}`')
        a209 = mylist[j]
        file_object.write(a209)
        file_object.write("\n")





    if f'ADD CONSTRAINT `FK_{class9_name}_{c7_at1}` FOREIGN KEY (`productID`) REFERENCES `Product` (`productID`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{class10_name_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a210 = mylist[j]
        file_object.write(a210)
        file_object.write("\n")

#---------------------------------------- ------------------------------------------- ----------------------


    if f'ALTER TABLE `{class5_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class5_name_0}`')
        a211 = mylist[j]
        file_object.write(a211)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{class5_name}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{class5_name_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a212 = mylist[j]
        file_object.write(a212)
        file_object.write("\n")


#--------------- -------------------------------- ----------------- ------------ ------ ---------- ----- -----

    if f'ALTER TABLE `{assoc8}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc8_0}`')
        a213 = mylist[j]
        file_object.write(a213)
        file_object.write("\n")





    if f'ADD CONSTRAINT `FK_{assoc8}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{assoc8_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a214 = mylist[j]
        file_object.write(a214)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{assoc8}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{assoc8_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a215 = mylist[j]
        file_object.write(a215)
        file_object.write("\n")

#------------------ -------------- ----------------------- ------------------------ -----------------  -------

    if f'ALTER TABLE `{class14_name}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{class14_name_0}`')
        a216 = mylist[j]
        file_object.write(a216)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{class14_name}_{c12_at1}` FOREIGN KEY (`{c12_at1}`) REFERENCES `{class12_name}` (`{c12_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{class14_name_0}_{c12_at1_0}` FOREIGN KEY (`{c12_at1_0}`) REFERENCES `{class12_name_0}` (`{c12_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a217 = mylist[j]
        file_object.write(a217)
        file_object.write("\n")

#------------------------------------------- ----------------------------- ---------------------------- ------------
    if f'ALTER TABLE `{assoc5}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc5_0}`')
        a218 = mylist[j]
        file_object.write(a218)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{assoc5}_{c7_at1}` FOREIGN KEY (`{c7_at1}`) REFERENCES `{class7_name}` (`{c7_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc5_0}_{c7_at1_0}` FOREIGN KEY (`{c7_at1_0}`) REFERENCES `{class7_name_0}` (`{c7_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a219 = mylist[j]
        file_object.write(a219)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{assoc5}_{c6_at1}` FOREIGN KEY (`{c6_at1}`) REFERENCES `{class6_name}` (`{c6_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{assoc5_0}_{c6_at1_0}` FOREIGN KEY (`{c6_at1_0}`) REFERENCES `{class6_name_0}` (`{c6_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a220 = mylist[j]
        file_object.write(a220)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{assoc8}_{c12_at1}` FOREIGN KEY (`{c12_at1}`) REFERENCES `{class12_name}` (`{c12_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT FK_{assoc5_0}_{c6_at1_0}` FOREIGN KEY (`{c6_at1_0}`) REFERENCES `{class6_name_0}` (`{c6_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a220 = mylist[j]
        file_object.write(a220)
        file_object.write("\n")


    if f'CREATE TABLE `{assoc1}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc1_0}` (')
        a221 = mylist[j]
        file_object.write(a221)
        file_object.write("\n")


    if f'KEY `FK_{assoc1}_{c01_at1}_idx` (`{c01_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc1_0}_{c01_at1_0}_idx` (`{c01_at1_0}`),')
        a222 = mylist[j]
        file_object.write(a222)
        file_object.write("\n")



    if f'KEY `FK_{assoc1}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc1_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a223 = mylist[j]
        file_object.write(a223)
        file_object.write("\n")


    if f'PRIMARY KEY (`{c01_at1}`,`{c1_at1}`)' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc1_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a224 = mylist[j]
        file_object.write(a224)
        file_object.write("\n")







    if f'CREATE TABLE `{assoc2}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc2_0}` (')
        a225 = mylist[j]
        file_object.write(a225)
        file_object.write("\n")


    if f'KEY `FK_{assoc2}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc2_0}_{c2_at1_0}_idx` (`{c2_at1_0}`)')
        a226 = mylist[j]
        file_object.write(a226)
        file_object.write("\n")



    #KEY `FK_CustomerShippingCartAssociation_customerID_idx` (`customerID`),


    if f'KEY `FK_{assoc2}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc2_0}_{c1_at1_0}_idx` (`{c1_at1_0}`)')
        a227 = mylist[j]
        file_object.write(a227)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c2_at1}`,`{c1_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c2_at1_0}`,`{c1_at1_0}`)')
        a228 = mylist[j]
        file_object.write(a228)
        file_object.write("\n")





    if f'CREATE TABLE `{assoc4}` (' in mylist[j]:

        mylist[j] = (f'CREATE TABLE `{assoc4_0}` ()')
        a229 = mylist[j]
        file_object.write(a229)
        file_object.write("\n")

    if f'KEY `FK_{assoc4}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc4_0}_{c3_at1_0}_idx` (`{c3_at1_0}`)')
        a230 = mylist[j]
        file_object.write(a230)
        file_object.write("\n")



    if f'KEY `FK_{assoc4}_{c01_at1}_idx` (`{c01_at1}`),' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc4_0}_{c01_at1_0}D_idx` (`{c01_at1_0}`)')
        a230 = mylist[j]
        file_object.write(a230)
        file_object.write("\n")




    if f'PRIMARY KEY (`{c3_at1}`,`{c01_at1}`)' in mylist[j]:

        mylist[j] = (f'PRIMARY KEY (`{c3_at1_0}`,`{c01_at1_0}`)')
        a231 = mylist[j]
        file_object.write(a231)
        file_object.write("\n")


    if f'ALTER TABLE `{assoc1}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc1_0}`')
        a232 = mylist[j]
        file_object.write(a232)
        file_object.write("\n")



    if f'ADD CONSTRAINT `FK_{assoc1}_{c01_at1}` FOREIGN KEY (`{c01_at1}`) REFERENCES `{class01_name}` (`{c01_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c01_at1_0}` FOREIGN KEY (`{c01_at1_0}`) REFERENCES `{class01_name_0}` (`{c01_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a233 = mylist[j]
        file_object.write(a233)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{assoc1}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a234 = mylist[j]
        file_object.write(a234)
        file_object.write("\n")




    if f'ALTER TABLE `{assoc2}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc2_0}`')
        a235 = mylist[j]
        file_object.write(a235)
        file_object.write("\n")






    if f'ADD CONSTRAINT `FK_{assoc2}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc2_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a236 = mylist[j]
        file_object.write(a236)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{assoc2}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc2_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a237 = mylist[j]
        file_object.write(a237)
        file_object.write("\n")



    if f'ALTER TABLE `{assoc4}`' in mylist[j]:

        mylist[j] = (f'ALTER TABLE `{assoc4_0}`')
        a238 = mylist[j]
        file_object.write(a238)
        file_object.write("\n")




    if f'ADD CONSTRAINT `FK_{assoc4}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc4_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a239 = mylist[j]
        file_object.write(a239)
        file_object.write("\n")


    if f'ADD CONSTRAINT `FK_{assoc4}_{c01_at1}` FOREIGN KEY (`{c01_at1}`) REFERENCES `{class01_name}` (`{c01_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc4_0}_{c01_at1_0}` FOREIGN KEY (`{c01_at1_0}`) REFERENCES `{class01_name_0}` (`{c01_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a240 = mylist[j]
        file_object.write(a240)
        file_object.write("\n")



#---------------------------------------------- --------------------------------------- ---------------------- ---



#------------------------------------------------- -----------------------------------------------------

        #file_object.close()




# no need to use replace if you're going to change the whole varchar


#print(mylist)

for  x in range(len(mylist)) :

    print(mylist[x])
    x += 1
    #ecommerce_Sol_ .sql
