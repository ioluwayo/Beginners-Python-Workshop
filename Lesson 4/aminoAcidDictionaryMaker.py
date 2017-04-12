# Created by ioluwayo on 2017-03-28.

"""
Makes a key value mapping with codons as keys and amino acids as values. See DNA to amino acid conversion table

This is what the dictionary looks like:

aminoAcidDictionary ={'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'AGG': 'R', 'UAU': 'Y',
                      'UAG': 'X', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'AAU': 'N', 'GUU': 'V', 'CAC': 'H', 'AAA': 'K',
                      'AGU': 'S', 'CAG': 'Q', 'CAA': 'Q', 'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'AUG': 'M', 'CGA': 'R',
                      'CCA': 'P', 'GAU': 'D', 'UGG': 'W', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G',
                      'GGC': 'G', 'GAG': 'E', 'UCC': 'S', 'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'GCA': 'A', 'GCC': 'A',
                      'CUU': 'L', 'UCA': 'S', 'GCG': 'A', 'UGA': 'X', 'AUC': 'I', 'AUA': 'I', 'UAA': 'X', 'GCU': 'A',
                      'CAU': 'H', 'CUA': 'L', 'CUC': 'L', 'UUG': 'L', 'ACG': 'T', 'CUG': 'L', 'UUU': 'F', 'CGU': 'R',
                      'CCG': 'P', 'UGC': 'C', 'UGU': 'C', 'AUU': 'I', 'ACA': 'T', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}

"""
def createAminoAcidDictionary():
    # SEE: Codon_to_amino Acid table for reference
    letters = ('G', 'A', 'C', 'U')
    codons = []  # a sequence of three nucleotides that together form a unit of genetic code in a DNA or RNA molecule.
    for a in letters:
        for b in letters:
            for c in letters:
                codons.append(a + b + c)  # this creates a list of all possible codons (permutations of DNA)
    print codons
    print 'length of all possible DNA codes: ', len(codons)  # 64 is expected

    #   A string of all amino acids represented by the first letter of their names
    amino_acid = "GGGGEEDDAAAAVVVVRRSSKKNNTTTTMIIIRRRRQQHHPPPPLLLLWXCCXXYYSSSSLLFF"
    amino_acid_dictionary = {} # empty
    # now create a dictionary of amino acid DNA pairs. e.g {'GGG': 'G','AUG': 'M','UUU': 'P'}
    for i in range(len(codons)):
        amino_acid_dictionary[codons[i]] = amino_acid[i] # this builds the dictionary. Key => value
    return amino_acid_dictionary

