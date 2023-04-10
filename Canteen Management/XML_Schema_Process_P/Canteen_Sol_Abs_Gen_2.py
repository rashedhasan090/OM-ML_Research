

import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Canteen Management/XML_Schema_Process_P'):
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
            OM_name = "Canteen"
            om_count = 0

            class1_name = "Payment"
            c1_at1 = "PaymentId"
            c1_at1_type = "int"
            c1_at2 = "ProductDetails"
            c1_at2_type = "varchar"

            class2_name = "User"
            c2_at1 = "UserId"
            c2_at1_type = "int"
            c2_at2 = "IntructionType"
            c2_at2_type = "varchar"


            class3_name = "Product"
            c3_at1 = "ProductId"
            c3_at1_type = "int"
            c3_at2 = "NoOfSoldProducts"
            c3_at2_type = "int"
            c3_at3 = "NoTotalProducts"
            c3_at3_type = "int"
            c3_at4 = "NoInventoryProducts"
            c3_at4_type = "int"
            c3_at5 = "ProductType"
            c3_at5_type = "int"
            c3_at6 = "Description"
            c3_at6_type = "int"


            class4_name = "Food"
            c4_at1 = "FoodCategory"
            c4_at1_type = "varchar"
            c4_at2 = "FoodType"
            c4_at2_type = "varchar"
            c4_at3 = "ItemId"
            c4_at3_type = "int"
            c4_at4 = "Price"
            c4_at4_type = "varchar"


            class5_name = "Salesman"
            c5_at1 = "TotalItemsSold"
            c5_at1_type = "varchar"


            class6_name = "Orders"
            c6_at1 = "OrdersName"
            c6_at1_type = "varchar"
            c6_at2 = "OrdersId"
            c6_at2_type = "int"
            c6_at3 = "OrderNumber"
            c6_at3_type = "varchar"
            c6_at4 = "Customer_Info"
            c6_at4_type = "varchar"


            class7_name = "Manager"
            c7_at1 = "ResponsibilityLog"
            c7_at1_type = "varchar"
            #c6_at2 = "categoryName"
            #c6_at2_type = "varchar"


            class8_name = "Canteen"
            c8_at1 = "CanteenId"
            c8_at1_type = "int"
            c8_at2 = "UserType"
            c8_at2_type = "varchar"


            assoc1 = "UserCanteenAssociation"
            assoc2 = "UserFoodAssociation"
            assoc3 = "CanteenProductAssociation"
            assoc4 = "CanteenFoodAssociation"
            assoc5 = "CanteenOrdersAssociation"
            assoc6 = "OrdersLibraryDbAssociation"
            assoc7 = "LibrarianBookAssociation"
            assoc8 = "OrdersFoodAssociation"
            assoc9 = "FoodLibraryDbAssociation"
            assoc10 = "UserProductAssociation"
            assoc11 = "ProductLibraryDbAssociation"

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

                if f'USE' in mylist[j]:
                    mylist[j] = (f"USE {OM_name_0}:{om_count};")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
            #
            #


                if f'CREATE DATABASE FOR' in mylist[j]:
                    mylist[j] = (f"")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
            #
            #


                if f'Table structure for' in mylist[j]:
                    mylist[j] = (f"")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
            #
            #

             #-------------------------------------------------------------------------


                if f'CREATE TABLE `{class3_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class3_name_0}` (")
                    a280 = mylist[j]
                    file_object.write(a280)
                    file_object.write("\n")




                if f'`{c8_at1}` {c8_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0},")
                    a281 = mylist[j]
                    file_object.write(a281)
                    file_object.write("\n")




                if f'`{c3_at6}` {c3_at6_type},' in mylist[j]:
                    mylist[j] = (f"`{c3_at6_0}` {c3_at6_type_0},")
                    a282 = mylist[j]
                    file_object.write(a282)
                    file_object.write("\n")




                if f'`{c3_at5}` {c3_at5_type},' in mylist[j]:
                    mylist[j] = (f"`{c3_at5_0}` {c3_at5_type_0},")
                    a283 = mylist[j]
                    file_object.write(a283)
                    file_object.write("\n")




                if f'`{c3_at4}` {c3_at4_type},' in mylist[j]:
                    mylist[j] = (f"`{c3_at4_0}` {c3_at4_type_0},")
                    a284 = mylist[j]
                    file_object.write(a284)
                    file_object.write("\n")




                if f'`{c3_at3}` {c3_at3_type},' in mylist[j]:
                    mylist[j] = (f"`{c3_at3_0}` {c3_at3_type_0},")
                    a285 = mylist[j]
                    file_object.write(a285)
                    file_object.write("\n")




                if f'`{c3_at2}` {c3_at2_type},' in mylist[j]:
                    mylist[j] = (f"`{c3_at2_0}` {c3_at2_type_0},")
                    a286 = mylist[j]
                    file_object.write(a286)
                    file_object.write("\n")




                if f'`{c3_at1}` {c3_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c3_at1_0}` {c3_at1_type_0} NOT NULL,")
                    a287 = mylist[j]
                    file_object.write(a287)
                    file_object.write("\n")




                if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c1_at1_0}` {c1_at1_type},")
                    a288 = mylist[j]
                    file_object.write(a288)
                    file_object.write("\n")





                if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c1_at1_0}` {c1_at1_type},")
                    a289 = mylist[j]
                    file_object.write(a289)
                    file_object.write("\n")




                if f'KEY `FK_{class3_name}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class3_name_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a290 = mylist[j]
                    file_object.write(a290)
                    file_object.write("\n")





                if f'KEY `FK_{class3_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class3_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
                    a291 = mylist[j]
                    file_object.write(a291)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c3_at1_0}`)")
                    a292 = mylist[j]
                    file_object.write(a292)
                    file_object.write("\n")



              #-------------------------------------------------------------------------------


                if f'CREATE TABLE `{class1_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class1_name_0}` (")
                    a293 = mylist[j]
                    file_object.write(a293)
                    file_object.write("\n")




                if f'`{c1_at2}` {c1_at2_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c1_at2_0}` {c1_at2_type_0}(64),")
                    a294 = mylist[j]
                    file_object.write(a294)
                    file_object.write("\n")




                if f'`{c1_at1}` {c1_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c1_at1_0}` {c1_at1_type_0} NOT NULL,")
                    a295 = mylist[j]
                    file_object.write(a295)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c1_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c1_at1_0}`)")
                    a296 = mylist[j]
                    file_object.write(a296)
                    file_object.write("\n")




               #----------------------------------------------------------------


                if f'CREATE TABLE `{class2_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class2_name_0}` (")
                    a297 = mylist[j]
                    file_object.write(a297)
                    file_object.write("\n")




                if f'`{c2_at2}` {c2_at2_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c2_at2_0}` {c2_at2_type_0}(64),")
                    a298 = mylist[j]
                    file_object.write(a298)
                    file_object.write("\n")



                if f'`{c8_at1}` {c8_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0},")
                    a299 = mylist[j]
                    file_object.write(a299)
                    file_object.write("\n")




                if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
                    a300 = mylist[j]
                    file_object.write(a300)
                    file_object.write("\n")




                if f'KEY `FK_{class2_name}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class2_name_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a301 = mylist[j]
                    file_object.write(a301)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c2_at1_0}`)")
                    a302 = mylist[j]
                    file_object.write(a302)
                    file_object.write("\n")




            #---------------------------------------------------------



                if f'CREATE TABLE `{class7_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class7_name_0}` (")
                    a303 = mylist[j]
                    file_object.write(a303)
                    file_object.write("\n")




                if f'`{c7_at1}` {c7_at1_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c7_at1_0}` {c7_at1_type_0}(64),")
                    a304 = mylist[j]
                    file_object.write(a304)
                    file_object.write("\n")




                if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
                    a305 = mylist[j]
                    file_object.write(a305)
                    file_object.write("\n")





                if f'KEY `FK_{class7_name}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class7_name_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
                    a306 = mylist[j]
                    file_object.write(a306)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c2_at1_0}`)")
                    a307 = mylist[j]
                    file_object.write(a307)
                    file_object.write("\n")



            #----------------------------------------------------------------



                if f'CREATE TABLE `{assoc10}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc10_0}` (")
                    a308 = mylist[j]
                    file_object.write(a308)
                    file_object.write("\n")




                if f'`{c3_at1}` {c3_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c3_at1_0}` {c3_at1_type_0} NOT NULL,")
                    a309 = mylist[j]
                    file_object.write(a309)
                    file_object.write("\n")




                if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
                    a310 = mylist[j]
                    file_object.write(a310)
                    file_object.write("\n")






                if f'KEY `FK_{assoc10}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc10_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
                    a311 = mylist[j]
                    file_object.write(a311)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c3_at1}`,`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c3_at1_0}`,`{c2_at1_0}`)")
                    a312 = mylist[j]
                    file_object.write(a312)
                    file_object.write("\n")



            #-----------------------------------------------------------------------------




                if f'CREATE TABLE `{class8_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class8_name_0}` (")
                    a313 = mylist[j]
                    file_object.write(a313)
                    file_object.write("\n")




                if f'`{c8_at2}` {c8_at2_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c8_at2_0}` {c8_at2_type_0}(64),")
                    a314 = mylist[j]
                    file_object.write(a314)
                    file_object.write("\n")





                if f'`{c6_at3}` {c6_at3_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c6_at3_0}` {c6_at3_type_0}(64),")
                    a315 = mylist[j]
                    file_object.write(a315)
                    file_object.write("\n")





                if f'PRIMARY KEY (`{c8_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c8_at1_0}`)")
                    a316 = mylist[j]
                    file_object.write(a316)
                    file_object.write("\n")




            #--------------------------------------------------------------

            #from ecommerce/ElectronicProduct



            #---------------------------------------------------------------------

            #-------------------------------------------------------------------------- ------------------


            #------------------------ ------------------------- -------------------------------- -------------

                if f'CREATE TABLE `{class5_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class5_name_0}` (")
                    a317 = mylist[j]
                    file_object.write(a317)
                    file_object.write("\n")




                if f'`{c5_at1}` {c5_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c5_at1_0}` {c5_at1_type_0},")
                    a318 = mylist[j]
                    file_object.write(a318)
                    file_object.write("\n")




                if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
                    a319 = mylist[j]
                    file_object.write(a319)
                    file_object.write("\n")




                if f'KEY `FK_{class5_name}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class5_name_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
                    a320 = mylist[j]
                    file_object.write(a320)
                    file_object.write("\n")





                if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c2_at1_0}`)")
                    a321 = mylist[j]
                    file_object.write(a321)
                    file_object.write("\n")



                  #-------------------------------------------------------------------------------



                if f'CREATE TABLE `{assoc5}` (' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str2_0}")
                    a322 = mylist[j]
                    file_object.write(a322)
                    file_object.write("\n")




                if f'`{c8_at1}` {c8_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0} NOT NULL,")
                    a323 = mylist[j]
                    file_object.write(a323)
                    file_object.write("\n")



                if f'`{c6_at2}` {c6_at2_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c6_at2_0}` {c6_at2_type_0} NOT NULL,")
                    a324 = mylist[j]
                    file_object.write(a324)
                    file_object.write("\n")



                if f'KEY `FK_{assoc5}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc5_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a325 = mylist[j]
                    file_object.write(a325)
                    file_object.write("\n")




                if f'KEY `FK_{assoc5}_{c6_at2}_idx` (`{c6_at2}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc5_0}_{c6_at2_0}_idx` (`{c6_at2_0}`),")
                    a326 = mylist[j]
                    file_object.write(a326)
                    file_object.write("\n")





                if f'PRIMARY KEY (`{c8_at1}`,`{c6_at2}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c8_at1_0}`,`{c6_at2_0}`)")
                    a327 = mylist[j]
                    file_object.write(a327)
                    file_object.write("\n")




                #-----------------------------------------------------------------------------

                if f'CREATE TABLE `{class4_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class4_name_0}` (")
                    a328 = mylist[j]
                    file_object.write(a328)
                    file_object.write("\n")




                if f'`{c4_at4}` {c4_at4_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c4_at4_0}` {c4_at4_type_0}(64),")
                    a329 = mylist[j]
                    file_object.write(a329)
                    file_object.write("\n")




                if f'`{c4_at2}` {c4_at2_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c4_at2_0}` {c4_at2_type_0}(64),")
                    a330 = mylist[j]
                    file_object.write(a330)
                    file_object.write("\n")




                if f'`{c4_at1}` {c4_at1_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c4_at1_0}` {c4_at1_type_0}(64),")
                    a331 = mylist[j]
                    file_object.write(a331)
                    file_object.write("\n")


                    #file_object.close()


                if f'`{c8_at1}` {c8_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c8_at1_0}` {c8_at1_type_0},")
                    a332 = mylist[j]
                    file_object.write(a332)
                    file_object.write("\n")


                    #file_object.close()

                if f'`{c6_at2}` {c6_at2_type},' in mylist[j]:
                    mylist[j] = (f"`{c6_at2_0}` {c6_at2_type_0},")
                    a333 = mylist[j]
                    file_object.write(a333)
                    file_object.write("\n")


                    #file_object.close()



                if f'`{c4_at3}` {c4_at3_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c4_at3_0}` {c4_at3_type_0} NOT NULL,")
                    a334 = mylist[j]
                    file_object.write(a334)
                    file_object.write("\n")


                    #file_object.close()




                if f'`{c4_at3}` {c4_at3_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c4_at3_0}` {c4_at3_type_0} NOT NULL,")
                    a334 = mylist[j]
                    file_object.write(a334)
                    file_object.write("\n")


                    #file_object.close()




                if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
                    mylist[j] = (f"`{c1_at1_0}` {c1_at1_type_0},")
                    a335 = mylist[j]
                    file_object.write(a335)
                    file_object.write("\n")


                    #file_object.close()


                if f'KEY `FK_{class4_name}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class4_name_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a336 = mylist[j]
                    file_object.write(a336)
                    file_object.write("\n")


                    #file_object.close()



                if f'KEY `FK_{class4_name}_{c6_at2}_idx` (`{c6_at2}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class4_name_0}_{c6_at2_0}_idx` (`{c6_at2_0}`),")
                    a337 = mylist[j]
                    file_object.write(a337)
                    file_object.write("\n")


                    #file_object.close()


                if f'KEY `FK_{class4_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{class4_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
                    a338 = mylist[j]
                    file_object.write(a338)
                    file_object.write("\n")


                    #file_object.close()



                if f'PRIMARY KEY (`{c4_at3}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c4_at3_0}`)")
                    a339 = mylist[j]
                    file_object.write(a339)
                    file_object.write("\n")


                    #file_object.close()


              #----------------------------------------------------------------------------

            #From ecommerce/ProductCategoryAssociation
            #<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductCatalogAssociation"/> </tuple>
            #<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductCategoryAssociation"/> </tuple>
            #<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductItemAssociation"/> </tuple>
            #<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductAssetAssociation"/> </tuple>


                if f'CREATE TABLE `{assoc6}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc6_0}` (")
                    a340 = mylist[j]
                    file_object.write(a340)
                    file_object.write("\n")
            #
            #


                if f'`{c6_at2}` int NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c6_at2_0}` int NOT NULL,")
                    a341 = mylist[j]
                    file_object.write(a341)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



                if f'`{c1_at1}` int NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c1_at1_0}` int NOT NULL,")
                    a342 = mylist[j]
                    file_object.write(a342)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



                if f'KEY `FK_{assoc6}_{c6_at2}_idx` (`{c6_at2}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc6_0}_{c6_at2_0}_idx` (`{c6_at2_0}`),")
                    a343 = mylist[j]
                    file_object.write(a343)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'KEY `FK_{assoc6}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc6_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
                    a344 = mylist[j]
                    file_object.write(a344)
                    file_object.write("\n")
            #
            #
                    #file_object.close()






                if f'PRIMARY KEY (`{c6_at2}`,`{c1_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c6_at2_0}`,`{c1_at1_0}`)")
                    a345 = mylist[j]
                    file_object.write(a345)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


            #-----------------------------------------------------------------------------


                if f'CREATE TABLE `{class6_name}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{class6_name_0}` (")
                    a346 = mylist[j]
                    file_object.write(a346)
            #         file_object.write("\n")
            #
            #


                if f'`{c6_at4}` {c6_at4_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c6_at4_0}` {c6_at4_type_0}(64),")
                    a347 = mylist[j]
                    file_object.write(a347)
                    file_object.write("\n")
            #
            #


                if f'`{c6_at1}` {c6_at1_type}(64),' in mylist[j]:
                    mylist[j] = (f"`{c6_at1_0}` {c6_at1_type_0}(64),")
                    a348 = mylist[j]
                    file_object.write(a348)
                    file_object.write("\n")


                    #file_object.close()


                if f'`{c6_at2}` {c6_at2_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c6_at2_0}` {c6_at2_type_0} NOT NULL,")
                    a349 = mylist[j]
                    file_object.write(a349)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'PRIMARY KEY (`{c6_at2}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c6_at2_0}`)")
                    a350 = mylist[j]
                    file_object.write(a350)
                    file_object.write("\n")
            #
            #
                    #file_object.close()






            #-----------------------------------------------------------------------


                if f'CREATE TABLE `{assoc2}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc2_0}` (")
                    a351 = mylist[j]
                    file_object.write(a351)
                    file_object.write("\n")
            #
            #


                if f'`{c4_at3}` {c4_at3_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c4_at3}` {c4_at3_type} NOT NULL,")
                    a352 = mylist[j]
                    file_object.write(a352)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'`{c2_at1}` {c2_at1_type} NOT NULL,' in mylist[j]:
                    mylist[j] = (f"`{c2_at1_0}` {c2_at1_type_0} NOT NULL,")
                    a353 = mylist[j]
                    file_object.write(a353)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'KEY `FK_{assoc2}_{c4_at3}_idx` (`{c4_at3}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc2_0}_{c4_at3_0}_idx` (`{c4_at3_0}`),")
                    a354 = mylist[j]
                    file_object.write(a354)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



                if f'KEY `FK_{assoc2}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc2_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
                    a355 = mylist[j]
                    file_object.write(a355)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'PRIMARY KEY (`{c4_at3}`,`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c4_at3_0}`,`{c2_at1_0}`)")
                    a356 = mylist[j]
                    file_object.write(a356)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


            #-----------------------------------------------------------------



                if f'ALTER TABLE `{class3_name}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{class3_name_0}`")
                    a357 = mylist[j]
                    file_object.write(a357)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{class3_name}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class3_name_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a358= mylist[j]
                    file_object.write(a358)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'ADD CONSTRAINT `FK_{class3_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class3_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a359= mylist[j]
                    file_object.write(a359)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



            #-------------------------------------------------- ------------------

                if f'ALTER TABLE `{class2_name}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{class2_name_0}`")
                    a360 = mylist[j]
                    file_object.write(a360)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{class2_name}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class2_name_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a361= mylist[j]
                    file_object.write(a361)
                    file_object.write("\n")
            #
            #
                    #file_object.close()

            #-----------------------------------------------------------------------


                if f'ALTER TABLE `{class7_name}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{class7_name_0}`")
                    a362 = mylist[j]
                    file_object.write(a362)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{class7_name}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class7_name_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a363= mylist[j]
                    file_object.write(a363)
                    file_object.write("\n")
            #
            #
                    #file_object.close()




            #------------ ----------------------- ------------------

                if f'ALTER TABLE `{assoc10}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc10_0}`")
                    a364 = mylist[j]
                    file_object.write(a364)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{assoc10}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc10_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a365= mylist[j]
                    file_object.write(a365)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'ADD CONSTRAINT `FK_{assoc10}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc10_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a365= mylist[j]
                    file_object.write(a365)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



            # ------------------------ -------------------------- -------------------

                if f'ALTER TABLE `{class5_name}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{class5_name_0}`")
                    a366 = mylist[j]
                    file_object.write(a366)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{class5_name}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class5_name_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a367= mylist[j]
                    file_object.write(a367)
                    file_object.write("\n")
            #
            #
                    #file_object.close()





            # ------------------------ -------------------------- -------------------


                if f'ALTER TABLE `{assoc5}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc5_0}`")
                    a368 = mylist[j]
                    file_object.write(a368)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{assoc5}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc5_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a369= mylist[j]
                    file_object.write(a369)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'ADD CONSTRAINT `FK_{assoc5}_{c6_at2}` FOREIGN KEY (`{c6_at2}`) REFERENCES `{class6_name}` (`{c6_at2}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc5_0}_{c6_at2_0}` FOREIGN KEY (`{c6_at2_0}`) REFERENCES `{class6_name_0}` (`{c6_at2_0}`) ON DELETE CASCADE ON UPDATE CASCADE;")
                    a370= mylist[j]
                    file_object.write(a370)
                    file_object.write("\n")
            #
            #
                    #file_object.close()




             #------------------------ -------------------------- -------------------


                if f'ALTER TABLE `{class4_name}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{class4_name_0}`")
                    a371 = mylist[j]
                    file_object.write(a371)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{class4_name}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class4_name_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a372= mylist[j]
                    file_object.write(a372)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'ADD CONSTRAINT `FK_{class4_name}_{c6_at2}` FOREIGN KEY (`{c6_at2}`) REFERENCES `{class6_name}` (`{c6_at2}`) ON DELETE CASCADE ON UPDATE CASCADE' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class4_name_0}_{c6_at2_0}` FOREIGN KEY (`{c6_at2_0}`) REFERENCES `{class6_name_0}` (`{c6_at2_0}`) ON DELETE CASCADE ON UPDATE CASCADE;")
                    a373= mylist[j]
                    file_object.write(a373)
                    file_object.write("\n")
            #
            #
                    #file_object.close()


                if f'ADD CONSTRAINT `FK_{class4_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{class4_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a374= mylist[j]
                    file_object.write(a374)
                    file_object.write("\n")
            #
            #
                    #file_object.close()



            # ------------------------ -------------------------- -------------------

                if f'ALTER TABLE `{assoc6}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc6_0}`")
                    a375 = mylist[j]
                    file_object.write(a375)
                    file_object.write("\n")
            #
            #


                if f'ADD CONSTRAINT `FK_{assoc6}_{c6_at2}` FOREIGN KEY (`{c6_at2}`) REFERENCES `{class6_name}` (`{c6_at2}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc6_0}_{c6_at2_0}` FOREIGN KEY (`{c6_at2_0}`) REFERENCES `{class6_name_0}` (`{c6_at2_0}`) ON DELETE CASCADE ON UPDATE CASCADE")
                    a376= mylist[j]
                    file_object.write(a362)
                    file_object.write("\n")
            # #
            #
                    #file_object.close()




                if f'ADD CONSTRAINT `FK_{assoc6}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc6_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a377= mylist[j]
                    file_object.write(a377)
                    file_object.write("\n")
            # #
            #
                    #file_object.close()



                if f'ADD CONSTRAINT `FK_{assoc6}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc6_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a377= mylist[j]
                    file_object.write(a377)
                    file_object.write("\n")
            # #
            #
                    #file_object.close()



            # ------------------------ -------------------------- -------------------


                if f'ALTER TABLE `{assoc2}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc2_0}`")
                    a378 = mylist[j]
                    file_object.write(a378)
                    file_object.write("\n")
            #



                if f'ADD CONSTRAINT `FK_{assoc2}_{c4_at3}` FOREIGN KEY (`{c4_at3}`) REFERENCES `{class4_name}` (`{c4_at3}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc2_0}_{c4_at3_0}` FOREIGN KEY (`{c4_at3_0}`) REFERENCES `{class4_name_0}` (`{c4_at3_0}`) ON DELETE CASCADE ON UPDATE CASCADE")
                    a378= mylist[j]
                    file_object.write(a378)
                    file_object.write("\n")
            #

                    #file_object.close()



                if f'ADD CONSTRAINT `FK_{assoc2}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc2_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a379= mylist[j]
                    file_object.write(a379)
                    file_object.write("\n")




                if f'--' in mylist[j]:
                    mylist[j] = (f"")
                    a380= mylist[j]
                    file_object.write(a380)
                    file_object.write("\n")



                if f'KEY `FK_{assoc10}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc10_0}_{c3_at1_0}_idx` (`{c3_at1_0}`),")
                    a381= mylist[j]
                    file_object.write(a381)
                    file_object.write("\n")



                if f'CREATE TABLE `{assoc3}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc3_0}` (")
                    a382= mylist[j]
                    file_object.write(a382)
                    file_object.write("\n")


                if f'KEY `FK_{assoc3}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc3_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a383= mylist[j]
                    file_object.write(a383)
                    file_object.write("\n")


                if f'KEY `FK_{assoc3}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc3_0}_{c3_at1_0}_idx` (`{c3_at1_0}`),")
                    a384= mylist[j]
                    file_object.write(a384)
                    file_object.write("\n")




                if f'PRIMARY KEY (`{c8_at1}`,`{c3_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c8_at1_0}`,`{c3_at1_0}`)")
                    a384= mylist[j]
                    file_object.write(a384)
                    file_object.write("\n")



                if f'CREATE TABLE `{assoc8}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc8_0}` (")
                    a384= mylist[j]
                    file_object.write(a384)
                    file_object.write("\n")



                if f'KEY `FK_{assoc8}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc8_0}_{c3_at1_0}_idx` (`{c3_at1_0}`),")
                    a385= mylist[j]
                    file_object.write(a385)
                    file_object.write("\n")


                if f'KEY `FK_{assoc8}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc8_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
                    a386= mylist[j]
                    file_object.write(a386)
                    file_object.write("\n")

                if f'PRIMARY KEY (`{c3_at1}`,`{c1_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c3_at1_0}`,`{c1_at1_0}`)")
                    a387= mylist[j]
                    file_object.write(a387)
                    file_object.write("\n")


                if f'CREATE TABLE `{assoc1}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc1_0}` (")
                    a388= mylist[j]
                    file_object.write(a388)
                    file_object.write("\n")


                if f'KEY `FK_{assoc1}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc1_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a389= mylist[j]
                    file_object.write(a389)
                    file_object.write("\n")


                if f'KEY `FK_{assoc1}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc1_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),")
                    a390= mylist[j]
                    file_object.write(a390)
                    file_object.write("\n")


                if f'PRIMARY KEY (`{c8_at1}`,`{c2_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c8_at1_0}`,`{c2_at1_0}`)")
                    a391= mylist[j]
                    file_object.write(a391)
                    file_object.write("\n")



                if f'CREATE TABLE `{assoc9}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc9_0}` (")
                    a392= mylist[j]
                    file_object.write(a392)
                    file_object.write("\n")



                if f'KEY `FK_{assoc9}_{c4_at3}_idx` (`{c4_at3}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc9_0}_{c4_at3_0}_idx` (`{c4_at3_0}`),")
                    a393= mylist[j]
                    file_object.write(a393)
                    file_object.write("\n")



                if f'KEY `FK_{assoc9}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc9_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),")
                    a394= mylist[j]
                    file_object.write(a394)
                    file_object.write("\n")



                if f'PRIMARY KEY (`{c4_at3}`,`{c1_at1}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c4_at3_0}`,`{c1_at1_0}`)")
                    a395= mylist[j]
                    file_object.write(a395)
                    file_object.write("\n")




            #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc8}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc8_0}`")
                    a396= mylist[j]
                    file_object.write(a396)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc8}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc8_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a397= mylist[j]
                    file_object.write(a397)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc8}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc8_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a398= mylist[j]
                    file_object.write(a398)
                    file_object.write("\n")




             #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc3}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc3_0}`")
                    a399= mylist[j]
                    file_object.write(a399)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc3}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc3_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a400= mylist[j]
                    file_object.write(a400)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc3}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc3_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a401= mylist[j]
                    file_object.write(a401)
                    file_object.write("\n")


              #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc1}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc1_0}`")
                    a402= mylist[j]
                    file_object.write(a402)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc1}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc1_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a403= mylist[j]
                    file_object.write(a403)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc1}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc1_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a401= mylist[j]
                    file_object.write(a404)
                    file_object.write("\n")



             #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc9}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc9_0}`")
                    a402= mylist[j]
                    file_object.write(a402)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc9}_{c4_at3}` FOREIGN KEY (`{c4_at3}`) REFERENCES `{class4_name}` (`{c4_at3}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc9_0}_{c4_at3_0}` FOREIGN KEY (`{c4_at3_0}`) REFERENCES `{class4_name_0}` (`{c4_at3_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a403= mylist[j]
                    file_object.write(a403)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc9}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc9_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;")
                    a404= mylist[j]
                    file_object.write(a404)
                    file_object.write("\n")

               # -------------------------------------------------------------------



                if f'CREATE TABLE `{assoc7}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc7_0}` (")
                    a405= mylist[j]
                    file_object.write(a405)
                    file_object.write("\n")



                if f'KEY `FK_{assoc7}_{c6_at2}_idx` (`{c6_at2}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc7_0}_{c6_at2_0}_idx` (`{c6_at2_0}`),")
                    a406= mylist[j]
                    file_object.write(a406)
                    file_object.write("\n")



                if f'KEY `FK_{assoc7}_{c4_at3}_idx` (`{c4_at3}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc7_0}_{c4_at3_0}_idx` (`{c4_at3_0}`),")
                    a407= mylist[j]
                    file_object.write(a407)
                    file_object.write("\n")


                if f'PRIMARY KEY (`{c6_at2}`,`{c4_at3}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c6_at2_0}`,`{c4_at3_0}`)")
                    a408= mylist[j]
                    file_object.write(a408)
                    file_object.write("\n")




            #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc7}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc7_0}`")
                    a409= mylist[j]
                    file_object.write(a409)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc7}_{c6_at2}` FOREIGN KEY (`{c6_at2}`) REFERENCES `{class6_name}` (`{c6_at2}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc7_0}_{c6_at2_0}` FOREIGN KEY (`{c6_at2_0}`) REFERENCES `{class6_name_0}` (`{c6_at2_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a410= mylist[j]
                    file_object.write(a410)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc7}_{c4_at3}` FOREIGN KEY (`{c4_at3}`) REFERENCES `{class4_name}` (`{c4_at3}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc7_0}_{c4_at3_0}` FOREIGN KEY (`{c4_at3_0}`) REFERENCES `{class4_name_0}` (`{c4_at3_0}`) ON DELETE CASCADE ON UPDATE CASCADE;")
                    a411= mylist[j]
                    file_object.write(a411)
                    file_object.write("\n")




               # -------------------------------------------------------------------



                if f'CREATE TABLE `{assoc4}` (' in mylist[j]:
                    mylist[j] = (f"CREATE TABLE `{assoc4_0}` (")
                    a412= mylist[j]
                    file_object.write(a412)
                    file_object.write("\n")



                if f'KEY `FK_{assoc4}_{c8_at1}_idx` (`{c8_at1}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc4_0}_{c8_at1_0}_idx` (`{c8_at1_0}`),")
                    a413= mylist[j]
                    file_object.write(a413)
                    file_object.write("\n")



                if f'KEY `FK_{assoc4}_{c4_at3}_idx` (`{c4_at3}`),' in mylist[j]:
                    mylist[j] = (f"KEY `FK_{assoc4_0}_{c4_at3_0}_idx` (`{c4_at3_0}`),")
                    a414= mylist[j]
                    file_object.write(a414)
                    file_object.write("\n")


                if f'PRIMARY KEY (`{c8_at1}`,`{c4_at3}`)' in mylist[j]:
                    mylist[j] = (f"PRIMARY KEY (`{c8_at1_0}`,`{c4_at3_0}`)")
                    a415= mylist[j]
                    file_object.write(a415)
                    file_object.write("\n")

            #   -------------------------------------------------------------------------------


                if f'ALTER TABLE `{assoc4}`' in mylist[j]:
                    mylist[j] = (f"ALTER TABLE `{assoc4_0}`")
                    a416= mylist[j]
                    file_object.write(a416)
                    file_object.write("\n")


                if f'ADD CONSTRAINT `FK_{assoc4}_{c8_at1}` FOREIGN KEY (`{c8_at1}`) REFERENCES `{class8_name}` (`{c8_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc4_0}_{c8_at1_0}` FOREIGN KEY (`{c8_at1_0}`) REFERENCES `{class8_name_0}` (`{c8_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,")
                    a417= mylist[j]
                    file_object.write(a417)
                    file_object.write("\n")



                if f'ADD CONSTRAINT `FK_{assoc4}_{c4_at3}` FOREIGN KEY (`{c4_at3}`) REFERENCES `{class4_name}` (`{c4_at3}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
                    mylist[j] = (f"ADD CONSTRAINT `FK_{assoc4_0}_{c4_at3_0}` FOREIGN KEY (`{c4_at3_0}`) REFERENCES `{class4_name_0}` (`{c4_at3_0}`) ON DELETE CASCADE ON UPDATE CASCADE;")
                    a418= mylist[j]
                    file_object.write(a418)
                    file_object.write("\n")


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
