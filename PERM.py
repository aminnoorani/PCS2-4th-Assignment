from math import factorial
from itertools import permutations
def perm(n):
    print (factorial(n))

    number = list(permutations(range(1, n + 1)))
    for i in number:
        print(' '.join(map(str, i)))

perm()
