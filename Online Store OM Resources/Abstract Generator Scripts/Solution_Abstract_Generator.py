
file_name = input("Enter The File's Name: ")
file_read = open(file_name, "r")
mylist = file_read.readlines()


OM_name = "OnlineStore_Sol_"
om_count = 0 

class1_name = "Admin"
c1_at1 = "AdminId"
c1_at1_type = "int"
c1_at2_type = "varchar"
c1_at2 = "AdminName"

class2_name = "Customer"
c2_at1 = "CustomerId"
c2_at1_type = "int"
c2_at2 = "CustomerName"
c2_at2_type = "varchar"
c2_at3 = "Address"
c2_at3_type = "varchar"
c2_at4 = "PhoneNo"
c2_at4_type = "int"

class3_name = "Payment"
c3_at1 = "PaymentId"
c3_at1_type = "int"
c3_at2 = "PaymentName"
c3_at2_type = "varchar"
c3_at3 = "CardType"
c3_at3_type = "varchar"
c3_at4 = "CardNo"
c3_at4_type = "int"

class4_name = "Guest"
c4_at1 = "GuestId"
c4_at1_type = "int"

class5_name = "Products"
c5_at1 = "ProductsId"
c5_at1_type = "int"
c5_at2 = "ProductsName"
c5_at2_type = "varchar"
c5_at3 = "Group"
c5_at3_type = "varchar"
c5_at4 = "Subgroup"
c5_at4_type = "varchar"

class6_name = "Cart"
c6_at1 = "CartId"
c6_at1_type = "int"
c6_at2 = "NumOfProducts"
c6_at2_type = "int"
c6_at3 = "Price"
c6_at3_type = "int"
c6_at4 = "Total"
c6_at4_type = "int"


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

src_mlpc_0 = "src_mlpc"
dst_mlpc_0 = "dst_mlpc"
dst_mlpc2_0 = "dst_mlpc2"


map_str1_0 = "map_str1"
map_str2_0 = "map_str2"
map_str3_0 = "map_str3"

file_object = open(f'OnlineStore_Solution_Abstract_only_1.txt', 'a')


