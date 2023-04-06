import os

for root, dirs, files in os.walk('/Users/rashedhasan/Desktop/UNL/Research/Object relational mapping/Step 5 - Abstraction/OM-Solution_Mapping/OM-ML_Research/E-commerce-OM-Resources/SQL_soluions/exp'):
    for file in files:
        filename, extension = os.path.splitext(file)
        if extension == '.txt':
            a = file
            print(a)

for file in a:
    f = open(a, 'r')
    lines = f.readlines()
    mystr = ''.join([line.strip() for line in lines])
    print(mystr)
    f.close()

# pol = mystr
# count = 0
# with open('sum_sl.txt', 'w') as fp:
#     for i in range(pol):
#         count += 1
#
#         fp.write(pol)
#         fp.write('\n')
