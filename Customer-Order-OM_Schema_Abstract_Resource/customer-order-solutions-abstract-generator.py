
file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "customerOrderObjectModel_Sol_"
om_count = 0 

class1_name = "Customer"
c1_at1 = "customerID"
c1_at1_type = "int"
c1_at2_type = "varchar"
c1_at2 = "customerName"
c1_at3 = "DType"
c1_at3_type = "varchar"


class2_name = "Order"
c2_at1 = "orderID"
c2_at1_type = "int"
c2_at2 = "orderValue"
c2_at2_type = "decimal"

assoc1 = "CustomerOrderAssociation"
src_mlpc = "ONE"
dst_mlpc = "MANY"

class3_name = "PreferredCustomer"
c3_at1 = "discount"
c3_at1_type = "Integer"

map_str1 = "Union Super Class"
map_str2 = "Union Sub Class"
map_str3 = "Joined Sub Class"

OM_name_0 = "OM_name_"

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

file_object = open(f'Customer_Order_Solution_Abstract_only_1.txt', 'a')


for j in range(len(mylist)):
    
    if f"USE {OM_name}" in mylist[j]:
        mylist[j] = (f"USE {OM_name_0}{om_count}")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        om_count += 1
        
    
    if f'CREATE TABLE `{class2_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class2_name_0}` (')
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")
        
        
    if f'`{c2_at2}` {c2_at2_type}' in mylist[j]:
        
        mylist[j] = (f"`{c2_at2_0}` {c2_at2_type_0}")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        
    if f'`{c2_at1}` {c2_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c2_at1_0}` {c2_at1_type_0} NOT NULL')
        a3 = mylist[j]
        file_object.write(a3)
        file_object.write("\n")
        
        
    if f'`{c1_at1}` {c1_at1_type},' in mylist[j]:
        
        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0},')
        a4 = mylist[j]
        file_object.write(a4)
        file_object.write("\n")
        
        
        
    if f'KEY `FK_{class2_name}_{c1_at1}_idx` (`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{class2_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`)')
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")
        
        
    if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c2_at1}`)')
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")  
        file_object.write("\n")
       
    if f'Table structure for table {class2_name}' in mylist[j]:
        
        mylist[j] = (f'Table structure for table {class2_name_0}')
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")
        file_object.write("\n")
        
    if f'Table structure for table {class3_name}' in mylist[j]:
        
        mylist[j] = (f'Table structure for table {class3_name_0}')
        a8 = mylist[j]
        file_object.write(a8)
        file_object.write("\n")
        
        
    if f'CREATE TABLE `{class3_name}`' in mylist[j]:
        
        mylist[j] = (f"CREATE TABLE `{class3_name_0}`")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        
    if f'`{c1_at2}` {c1_at2_type}' in mylist[j]:
        
        mylist[j] = (f"`{c1_at2_0}` {c1_at2_type_0}")
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")
        
        
    if f'`{c1_at1}` {c1_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0} NOT NULL')
        a11 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")  
        file_object.write("\n")
        
        
    if f'`{c3_at1}` {c3_at1_type}' in mylist[j]:
        
        mylist[j] = (f'`{c3_at1_0}` {c3_at1_type_0}')
        a12 = mylist[j]
        file_object.write(a12)
        file_object.write("\n")  
        file_object.write("\n")
        
        

    if f'KEY `FK_{class3_name}_{c1_at1}_idx` (`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{class3_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`)')
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")  
        
        
    if f'PRIMARY KEY (`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c1_at1_0}`)')
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")  
        
    if f'Table structure for table {class1_name}' in mylist[j]:
        
        mylist[j] = (f'Table structure for table {class1_name_0}')
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        
    if f'CREATE TABLE `{class1_name}`' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class1_name_0}`')
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        
    if f'ALTER TABLE `{class2_name}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{class2_name_0}`')
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")
        
         
    if f'ADD CONSTRAINT `FK_{class2_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class2_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        
         
    if f'ALTER TABLE `{class3_name}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{class3_name_0}`')
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
        
    if f'ADD CONSTRAINT `FK_{class3_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class3_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")
        
    if f'CREATE TABLE `{assoc1}`' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc1_0}`')
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")  
        
        
    if f'PRIMARY KEY (`{c2_at1}`,`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c2_at1_0}`,`{c1_at1_0}`)')
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")  
        
        
    if f'Table structure for table {assoc1}' in mylist[j]:
        
        mylist[j] = (f'Table structure for table {assoc1}')
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")
        
        
    if f'ALTER TABLE `{assoc1}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc1_0}`')
        a24 = mylist[j]
        file_object.write(a24)
        file_object.write("\n")
        
        
        
        
    if f'ADD CONSTRAINT `FK_{assoc1}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        

    if f'ADD CONSTRAINT `FK_{assoc1}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE' in mylist[j]:

        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE')
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
        
        
        
    if f'KEY `FK_{assoc1}_{c2_at1}_idx` (`{c2_at1}`)' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc1_0}_{c2_at1_0}_idx` (`{c2_at1_0}`)')
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")
        
          
    if f'KEY `FK_{assoc1}_{c1_at1}_idx` (`{c1_at1}`)' in mylist[j]:

        mylist[j] = (f'KEY `FK_{assoc1_0}_{c1_at1_0}_idx` (`{c1_at1_0}`)')
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")
        
        
    if f'`{c3_at1}` int' in mylist[j]:

        mylist[j] = (f'`{c3_at1_0}` int')
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        
        
    if f'`{c1_at3}` {c1_at3_type}(64)' in mylist[j]:

        mylist[j] = (f'`{c1_at3_0}` {c1_at3_type_0}(64)')
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        
        
        
        #file_object.close() 
        
       
        
        
        
    
    # no need to use replace if you're going to change the whole string

        
#print(mylist)

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1
