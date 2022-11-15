
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

file_object = open(f'OnlineStore_OM_Abstract_only.txt', 'a')


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
        
        
    if f'attrSet = {c2_at1}+{c2_at2}+{c2_at3}+{c2_at4}' in mylist[j]:
        
        mylist[j] = (f"attrSet = {c2_at1_0}+{c2_at2_0}+{c2_at3_0}+{c2_at4_0}")
        a9 = mylist[j]
        file_object.write(a9)
        file_object.write("\n")
        
    if f'id={c2_at1}' in mylist[j]:
        
        mylist[j] = (f"id={c2_at1_0}")
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
        file_object.write(a12)
        file_object.write("\n")  
        file_object.write("\n")
        
        
    if f'one sig {c2_at3} extends {c2_at3_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c2_at3_0} extends {c2_at3_type_0}')
        a13 = mylist[j]
        file_object.write(a13)
        file_object.write("\n")  
        file_object.write("\n")
        
    if f'one sig {c2_at4} extends {c2_at4_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c2_at4_0} extends {c2_at4_type_0}')
        a14 = mylist[j]
        file_object.write(a14)
        file_object.write("\n")  
        file_object.write("\n")
        
        
    if f'one sig {class3_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class3_name_0} extends Class')
        a15 = mylist[j]
        file_object.write(a15)
        file_object.write("\n")
        
        
    if f'attrSet = {c3_at1}+{c3_at2}+{c3_at3}+{c3_at4}' in mylist[j]:

        mylist[j] = (f"attrSet = {c3_at1_0}+{c3_at2_0}+{c3_at3_0}+{c3_at4_0}")
        a16 = mylist[j]
        file_object.write(a16)
        file_object.write("\n")
        
        
    if f'id={c3_at1}' in mylist[j]:

        mylist[j] = (f"id={c3_at1_0}")
        a17 = mylist[j]
        file_object.write(a17)
        file_object.write("\n")


    if f'one sig {c3_at1} extends {c3_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c3_at1_0} extends {c3_at1_type_0}')
        a18 = mylist[j]
        file_object.write(a18)
        file_object.write("\n") 
        
        
    if f'one sig {c3_at2} extends {c3_at2_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c3_at2_0} extends {c3_at2_type_0}')
        a19 = mylist[j]
        file_object.write(a19)
        file_object.write("\n")
        
        
    if f'one sig {c3_at3} extends {c3_at3_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c3_at3_0} extends {c3_at3_type_0}')
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")
        
    if f'one sig {c3_at4} extends {c3_at4_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c3_at4_0} extends {c3_at4_type_0}')
        a20 = mylist[j]
        file_object.write(a20)
        file_object.write("\n")
        
        
    #--------------------------------------------------------------------
        
    if f'one sig {class4_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class4_name_0} extends Class')
        a21 = mylist[j]
        file_object.write(a21)
        file_object.write("\n")
        
        
    if f'attrSet = {c4_at1}' in mylist[j]:

        mylist[j] = (f"attrSet = {c4_at1_0}")
        a22 = mylist[j]
        file_object.write(a22)
        file_object.write("\n")
        
        
    if f'id={c4_at1}' in mylist[j]:

        mylist[j] = (f"id={c4_at1_0}")
        a23 = mylist[j]
        file_object.write(a23)
        file_object.write("\n")


    if f'one sig {c4_at1} extends {c4_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c4_at1_0} extends {c4_at1_type_0}')
        a24 = mylist[j]
        file_object.write(a24)
        file_object.write("\n") 
   
    #---------------------------------------------------------------------     
    if f'one sig {class5_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class5_name_0} extends Class')
        a25 = mylist[j]
        file_object.write(a25)
        file_object.write("\n")
        
        
    if f'attrSet = {c5_at1}+{c5_at2}+{c5_at3}+{c5_at4}' in mylist[j]:

        mylist[j] = (f"attrSet = {c5_at1_0}+{c5_at2_0}+{c5_at3_0}+{c5_at4_0}")
        a26 = mylist[j]
        file_object.write(a26)
        file_object.write("\n")
        
        
    if f'id={c5_at1}' in mylist[j]:

        mylist[j] = (f"id={c5_at1_0}")
        a27 = mylist[j]
        file_object.write(a27)
        file_object.write("\n")


    if f'one sig {c5_at1} extends {c5_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c5_at1_0} extends {c5_at1_type_0}')
        a28 = mylist[j]
        file_object.write(a28)
        file_object.write("\n") 
        
        
    if f'one sig {c5_at2} extends {c5_at2_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c5_at2_0} extends {c5_at2_type_0}')
        a29 = mylist[j]
        file_object.write(a29)
        file_object.write("\n")
        
        
    if f'one sig {c5_at3} extends {c5_at3_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c5_at3_0} extends {c5_at3_type_0}')
        a30 = mylist[j]
        file_object.write(a30)
        file_object.write("\n")
        
    if f'one sig {c5_at4} extends {c5_at4_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c5_at4_0} extends {c5_at4_type_0}')
        a31 = mylist[j]
        file_object.write(a31)
        file_object.write("\n") 
        
        
    #----------------------------------------------------------------------
    
    if f'one sig {class6_name} extends Class' in mylist[j]:
        
        mylist[j] = (f'one sig {class6_name_0} extends Class')
        a49 = mylist[j]
        file_object.write(a49)
        file_object.write("\n")
        
        
    if f'attrSet = {c6_at1}+{c6_at2}+{c6_at3}+{c6_at4}' in mylist[j]:

        mylist[j] = (f"attrSet = {c6_at1_0}+{c6_at2_0}+{c6_at3_0}+{c6_at4_0}")
        a50 = mylist[j]
        file_object.write(a50)
        file_object.write("\n")
        
        
    if f'id={c6_at1}' in mylist[j]:

        mylist[j] = (f"id={c6_at1_0}")
        a51 = mylist[j]
        file_object.write(a51)
        file_object.write("\n")


    if f'one sig {c6_at1} extends {c6_at1_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c6_at1_0} extends {c6_at1_type_0}')
        a52 = mylist[j]
        file_object.write(a52)
        file_object.write("\n") 
        
        
    if f'one sig {c6_at2} extends {c6_at2_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c6_at2_0} extends {c6_at2_type_0}')
        a53 = mylist[j]
        file_object.write(a53)
        file_object.write("\n")
        
        
    if f'one sig {c6_at3} extends {c6_at3_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c6_at3_0} extends {c6_at3_type_0}')
        a54 = mylist[j]
        file_object.write(a54)
        file_object.write("\n")
        
    if f'one sig {c6_at4} extends {c6_at4_type}' in mylist[j]:
        
        mylist[j] = (f'one sig {c6_at4_0} extends {c6_at4_type_0}')
        a55 = mylist[j]
        file_object.write(a55)
        file_object.write("\n") 
        
        
    
    #----------------------------------------------------------------------
     
    if f'one sig {assoc1} extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc1_0} extends Association')
        a32 = mylist[j]
        file_object.write(a32)
        file_object.write("\n") 
        
        
    if f'src = {class1_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class1_name_0}')
        a33 = mylist[j]
        file_object.write(a33)
        file_object.write("\n")  
        
    if f'dst= {class5_name}' in mylist[j]:
        
        mylist[j] = (f'dst= {class5_name_0}')
        a34 = mylist[j]
        file_object.write(a34)
        file_object.write("\n")
    
    #----------------------------------------------------------------------
    if f'one sig {assoc2} extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc2_0} extends Association')
        a35 = mylist[j]
        file_object.write(a35)
        file_object.write("\n") 
        
        
    if f'src = {class2_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class1_name_0}')
        a36 = mylist[j]
        file_object.write(a36)
        file_object.write("\n")  
        
    
    if f'dst= {class6_name}' in mylist[j]:
        
        mylist[j] = (f'dst= {class6_name_0}')
        a56 = mylist[j]
        file_object.write(a56)
        file_object.write("\n")
    
    #----------------------------------------------------------------------
        
    if f'one sig {assoc3} extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc3_0} extends Association')
        a37 = mylist[j]
        file_object.write(a37)
        file_object.write("\n") 
        
        
    if f'src = {class4_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class4_name_0}')
        a38 = mylist[j]
        file_object.write(a38)
        file_object.write("\n")  
        
        
        
 #----------------------------------------------------------------------
        
    if f'one sig {assoc4} extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc4_0} extends Association')
        a39 = mylist[j]
        file_object.write(a39)
        file_object.write("\n") 
        
        
    if f'src = {class6_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class6_name_0}')
        a40 = mylist[j]
        file_object.write(a40)
        file_object.write("\n")  
        
        
        
