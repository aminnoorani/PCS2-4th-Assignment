import sys

def modifiedFastaRead(filename):
    """This reads the Rosalind file and turns the sequences into a list"""
    fasta = {}
    count = -1
    with open(filename, "r") as file_one:
        for line in file_one:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                count += 1
                fasta[count] = []
                continue
            sequence = line
            fasta[count].append(sequence)
        numberDictKey = len(fasta)
        numberOfValueInKey = 0
        singleDna = ""
        for numberDictKey in fasta:
            valuesInKey = fasta[numberDictKey]
            numberOfValueInKey = len(valuesInKey)

            for numberOfValueInKey in valuesInKey:
                singleDna += numberOfValueInKey

                fasta[numberDictKey] = singleDna
            singleDna = ""
    return fasta

def hammingDistance(a,b):
    """This function creates the damming distance between two strings"""
    hamming = 0
    for x, y in zip(a, b):
        if x != y:
            hamming += 1
    return hamming


#Get the dictionary from the Rosalind file and change to keys that are traversable int(s)
print("Get the dictionary from the Rosalind file and change to keys that are traversable int(s)")
rosalindDict = modifiedFastaRead(inputFilepath)
print("Keys in the dictionary")
print(rosalindDict.keys().__str__() + '\n')

count = 0
for i in rosalindDict:
    print("rosalindDict[" + '{}'.format(count) + "]")
    print('{}'.format(rosalindDict[i]))
    count += 1
print('\n')

#Get the number of bases for the string p-distance (hamming distance / base length of sequence)
print("Get the number of baselength for the string p-distance (hamming distance / base length of sequence)")
baselength = 0
for i in rosalindDict:
    baselength = len(rosalindDict[i])
print("The baselength of each sequence is " + '{}'.format(baselength)  + '\n')

#Now we need to get the number of rows and columns for the matrix
print("Now we need to get the number of rows and columns for the matrix")
numberOfRowsAndColumns = rosalindDict.__len__()
print("The number of rows and columns for the matrix is " + '{}'.format(numberOfRowsAndColumns) + '\n')

#Now we need to write the answer
print("Writing answer to: " + outputFilepath)

with open(outputFilepath, 'w') as f:
    for columnNumber in range(numberOfRowsAndColumns):
        for rowNumber in range(numberOfRowsAndColumns):
            h = hammingDistance(rosalindDict[rowNumber],rosalindDict[columnNumber]).__float__() / baselength.__float__()
            h = format(h,'.5f')
            f.write('{}'.format(h) + " ")
        f.write('\n')