for j in range(len(mylist)):
    
    if f"USE {OM_name}" in mylist[j]:
        mylist[j] = (f"USE {OM_name_0}{om_count}")
        a0 = mylist[j]
        file_object.write(a0)
        file_object.write("\n")
        om_count += 1
        

        
    
    if f'CREATE TABLE `{class5_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class5_name_0}` (')
        a1 = mylist[j]
        file_object.write(a1)
        file_object.write("\n")
        
        
    if f'`{c5_at4}` {c5_at4_type}(64)' in mylist[j]:
        
        mylist[j] = (f"`{c5_at4_0}` {c5_at4_type_0}(64)")
        a2 = mylist[j]
        file_object.write(a2)
        file_object.write("\n")
        
    if f'`{c5_at3}` {c5_at3_type}(64)' in mylist[j]:
        
        mylist[j] = (f'`{c5_at3_0}` {c5_at3_type_0}(64)')
        a3 = mylist[j]
        file_object.write(a3)
        file_object.write("\n")
        
        
    if f'`{c5_at2}` {c5_at2_type}(64)' in mylist[j]:
        
        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0},')
        a4 = mylist[j]
        file_object.write(a4)
        file_object.write("\n")
        
        
    if f'`{c5_at1}` {c5_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c5_at1_0}` {c5_at1_type_0},')
        a04 = mylist[j]
        file_object.write(a04)
        file_object.write("\n")
      
    if f'`{c4_at1}` {c4_at1_type}' in mylist[j]:
        
        mylist[j] = (f'`{c4_at1_0}` {c4_at1_type_0},')
        a004 = mylist[j]
        file_object.write(a004)
        file_object.write("\n")
        
    if f'`{c2_at1}` {c2_at1_type}' in mylist[j]:
        
        mylist[j] = (f'`{c2_at1_0}` {c2_at1_type_0},')
        a0004 = mylist[j]
        file_object.write(a0004)
        file_object.write("\n")
        
    if f'`{c1_at1}` {c1_at1_type}' in mylist[j]:
        
        mylist[j] = (f'`{c1_at1_0}` {c1_at1_type_0},')
        a00004 = mylist[j]
        file_object.write(a00004)
        file_object.write("\n")     
        
    if f'KEY `FK_{class5_name}_{c4_at1}_idx` (`{c4_at1}`),' in mylist[j]:
        
        mylist[j] = (f'FK_{class5_name_0}_{c4_at1_0}_idx` (`{c4_at1_0}`),')
        a5 = mylist[j]
        file_object.write(a5)
        file_object.write("\n")
        
        
    if f'KEY `FK_{class5_name}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        
        mylist[j] = (f'FK_{class5_name_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),')
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")
        
        
    if f'KEY `FK_{class5_name}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
        
        mylist[j] = (f'FK_{class5_name_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a6 = mylist[j]
        file_object.write(a6)
        file_object.write("\n")
        
        
    if f'PRIMARY KEY (`{c5_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c5_at1_0}`)')
        a7 = mylist[j]
        file_object.write(a7)
        file_object.write("\n")  
        file_object.write("\n")
       
   
  #-----------------------------------------------------------------------------------      
        

        
        
    
    if f'CREATE TABLE `{class3_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class3_name_0}` (')
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        
        
    if f'`{c3_at3}` {c3_at3_type}(64)' in mylist[j]:
        
        mylist[j] = (f"`{c3_at3_0}` {c3_at3_type_0}(64)")
        a10 = mylist[j]
        file_object.write(a10)
        file_object.write("\n")
        
    if f'`{c3_at2}` {c3_at2_type}(64)' in mylist[j]:
        
        mylist[j] = (f'`{c3_at2_0}` {c3_at2_type_0}(64)')
        a11 = mylist[j]
        file_object.write(a11)
        file_object.write("\n")
        
        
    if f'`{c3_at4}` {c3_at4_type}' in mylist[j]:
        
        mylist[j] = (f'`{c3_at4_0}` {c3_at4_type_0},')
        a12 = mylist[j]
        file_object.write(a12)
        file_object.write("\n")
        
        
    if f'`{c3_at1}` {c3_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c3_at1_0}` {c3_at1_type_0} NOT NULL,')
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")
      
    
    if f'PRIMARY KEY (`{c3_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c3_at1_0}`)')
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n") 
        
    #-----------------------------------------------------------------------------
    
 
        
        
    
    if f'CREATE TABLE `{class2_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class2_name_0}` (')
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        
        
    if f'`{c2_at3}` {c2_at3_type}(64)' in mylist[j]:
        
        mylist[j] = (f"`{c2_at3_0}` {c2_at3_type_0}(64)")
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        
    if f'`{c2_at2}` {c2_at2_type}(64)' in mylist[j]:
        
        mylist[j] = (f'`{c2_at2_0}` {c2_at2_type_0}(64)')
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")
        
        
    if f'`{c2_at4}` {c2_at4_type}' in mylist[j]:
        
        mylist[j] = (f'`{c2_at4_0}` {c2_at4_type_0},')
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n")
        
        
    if f'`{c2_at1}` {c2_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c2_at1_0}` {c2_at1_type_0} NOT NULL,')
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
      
    
    if f'PRIMARY KEY (`{c2_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c2_at1_0}`)')
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n") 
    
    
    #-----------------------------------------------------------------------
    

        
        
    
    if f'CREATE TABLE `{class4_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class4_name_0}` (')
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")
        
        
        
    if f'`{c4_at1}` {c4_at1_type} NOT NULL' in mylist[j]:
        
        mylist[j] = (f'`{c4_at1_0}` {c4_at1_type_0} NOT NULL,')
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")
      
    
    if f'PRIMARY KEY (`{c4_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c4_at1_0}`)')
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n") 
    
    #------------------------------------------------------------------
    
    

        
        
    
    if f'CREATE TABLE `{class1_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class1_name_0}` (')
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        
        
        
    if f'`{c1_at2}` {c1_at2_type}(64)' in mylist[j]:
        
        mylist[j] = (f'`{c1_at2_0}` {c1_at2_type_0}(64)')
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
      
    
    if f'PRIMARY KEY (`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c1_at1_0}`)')
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n") 
    
    
    #----------------------------------------------------------
    
    

        
        
    if f'CREATE TABLE `{assoc5}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc5_0}` (')
        a027 = mylist[j]
        file_object.write(a027)
        file_object.write("\n")
        
        
    
    if f'KEY `FK_{assoc5}_{c3_at1}_idx` (`{c3_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc5_0}_{c3_at1_0}_idx` (`{c3_at1_0}`),')
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n")
        
       
        
    if f'KEY `FK_{assoc5}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc5_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),')
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        
        
    if f'PRIMARY KEY (`{c3_at1}`,`{c2_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c3_at1_0}`,`{c2_at1_0}`)')
        a029 = mylist[j]
        file_object.write(a029)
        file_object.write("\n")
        
