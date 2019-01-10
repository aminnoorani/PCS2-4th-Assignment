#returns a consensus string and profile matrix
def consensus(fasta_file):
    #creates list of dna strings from file in fasta format
    lines = list(open(fasta_file, "r"))
    dna_strings, i = [], 0
    while i < len(lines):
        if lines[i][0] == ">":
            j = i + 1
            dna_string = ''
            while j < len(lines) and lines[j][0] != ">":
                dna_string = dna_string + lines[j].strip("\n")
                j += 1
            dna_strings.append(dna_string)
        i += 1
    #creates profile matrix
    columns = len(dna_strings[0])
    profiles = {'A': [0 for i in range(0, columns)], 'C': [0 for i in range(0, columns)],
                'G' : [0 for i in range(0, columns)], 'T': [0 for i in range(0, columns)] }
    for dna in dna_strings:
        i = 0
        while i < len(dna):
            profiles[dna[i]][i] += 1
            i += 1
    #prints consensus string and profile matrix
    cons_str = []
    #zips all the values of profiles together to take max of each index
    maxes = [max(i) for i in zip([max(i) for i in zip(profiles['A'], profiles['T'])], [max(i) for i in zip(profiles['G'], profiles['C'])])]
    cons_str = maxes
    for item in profiles.items():
        i = 0
        while i < len(maxes):
            if maxes[i] == item[1][i]:
                cons_str[i] = item[0]
            i += 1
        print(item[0] + ':', *item[1])
    print(''.join(cons_str))
