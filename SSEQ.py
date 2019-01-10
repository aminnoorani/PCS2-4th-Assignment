#SHould Enter input and output path

def fastaRead(filename):
    """This reads the Rosalind file and turns the sequences into a list, changes the keys to numbers"""
    fasta = {}
    rosalindFile = "false"
    oneString = ""
    with open(filename, "r") as file_test:
        for tmpline in file_test:
            tmpline = tmpline.strip()
            if tmpline.startswith(">"):
                rosalindFile = "true"
            elif (rosalindFile == "false"):
                oneString += tmpline
    if(rosalindFile == "false"):
        return oneString
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

print("Get the strings into a dictionary...")
rosalindDict = fastaRead(inputFilePath)

#Get the original string and subsequence
originalString = rosalindDict[0]
subsequenceString = rosalindDict[1]

#Get each character in the subsequence and examine it in the original string
with open(outputFilePath, 'w') as f:
    indexOfOriginalSequence = 0
    characterFound = "false"
    for charInSequence in subsequenceString:
        characterFound = "false"
        while (characterFound == "false"):
            if (charInSequence == originalString[indexOfOriginalSequence]):
                indexOfOriginalSequence += 1
                f.write('{}'.format(indexOfOriginalSequence) + " ")
                indexOfOriginalSequence -= 1
                characterFound = "true"
            indexOfOriginalSequence += 1

print("Character locations have been written to: " + outputFilePath)
