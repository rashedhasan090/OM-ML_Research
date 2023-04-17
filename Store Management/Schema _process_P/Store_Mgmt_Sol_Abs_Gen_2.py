
import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Store Management/Schema _process_P'):
    for file in files:
        #each file

        filename, extension = os.path.splitext(file)
        if extension == '.sql':
            i +=1
            # a = file
            # print(a)
            print(file)
            file_read = open(file, 'r')
            mylist = file_read.readlines()
            OM_name = "Store"
            om_count = 0

            class1_name = "StoreDatabase"
            c1_at1 = "StoreDbId"
            c1_at1_type = "Integer"
            c1_at2 = "ListOFStocks"
            c1_at2_type = "string"

            class2_name = "User"
            c2_at1 = "UserId"
            c2_at1_type = "Integer"
            c2_at2 = "UserName"
            c2_at2_type = "string"


            class3_name = "Store"
            c3_at1 = "StoreId"
            c3_at1_type = "Integer"
            c3_at2 = "NoSoldProducts"
            c3_at2_type = "Integer"
            c3_at3 = "NoReservedProducts"
            c3_at3_type = "Integer"
            c3_at4 = "StoreType"
            c3_at4_type = "Integer"
            c3_at5 = "StoreName"
            c3_at5_type = "Integer"
            c3_at6 = "TotalAmount"
            c3_at6_type = "Integer"


            class4_name = "Stock"
            c4_at1 = "Type"
            c4_at1_type = "string"
            c4_at2 = "StockItems"
            c4_at2_type = "string"
            c4_at3 = "StockId"
            c4_at3_type = "Integer"
            c4_at4 = "StockDescription"
            c4_at4_type = "string"


            class5_name = "Owner"
            c5_at1 = "ownerName"
            c5_at1_type = "string"


            class6_name = "Customer"
            c6_at1 = "CustomerName"
            c6_at1_type = "string"
            c6_at2 = "CustomerId"
            c6_at2_type = "Integer"
            c6_at3 = "CustomerAddress"
            c6_at3_type = "string"
            c6_at4 = "CustomerPhone"
            c6_at4_type = "string"


            class7_name = "Staff"
            c7_at1 = "Dept"
            c7_at1_type = "string"
            #c6_at2 = "categoryName"
            #c6_at2_type = "string"


            class8_name = "StoreManagementSystem"
            c8_at1 = "TransactionId"
            c8_at1_type = "Integer"
            c8_at2 = "UserType"
            c8_at2_type = "string"


            assoc1 = "UserSMSAssociation"
            assoc2 = "UserStockAssociation"
            assoc3 = "SMSStoreAssociation"
            assoc4 = "SMSStockAssociation"
            assoc5 = "SMSCustomerAssociation"
            assoc6 = "CustomerStoreDbAssociation"
            assoc7 = "CustomerStockAssociation"
            assoc8 = "StoreStoreDbAssociation"
            assoc9 = "StockStoreDbAssociation"
            assoc10 = "UserStoreAssociation"
            # assoc11 = "ProductLibraryDbAssociation"

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
            #c6_at2_type = "string"



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
            assoc11_0 = "assoc11"


            src_mlpc_0 = "src_mlpc"
            src_mlpc2_0 = "src_mlpc2"
            dst_mlpc_0 = "dst_mlpc"
            dst_mlpc2_0 = "dst_mlpc2"

            map_str1_0 = "map_str1"
            map_str2_0 = "map_str2"
            map_str3_0 = "map_str3"

            assoc_str1_0 = "assoc_str1"
            assoc_str2_0 = "assoc_str2"

            file_object = open(file+'.txt', 'a')


            for j in range(len(mylist)):

                if f'module' in mylist[j]:
                    mylist[j] = (f"module {OM_name_0} {om_count};")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
            #
            #


                if f'open Declaration' in mylist[j]:
                    mylist[j] = (f"open Declaration")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
            #




                if f'no parent' in mylist[j]:
                    mylist[j] = (f"no parent")
                    a281 = mylist[j]
                    file_object.write(a281)
                    file_object.write("\n")




                if f'isAbstract = No' in mylist[j]:
                    mylist[j] = (f"isAbstract = No")
                    a282 = mylist[j]
                    file_object.write(a282)
                    file_object.write("\n")



                if f'src_multiplicity = {src_mlpc}' in mylist[j]:
                    mylist[j] = (f"src_multiplicity = {src_mlpc_0}")
                    a0282 = mylist[j]
                    file_object.write(a0282)
                    file_object.write("\n")



                if f'src_multiplicity = {src_mlpc2}' in mylist[j]:
                    mylist[j] = (f"src_multiplicity = {src_mlpc2_0}")
                    a00282 = mylist[j]
                    file_object.write(a00282)
                    file_object.write("\n")


                if f'dst_multiplicity = {dst_mlpc}' in mylist[j]:
                    mylist[j] = (f"dst_multiplicity = {dst_mlpc_0}")
                    a000282 = mylist[j]
                    file_object.write(a000282)
                    file_object.write("\n")


                if f'dst_multiplicity = {dst_mlpc2}' in mylist[j]:
                    mylist[j] = (f"dst_multiplicity = {dst_mlpc2_0}")
                    a0000282 = mylist[j]
                    file_object.write(a0000282)
                    file_object.write("\n")



                if f'pred show' in mylist[j]:
                    mylist[j] = (f"pred show")
                    a027 = mylist[j]
                    file_object.write(a027)
                    file_object.write("\n")



                if f'run show' in mylist[j]:
                    mylist[j] = (f"run show")
                    a028 = mylist[j]
                    file_object.write(a028)
                    file_object.write("\n")



             # #-------------------------------------------------------------------------
            #class1

             #-------------------------------------------------------------------------



                if f'one sig {class1_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class1_name_0} extends Class")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")




                if f'id={c1_at1}' in mylist[j]:
                    mylist[j] = (f"id={c1_at1_0}")
                    a280 = mylist[j]
                    file_object.write(a280)
                    file_object.write("\n")


                if f'attrSet = {c1_at1}+{c1_at2}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c1_at1_0}+{c1_at2_0}")
                    a283 = mylist[j]
                    file_object.write(a283)
                    file_object.write("\n")




                if f'one sig {c1_at1} extends {c1_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c1_at1_0} extends {c1_at1_type_0}")
                    a284 = mylist[j]
                    file_object.write(a284)
                    file_object.write("\n")



                if f'one sig {c1_at2} extends {c1_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c1_at2_0} extends {c1_at2_type_0}")
                    a284 = mylist[j]
                    file_object.write(a284)
                    file_object.write("\n")


            #-------------------------------------------------------------------------



             # #-------------------------------------------------------------------------
            #class2

             #-------------------------------------------------------------------------



                if f'one sig {class2_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class2_name_0} extends Class")
                    a381 = mylist[j]
                    file_object.write(a381)
                    file_object.write("\n")




                if f'id={c2_at1}' in mylist[j]:
                    mylist[j] = (f"id={c2_at1_0}")
                    a382 = mylist[j]
                    file_object.write(a382)
                    file_object.write("\n")


                if f'attrSet = {c2_at1}+{c2_at2}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c2_at1_0}+{c2_at2_0}")
                    a383 = mylist[j]
                    file_object.write(a383)
                    file_object.write("\n")




                if f'one sig {c2_at1} extends {c2_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c2_at1_0} extends {c2_at1_type_0}")
                    a384 = mylist[j]
                    file_object.write(a384)
                    file_object.write("\n")



                if f'one sig {c2_at2} extends {c2_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c2_at1_0} extends {c2_at2_type_0}")
                    a385 = mylist[j]
                    file_object.write(a385)
                    file_object.write("\n")


            #-------------------------------------------------------------------------






             # #-------------------------------------------------------------------------
            #class3

             #-------------------------------------------------------------------------



                if f'one sig {class3_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class3_name_0} extends Class")
                    a386 = mylist[j]
                    file_object.write(a386)
                    file_object.write("\n")



                if f'id={c3_at1}' in mylist[j]:
                    mylist[j] = (f"id={c3_at1_0}")
                    a387 = mylist[j]
                    file_object.write(a387)
                    file_object.write("\n")


                if f'attrSet = {c3_at1}+{c3_at2}+{c3_at3}+{c3_at4}+{c3_at5}+{c3_at6}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c3_at1_0}+{c3_at2_0}+{c3_at3_0}+{c3_at4_0}{c3_at5_0}+{c3_at6_0}")
                    a388 = mylist[j]
                    file_object.write(a388)
                    file_object.write("\n")



                if f'one sig {c3_at1} extends {c3_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at1_0} extends {c3_at1_type_0}")
                    a389 = mylist[j]
                    file_object.write(a389)
                    file_object.write("\n")



                if f'one sig {c3_at2} extends {c3_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at2_0} extends {c3_at2_type_0}")
                    a390 = mylist[j]
                    file_object.write(a390)
                    file_object.write("\n")


                if f'one sig {c3_at3} extends {c3_at3_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at3_0} extends {c3_at3_type_0}")
                    a391 = mylist[j]
                    file_object.write(a391)
                    file_object.write("\n")


                if f'one sig {c3_at4} extends {c3_at4_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at4_0} extends {c3_at4_type_0}")
                    a392 = mylist[j]
                    file_object.write(a392)
                    file_object.write("\n")


                if f'one sig {c3_at5} extends {c3_at5_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at5_0} extends {c3_at5_type_0}")
                    a393 = mylist[j]
                    file_object.write(a393)
                    file_object.write("\n")

                if f'one sig {c3_at6} extends {c3_at6_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c3_at6_0} extends {c3_at6_type_0}")
                    a394 = mylist[j]
                    file_object.write(a394)
                    file_object.write("\n")


            #-------------------------------------------------------------------------






            ##-------------------------------------------------------------------------
            #class4

            #-------------------------------------------------------------------------



                if f'one sig {class4_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class4_name_0} extends Class")
                    a395 = mylist[j]
                    file_object.write(a395)
                    file_object.write("\n")



                if f'id={c4_at3}' in mylist[j]:
                    mylist[j] = (f"id={c4_at3_0}")
                    a396 = mylist[j]
                    file_object.write(a396)
                    file_object.write("\n")


                if f'attrSet = {c4_at1}+{c4_at2}+{c4_at3}+{c4_at4}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c4_at1_0}+{c4_at2_0}+{c4_at3_0}+{c4_at4_0}")
                    a397 = mylist[j]
                    file_object.write(a397)
                    file_object.write("\n")



                if f'one sig {c4_at1} extends {c4_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c4_at1_0} extends {c4_at1_type_0}")
                    a398 = mylist[j]
                    file_object.write(a398)
                    file_object.write("\n")



                if f'one sig {c4_at2} extends {c4_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c4_at2_0} extends {c4_at2_type_0}")
                    a399 = mylist[j]
                    file_object.write(a399)
                    file_object.write("\n")


                if f'one sig {c4_at3} extends {c4_at3_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c4_at3_0} extends {c4_at3_type_0}")
                    a400 = mylist[j]
                    file_object.write(a400)
                    file_object.write("\n")




                if f'one sig {c4_at4} extends {c4_at4_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c4_at4_0} extends {c4_at4_type_0}")
                    a401 = mylist[j]
                    file_object.write(a401)
                    file_object.write("\n")


              ##-------------------------------------------------------------------------
            #class5

            #-------------------------------------------------------------------------



                if f'one sig {class5_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class5_name_0} extends Class")
                    a402 = mylist[j]
                    file_object.write(a402)
                    file_object.write("\n")



                if f'attrSet = {c5_at1}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c5_at1_0}")
                    a403 = mylist[j]
                    file_object.write(a403)
                    file_object.write("\n")



                if f'one parent' in mylist[j]:
                    mylist[j] = (f"one parent")
                    a404 = mylist[j]
                    file_object.write(a404)
                    file_object.write("\n")



                if f'parent in {class2_name}' in mylist[j]:
                    mylist[j] = (f"parent in {class2_name_0}")
                    a405 = mylist[j]
                    file_object.write(a405)
                    file_object.write("\n")


                if f'id = {c2_at1}' in mylist[j]:
                    mylist[j] = (f"id = {c2_at1_0}")
                    a406 = mylist[j]
                    file_object.write(a406)
                    file_object.write("\n")




                if f'one sig {c5_at1} extends {c5_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c5_at1_0} extends {c5_at1_type_0}")
                    a407 = mylist[j]
                    file_object.write(a407)
                    file_object.write("\n")


            #class6

            #-------------------------------------------------------------------------



                if f'one sig {class6_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class6_name_0} extends Class")
                    a408 = mylist[j]
                    file_object.write(a408)
                    file_object.write("\n")



                if f'attrSet = {c6_at1}+{c6_at2}+{c6_at3}+{c6_at4}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c6_at1_0}+{c6_at2_0}+{c6_at3_0}+{c6_at4_0}")
                    a409 = mylist[j]
                    file_object.write(a409)
                    file_object.write("\n")



                if f'id={c6_at2}' in mylist[j]:
                    mylist[j] = (f"id={c6_at2_0}")
                    a410 = mylist[j]
                    file_object.write(a410)
                    file_object.write("\n")


                if f'one sig {c6_at1} extends {c6_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c6_at1_0} extends {c6_at1_type_0}")
                    a411 = mylist[j]
                    file_object.write(a411)
                    file_object.write("\n")



                if f'one sig {c6_at2} extends {c6_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c6_at2_0} extends {c6_at2_type_0}")
                    a412 = mylist[j]
                    file_object.write(a412)
                    file_object.write("\n")



                if f'one sig {c6_at3} extends {c6_at3_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c6_at3_0} extends {c6_at3_type_0}")
                    a413 = mylist[j]
                    file_object.write(a413)
                    file_object.write("\n")



                if f'one sig {c6_at4} extends {c6_at4_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c6_at4_0} extends {c6_at4_type_0}")
                    a414 = mylist[j]
                    file_object.write(a414)
                    file_object.write("\n")





            #class7

            #-------------------------------------------------------------------------



                if f'one sig {class7_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class7_name_0} extends Class")
                    a415 = mylist[j]
                    file_object.write(a415)
                    file_object.write("\n")



                if f'attrSet = {c7_at1}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c7_at1_0}")
                    a416 = mylist[j]
                    file_object.write(a416)
                    file_object.write("\n")


                if f'one sig {c7_at1} extends {c7_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c7_at1_0} extends {c7_at1_type_0}")
                    a417 = mylist[j]
                    file_object.write(a417)
                    file_object.write("\n")




             #class8

            #-------------------------------------------------------------------------



                if f'one sig {class8_name} extends Class' in mylist[j]:
                    mylist[j] = (f"one sig {class8_name_0} extends Class")
                    a418 = mylist[j]
                    file_object.write(a418)
                    file_object.write("\n")


                if f'attrSet = {c8_at1}+{c8_at2}+{c2_at2}+{c6_at3}' in mylist[j]:
                    mylist[j] = (f"attrSet = {c8_at1_0}+{c8_at2_0}+{c2_at2_0}+{c6_at3_0}")
                    a419 = mylist[j]
                    file_object.write(a419)
                    file_object.write("\n")



                if f'id={c8_at1}' in mylist[j]:
                    mylist[j] = (f"id={c8_at1_0}")
                    a420 = mylist[j]
                    file_object.write(a420)
                    file_object.write("\n")


                if f'one sig {c8_at1} extends {c8_at1_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c8_at1_0} extends {c8_at1_type_0}")
                    a421 = mylist[j]
                    file_object.write(a421)
                    file_object.write("\n")

                if f'one sig {c8_at2} extends {c8_at2_type}' in mylist[j]:
                    mylist[j] = (f"one sig {c8_at2_0} extends {c8_at2_type_0}")
                    a422 = mylist[j]
                    file_object.write(a422)
                    file_object.write("\n")


             #assoc1

            #-------------------------------------------------------------------------


                if f'one sig {assoc1} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc1_0} extends Association")
                    a423 = mylist[j]
                    file_object.write(a423)
                    file_object.write("\n")


                if f'src = {class8_name}' in mylist[j]:
                    mylist[j] = (f"src = {class8_name_0}")
                    a424 = mylist[j]
                    file_object.write(a424)
                    file_object.write("\n")

                if f'dst= {class2_name}' in mylist[j]:
                    mylist[j] = (f"dst= {class2_name_0}")
                    a425 = mylist[j]
                    file_object.write(a425)
                    file_object.write("\n")




             #assoc2

            #-------------------------------------------------------------------------


                if f'one sig {assoc2} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc2_0} extends Association")
                    a0425 = mylist[j]
                    file_object.write(a0425)
                    file_object.write("\n")


                if f'src = {class2_name}' in mylist[j]:
                    mylist[j] = (f"src = {class2_name_0}")
                    a0424 = mylist[j]
                    file_object.write(a0424)
                    file_object.write("\n")

            #     if f'dst= {class2_name}' in mylist[j]:
            #         mylist[j] = (f"dst= {class2_name_0}")
            #         a425 = mylist[j]
            #         file_object.write(a425)
            #         file_object.write("\n")



             #assoc3

            #-------------------------------------------------------------------------


                if f'one sig {assoc3} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc3_0} extends Association")
                    a426 = mylist[j]
                    file_object.write(a426)
                    file_object.write("\n")


            #     if f'src = {class2_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class2_name_0}")
            #         a427 = mylist[j]
            #         file_object.write(a427)
            #         file_object.write("\n")

                if f'dst= {class3_name}' in mylist[j]:
                    mylist[j] = (f"dst= {class3_name_0}")
                    a427 = mylist[j]
                    file_object.write(a427)
                    file_object.write("\n")



            #----------------------------------------- -------------------------------
            #assoc4


            #-------------------------------------------------------------------------


                if f'one sig {assoc4} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc4_0} extends Association")
                    a428 = mylist[j]
                    file_object.write(a428)
                    file_object.write("\n")


            #     if f'src = {class2_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class2_name_0}")
            #         a427 = mylist[j]
            #         file_object.write(a427)
            #         file_object.write("\n")

                if f'dst= {class4_name}' in mylist[j]:
                    mylist[j] = (f"dst= {class4_name_0}")
                    a429 = mylist[j]
                    file_object.write(a429)
                    file_object.write("\n")


            #----------------------------------------- -------------------------------
            #assoc5


            #-------------------------------------------------------------------------


                if f'one sig {assoc5} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc5_0} extends Association")
                    a430 = mylist[j]
                    file_object.write(a430)
                    file_object.write("\n")


            #     if f'src = {class2_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class2_name_0}")
            #         a427 = mylist[j]
            #         file_object.write(a427)
            #         file_object.write("\n")

                if f'dst= {class6_name}' in mylist[j]:
                    mylist[j] = (f"dst= {class6_name_0}")
                    a430 = mylist[j]
                    file_object.write(a430)
                    file_object.write("\n")


            #----------------------------------------- -------------------------------
            #assoc6


            #-------------------------------------------------------------------------


                if f'one sig {assoc6} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc6_0} extends Association")
                    a431 = mylist[j]
                    file_object.write(a431)
                    file_object.write("\n")


                if f'src = {class6_name}' in mylist[j]:
                    mylist[j] = (f"src = {class6_name_0}")
                    a432 = mylist[j]
                    file_object.write(a432)
                    file_object.write("\n")

                if f'dst= {class1_name}' in mylist[j]:
                    mylist[j] = (f"dst= {class1_name_0}")
                    a433 = mylist[j]
                    file_object.write(a433)
                    file_object.write("\n")



             #----------------------------------------- -------------------------------
            #assoc7


            #-------------------------------------------------------------------------


                if f'one sig {assoc7} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc7_0} extends Association")
                    a0431 = mylist[j]
                    file_object.write(a0431)
                    file_object.write("\n")



            #----------------------------------------- -------------------------------
            #assoc8


            #-------------------------------------------------------------------------


                if f'one sig {assoc8} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc8_0} extends Association")
                    a434 = mylist[j]
                    file_object.write(a434)
                    file_object.write("\n")


            #     if f'src = {class6_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class6_name_0}")
            #         a432 = mylist[j]
            #         file_object.write(a432)
            #         file_object.write("\n")

            #     if f'dst= {class4_name}' in mylist[j]:
            #         mylist[j] = (f"dst= {class4_name_0}")
            #         a433 = mylist[j]
            #         file_object.write(a433)
            #         file_object.write("\n")





            #----------------------------------------- -------------------------------
            #assoc11


            #-------------------------------------------------------------------------


            #     if f'one sig {assoc11} extends Association' in mylist[j]:
            #         mylist[j] = (f"one sig {assoc11_0} extends Association")
            #         a435 = mylist[j]
            #         file_object.write(a435)
            #         file_object.write("\n")


                if f'src = {class1_name}' in mylist[j]:
                    mylist[j] = (f"src = {class1_name_0}")
                    a436 = mylist[j]
                    file_object.write(a436)
                    file_object.write("\n")

            #     if f'dst= {class4_name}' in mylist[j]:
            #         mylist[j] = (f"dst= {class4_name_0}")
            #         a433 = mylist[j]
            #         file_object.write(a433)
            #         file_object.write("\n")



            #----------------------------------------- -------------------------------
            #assoc9


            #-------------------------------------------------------------------------


                if f'one sig {assoc9} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc9_0} extends Association")
                    a437 = mylist[j]
                    file_object.write(a437)
                    file_object.write("\n")


            #     if f'src = {class1_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class1_name_0}")
            #         a436 = mylist[j]
            #         file_object.write(a436)
            #         file_object.write("\n")

            #     if f'dst= {class4_name}' in mylist[j]:
            #         mylist[j] = (f"dst= {class4_name_0}")
            #         a433 = mylist[j]
            #         file_object.write(a433)
            #         file_object.write("\n")



            #----------------------------------------- -------------------------------
            #assoc10


            #-------------------------------------------------------------------------


                if f'one sig {assoc10} extends Association' in mylist[j]:
                    mylist[j] = (f"one sig {assoc10_0} extends Association")
                    a438 = mylist[j]
                    file_object.write(a438)
                    file_object.write("\n")


            #     if f'src = {class1_name}' in mylist[j]:
            #         mylist[j] = (f"src = {class1_name_0}")
            #         a436 = mylist[j]
            #         file_object.write(a436)
            #         file_object.write("\n")

            #     if f'dst= {class4_name}' in mylist[j]:
            #         mylist[j] = (f"dst= {class4_name_0}")
            #         a433 = mylist[j]
            #         file_object.write(a433)
            #         file_object.write("\n")



file_object.close()



            #open this file

            #process files

            #save files
            # filename, extension = os.path.splitext(file)
            # if extension == '.sql':
            #     a = file
            #     print(a)
    #print(mylist)


    # for file in a:
    #     file_read = open(a, 'r')
    #
    # #file_name = "ecommerce_Sol_211.sql"
    # # file_read = open(file_name, "r")
    # mylist = file_read.readlines()

    # file_name = input("Enter The File's Name: ")
    # file_read = open(file_name, "r")
    # mylist = file_read.readlines()

print(i)
#---------------------------------------------- --------------------------------------- ---------------------- ---



#------------------------------------------------- -----------------------------------------------------

        #file_object.close()




# no need to use replace if you're going to change the whole varchar


#print(mylist)

# for  x in range(len(mylist)) :
#
#     print(mylist[x])
#     x += 1
    #ecommerce_Sol_ .sql
