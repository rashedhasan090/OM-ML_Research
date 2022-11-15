
#Extract Solution Mapping Strategy of OnlineStore Object Model 
#Processing the XML files 

file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "OnlineStore"
om_count = 0 

class1_name = "Admin"
c1_at1 = "AdminId"
c1_at1_type = "Integer"
c1_at2_type = "string"
c1_at2 = "AdminName"

class2_name = "Customer"
c2_at1 = "CustomerId"
c2_at1_type = "Integer"
c2_at2 = "CustomerName"
c2_at2_type = "string"
c2_at3 = "Address"
c2_at3_type = "string"
c2_at4 = "PhoneNo"
c2_at4_type = "Integer"

class3_name = "Payment"
c3_at1 = "PaymentId"
c3_at1_type = "Integer"
c3_at2 = "PaymentName"
c3_at2_type = "string"
c3_at3 = "CardType"
c3_at3_type = "string"
c3_at4 = "CardNo"
c3_at4_type = "Integer"

class4_name = "Guest"
c4_at1 = "GuestId"
c4_at1_type = "Integer"

class5_name = "Products"
c5_at1 = "ProductsId"
c5_at1_type = "Integer"
c5_at2 = "ProductsName"
c5_at2_type = "string"
c5_at3 = "Group"
c5_at3_type = "string"
c5_at4 = "Subgroup"
c5_at4_type = "string"

class6_name = "Cart"
c6_at1 = "CartId"
c6_at1_type = "Integer"
c6_at2 = "NumOfProducts"
c6_at2_type = "Integer"
c6_at3 = "Price"
c6_at3_type = "Integer"
c6_at4 = "Total"
c6_at4_type = "Integer"


assoc1 = "AdminProductsAssociation"
assoc2 = "CustomerProductsAssociation"
assoc3 = "ProductsGuestAssociation"
assoc4 = "CustomerCartAssociation"
assoc5 = "CustomerPaymentAssociation"

src_mlpc = "ONE"
dst_mlpc = "MANY"
dst_mlpc2 = "ONE"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"


file_object = open(f'OnlineStore_Mapping_strategy_1.txt', 'a')
   




for j in range(len(mylist)):
    
    if f'Run mapping_run_OnlineStore for 32' in mylist[j]:
        mylist[j] = (f"{OM_name}_Solution : {om_count} ")
        a00 = mylist[j]
        file_object.write(a00)
        file_object.write("\n")
        print(mylist[j])
        print("")
        om_count += 1
        
        
    if f'<sig label="OnlineStore/Admin" ID="20" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class1_name} ")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
       
    
    if f'<sig label="OnlineStore/Customer" ID="21" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} ")
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")
        print(mylist[j])
        print("") 
   

    if f'<sig label="OnlineStore/Payment" ID="22" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} ")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        print(mylist[j])
        print("") 

        
    if f'<sig label="OnlineStore/Guest" ID="23" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class4_name} ")
        a3 = mylist[j]
        file_object.write(a3)
        file_object.write("\n")
        print(mylist[j])
        print("") 
    
    
    if f'<sig label="OnlineStore/Products" ID="24" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name} ")
        a4 = mylist[j]
        file_object.write(a4)
        file_object.write("\n")
        print(mylist[j])
        print("") 
     
     
    if f'<sig label="OnlineStore/Cart" ID="25" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name} ")
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")
        print(mylist[j])
        print("")
         
 
    if f'<tuple> <atom label="OnlineStore/Admin"/> <atom label="OnlineStore/AdminId"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class1_name} Attribute {c1_at1}: {c1_at1_type} \n Primary Key")
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Admin"/> <atom label="OnlineStore/AdminName"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class1_name} Attribute {c1_at2}: {c1_at2_type}")
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Customer"/> <atom label="OnlineStore/CustomerId"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} Attribute {c2_at1}: {c2_at1_type} \n Primary Key")
        a8 = mylist[j]
        file_object.write(a8)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
           
    if f'<tuple> <atom label="OnlineStore/Customer"/> <atom label="OnlineStore/PhoneNo"/> </tuple>"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} Attribute {c2_at4}: {c2_at4_type}")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f' <tuple> <atom label="OnlineStore/Customer"/> <atom label="OnlineStore/CustomerName"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} Attribute {c2_at2}: {c2_at2_type}")
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="OnlineStore/Customer"/> <atom label="OnlineStore/Address"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} Attribute {c2_at3}: {c2_at3_type}")
        a11 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
        
    if f'<tuple> <atom label="OnlineStore/Payment"/> <atom label="OnlineStore/PaymentId"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} Attribute {c3_at1}: {c3_at1_type} \n Primary Key")
        a12 = mylist[j]
        file_object.write(a12)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    
    if f'<tuple> <atom label="OnlineStore/Payment"/> <atom label="OnlineStore/CardNo"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} Attribute {c3_at4}: {c3_at4_type}")
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Payment"/> <atom label="OnlineStore/PaymentName"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} Attribute {c3_at2}: {c3_at2_type}")
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
        
    if f'<tuple> <atom label="OnlineStore/Payment"/> <atom label="OnlineStore/CardType"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} Attribute {c3_at3}: {c3_at3_type}")
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        print(mylist[j])
        print("")
            
       
    if f'<tuple> <atom label="OnlineStore/Guest"/> <atom label="OnlineStore/GuestId"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class4_name} Attribute {c4_at1}: {c4_at1_type} \n Primary Key")
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
       
    if f'<tuple> <atom label="OnlineStore/Products"/> <atom label="OnlineStore/ProductsId"/> </tuple>"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name} Attribute {c5_at1}: {c5_at1_type} \n Primary Key")
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")
        print(mylist[j])
        print("")
    
    
    if f'<tuple> <atom label="OnlineStore/Products"/> <atom label="OnlineStore/ProductsName"/> </tuple>"/> </tuple>"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name} Attribute {c5_at2}: {c5_at2_type}")
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Products"/> <atom label="OnlineStore/Group"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name} Attribute {c5_at3}: {c5_at3_type}")
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Products"/> <atom label="OnlineStore/Subgroup"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name} Attribute {c5_at4}: {c5_at4_type}")
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Cart"/> <atom label="OnlineStore/CartId"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name} Attribute {c6_at1}: {c6_at1_type} \n Primary Key")
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="OnlineStore/Cart"/> <atom label="OnlineStore/NumOfProducts"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name} Attribute {c6_at2}: {c6_at2_type}")
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
        
    if f'<tuple> <atom label="OnlineStore/Cart"/> <atom label="OnlineStore/Price"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name} Attribute {c6_at3}: {c6_at3_type}")
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'<tuple> <atom label="OnlineStore/Cart"/> <atom label="OnlineStore/Total"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name} Attribute {c6_at4}: {c6_at4_type}")
        a24 = mylist[j]
        file_object.write(a24)
        file_object.write("\n")
        print(mylist[j])
        print("")   
           

    
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Admin"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class1_name} : {map_str2}")
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Admin"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class1_name} : {map_str1}")
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Admin"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class1_name} : {map_str3}")
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
#------------------------------------------------------------------------------------
        
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name} : {map_str2}")
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name} : {map_str1}")
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class2_name} : {map_str3}")
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
        
