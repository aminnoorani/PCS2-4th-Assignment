def reverseStr(string):
    """ Reverse string """
    return string[::-1]


def complementStrand(string):
    """ Complement a Strand of DNA """

    # New output string
    newStr = ""


    # Iterate over reversed string
    for c in string:
        if c == "A":
            newStr += "T"
        elif c == "T":
            newStr += "A"
        elif c == "C":
            newStr += "G"
        elif c == "G":
            newStr += "C"
    return newStr

testString = "GCTGCACCGCATAAGGAAT"
reverse_string = reverseStr(testString)
print(complementStrand(reverse_string))
