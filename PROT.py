def rna_to_protein(rna, codon="PROT_helper_example.txt"):

    # reading in the rna codon table
    lines = list(open(codon, "r"))
    rna_codon = {}
    for line in lines:
        rna_codon[line[0] + line[1] + line[2]] = line[4]

    # rna --> protein
    i, triple, protein = 0, '',''
    while i < len(rna):
        if len(triple) == 3:
            protein += rna_codon[triple]
            triple = ''
        triple += rna[i]
        i += 1
    return protein
