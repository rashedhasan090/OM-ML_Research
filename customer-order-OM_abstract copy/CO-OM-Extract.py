#Combined_Constraint_and_abstract_Generator_CustomerOrder_model_als file 




file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


#Variable Declaration 
OM_name = "customerOrderObjectModel"
class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "Integer"
c1_at2_type = "String"
c1_at2 = "customerName"

class2_name = "Order"
c2_at1 = "orderID"
c2_at1_type = "Integer"
c2_at2 = "orderValue"
c2_at2_type = "String"

assoc1 = "CustomerOrderAssociation"


class3_name = "PreferredCustomer"
c3_at1 = "discount"
c3_at1_type = "Integer"



for j in range(len(mylist)):
    
   ####### OM Name  
    if "module" in mylist[j]:
        mylist[j] = (f"module: Base_OM >{OM_name}")
        #table_count += 1
        #hist[0] = table_count - 1
        
    ####### Class 1
        
    if (f"one sig {class1_name} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class1_name} (Union Super Class)")
        #table_count += 1
        #hist[0] = table_count - 1
        
    if (f"attrSet = {c1_at1}+{c1_at2}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c1_at1}: {c1_at1_type} | {c1_at2}: {c1_at2_type}")
        #mylist[j] = (f"{c1_at2}: {c1_at2_type}")
        #table_count += 1
        #hist[0] = table_count - 1    
        
    if (f"id={c1_at1}") in mylist[j]:
        
        mylist[j] = (f"{c1_at1} - Primary Key")
        
     
    ######## Class 2 
    
    if (f"one sig {class2_name} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class2_name} (Joined Sub Class)")
        
    if (f"attrSet = {c2_at1}+{c2_at2}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c2_at1}: {c2_at1_type} | {c2_at2}: {c2_at2_type}")
        
    if (f"id={c2_at1}") in mylist[j]:
        
        mylist[j] = (f"{c1_at1} - Primary Key")
        
  ####### Association 1 
    
    if (f"one sig {assoc1} extends Association") in mylist[j]:
        mylist[j] = (f"Class {assoc1} (Association Type)")
        
    if (f"src = {class1_name}") in mylist[j]:
        mylist[j] = (f"Source Class: {class1_name} (for one {class1_name}  ) ")
         
    if (f"dst = {class2_name}") in mylist[j]:
        mylist[j] = (f"Destination Class: {class2_name} (Many {class2_name} )")   
        
    if (f"src_multiplicity = ONE") in mylist[j]:
        mylist[j] = (f"")   
        
    if (f"dst_multiplicity = MANY") in mylist[j]:
        mylist[j] = (f"")   
        
     
         
######## Class 3 
    
    if (f"one sig {class3_name} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class3_name} (Union Sub Class)")
        
    if (f"attrSet = {c3_at1}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c3_at1}: {c3_at1_type}")
        
    if (f"parent in {class1_name}") in mylist[j]:

        mylist[j] = (f"Parent Class - {class1_name}")
        
    if (f"isAbstract = No") in mylist[j]:
        mylist[j] = (f"")     
        
 ###### Deducting external entities 

    if (f"pred show") in mylist[j]:
        mylist[j] = (f"")    
        
    if (f"extends Integer") in mylist[j]:
        mylist[j] = (f"")  
   
    if (f"extends Real") in mylist[j]:
        mylist[j] = (f"")  
        
    if (f"extends string") in mylist[j]:
        mylist[j] = (f"")  
    
    if (f"run show for 16") in mylist[j]:
        mylist[j] = (f"") 
        
#Display Output 

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1


# Write Output to a file 

listToStr = ' '.join([str(elem) for elem in mylist])


f = open("Om_constraint_CustomerOrderOM.txt", "w+")
f.write(listToStr)
f.close()






#------------------------------------------------------------------------


#file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()

#mylist = ['one sig Order extends Class','one sig Customer extends Class', 'one sig PreferredCustomer extends Class', 'One sig computing extends Class', 'src = customer', 'dst = order']

# variable declaration 

OM_name_0 = "customerOrderObjectModel"
class1_name_0 = "Customer"
c1_at1_0 = "customerID"
c1_at1_type_0 = "Integer"
c1_at2_type_0 = "String"
c1_at2_0 = "customerName"

class2_name_0 = "Order"
c2_at1_0 = "orderID"
c2_at1_type_0 = "Integer"
c2_at2_0 = "orderValue"
c2_at2_type_0 = "String"

assoc1_0 = "CustomerOrderAssociation"

