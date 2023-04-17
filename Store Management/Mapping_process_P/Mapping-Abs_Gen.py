

import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Store Management/Mapping_process_P'):
    for file in files:
        #each file

        filename, extension = os.path.splitext(file)
        if extension == '.xml':
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



                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/StoreDatabase"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str2_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/StoreDatabase"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str1_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/StoreDatabase"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str3_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

             #-------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/Owner"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str1_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/Owner"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str2_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/Owner"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str3_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

              #-------------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/Staff"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str1_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/Staff"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str2_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/Staff"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str3_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


               #----------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/StoreManagementSystem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str1_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/StoreManagementSystem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str2_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/StoreManagementSystem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str3_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #---------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str1_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str2_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str3_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")





            #----------------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/Store"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str1_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/Store"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str2_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/Store"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str3_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #-----------------------------------------------------------------------------




                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="store/User"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str1_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="store/User"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str2_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="store/User"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str3_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #--------------------------------------------------------------

            #from store/ElectronicStore



            #---------------------------------------------------------------------

            #-------------------------------------------------------------------------- ------------------


            #------------------------ ------------------------- -------------------------------- -------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="UserSMSAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str1_0}")
                    a31 = mylist[j]
                    file_object.write(a31)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="UserSMSAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str2_0}")
                    a31 = mylist[j]
                    file_object.write(a31)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                    #---------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="UserStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str1_0}")
                    a32 = mylist[j]
                    file_object.write(a32)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="UserStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str2_0}")
                    a32 = mylist[j]
                    file_object.write(a32)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                  #-------------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/SMSStoreAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str1_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/SMSStoreAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str2_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                #-----------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/SMSStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str2_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/SMSStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str1_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                 #-------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/CustomerStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str2_0}")
                    a35 = mylist[j]
                    file_object.write(a35)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/CustomerStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str1_0}")
                    a35 = mylist[j]
                    file_object.write(a35)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()

              #----------------------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/SMSCustomerAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str2_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/SMSCustomerAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str1_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/CustomerStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str2_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/CustomerStockAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str1_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/StoreStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str2_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/StoreStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str1_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()



            #-----------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/StockStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str2_0}")
                    a39 = mylist[j]
                    file_object.write(a39)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/StockStoreDbAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str1_0}")
                    a39 = mylist[j]
                    file_object.write(a39)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()



            #-----------------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/UserStoreAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str2_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/UserStoreAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str1_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()




 #-----------------------------------------------------------------------



#     if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="store/StoreLibraryDbAssociation"/> </tuple>' in mylist[j]:
#         mylist[j] = (f"Association Strategy for {assoc11_0} : {assoc_str2_0}")
#         a40 = mylist[j]
#         file_object.write(a40)
#         file_object.write("\n")
#         print(mylist[j])
#         print("")


#     if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="store/StoreLibraryDbAssociation"/> </tuple>' in mylist[j]:
#         mylist[j] = (f"Association Strategy for {assoc11_0} : {assoc_str1_0}")
#         a40 = mylist[j]
#         file_object.write(a40)
#         file_object.write("\n")
#         print(mylist[j])
#         print("")
#         #file_object.close()



#traffic_control_Sol_58.xml
#traffic_control_Sol_ .xml

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
