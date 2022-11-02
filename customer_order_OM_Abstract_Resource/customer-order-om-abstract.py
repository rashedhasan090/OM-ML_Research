
file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "customerOrderObjectModel"
om_count = 0 

class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "Integer"
c1_at2_type = "string"
c1_at2 = "customerName"
c1_at3 = "DType"
c1_at3_type = "varchar"


class2_name = "Order"
c2_at1 = "orderID"
c2_at1_type = "Integer"
c2_at2 = "orderValue"
c2_at2_type = "Real"

assoc1 = "CustomerOrderAssociation"
src_mlpc = "ONE"
dst_mlpc = "MANY"

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

src_mlpc_0 = "src_mlpc"
dst_mlpc_0 = "dst_mlpc"

class3_name_0 = "class3_name"
c3_at1_0 = "c3_at1"
c3_at1_type_0 = "c3_at1_type"

map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

file_object = open(f'Customer_Order_OM_Abstract_only.txt', 'a')


for j in range(len(mylist)):
    
    if f"module {OM_name}" in mylist[j]:
        mylist[j] = (f"module {OM_name_0}")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        om_count += 1
        
    
    if f'one sig {class1_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class1_name_0} extends Class')
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")
        
        
    if f'attrSet = {c1_at1}+{c1_at2}' in mylist[j]:
        
        mylist[j] = (f"attrSet = {c1_at1_0}+{c1_at2_0}")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        
    if f'id={c1_at1}' in mylist[j]:
        
        mylist[j] = (f'id={c1_at1_0}')
        a3 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        
        
    if f'isAbstract = No' in mylist[j]:
        
        mylist[j] = ('isAbstract = No')
        a4 = mylist[j]
        file_object.write(a4)
        file_object.write("\n")
        
        
        
    if f'no parent' in mylist[j]:
        
        mylist[j] = ('no parent')
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")
        
        
    if f'one sig {c1_at1} extends {c1_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c1_at1_0} extends {c1_at1_type_0}')
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")  
        file_object.write("\n")
       
    if f'one sig {c1_at2} extends {c1_at2_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c1_at2_0} extends {c1_at2_type_0}')
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")
        file_object.write("\n")
        
    if f'one sig {class2_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class2_name_0} extends Class')
        a8 = mylist[j]
        file_object.write(a8)
        file_object.write("\n")
        
        
    if f'attrSet = {c2_at1}+{c2_at2}' in mylist[j]:
        
        mylist[j] = (f"attrSet = {c2_at1_0}+{c2_at2_0}")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        
    if f'id={c2_at1}' in mylist[j]:
        
        mylist[j] = (f"id={c2_at1_type}")
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")
        
        
    if f'one sig {c2_at1} extends {c2_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c2_at1_0} extends {c2_at1_type_0}')
        a11 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")  
        file_object.write("\n")
        
        
    if f'one sig {c2_at2} extends {c2_at2_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c2_at2_0} extends {c2_at2_type_0}')
        a12 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")  
        file_object.write("\n")
        
        

    if f'one sig {assoc1} extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc1_0} extends Association')
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")  
        
        
    if f'src = {class1_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class1_name_0}')
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")  
        
    if f'dst = {class2_name}' in mylist[j]:
        
        mylist[j] = (f'dst = {class2_name_0}')
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        
    if f'src_multiplicity = {src_mlpc}' in mylist[j]:
        
        mylist[j] = (f'src_multiplicity = {src_mlpc_0}')
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        
    if f'dst_multiplicity = {dst_mlpc}' in mylist[j]:
        
        mylist[j] = (f'dst_multiplicity = {dst_mlpc_0}')
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")
        
         
    if f'one sig {class3_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class3_name_0} extends Class')
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        
         
    if f'attrSet = {c3_at1}' in mylist[j]:
        
        mylist[j] = (f'attrSet = {c3_at1_0}')
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        
    if f'one parent' in mylist[j]:
        
        mylist[j] = (f'one parent')
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
        
    if f'parent in {class1_name}' in mylist[j]:
        
        mylist[j] = (f'parent in {class1_name_0}')
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")  
        
        
    if f'one sig {c3_at1} extends {c3_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c3_at1_0} extends {c3_at1_type_0}')
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")  
        
        
    if f'pred show' in mylist[j]:
        
        mylist[j] = (f'pred show')
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")
        
        
    if f'run show for 16' in mylist[j]:
        
        mylist[j] = (f'run show for 16')
        a24 = mylist[j]
        file_object.write(a24)
        file_object.write("\n")
        file_object.close() 
        
        
    
    # no need to use replace if you're going to change the whole string

        
#print(mylist)

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1