#-----------------------------------------------------------------------



        
        
    
    if f'CREATE TABLE `{class6_name}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{class6_name_0}` (')
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n")
        
        
        
    if f'`{c6_at4}` {c6_at4_type},' in mylist[j]:
        
        mylist[j] = (f'`{c6_at4_0}` {c6_at4_type_0},')
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n")
        
    if f'`{c6_at3}` {c6_at3_type},' in mylist[j]:
        
        mylist[j] = (f'`{c6_at3_0}` {c6_at3_type_0},')
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")
        
        
    if f'`{c6_at2}` {c6_at2_type},' in mylist[j]:
        
        mylist[j] = (f'`{c6_at2_0}` {c6_at2_type_0},')
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
      
    
    
    if f'`{c6_at1}` {c6_at1_type} NOT NULL,' in mylist[j]:
        
        mylist[j] = (f'`{c6_at1_0}` {c6_at1_type_0} NOT NULL,')
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n")

    
    if f'PRIMARY KEY (`{c6_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c6_at1_0}`)')
        a36 = mylist[j]
        file_object.write(a36)
        file_object.write("\n") 
    

#-------------------------------------------------------------------


  

        
        
    
    if f'CREATE TABLE `{assoc4}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc4_0}` (')
        a38 = mylist[j]
        file_object.write(a38)
        file_object.write("\n")
        
        
        
    if f'KEY `FK_{assoc4}_{c6_at1}_idx` (`{c6_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc4_0}_{c6_at1_0}_idx` (`{c6_at1_0}`),')
        a39 = mylist[j]
        file_object.write(a39)
        file_object.write("\n")
        
        
    if f'KEY `FK_{assoc4}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc4_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),')
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")
  

    if f'KEY `FK_{assoc4}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc4_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),')
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")
  




    if f'PRIMARY KEY (`{c6_at1}`,`{c2_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c6_at1_0}`,`{c2_at1_0}`)')
        a41 = mylist[j]
        file_object.write(a41)
        file_object.write("\n")
    
        #file_object.close() 
        
       
 #------------------------------------------------------------------------ 
        
    if f'ALTER TABLE `{class5_name}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{class5_name_0}`')
        a42 = mylist[j]
        file_object.write(a42)
        file_object.write("\n")
    
        #file_object.close() 
        
        
    if f'ADD CONSTRAINT `FK_{class5_name}_{c4_at1}` FOREIGN KEY (`{c4_at1}`) REFERENCES `{class4_name}` (`{c4_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class5_name_0}_{c4_at1_0}` FOREIGN KEY (`{c4_at1_0}`) REFERENCES `{class4_name_0}` (`{c4_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a43 = mylist[j]
        file_object.write(a43)
        file_object.write("\n")
        
        
    if f'ADD CONSTRAINT `FK_{class5_name}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class5_name_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a44 = mylist[j]
        file_object.write(a44)
        file_object.write("\n")
        
        
    if f'ADD CONSTRAINT `FK_{class5_name}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class5_name_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a45 = mylist[j]
        file_object.write(a45)
        file_object.write("\n")
    
    
    
    
    #------------------------------------------------------------------------ 
        
    if f'ALTER TABLE `{assoc5}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc5_0}`')
        a46 = mylist[j]
        file_object.write(a46)
        file_object.write("\n")
    
        #file_object.close() 
        
        
    if f' ADD CONSTRAINT `FK_{assoc5}_{c3_at1}` FOREIGN KEY (`{c3_at1}`) REFERENCES `{class3_name}` (`{c3_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc5_0}_{c3_at1_0}` FOREIGN KEY (`{c3_at1_0}`) REFERENCES `{class3_name_0}` (`{c3_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a47 = mylist[j]
        file_object.write(a47)
        file_object.write("\n")
        
        
    if f'ADD CONSTRAINT `FK_{assoc5}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc5_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a48 = mylist[j]
        file_object.write(a48)
        file_object.write("\n")
        
        
