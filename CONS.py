def print_profile(nt, lst):
    print(nt, ": ", sep = '', end = '')
    for item in lst:
        print(item, end = ' ')
    print()

f = open("rosalind_cons.txt")
lst = f.read()
f.close()

lst = lst.replace('\n', '')
lst = lst.split('>')
dna = list()

for item in lst:
    if (len(item) < 1):
        continue
    v = item[13::]
    dna.append(v)

dnaLen = len(dna[0])
profA = []
profC = []
profG = []
profT = []
for i in range(0, dnaLen):
    profA.insert(i, 0)
    profC.insert(i, 0)
    profG.insert(i, 0)
    profT.insert(i, 0)

for i in range(0, dnaLen):
    for j in range(0, len(dna)):
        if (dna[j][i] == 'A'):
            profA[i] += 1
        elif (dna[j][i] == 'C'):
            profC[i] += 1
        elif (dna[j][i] == 'G'):
            profG[i] += 1
        elif (dna[j][i] == 'T'):
            profT[i] += 1

cons = str()
for i in range(0, dnaLen):
    x = max([profA[i], profC[i], profG[i], profT[i]])
    if (profA[i] == x):
        cons += "A"
    elif (profC[i] == x):
        cons += "C"
    elif (profG[i] == x):
        cons += "G"
    elif (profT[i] == x):
        cons += "T"

print(cons)
print_profile("A", profA)
print_profile("C", profC)
print_profile("G", profG)
print_profile("T", profT)
