file1 = open('OM_multiply_NP.txt', 'r')
file2 = open('NP-mapping.txt', 'r')
file3 = open('NP-schema.txt', 'r')
Lines =  file1.readlines()
Lines2 = file2.readlines()
Lines3 = file3.readlines()


count = 0

with open('labeled-set-not-pareto.txt', 'w') as f:
    for i in range(len(Lines)):
        count += 1

        a = (f'NP,{Lines[i]},{Lines2[i]},{Lines3[i]}')
        result = "".join(line.strip() for line in a.splitlines())
        f.write(result)
        f.write('\n')

        #print (result)
