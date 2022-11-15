#Generate Abstract from saved file 
#OnlineStore Mapping Abstract Generator 

file_name = input("Enter File Name to Generate Abstract: ")
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

assoc_type1 = "ForeignKeyEmbeddingStrategy"
assoc_type2 = "OwnAssociationTableStrategy"

src_mlpc = "ONE"
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
c1_at2_type_0 = "c1_at2_type"
c1_at2_0 = "c1_at2"

class2_name_0 = "class2_name"
c2_at1_0 = "c2_at1"
c2_at1_type_0 = "c2_at1_type"
c2_at2_0 = "c2_at2"
c2_at2_type_0 = "c2_at2_type"
c2_at3_0 = "c2_at3"
c2_at3_type_0 = "c2_at3_type"
c2_at4_0 = "c2_at4"
c2_at4_type_0 = "c2_at4_type"

class3_name_0 = "class3_name"
c3_at1_0 = "c3_at1"
c3_at1_type_0 = "c3_at1_type"
c3_at2_0 = "c3_at2"
c3_at2_type_0 = "c3_at2_type"
c3_at3_0 = "c3_at3"
c3_at3_type_0 = "c3_at3_type"
c3_at4_0 = "c3_at4"
c3_at4_type_0 = "c3_at4_type"

class4_name_0 = "class4_name"
c4_at1_0 = "c4_at1"
c4_at1_type_0 = "c4_at1_type"

class5_name_0 = "class5_name"
c5_at1_0 = "c5_at1"
c5_at1_type_0 = "c5_at1_type"
c5_at2_0 = "c5_at2"
c5_at2_type_0 = "c5_at2_type"
c5_at3_0 = "c5_at3"
c5_at3_type_0 = "c5_at3_type"
c5_at4_0 = "c5_at4"
c5_at4_type_0 = "c5_at4_type"

class6_name_0 = "class6_name"
c6_at1_0 = "c6_at1"
c6_at1_type_0 = "c6_at1_type"
c6_at2_0 = "c6_at2"
c6_at2_type_0 = "c6_at2_type"
c6_at3_0 = "c6_at3"
c6_at3_type_0 = "c6_at3_type"
c6_at4_0 = "c6_at4"
c6_at4_type_0 = "c6_at4_type"


assoc1_0 = "assoc1"
assoc2_0 = "assoc2"
assoc3_0 = "assoc3"
assoc4_0 = "assoc4"
assoc5_0 = "assoc5"
assoc_type1_0 = "assoc_type1"
assoc_type2_0 = "assoc_type2"

src_mlpc_0 = "src_mlpc"
dst_mlpc_0 = "dst_mlpc"
dst_mlpc2_0 = "dst_mlpc2"


map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

file_object = open(f'Online_Store_Mapping_strategy_abstract_1.txt', 'a')


