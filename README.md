# OM-ML_Research
Experiments and Tools for the OM Project 


## Customer-Order Object Model Trademaker

### Generating Object Model Abstract 
Resource Folder: customer_order_OM_Abstract_Resource 

Files: customer-order-om-abstract.exe, customer-order-om-abstract.py and input file. 

exe file would take .als input and generate abstract instantly 
Output will be generated at Customer_Order_OM_Abstract_only.txt file. 

### Generating Solution Schema Abstract 
Resource Folder: Customer-Order-OM_Schema_Abstract_Resource 

Files: customer-order-solutions-abstract-generator.exe, customer-order-solutions-abstract-generator.py and input files. 

exe file would take .sql input and generate abstract instantly 
Output will be generated at Customer_Order_OM_Abstract_only.txt file. 


### Mapping Extraction 

Resource Folder: customer_order_OM_solution_mapping_extraction_resources

1. It contains the program om_sol_extract.exe file. 
2. It contains the solution files. 
3. The program takes input , the XML files (e.g. customer_order_sol_1.xml)
4. It extracts necessary information along with the mapping. 
5. If mapping changes based on different solution, it captures it dynamically. 
6. It would generate a file OM_Mapping_strategy_1.txt. 
7. The program would compute the mapping and immediately ask for next file to generate abstracts. 
8. The input should be given as OM_Mapping_strategy_1.txt and it would generate the abstract format immediately 
9. Which should be saved at OM_Mapping_strategy_abstract_1.txt file. 
10. The original python source file (om_sol_extract.py) is also included in the folder.

