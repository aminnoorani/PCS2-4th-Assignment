def whichTrans(base1, base2):
    if (base1 == 'A' and base2 == 'G'):
        return 'transition'
    if (base1 == 'G' and base2 == 'A'):
        return 'transition'
    if (base1 == 'C' and base2 == 'T'):
        return 'transition'
    if (base1 == 'T' and base2 == 'C'):
        return 'transition' # pyridine-pyridine or purine-purine switch
    else:
        return 'transversion' # pyridine-purine or purine-pyridine switch

def main():

    # open file, extract data
    dataFile = open('example.txt','r')
    dnaList = dataFile.read().replace('\n','').split('>')
    dataFile.close()

    # create variables to manipulate
    string1 = dnaList[1][13:]
    string2 = dnaList[2][13:]
    transitionCount = 0
    transversionCount = 0

    # find out whether counting point mutations are transitions or transversions
    for x in range(len(string1)):
        first = string1[x]
        second = string2[x]
        if (first != second):
            result = whichTrans(first, second)
            if (result == 'transition'):
                transitionCount += 1
            if (result == 'transversion'):
                transversionCount += 1

    # find transition/transversion ratio
    ratio = float(transitionCount / transversionCount)

    # output results
    outputFile = open('output.txt','w')
    outputFile.writelines(str(ratio))
    outputFile.close()

if __name__ == "__main__":
    main()