#-----------------------------------------------------------
        
        
    if f'ALTER TABLE `{assoc4}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc4_0}`')
        a49 = mylist[j]
        file_object.write(a49)
        file_object.write("\n")
    
        #file_object.close() 
        
        
    if f' ADD CONSTRAINT `FK_{assoc4}_{c6_at1}` FOREIGN KEY (`{c6_at1}`) REFERENCES `{class6_name}` (`{c6_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc4_0}_{c6_at1_0}` FOREIGN KEY (`{c6_at1_0}`) REFERENCES `{class6_name_0}` (`{c6_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a50 = mylist[j]
        file_object.write(a50)
        file_object.write("\n")
        
        
    if f'ADD CONSTRAINT `FK_{assoc4}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc4_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a51 = mylist[j]
        file_object.write(a51)
        file_object.write("\n")
        #file_object.close() 
    
    #-----------------------------------------------------------
   
    if f'Table structure for table' in mylist[j]:
        
        mylist[j] = (f'')
        a53 = mylist[j]
        file_object.write(a53)
        file_object.write("\n")  


    if f'CREATE TABLE `{assoc1}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc1_0}` (')
        a52 = mylist[j]
        file_object.write(a52)
        file_object.write("\n")
        
        
    if f'KEY `FK_{assoc1}_{c5_at1}_idx` (`{c5_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc1_0}_{c5_at1_0}_idx` (`{c5_at1_0}`),')
        a54 = mylist[j]
        file_object.write(a54)
        file_object.write("\n")
        
        
    if f'KEY `FK_{assoc1}_{c1_at1}_idx` (`{c1_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc1_0}_{c1_at1_0}_idx` (`{c1_at1_0}`),')
        a55 = mylist[j]
        file_object.write(a55)
        file_object.write("\n")
        
        
                
    if f'PRIMARY KEY (`{c5_at1}`,`{c1_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c5_at1_0}`,`{c1_at1_0}`)')
        a56 = mylist[j]
        file_object.write(a56)
        file_object.write("\n")
        

      #---------------------------------------------------------------
    
    
    if f'ALTER TABLE `{assoc1}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc1_0}`')
        a57 = mylist[j]
        file_object.write(a57)
        file_object.write("\n")

        
            
    if f'ADD CONSTRAINT `FK_{assoc1}_{c5_at1}` FOREIGN KEY (`{c5_at1}`) REFERENCES `{class5_name}` (`{c5_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c5_at1_0}` FOREIGN KEY (`{c5_at1_0}`) REFERENCES `{class5_name_0}` (`{c5_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a58 = mylist[j]
        file_object.write(a58)
        file_object.write("\n")
        
        
    if f'ADD CONSTRAINT `FK_{assoc1}_{c1_at1}` FOREIGN KEY (`{c1_at1}`) REFERENCES `{class1_name}` (`{c1_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc1_0}_{c1_at1_0}` FOREIGN KEY (`{c1_at1_0}`) REFERENCES `{class1_name_0}` (`{c1_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a59 = mylist[j]
        file_object.write(a59)
        file_object.write("\n")
      
    
    if f'ADD CONSTRAINT `FK_{class5_name}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{class5_name_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a60 = mylist[j]
        file_object.write(a60)
        file_object.write("\n")
        
        #-----------------------------------------------------------------------
        
        
    if f'CREATE TABLE `{assoc3}`' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc3_0}`')
        a61 = mylist[j]
        file_object.write(a61)
        file_object.write("\n")
        
    if f'KEY `FK_{assoc3}_{c5_at1}_idx` (`{c5_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc3_0}_{c5_at1_0}_idx` (`{c5_at1_0}`),')
        a62 = mylist[j]
        file_object.write(a62)
        file_object.write("\n")
  
    if f'KEY `FK_{assoc3}_{c4_at1}_idx` (`{c4_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc3}_{c4_at1}_idx` (`{c4_at1}`),')
        a63 = mylist[j]
        file_object.write(a63)
        file_object.write("\n")
        
        
    if f'KEY `PRIMARY KEY (`{c5_at1}`,`{c4_at1}`)' in mylist[j]:
        
        mylist[j] = (f'KEY `PRIMARY KEY (`{c5_at1_0}`,`{c4_at1_0}`)')
        a64 = mylist[j]
        file_object.write(a64)
        file_object.write("\n")

     
    if f'ALTER TABLE `{assoc3}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc3_0}`')
        a65 = mylist[j]
        file_object.write(a65)
        file_object.write("\n")
        
        
        
             
    if f'ADD CONSTRAINT `FK_{assoc3}_{c5_at1}` FOREIGN KEY (`{c5_at1}`) REFERENCES `{class5_name}` (`{c5_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc3_0}_{c5_at1_0}` FOREIGN KEY (`{c5_at1_0}`) REFERENCES `{class5_name_0}` (`{c5_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a66 = mylist[j]
        file_object.write(a66)
        file_object.write("\n")
 
 
    if f'ADD CONSTRAINT `FK_{assoc3}_{c4_at1}` FOREIGN KEY (`{c4_at1}`) REFERENCES `{class4_name}` (`{c4_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc3_0}_{c4_at1_0}` FOREIGN KEY (`{c4_at1_0}`) REFERENCES `{class4_name_0}` (`{c4_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE;')
        a67 = mylist[j]
        file_object.write(a67)
        file_object.write("\n")
        
        
        
    #------------------------------------------------------------------
    
      
    if f'KEY `FK_{assoc2}_{c5_at1}_idx` (`{c5_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc2_0}_{c5_at1_0}_idx` (`{c5_at1_0}`),')
        a69 = mylist[j]
        file_object.write(a69)
        file_object.write("\n")
        
        
    
    if f'CREATE TABLE `{assoc2}` (' in mylist[j]:
        
        mylist[j] = (f'CREATE TABLE `{assoc2_0}` (')
        a70 = mylist[j]
        file_object.write(a70)
        file_object.write("\n")
        

        
    if f'KEY `FK_{assoc2}_{c2_at1}_idx` (`{c2_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc2_0}_{c2_at1_0}_idx` (`{c2_at1_0}`),')
        a71 = mylist[j]
        file_object.write(a71)
        file_object.write("\n") 
    
    
    if f'PRIMARY KEY (`{c5_at1}`,`{c2_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c5_at1_0}`,`{c2_at1_0}`)')
        a72 = mylist[j]
        file_object.write(a72)
        file_object.write("\n") 
        
        
        
        #----------------------------------------------------------------------------------
        

    if f'ALTER TABLE `{assoc2}`' in mylist[j]:
        
        mylist[j] = (f'ALTER TABLE `{assoc2_0}`')
        a73 = mylist[j]
        file_object.write(a73)
        file_object.write("\n")
        
    if f'ADD CONSTRAINT `FK_{assoc2}_{c5_at1}` FOREIGN KEY (`{c5_at1}`) REFERENCES `{class5_name}` (`{c5_at1}`) ON DELETE CASCADE ON UPDATE CASCADE,' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc2_0}_{c5_at1_0}` FOREIGN KEY (`{c5_at1_0}`) REFERENCES `{class5_name_0}` (`{c5_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a74 = mylist[j]
        file_object.write(a74)
        file_object.write("\n") 
        
        
    if f'ADD CONSTRAINT `FK_{assoc2}_{c2_at1}` FOREIGN KEY (`{c2_at1}`) REFERENCES `{class2_name}` (`{c2_at1}`) ON DELETE CASCADE ON UPDATE CASCADE;' in mylist[j]:
        
        mylist[j] = (f'ADD CONSTRAINT `FK_{assoc2_0}_{c2_at1_0}` FOREIGN KEY (`{c2_at1_0}`) REFERENCES `{class2_name_0}` (`{c2_at1_0}`) ON DELETE CASCADE ON UPDATE CASCADE,')
        a75 = mylist[j]
        file_object.write(a75)
        file_object.write("\n")
        
     
    #---------------------------------------------------------------------------------
    
    if f'KEY `FK_{assoc3}_{c4_at1}_idx` (`{c4_at1}`),' in mylist[j]:
        
        mylist[j] = (f'KEY `FK_{assoc3_0}_{c4_at1_0}_idx` (`{c4_at1_0}`),')
        a76 = mylist[j]
        file_object.write(a76)
        file_object.write("\n")
        
        
    if f'PRIMARY KEY (`{c5_at1}`,`{c4_at1}`)' in mylist[j]:
        
        mylist[j] = (f'PRIMARY KEY (`{c5_at1_0}`,`{c4_at1_0}`)')
        a77 = mylist[j]
        file_object.write(a77)
        file_object.write("\n")
        
        
        

    
    
        #file_object.close() 
    
    
        
    
    # no need to use replace if you're going to change the whole string

        
#print(mylist)

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1
