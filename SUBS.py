# Note: Rosalind uses 1-based numbering, which is accounted for
#       in my solution.

# Note: Instead of using the .find method, I wanted to implement this
#       from scratch, which is why the code is less concise.

def find_motif(string, substring):
    j, k, indices = 0, 0, ''
    while k < len(string):
        if string[j:k+1] == substring:
            indices = indices + str(j+1) + ' '
            j += 1
            k = j
        elif len(string[j:k+1]) >= len(substring):
            j += 1
            k = j
        elif string[j] == substring[0]:
            k += 1
        else:
            j += 1
            k += 1
    print(indices)
