def hammondDistance(a, b):
    # Helper counter
    diffCounter = 0

    for charA, charB in zip(a, b):
        if charA != charB:
            diffCounter += 1

    # Return hammond distance
    return diffCounter

str1 = "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"

print(hammondDistance(str1, str2))
