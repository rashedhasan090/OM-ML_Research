file1 = open('OM_multiply_Pareto.txt', 'r')
file2 = open('Mapping_Abstract_Pareto.txt', 'r')
file3 = open('Schema_Abstracts_Pareto.txt', 'r')
Lines =  file1.readlines()
Lines2 = file2.readlines()
Lines3 = file3.readlines()


count = 0

with open('unlabeled-set-pareto.txt', 'w') as f:
    for i in range(len(Lines)):
        count += 1

        a = (f'{Lines[i]},{Lines2[i]},{Lines3[i]}')
        result = "".join(line.strip() for line in a.splitlines())
        f.write(result)
        f.write('\n')

        #print (result)