class3_name_0 = "PreferredCustomer"
c3_at1_0 = "discount"
c3_at1_type_0 = "Integer"

map_str1_0 = "Union Super Class"
map_str2_0 = "Union Sub Class"
map_str3_0 = "Joined Sub Class"

OM_name_1 = "OM_name"
class1_name_1 = "class1_name"
c1_at1_1 = "c1_at1"
c1_at1_type_1 = "c1_at1_type"
c1_at2_type_1 = "c1_at2_type"
c1_at2_1 = "c1_at2"

class2_name_1 = "class2_name"
c2_at1_1 = "c2_at1"
c2_at1_type_1 = "c2_at1_type"
c2_at2_1 = "c2_at2"
c2_at2_type_1 = "c2_at2_type"

assoc1_1 = "assoc1"

class3_name_1 = "class3_name"
c3_at1_1 = "c3_at1"
c3_at1_type_1 = "c3_at1_type"

map_str1_1 = "map_str1"
map_str2_1 = "map_str2"
map_str3_1 = "map_str3"


#computation in list 

for j in range(len(mylist)):
    
   ####### OM Name  
    if "module" in mylist[j]:
        mylist[j] = (f"module: Base_OM >{OM_name_0}")
        #table_count += 1
        #hist[0] = table_count - 1
        
    ####### Class 1
        
    if (f"one sig {class1_name_0} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class1_name_1} : (Table_Order_3_on_solution)")
        #table_count += 1
        #hist[0] = table_count - 1
        
    if (f"attrSet = {c1_at1_0}+{c1_at2_0}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c1_at1_1}: {c1_at1_type_1} | {c1_at2_1}: {c1_at2_type_1}")
        #mylist[j] = (f"{c1_at2}: {c1_at2_type}")
        #table_count += 1
        #hist[0] = table_count - 1    
        
    if (f"id={c1_at1_0}") in mylist[j]:
        
        mylist[j] = (f"{c1_at1_1} - Primary Key")
        
     
    ######## Class 2 
    
    if (f"one sig {class2_name_0} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class2_name_1}: (Table_Order_1_on_solution)")
        
    if (f"attrSet = {c2_at1_0}+{c2_at2_0}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c2_at1_1}: {c2_at1_type_1} | {c2_at2_1}: {c2_at2_type_1}")
        
    if (f"id={c2_at1_0}") in mylist[j]:
        
        mylist[j] = (f"{c1_at1_1} - Primary Key")
        
####### Association 1 
    
    if (f"one sig {assoc1_0} extends Association") in mylist[j]:
        mylist[j] = (f"Class {assoc1_1} (Association Type)")
        
    if (f"src = {class1_name_0}") in mylist[j]:
        mylist[j] = (f"Source Class: {class1_name_1} (for one {class1_name_1}  ) ")
         
    if (f"dst = {class2_name_0}") in mylist[j]:
        mylist[j] = (f"Destination Class: {class2_name_1} (Many {class2_name_1} )")   
        
    if (f"src_multiplicity = ONE") in mylist[j]:
        mylist[j] = (f"")   
        
    if (f"dst_multiplicity = MANY") in mylist[j]:
        mylist[j] = (f"")   
        
     
         
######## Class 3 
    
    if (f"one sig {class3_name_0} extends Class") in mylist[j]:
        mylist[j] = (f"Class {class3_name_1}: (Table_Order_2_on_solution)")
        
    if (f"attrSet = {c3_at1_0}") in mylist[j]:
        
        mylist[j] = (f"Attributes - {c3_at1_1}: {c3_at1_type_1}")
        
    if (f"parent in {class1_name_0}") in mylist[j]:

        mylist[j] = (f"Parent Class - {class1_name_1}")
        
    if (f"isAbstract = No") in mylist[j]:
        mylist[j] = (f"")     
        
 ###### Deducting external entities 

    if (f"pred show") in mylist[j]:
        mylist[j] = (f"")    
        
    if (f"extends Integer") in mylist[j]:
        mylist[j] = (f"")  
   
    if (f"extends Real") in mylist[j]:
        mylist[j] = (f"")  
        
    if (f"extends string") in mylist[j]:
        mylist[j] = (f"")  
    
    if (f"run show for 16") in mylist[j]:
        mylist[j] = (f"") 
        
# Display result 

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1
  
listToStr = ' '.join([str(elem) for elem in mylist])


# Write Abstract to a file 
f = open("Om_constraints_and_abs_CustomerOrderOM.txt", "w+")
f.write(listToStr)
f.close()