#---------------------------------------------------------------------


    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Payment"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name} : {map_str2}")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Payment"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name} : {map_str1}")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Payment"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class3_name} : {map_str3}")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        print(mylist[j])
        print("") 
  
 #-------------------------------------------------------------------------
    
    
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Guest"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class4_name} : {map_str2}")
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Guest"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class4_name} : {map_str1}")
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Guest"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class4_name} : {map_str3}")
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")
        print(mylist[j])
        print("") 
    
  #-------------------------------------------------------------------------------


    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Products"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class5_name} : {map_str2}")
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Products"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class5_name} : {map_str1}")
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Products"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class5_name} : {map_str3}")
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
   #----------------------------------------------------------------


    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="OnlineStore/Cart"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class6_name} : {map_str2}")
        a30 = mylist[j]
        file_object.write(a30)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="OnlineStore/Cart"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class6_name} : {map_str1}")
        a30 = mylist[j]
        file_object.write(a30)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="OnlineStore/Cart"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy for {class6_name} : {map_str3}")
        a30 = mylist[j]
        file_object.write(a30)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
#---------------------------------------------------------


    
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="OnlineStore/ProductsGuestAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3} : ForeignKeyEmbeddingStrategy")
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n")
        print(mylist[j])
        print("")  
    
    
    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="OnlineStore/ProductsGuestAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3} : OwnAssociationTableStrategy")
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n")
        print(mylist[j])
        print("")  
        
        #---------------------------------------------------------------------------
        
    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="OnlineStore/AdminProductsAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1} : OwnAssociationTableStrategy")
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="OnlineStore/AdminProductsAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1} : ForeignKeyEmbeddingStrategy")
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n")
        print(mylist[j])
        print("")  
        
      #-------------------------------------------------------------------------------
    
    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="OnlineStore/CustomerProductsAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2} : OwnAssociationTableStrategy")
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="OnlineStore/CustomerProductsAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2} : ForeignKeyEmbeddingStrategy")
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")
        print(mylist[j])
        print("")  
          
    
    #-----------------------------------------------------------------------------
       
    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="OnlineStore/CustomerCartAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4} : OwnAssociationTableStrategy")
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="OnlineStore/CustomerCartAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4} : ForeignKeyEmbeddingStrategy")
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
        print(mylist[j])
        print("")  
          
     #-------------------------------------------------------------------------
    
    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="OnlineStore/CustomerPaymentAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5} : OwnAssociationTableStrategy")
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
        
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="OnlineStore/CustomerPaymentAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5} : ForeignKeyEmbeddingStrategy")
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        file_object.close()
           
    
        
     
        
print("------------------------------------------------------------------")

