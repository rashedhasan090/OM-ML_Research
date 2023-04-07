

import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/E-commerce-OM-Resources/All XML and SQL Soln 2'):
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


            assoc_str1 = "ForeignKeyEmbeddingStrategy"
            assoc_str2 = "OwnAssociationTableStrategy"

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

            assoc_str1_0 = "assoc_str1"
            assoc_str2_0 = "assoc_str2"

            file_object = open(file+'.txt', 'a')



            for j in range(len(mylist)):


                if f'<tuple> <atom label="assertions/relationalModel/Table$0"/> <atom label="ecommerce/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name: {class1_name_0}")
                    a1 = mylist[j]
                    file_object.write(a1)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="assertions/relationalModel/Table$1"/> <atom label="ecommerce/Order"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name: {class01_name_0}")
                    a2 = mylist[j]
                    file_object.write(a2)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$2"/> <atom label="ecommerce/ShippingCart"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class2_name_0}")
                    a3 = mylist[j]
                    file_object.write(a3)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")




                if f'<tuple> <atom label="assertions/relationalModel/Table$3"/> <atom label="ecommerce/Item"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class3_name_0}")
                    a4 = mylist[j]
                    file_object.write(a4)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="assertions/relationalModel/Table$4"/> <atom label="ecommerce/CartItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class4_name_0}")
                    a5 = mylist[j]
                    file_object.write(a5)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="assertions/relationalModel/Table$5"/> <atom label="ecommerce/OrderItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class5_name_0}")
                    a6 = mylist[j]
                    file_object.write(a6)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")





                if f'<tuple> <atom label="assertions/relationalModel/Table$6"/> <atom label="ecommerce/ProductItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {assoc7_0}")
                    a7 = mylist[j]
                    file_object.write(a7)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$7"/> <atom label="ecommerce/ProductCategoryAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {assoc5_0}")
                    a8 = mylist[j]
                    file_object.write(a8)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")






                if f'<tuple> <atom label="assertions/relationalModel/Table$8"/> <atom label="ecommerce/Catalog"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class8_name_0}")
                    a9 = mylist[j]
                    file_object.write(a9)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="assertions/relationalModel/Table$9"/> <atom label="ecommerce/ProductAssetAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {assoc8_0}")
                    a10 = mylist[j]
                    file_object.write(a10)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$10"/> <atom label="ecommerce/Media"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class13_name_0}")
                    a11 = mylist[j]
                    file_object.write(a11)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$11"/> <atom label="ecommerce/Category"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class6_name_0}")
                    a12 = mylist[j]
                    file_object.write(a12)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")




                if f'<tuple> <atom label="assertions/relationalModel/Table$12"/> <atom label="ecommerce/Product"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class7_name_0}")
                    a13 = mylist[j]
                    file_object.write(a13)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$13"/> <atom label="ecommerce/ElectronicProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class10_name_0}")
                    a14 = mylist[j]
                    file_object.write(a14)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")




                if f'<tuple> <atom label="assertions/relationalModel/Table$14"/> <atom label="ecommerce/Service"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class11_name_0}")
                    a15 = mylist[j]
                    file_object.write(a15)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="assertions/relationalModel/Table$15"/> <atom label="ecommerce/Asset"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class12_name_0}")
                    a16 = mylist[j]
                    file_object.write(a16)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                #---------------------------------------------------------------------------------
                if f'<tuple> <atom label="assertions/relationalModel/Table$16"/> <atom label="ecommerce/Documents"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name {class14_name_0}")
                    a17 = mylist[j]
                    file_object.write(a17)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



                if f'<tuple> <atom label="assertions/relationalModel/Table$17"/> <atom label="ecommerce/PhysicalProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Table Name: {class9_name_0}")
                    a18 = mylist[j]
                    file_object.write(a18)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")




            #---------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str2_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str1_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Customer"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str3_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

             #-------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Category"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str1_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Category"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str2_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Category"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str3_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

              #-------------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Product"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str1_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Product"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str2_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Product"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str3_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


               #----------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Asset"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class12_name_0} : {map_str1_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Asset"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class12_name_0} : {map_str2_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Asset"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str3_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #---------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/CartItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class4_name_0} : {map_str1_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/CartItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class4_name_0} : {map_str2_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/CartItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class4_name_0} : {map_str3_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")





            #----------------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/OrderItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str1_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/OrderItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str2_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/OrderItem"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str3_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #-----------------------------------------------------------------------------




                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/PhysicalProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class9_name_0} : {map_str1_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/PhysicalProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class9_name_0} : {map_str2_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/PhysicalProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class9_name_0} : {map_str3_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #--------------------------------------------------------------

            #from ecommerce/ElectronicProduct




                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/ElectronicProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class10_name_0} : {map_str1_0}")
                    a102 = mylist[j]
                    file_object.write(a102)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/ElectronicProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class10_name_0} : {map_str2_0}")
                    a102 = mylist[j]
                    file_object.write(a102)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/ElectronicProduct"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class10_name_0} : {map_str3_0}")
                    a102 = mylist[j]
                    file_object.write(a102)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

            #---------------------------------------------------------------------

                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Service"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str1_0}")
                    a103 = mylist[j]
                    file_object.write(a103)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Service"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str2_0}")
                    a103 = mylist[j]
                    file_object.write(a103)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Service"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str3_0}")
                    a103 = mylist[j]
                    file_object.write(a103)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
            #-------------------------------------------------------------------------- ------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Media"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str1_0}")
                    a104 = mylist[j]
                    file_object.write(a104)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Media"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str2_0}")
                    a104 = mylist[j]
                    file_object.write(a104)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Media"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class11_name_0} : {map_str3_0}")
                    a104 = mylist[j]
                    file_object.write(a104)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #-------------------------------- -------------------- ------------------------ -----------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="ecommerce/Documents"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class14_name_0} : {map_str1_0}")
                    a105 = mylist[j]
                    file_object.write(a105)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="ecommerce/Documents"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class14_name_0} : {map_str2_0}")
                    a105 = mylist[j]
                    file_object.write(a105)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="ecommerce/Documents"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class14_name_0} : {map_str3_0}")
                    a105 = mylist[j]
                    file_object.write(a105)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")



            #------------------------ ------------------------- -------------------------------- -------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/CustomerOrderAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str1_0}")
                    a31 = mylist[j]
                    file_object.write(a31)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/CustomerOrderAssociation"/> </tuple>' in mylist[j]:
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

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ShippingCartItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str1_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ShippingCartItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str2_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                #-----------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/OrderItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str2_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/OrderItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str1_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                 #-------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductCatalogAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str2_0}")
                    a35 = mylist[j]
                    file_object.write(a35)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductCatalogAssociation"/> </tuple>' in mylist[j]:
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


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductCategoryAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str2_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductCategoryAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str1_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str2_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductItemAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str1_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="ecommerce/ProductAssetAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str2_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="ecommerce/ProductAssetAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str1_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
        #file_object.close()


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