#--------------------------------------------------------------------------

    if f'one sig {assoc5}  extends Association' in mylist[j]:
        
        mylist[j] = (f'one sig {assoc5_0} extends Association')
        a41 = mylist[j]
        file_object.write(a41)
        file_object.write("\n") 
        
        
    if f'src = {class3_name}' in mylist[j]:
        
        mylist[j] = (f'src = {class3_name_0}')
        a42 = mylist[j]
        file_object.write(a42)
        file_object.write("\n") 
        
        
    if f'dst= {class3_name}' in mylist[j]:
        
        mylist[j] = (f'dst= {class3_name_0}')
        a57 = mylist[j]
        file_object.write(a57)
        file_object.write("\n")

#----------------------------------------------------------------------
        
        
        
#---------------------------------------------------------------------

        
    if f'src_multiplicity = {src_mlpc}' in mylist[j]:
        
        mylist[j] = (f'src_multiplicity = {src_mlpc_0}')
        a43 = mylist[j]
        file_object.write(a43)
        file_object.write("\n")
        
    if f'dst_multiplicity = {dst_mlpc}' in mylist[j]:
        
        mylist[j] = (f'dst_multiplicity = {dst_mlpc_0}')
        a44 = mylist[j]
        file_object.write(a44)
        file_object.write("\n")
        
    if f'dst_multiplicity = {dst_mlpc2}' in mylist[j]:
        
        mylist[j] = (f'dst_multiplicity = {dst_mlpc2_0}')
        a48 = mylist[j]
        file_object.write(a48)
        file_object.write("\n")   
         
        
    if f'one parent' in mylist[j]:
        
        mylist[j] = (f'one parent')
        a45 = mylist[j]
        file_object.write(a45)
        file_object.write("\n")
        
  
        
        
    if f'pred show' in mylist[j]:
        
        mylist[j] = (f'pred show')
        a46 = mylist[j]
        file_object.write(a46)
        file_object.write("\n")
        
        
    if f'run show for 16' in mylist[j]:
        
        mylist[j] = (f'run show for 38')
        a47 = mylist[j]
        file_object.write(a47)
        file_object.write("\n")
        file_object.close() 
        
        
    
    # no need to use replace if you're going to change the whole string

        
#print(mylist)

for  x in range(len(mylist)) :
   
    print(mylist[x]) 
    x += 1
