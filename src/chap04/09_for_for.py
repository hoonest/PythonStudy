

for i in range (2, 10) :
    print('== {0} 단 =='.format(i))
    for j in range (1, 10):
        result = i * j
        print('{0} x {1} = {2}'.format(i, j, result))




print("\r")

for j in range(2, 10):
    print('\t== {0} 단 ==\t|'.format(j), end="\t")

for i in range(1, 10):
    print("")
    for j in range (2, 10):
        result = i * j
        if result < 10:
            result = " {0}".format(result)
        #print("==" + i2 + "==" + j2 + "==" + result2)
        print('\t{0} x {1} = {2}\t|'.format(j, i, result), end = "\t")