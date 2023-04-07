



import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/E-commerce-OM-Resources/All XML and SQL Soln'):
    for file in files:
        #each file

        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            i +=1
            # a = file
            # print(a)
            print("Analyzed File: " + file)
            file_read = open(file, 'r')
            lines = file_read.readlines()


            file_object = open('Solution-Schemas.txt', 'a')

            for j in range(len(lines)):
                mystr = ''.join([line.strip() for line in lines])
                #print(mystr)
                file_object.write(mystr)

            file_object.close()


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

print("Total Analyzed File: " + str(i))
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
