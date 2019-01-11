def count_transitions(s, t):
    count = 0
    for i in range(0, len(s)):
        if ((s[i] == 'A' and t[i] == 'G') or
            (s[i] == 'G' and t[i] == 'A') or
            (s[i] == 'C' and t[i] == 'T') or
            (s[i] == 'T' and t[i] == 'C')):
            count += 1
    return count

def count_transversions(s, t):
    count = 0
    for i in range(0, len(s)):
        if ((s[i] == 'A' and t[i] == 'C') or
            (s[i] == 'A' and t[i] == 'T') or
            (s[i] == 'C' and t[i] == 'A') or
            (s[i] == 'C' and t[i] == 'G') or
            (s[i] == 'G' and t[i] == 'C') or
            (s[i] == 'G' and t[i] == 'T') or
            (s[i] == 'T' and t[i] == 'A') or
            (s[i] == 'T' and t[i] == 'G')):
            count += 1
    return count

def get_transition_transversion_ratio(s, t):
    return count_transitions(s, t) / count_transversions(s, t)

f = open("rosalind_tran.txt")
lst = f.read()
f.close()

lst = lst.replace('\n', '')
lst = lst.split('>')
dna = []

for item in lst:
    if (len(item) < 1):
        continue

    dna.append(item[13::])

print(get_transition_transversion_ratio(dna[0], dna[1]))