for j in range(len(mylist)):
    
    if f'{OM_name}' in mylist[j]:
        mylist[j] = (f"{OM_name_0}_Solution : {om_count}")
        om_count += 1
        b0 = mylist[j]
        file_object.write(b0)
        file_object.write("\n")
        print(mylist[j])
        print("")
    
    if f'Table Name: {class1_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class1_name_0}")
        b1 = mylist[j]
        file_object.write(b1)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Table Name: {class2_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name_0}")
        b2 = mylist[j]
        file_object.write(b2)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Table Name: {class3_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name_0}")
        b3 = mylist[j]
        file_object.write(b3)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table Name: {class4_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class4_name_0}")
        b4 = mylist[j]
        file_object.write(b4)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table Name: {class5_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class5_name_0}")
        b5 = mylist[j]
        file_object.write(b5)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
        
    if f'Table Name: {class6_name}' in mylist[j]:
        mylist[j] = (f"Table Name: {class6_name_0}")
        b6 = mylist[j]
        file_object.write(b6)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Table: {class1_name} Attribute {c1_at1}: {c1_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class1_name_0} Attribute {c1_at1_0}: {c1_at1_type_0} \n Primary Key")
        b7 = mylist[j]
        file_object.write(b7)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'Table: {class1_name} Attribute {c1_at2}: {c1_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class1_name_0} Attribute {c1_at2_0}: {c1_at2_type_0}")
        b8 = mylist[j]
        file_object.write(b8)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
     
    if f'Table: {class2_name} Attribute {c2_at1}: {c2_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class2_name_0} Attribute {c2_at1_0}: {c1_at1_type_0} \n Primary Key")
        b9 = mylist[j]
        file_object.write(b9)
        file_object.write("\n")
        print(mylist[j])
        print("")
    
    if f'Table: {class2_name} Attribute {c2_at2}: {c2_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class2_name_0} Attribute {c2_at2_0}: {c2_at2_type_0}")
        b10 = mylist[j]
        file_object.write(b10)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class2_name} Attribute {c2_at3}: {c2_at3_type}' in mylist[j]:
        mylist[j] = (f"Table: {class2_name_0} Attribute {c2_at3_0}: {c2_at3_type_0}")
        b11 = mylist[j]
        file_object.write(b11)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Table: {class2_name} Attribute {c2_at4}: {c2_at4_type}' in mylist[j]:
        mylist[j] = (f"Table: {class2_name_0} Attribute {c2_at4_0}: {c2_at4_type_0}")
        b12 = mylist[j]
        file_object.write(b12)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class3_name} Attribute {c3_at1}: {c3_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Attribute {c3_at1_0}: {c3_at1_type_0} \n Primary Key")
        b13 = mylist[j]
        file_object.write(b13)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class3_name} Attribute {c3_at2}: {c3_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Attribute {c3_at2_0}: {c3_at2_type_0}")
        b14 = mylist[j]
        file_object.write(b14)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
        
    if f'Table: {class3_name} Attribute {c3_at4}: {c3_at4_type}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Attribute {c3_at4_0}: {c3_at4_type_0}")
        b15 = mylist[j]
        file_object.write(b15)
        file_object.write("\n")
        print(mylist[j])
        print("")


          
    if f'Table: {class4_name} Attribute {c4_at1}: {c4_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class4_name_0} Attribute {c4_at1_0}: {c4_at1_type_0} \n Primary Key")
        b16 = mylist[j]
        file_object.write(b16)
        file_object.write("\n")
        print(mylist[j])
        print("")
      
        
        
    if f'Table: {class5_name} Attribute {c5_at1}: {c5_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class5_name_0} Attribute {c5_at1_0}: {c5_at1_type_0} \n Primary Key")
        b17 = mylist[j]
        file_object.write(b17)
        file_object.write("\n")
        print(mylist[j])
        print("")
      
    
            
    if f'Table: {class5_name} Attribute {c5_at2}: {c5_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class5_name_0} Attribute {c5_at2_0}: {c5_at2_type_0}")
        b18 = mylist[j]
        file_object.write(b18)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table: {class5_name} Attribute {c5_at3}: {c5_at3_type}' in mylist[j]:
        mylist[j] = (f"Table: {class5_name_0} Attribute {c5_at3_0}: {c5_at3_type_0}")
        b19 = mylist[j]
        file_object.write(b19)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table: {class5_name} Attribute {c5_at4}: {c5_at4_type}' in mylist[j]:
        mylist[j] = (f"Table: {class5_name_0} Attribute {c5_at4_0}: {c5_at4_type_0}")
        b20 = mylist[j]
        file_object.write(b20)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table: {class6_name} Attribute {c6_at1}: {c6_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class6_name_0} Attribute {c6_at1_0}: {c6_at1_type_0} \n Primary Key")
        b21 = mylist[j]
        file_object.write(b21)
        file_object.write("\n")
        print(mylist[j])
        print("")
      
      
        
    if f'Table: {class6_name} Attribute {c6_at2}: {c6_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class6_name_0} Attribute {c6_at2_0}: {c6_at2_type_0}")
        b22 = mylist[j]
        file_object.write(b22)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Table: {class6_name} Attribute {c6_at3}: {c6_at3_type}' in mylist[j]:
        mylist[j] = (f"Table: {class6_name_0} Attribute {c6_at3_0}: {c6_at3_type_0}")
        b23 = mylist[j]
        file_object.write(b23)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Table: {class6_name} Attribute {c6_at4}: {c6_at4_type}' in mylist[j]:
        mylist[j] = (f"Table: {class6_name_0} Attribute {c6_at4_0}: {c6_at4_type_0}")
        b24 = mylist[j]
        file_object.write(b24)
        file_object.write("\n")
        print(mylist[j])
        print("")
     
    
    if f'Mapping Strategy for {class1_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str2_0}")
        b25 = mylist[j]
        file_object.write(b25)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class1_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str1_0}")
        b25 = mylist[j]
        file_object.write(b25)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class1_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str3_0}")
        b25 = mylist[j]
        file_object.write(b25)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class2_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str2_0}")
        b26 = mylist[j]
        file_object.write(b26)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class2_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str1_0}")
        b26 = mylist[j]
        file_object.write(b26)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class2_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str3_0}")
        b26 = mylist[j]
        file_object.write(b26)
        file_object.write("\n")
        print(mylist[j])
        print("")   
        
        
    if f'Mapping Strategy for {class3_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str2_0}")
        b27 = mylist[j]
        file_object.write(b27)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class3_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str1_0}")
        b27 = mylist[j]
        file_object.write(b27)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class3_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str3_0}")
        b27 = mylist[j]
        file_object.write(b27)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class4_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class4_name_0}: {map_str1_0}")
        b28 = mylist[j]
        file_object.write(b28)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class4_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class4_name_0}: {map_str2_0}")
        b28 = mylist[j]
        file_object.write(b28)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class4_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class4_name_0}: {map_str2_0}")
        b28 = mylist[j]
        file_object.write(b28)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class5_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class5_name_0}: {map_str1_0}")
        b29 = mylist[j]
        file_object.write(b29)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class5_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class5_name_0}: {map_str2_0}")
        b29 = mylist[j]
        file_object.write(b29)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class5_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class5_name_0}: {map_str2_0}")
        b29 = mylist[j]
        file_object.write(b29)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class6_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class6_name_0}: {map_str1_0}")
        b30 = mylist[j]
        file_object.write(b30)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Mapping Strategy for {class6_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class6_name_0}: {map_str2_0}")
        b30 = mylist[j]
        file_object.write(b30)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy for {class6_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class6_name_0}: {map_str2_0}")
        b30 = mylist[j]
        file_object.write(b30)
        file_object.write("\n")
        print(mylist[j])
        print("")
  

    if f'Association Strategy for {assoc1} : {assoc_type1}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_type1_0}")
        b31 = mylist[j]
        file_object.write(b31)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'Association Strategy for {assoc1} : {assoc_type2}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_type2_0}")
        b31 = mylist[j]
        file_object.write(b31)
        file_object.write("\n")
        print(mylist[j])
        print("")  
        
        
    if f'Association Strategy for {assoc2} : {assoc_type1}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_type1_0}")
        b32 = mylist[j]
        file_object.write(b32)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'Association Strategy for {assoc2} : {assoc_type2}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_type2_0}")
        b32 = mylist[j]
        file_object.write(b32)
        file_object.write("\n")
        print(mylist[j])
        print("")  
        
        
    if f'Association Strategy for {assoc3} : {assoc_type1}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_type1_0}")
        b33 = mylist[j]
        file_object.write(b33)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'Association Strategy for {assoc3} : {assoc_type2}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_type2_0}")
        b33 = mylist[j]
        file_object.write(b33)
        file_object.write("\n")
        print(mylist[j])
        print("")  


    if f'Association Strategy for {assoc4} : {assoc_type1}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_type1_0}")
        b34 = mylist[j]
        file_object.write(b34)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'Association Strategy for {assoc4} : {assoc_type2}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_type2_0}")
        b34 = mylist[j]
        file_object.write(b34)
        file_object.write("\n")
        print(mylist[j])
        print("")  

        
        
        
    if f'Association Strategy for {assoc5} : {assoc_type1}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_type1_0}")
        b35 = mylist[j]
        file_object.write(b35)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'Association Strategy for {assoc5} : {assoc_type2}' in mylist[j]:
        mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_type2_0}")
        b35 = mylist[j]
        file_object.write(b35)
        file_object.write("\n")
        print(mylist[j])
        print("")  

     
