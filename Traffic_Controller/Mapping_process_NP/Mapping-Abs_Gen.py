

import os
i = 0
for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/Traffic_Controller/Mapping_process_NP'):
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
            OM_name = "traffic_control"
            om_count = 0

            class1_name = "GIS"
            c1_at1 = "GISRoute"
            c1_at1_type = "int"
            c1_at2 = "SATLocation"
            c1_at2_type = "varchar"

            class2_name = "Traffic_Controller"
            c2_at1 = "EmployeeId"
            c2_at1_type = "int"
            c2_at2 = "Duty_Officer"
            c2_at2_type = "varchar"


            class3_name = "Report"
            c3_at1 = "ReportId"
            c3_at1_type = "int"
            c3_at2 = "Incident_No"
            c3_at2_type = "int"
            c3_at3 = "Reporting_Officer"
            c3_at3_type = "int"
            c3_at4 = "caseid"
            c3_at4_type = "int"
            c3_at5 = "Location"
            c3_at5_type = "int"
            c3_at6 = "FineAmount"
            c3_at6_type = "int"


            class4_name = "Insurance_Company"
            c4_at1 = "IC_Name"
            c4_at1_type = "varchar"
            c4_at2 = "IC_Address"
            c4_at2_type = "varchar"
            c4_at3 = "Policy_No"
            c4_at3_type = "int"
            c4_at4 = "Policy_Date"
            c4_at4_type = "varchar"


            class5_name = "Insurance"
            c5_at1 = "Insurancedetails"
            c5_at1_type = "varchar"


            class6_name = "Driver"
            c6_at1 = "DriverName"
            c6_at1_type = "varchar"
            c6_at2 = "DriverLNo"
            c6_at2_type = "int"
            c6_at3 = "Insurance_company"
            c6_at3_type = "varchar"
            c6_at4 = "LicDuration"
            c6_at4_type = "varchar"


            class7_name = "VehicleDetails"
            c7_at1 = "VIN_NVMC"
            c7_at1_type = "varchar"
            #c6_at2 = "categoryName"
            #c6_at2_type = "varchar"


            class8_name = "TARS"
            c8_at1 = "TARS_NO"
            c8_at1_type = "int"
            c8_at2 = "TARS_NAME"
            c8_at2_type = "varchar"


            assoc1 = "Traffic_ControllerTARSAssociation"
            assoc2 = "Traffic_ControllerInsurance_CompanyAssociation"
            assoc3 = "TARSReportAssociation"
            assoc4 = "TARSInsurance_CompanyAssociation"
            assoc5 = "TARSDriverAssociation"
            assoc6 = "DriverGISAssociation"
            assoc7 = "DriverInsurance_CompanyAssociation"
            assoc8 = "ReportGISAssociation"
            assoc9 = "Insurance_CompanyGISAssociation"
            assoc10 = "Traffic_ControllerReportAssociation"
            assoc11 = "ReportLibraryDbAssociation"

            src_mlpc = "ONE"
            src_mlpc2 = "MANY"
            dst_mlpc = "MANY"
            dst_mlpc2 = "ONE"

            map_str1 = "Union Super Class"
            map_str2 = "Union Sub Class"
            map_str3 = "Joined Sub Class"

            assoc_str1 = "ForeignKeyEmbeddingStrategy"
            assoc_str2 = "OwnAssociationTableStrategy"

            #--------------------------------
            OM_name_0 = "OM_name"
            #om_count = 0

            class1_name_0 = "class1_name"
            c1_at1_0 = "c1_at1"
            c1_at1_type_0 = "c1_at1_type"
            c1_at2_0 = "c1_at2"
            c1_at2_type_0 = "c1_at2_type"

            class2_name_0 = "class2_name"
            c2_at1_0 = "c2_at1"
            c2_at1_type_0 = "c2_at1_type"
            c2_at2_0 = "c2_at2"
            c2_at2_type_0 = "c2_at2_type"


            class3_name_0 = "class3_name"
            c3_at1_0 = "c3_at1"
            c3_at1_type_0 = "c3_at1_type"
            c3_at2_0 = "c3_at2"
            c3_at2_type_0 = "c3_at2_type"
            c3_at3_0 = "c3_at3"
            c3_at3_type_0 = "c3_at3_type"
            c3_at4_0 = "c3_at4"
            c3_at4_type_0 = "c3_at4_type"
            c3_at5_0 = "c3_at5"
            c3_at5_type_0 = "c3_at5_type"
            c3_at6_0 = "c3_at6"
            c3_at6_type_0 = "c3_at6_type"


            class4_name_0 = "class4_name"
            c4_at1_0 = "c4_at1"
            c4_at1_type_0 = "c4_at1_type"
            c4_at2_0 = "c4_at2"
            c4_at2_type_0 = "c4_at2_type"
            c4_at3_0 = "c4_at3"
            c4_at3_type_0 = "c4_at3_type"
            c4_at4_0 = "c4_at4"
            c4_at4_type_0 = "c4_at4_type"




            class5_name_0 = "class5_name"
            c5_at1_0 = "c5_at1"
            c5_at1_type_0 = "c5_at1_type"



            class6_name_0 = "class6_name"
            c6_at1_0 = "c6_at1_0"
            c6_at1_type_0 = "c6_at1_type"
            c6_at2_0 = "c6_at2"
            c6_at2_type_0 = "c6_at2_type"
            c6_at3_0 = "c6_at3"
            c6_at3_type_0 = "c6_at3_type"
            c6_at4_0 = "c6_at4"
            c6_at4_type_0 = "c6_at4_type"



            class7_name_0 = "class7_name"
            c7_at1_0 = "c7_at1"
            c7_at1_type_0 = "c7_at1_type"
            #c6_at2 = "categoryName"
            #c6_at2_type = "varchar"



            class8_name_0 = "class8_name"
            c8_at1_0 = "c8_at1"
            c8_at1_type_0 = "c8_at1_type"
            c8_at2_0 = "c8_at2"
            c8_at2_type_0 = "c8_at2_type"



            assoc1_0 = "assoc1"
            assoc2_0 = "assoc2"
            assoc3_0 = "assoc3"
            assoc4_0 = "assoc4"
            assoc5_0 = "assoc5"
            assoc6_0 = "assoc6"
            assoc7_0 = "assoc7"
            assoc8_0 = "assoc8"
            assoc9_0 = "assoc9"
            assoc10_0 = "assoc10"
            assoc11_0 = "assoc11"


            src_mlpc_0 = "src_mlpc"
            src_mlpc2_0 = "src_mlpc2"
            dst_mlpc_0 = "dst_mlpc"
            dst_mlpc2_0 = "dst_mlpc2"

            map_str1_0 = "map_str1"
            map_str2_0 = "map_str2"
            map_str3_0 = "map_str3"

            assoc_str1_0 = "assoc_str1"
            assoc_str2_0 = "assoc_str2"

            file_object = open(file+'.txt', 'a')



            for j in range(len(mylist)):


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/GIS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str2_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/GIS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str1_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/GIS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class1_name_0} : {map_str3_0}")
                    a27 = mylist[j]
                    file_object.write(a27)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

             #-------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/Insurance"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str1_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/Insurance"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str2_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/Insurance"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class5_name_0} : {map_str3_0}")
                    a28 = mylist[j]
                    file_object.write(a28)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

              #-------------------------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/VehicleDetails"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str1_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/VehicleDetails"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str2_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/VehicleDetails"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class7_name_0} : {map_str3_0}")
                    a29 = mylist[j]
                    file_object.write(a29)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


               #----------------------------------------------------------------


                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/TARS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str1_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/TARS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str2_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/TARS"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class8_name_0} : {map_str3_0}")
                    a30 = mylist[j]
                    file_object.write(a30)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #---------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/Driver"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str1_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/Driver"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str2_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/Driver"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class6_name_0} : {map_str3_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")





            #----------------------------------------------------------------



                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/Report"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str1_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/Report"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str2_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/Report"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class3_name_0} : {map_str3_0}")
                    a100 = mylist[j]
                    file_object.write(a100)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #-----------------------------------------------------------------------------




                if f'<tuple> <atom label="ORMStrategies/UnionSuperclassStrategy"/> <atom label="traffic_control/Traffic_Controller"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str1_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/UnionSubclassStrategy"/> <atom label="traffic_control/Traffic_Controller"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str2_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="ORMStrategies/JoinedSubclassStrategy"/> <atom label="traffic_control/Traffic_Controller"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Mapping Strategy for {class2_name_0} : {map_str3_0}")
                    a101 = mylist[j]
                    file_object.write(a101)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


            #--------------------------------------------------------------

            #from traffic_control/ElectronicReport



            #---------------------------------------------------------------------

            #-------------------------------------------------------------------------- ------------------


            #------------------------ ------------------------- -------------------------------- -------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="Traffic_ControllerTARSAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str1_0}")
                    a31 = mylist[j]
                    file_object.write(a31)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="Traffic_ControllerTARSAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc1_0} : {assoc_str2_0}")
                    a31 = mylist[j]
                    file_object.write(a31)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                    #---------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="Traffic_ControllerInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str1_0}")
                    a32 = mylist[j]
                    file_object.write(a32)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="Traffic_ControllerInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc2_0} : {assoc_str2_0}")
                    a32 = mylist[j]
                    file_object.write(a32)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                  #-------------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/TARSReportAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str1_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/TARSReportAssociationn"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc3_0} : {assoc_str2_0}")
                    a33 = mylist[j]
                    file_object.write(a33)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                #-----------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/TARSInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str2_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/TARSInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc4_0} : {assoc_str1_0}")
                    a34 = mylist[j]
                    file_object.write(a34)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")

                 #-------------------------------------------------------------------------

                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/DriverGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str2_0}")
                    a35 = mylist[j]
                    file_object.write(a35)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/DriverGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc6_0} : {assoc_str1_0}")
                    a35 = mylist[j]
                    file_object.write(a35)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()

              #----------------------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/TARSDriverAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str2_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/TARSDriverAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc5_0} : {assoc_str1_0}")
                    a36 = mylist[j]
                    file_object.write(a36)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/DriverInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str2_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/DriverInsurance_CompanyAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc7_0} : {assoc_str1_0}")
                    a37 = mylist[j]
                    file_object.write(a37)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()


            #-----------------------------------------------------------------------


                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/ReportGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str2_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/ReportGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc8_0} : {assoc_str1_0}")
                    a38 = mylist[j]
                    file_object.write(a38)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()



            #-----------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/Insurance_CompanyGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str2_0}")
                    a39 = mylist[j]
                    file_object.write(a39)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/Insurance_CompanyGISAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc9_0} : {assoc_str1_0}")
                    a39 = mylist[j]
                    file_object.write(a39)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
                    #file_object.close()



            #-----------------------------------------------------------------------



                if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/Traffic_ControllerReportAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str2_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")


                if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/Traffic_ControllerReportAssociation"/> </tuple>' in mylist[j]:
                    mylist[j] = (f"Association Strategy for {assoc10_0} : {assoc_str1_0}")
                    a40 = mylist[j]
                    file_object.write(a40)
                    file_object.write("\n")
                    print(mylist[j])
                    print("")
        #file_object.close()




 #-----------------------------------------------------------------------



#     if f'<tuple> <atom label="AssociationMappings/OwnAssociationTableStrategy"/> <atom label="traffic_control/ReportLibraryDbAssociation"/> </tuple>' in mylist[j]:
#         mylist[j] = (f"Association Strategy for {assoc11_0} : {assoc_str2_0}")
#         a40 = mylist[j]
#         file_object.write(a40)
#         file_object.write("\n")
#         print(mylist[j])
#         print("")


#     if f'<tuple> <atom label="AssociationMappings/ForeignKeyEmbeddingStrategy"/> <atom label="traffic_control/ReportLibraryDbAssociation"/> </tuple>' in mylist[j]:
#         mylist[j] = (f"Association Strategy for {assoc11_0} : {assoc_str1_0}")
#         a40 = mylist[j]
#         file_object.write(a40)
#         file_object.write("\n")
#         print(mylist[j])
#         print("")
#         #file_object.close()






#traffic_control_Sol_58.xml
#traffic_control_Sol_ .xml

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
