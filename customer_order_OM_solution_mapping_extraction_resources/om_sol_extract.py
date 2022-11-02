
#Extract Solution Mapping Strategy

file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "customerOrderObjectModel"
om_count = 0 

class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "Integer"
c1_at2_type = "varchar"
c1_at2 = "customerName"
c1_at3 = "DType"
c1_at3_type = "varchar"


class2_name = "Order"
c2_at1 = "orderID"
c2_at1_type = "Integer"
c2_at2 = "orderValue"
c2_at2_type = "decimal"

assoc1 = "CustomerOrderAssociation"

class3_name = "PreferredCustomer"
c3_at1 = "discount"
c3_at1_type = "Integer"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"

reg1 = "/> <atom label="
str1 = '<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="customerOrderObjectModel/PreferredCustomer"/></tuple>'

str2 = "customerOrderObjectModel/Customer"



file_object = open(f'OM_Mapping_strategy_1.txt', 'a')
   




for j in range(len(mylist)):
    
    if f'Run mapping_run_customerOrderObjectModel for 11' in mylist[j]:
        mylist[j] = (f"{OM_name}_Solution : {om_count} ")
        a00 = mylist[j]
        file_object.write(a00)
        file_object.write("\n")
        print(mylist[j])
        print("")
        om_count += 1
        
        
    if f'<sig label="customerOrderObjectModel/Customer" ID="20" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class1_name} ")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
       
    
    if f'<tuple> <atom label="customerOrderObjectModel/Customer"/> <atom label="customerOrderObjectModel/customerID"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class1_name} Attribute {c1_at1}: {c1_at1_type} \n Primary Key")
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")
        print(mylist[j])
        print("") 
    
    if f'<tuple> <atom label="customerOrderObjectModel/Customer"/> <atom label="customerOrderObjectModel/customerName"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class1_name} Attribute {c1_at2}: {c1_at2_type}")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        print(mylist[j])
        print("") 
    

       
    if f'<sig label="customerOrderObjectModel/Order" ID="21" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class2_name} ")
        a3 = mylist[j]
        file_object.write(a3)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
      
    if f'<tuple> <atom label="customerOrderObjectModel/Order"/> <atom label="customerOrderObjectModel/orderID"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class2_name} Attribute {c2_at1}: {c2_at1_type} \n Primary Key")
        a4 = mylist[j]
        file_object.write(a4)
        file_object.write("\n")
        print(mylist[j])
        print("") 
        
    if f'<tuple> <atom label="customerOrderObjectModel/Order"/> <atom label="customerOrderObjectModel/orderValue"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class2_name} Attribute {c2_at2}: {c2_at2_type}")
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")
        print(mylist[j])
        print("") 
    
        
    if f'<sig label="customerOrderObjectModel/PreferredCustomer" ID="22" parentID="10" one="yes">' in mylist[j]:
        mylist[j] = (f"Table Name: {class3_name} ")
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")
        print(mylist[j])
        print("")
           
        
    if f'<tuple> <atom label="customerOrderObjectModel/PreferredCustomer"/> <atom label="customerOrderObjectModel/discount"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class3_name} Attribute {c3_at1}: {c3_at1_type} ")
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")
        print(mylist[j])
        print("")
  
    if f'<tuple> <atom label="customerOrderObjectModel/PreferredCustomer"/> <atom label="customerOrderObjectModel/customerID"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class3_name} Attribute {c1_at1}: {c1_at1_type} \n Foreign Key ")
        a8 = mylist[j]
        file_object.write(a8)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="customerOrderObjectModel/PreferredCustomer"/> <atom label="customerOrderObjectModel/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Table: {class3_name} Parent Class {class1_name} ")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        print(mylist[j])
        print("")
              
        
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="customerOrderObjectModel/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name} : {map_str2}")
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="customerOrderObjectModel/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name} : {map_str1}")
        a11 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
 
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="customerOrderObjectModel/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name} : {map_str3}")
        a12 = mylist[j]
        file_object.write(a12)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="customerOrderObjectModel/Order"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name} : {map_str2}")
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="customerOrderObjectModel/Order"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name} : {map_str1}")
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
 
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="customerOrderObjectModel/Order"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name} : {map_str3}")
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="customerOrderObjectModel/PreferredCustomer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name} : {map_str2}")
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        

    if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="customerOrderObjectModel/PreferredCustomer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name} : {map_str1}")
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
 
    if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="customerOrderObjectModel/PreferredCustomer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name} : {map_str3}")
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'<tuple> <atom label="customerOrderObjectModel/CustomerOrderAssociation"/> <atom label="customerOrderObjectModel/Customer"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Table {assoc1} \n Source : {class1_name}")
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'<tuple> <atom label="customerOrderObjectModel/CustomerOrderAssociation"/> <atom label="customerOrderObjectModel/Order"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Table {assoc1} \n Destination : {class2_name}")
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")
        print(mylist[j])
        print("")
    
    
    if f'<tuple> <atom label="customerOrderObjectModel/CustomerOrderAssociation"/> <atom label="AssociationMappings/Declaration/MANY"/> </tuple>' in mylist[j]:
        mylist[j] = (f"One To Many Association \n Source > Destination")
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")
        print(mylist[j])
        print("")
        

           
    if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="customerOrderObjectModel/CustomerOrderAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Mapping Strategy: Foreign Key Embedding")
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")
        print(mylist[j])
        print("")
        



    if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="customerOrderObjectModel/CustomerOrderAssociation"/> </tuple>' in mylist[j]:
        mylist[j] = (f"Association Mapping Strategy: Own Association Table")
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")
        file_object.close()
        print(mylist[j])
        print("")
        
        
print("------------------------------------------------------------------")


#Generate Abstract from saved file 

