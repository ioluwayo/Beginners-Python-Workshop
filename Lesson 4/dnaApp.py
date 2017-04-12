# Created by ioluwayo on 2017-03-28.

'''
    This program reads a DNA sequence from a file, and converts teh sequence
    to a protein. A few helper functions have been left out for you to implement
    yourself. You should get into the habit of puting your functions in modules.
'''

def makeProteinUsingDictionary(rna):
  #now we need to amino acid dictionary.
  # i created it in advance for us.
  aminoAcidDictionary ={'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'AGG': 'R', 'UAU': 'Y',
                        'UAG': 'X', 'AGC': 'S', 'AAG': 'K', 'AGA': 'R', 'AAU': 'N', 'GUU': 'V', 'CAC': 'H', 'AAA': 'K',
                        'AGU': 'S', 'CAG': 'Q', 'CAA': 'Q', 'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'AUG': 'M', 'CGA': 'R',
                        'CCA': 'P', 'GAU': 'D', 'UGG': 'W', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G',
                        'GGC': 'G', 'GAG': 'E', 'UCC': 'S', 'UAC': 'Y', 'GAC': 'D', 'GAA': 'E', 'GCA': 'A', 'GCC': 'A',
                        'CUU': 'L', 'UCA': 'S', 'GCG': 'A', 'UGA': 'X', 'AUC': 'I', 'AUA': 'I', 'UAA': 'X', 'GCU': 'A',
                        'CAU': 'H', 'CUA': 'L', 'CUC': 'L', 'UUG': 'L', 'ACG': 'T', 'CUG': 'L', 'UUU': 'F', 'CGU': 'R',
                        'CCG': 'P', 'UGC': 'C', 'UGU': 'C', 'AUU': 'I', 'ACA': 'T', 'UUA': 'L', 'CGC': 'R', 'UUC': 'F'}
  protein = ''  # empty string.We will grow it as we loop through the rna in triplets converting each group to an
  # aminoacid
  for i in range(0, lengthOfSequence, 3):  # codons are in triplets
      codon = rna[i:i + 3]  # we need 3. so we go from i to i + 3
      aminoacid = aminoAcidDictionary[codon]  # using dictionary to get amino acid
      protein += aminoacid  # concatenating the amino acids to form a protein. we keep growing the protein,
      # we dont replace it
  return protein # the function returns the result


def convertDnaToRna(dna):
    dna = dna.upper()
    rna = dna.replace('T','U')
    return rna


# This here is the main function in this module.
  infile1 = open("dna.text")  # open the text file
  dna = infile1.read().strip() # read everything once and remove trailing spaces
  dna = dna.replace('\n', '')  # remove newline character
  lengthOfSequence = len(dna) # get the lenght of the sequence.
  #print "length the DNA sequence is:", lengthOfSequence

  # use the dna to rna function to convert the sequence to rna
  rna = convertDnaToRna(dna)

  
  #print aminoAcidDictionary
  
  # You should use this to  test the dictionary to see that it maps correctly.
  # print "This expected {'GGG': 'G','AUG': 'M','UUU': 'F'}"
  # print "GGG:", aminoAcidDictionary["GGG"]
  # print "AUG:", aminoAcidDictionary["AUG"]
  # print "UUU:", aminoAcidDictionary["UUU"]
  #
  
  # now lets make the protein (amino acid sequence) from rna  sequence
  protein = makeProteinUsingDictionary(rna)
  print protein
  
  # I left the writing to output file out as a task.