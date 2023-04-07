file1 = open('open_multiple_1.txt', 'r')
file2 = open('sol202-12239_mapping.txt', 'r')
file3 = open('sol202-12239.txt', 'r')
Lines =  file1.readlines()
Lines2 = file2.readlines()
Lines3 = file3.readlines()


count = 0

with open('labeled-set.txt', 'w') as f:
    for i in range(len(Lines)):
        count += 1

        a = (f'{Lines[i]},{Lines2[i]},{Lines3[i]},NP')
        result = "".join(line.strip() for line in a.splitlines())
        f.write(result)
        f.write('\n')

        #print (result)
