import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein, generic_dna
from Bio.Blast import NCBIStandalone

testSeq = Seq("GTACCGTCA", generic_dna)

print(testSeq)
print(testSeq.alphabet)
print("hello")