file_name = input("Enter File Name to Generate Abstract: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "customerOrderObjectModel"
om_count = 0 

class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "Integer"
c1_at2_type = "varchar"
c1_at2 = "customerName"
c1_at3 = "DType"
c1_at3_type = "varchar"


class2_name = "Order"
c2_at1 = "orderID"
c2_at1_type = "Integer"
c2_at2 = "orderValue"
c2_at2_type = "decimal"

assoc1 = "CustomerOrderAssociation"

class3_name = "PreferredCustomer"
c3_at1 = "discount"
c3_at1_type = "Integer"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"

OM_name_0 = "OM_name"

class1_name_0 = "class1_name"
c1_at1_0 = "c1_at1"
c1_at1_type_0 = "c1_at1_type"
c1_at2_type_0 = "c1_at2_type"
c1_at2_0 = "c1_at2"
c1_at3_0 = "c1_at3"
c1_at3_type_0 = "c1_at3_type"


class2_name_0 = "class2_name"
c2_at1_0 = "c2_at1"
c2_at1_type_0 = "c2_at1_type"
c2_at2_0 = "c2_at2"
c2_at2_type_0 = "c2_at2_type"

assoc1_0 = "assoc1"

class3_name_0 = "class3_name"
c3_at1_0 = "c3_at1"
c3_at1_type_0 = "c3_at1_type"

map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

file_object = open(f'OM_Mapping_strategy_abstract_1.txt', 'a')


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
        
    if f'Table: {class1_name} Attribute {c1_at1}: {c1_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class1_name_0} Attribute {c1_at1_0}: {c1_at1_type_0} \n Primary Key")
        b4 = mylist[j]
        file_object.write(b4)
        file_object.write("\n")
        print(mylist[j])
        print("")


    if f'Table: {class1_name} Attribute {c1_at2}: {c1_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class1_name_0} Attribute {c1_at2_0}: {c1_at2_type_0}")
        b5 = mylist[j]
        file_object.write(b5)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class2_name} Attribute {c2_at2}: {c2_at2_type}' in mylist[j]:
        mylist[j] = (f"Table: {class2_name_0} Attribute {c2_at2_0}: {c1_at2_type_0}")
        b6 = mylist[j]
        file_object.write(b6)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class3_name} Attribute {c3_at1}: {c3_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Attribute {c3_at1_0}: {c3_at1_type_0}")
        b7 = mylist[j]
        file_object.write(b7)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class3_name} Attribute {c1_at1}: {c1_at1_type}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Attribute {c1_at1_0}: {c1_at1_type_0} \n Foreign Key")
        b8 = mylist[j]
        file_object.write(b8)
        file_object.write("\n")
        print(mylist[j])
        print("")

    if f'Table: {class3_name} Parent Class {class1_name}' in mylist[j]:
        mylist[j] = (f"Table: {class3_name_0} Parent Class {class1_name_0}")
        b9 = mylist[j]
        file_object.write(b9)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Association Table {assoc1}' in mylist[j]:
        mylist[j] = (f"Association Table {assoc1_0}")
        b10 = mylist[j]
        file_object.write(b10)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
     
    if f'Source : {class1_name}' in mylist[j]:
        mylist[j] = (f"Source : {class1_name_0}")
        b11 = mylist[j]
        file_object.write(b11)
        file_object.write("\n")
        print(mylist[j])
        print("")
       
    if f'Destination : {class2_name}' in mylist[j]:
        mylist[j] = (f"Destination : {class2_name_0}")
        b12 = mylist[j]
        file_object.write(b12)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'One To Many Association' in mylist[j]:
        mylist[j] = (f"One To Many Association")
        b13 = mylist[j]
        file_object.write(b13)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
        
    if f'Source > Destination' in mylist[j]:
        mylist[j] = (f"Source > Destination")
        b14 = mylist[j]
        file_object.write(b14)
        file_object.write("\n")
        print(mylist[j])
        print("")
     
    
    if f'Mapping Strategy of Table {class1_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str2_0}")
        b15 = mylist[j]
        file_object.write(b15)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class1_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str1_0}")
        b16 = mylist[j]
        file_object.write(b16)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class1_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class1_name_0}: {map_str3_0}")
        b17 = mylist[j]
        file_object.write(b17)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class2_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str2_0}")
        b18 = mylist[j]
        file_object.write(b18)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class2_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str1_0}")
        b19 = mylist[j]
        file_object.write(b19)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class2_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class2_name_0}: {map_str3_0}")
        b20 = mylist[j]
        file_object.write(b20)
        file_object.write("\n")
        print(mylist[j])
        print("")   
        
        
    if f'Mapping Strategy of Table {class3_name} : {map_str2}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str2_0}")
        b21 = mylist[j]
        file_object.write(b21)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class3_name} : {map_str1}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str1_0}")
        b22 = mylist[j]
        file_object.write(b22)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Mapping Strategy of Table {class3_name} : {map_str3}' in mylist[j]:
        mylist[j] = (f"Mapping Strategy of Table {class3_name_0}: {map_str3_0}")
        b23 = mylist[j]
        file_object.write(b23)
        file_object.write("\n")
        print(mylist[j])
        print("")
      
    if f'Association Mapping Strategy: Foreign Key Embedding' in mylist[j]:
        mylist[j] = (f"Association Mapping Strategy: Foreign Key Embedding")
        b24 = mylist[j]
        file_object.write(b24)
        file_object.write("\n")
        print(mylist[j])
        print("")
        
    if f'Association Mapping Strategy: Own Association Table' in mylist[j]:
        mylist[j] = (f"Association Mapping Strategy: Own Association Table")
        b25 = mylist[j]
        file_object.write(b25)
        file_object.write("\n")
        file_object.close()
        print(mylist[j])
        print("")
        

        


     
    
    
        

