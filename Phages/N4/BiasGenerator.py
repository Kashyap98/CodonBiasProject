from Bio import SeqIO
from Bio.SeqUtils import CodonUsage as CU
import os
import glob

CodonsDict = {
    'TTT': 0, 'TTC': 0, 'TTA': 0, 'TTG': 0, 'CTT': 0,
    'CTC': 0, 'CTA': 0, 'CTG': 0, 'ATT': 0, 'ATC': 0,
    'ATA': 0, 'ATG': 0, 'GTT': 0, 'GTC': 0, 'GTA': 0,
    'GTG': 0, 'TAT': 0, 'TAC': 0, 'TAA': 0, 'TAG': 0,
    'CAT': 0, 'CAC': 0, 'CAA': 0, 'CAG': 0, 'AAT': 0,
    'AAC': 0, 'AAA': 0, 'AAG': 0, 'GAT': 0, 'GAC': 0,
    'GAA': 0, 'GAG': 0, 'TCT': 0, 'TCC': 0, 'TCA': 0,
    'TCG': 0, 'CCT': 0, 'CCC': 0, 'CCA': 0, 'CCG': 0,
    'ACT': 0, 'ACC': 0, 'ACA': 0, 'ACG': 0, 'GCT': 0,
    'GCC': 0, 'GCA': 0, 'GCG': 0, 'TGT': 0, 'TGC': 0,
    'TGA': 0, 'TGG': 0, 'CGT': 0, 'CGC': 0, 'CGA': 0,
    'CGG': 0, 'AGT': 0, 'AGC': 0, 'AGA': 0, 'AGG': 0,
    'GGT': 0, 'GGC': 0, 'GGA': 0, 'GGG': 0}


# this dictionary shows which codons encode the same AA
SynonymousCodons = {
    'CYS': ['TGT', 'TGC'],
    'ASP': ['GAT', 'GAC'],
    'SER': ['TCT', 'TCG', 'TCA', 'TCC', 'AGC', 'AGT'],
    'GLN': ['CAA', 'CAG'],
    'MET': ['ATG'],
    'ASN': ['AAC', 'AAT'],
    'PRO': ['CCT', 'CCG', 'CCA', 'CCC'],
    'LYS': ['AAG', 'AAA'],
    'STOP': ['TAG', 'TGA', 'TAA'],
    'THR': ['ACC', 'ACA', 'ACG', 'ACT'],
    'PHE': ['TTT', 'TTC'],
    'ALA': ['GCA', 'GCC', 'GCG', 'GCT'],
    'GLY': ['GGT', 'GGG', 'GGA', 'GGC'],
    'ILE': ['ATC', 'ATA', 'ATT'],
    'LEU': ['TTA', 'TTG', 'CTC', 'CTT', 'CTG', 'CTA'],
    'HIS': ['CAT', 'CAC'],
    'ARG': ['CGA', 'CGC', 'CGG', 'CGT', 'AGG', 'AGA'],
    'TRP': ['TGG'],
    'VAL': ['GTA', 'GTC', 'GTG', 'GTT'],
    'GLU': ['GAG', 'GAA'],
    'TYR': ['TAT', 'TAC']}

outputFile = open(os.getcwd() + "\\output.txt", "w")
codonCount = CodonsDict.copy()
codonRatios = CodonsDict.copy()

#Count codons
for file in glob.glob(os.path.join(os.getcwd(), '*.fasta')):
    name = os.path.basename(file)
    fastaFile = open(name)

    for cur_record in SeqIO.parse(fastaFile, "fasta"):
        # make sure the sequence is lower case
        if str(cur_record.seq).islower():
            dna_sequence = str(cur_record.seq).upper()
        else:
            dna_sequence = str(cur_record.seq)
        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            if codon in codonCount:
                codonCount[codon] += 1
            else:
                print("illegal codon %s in gene: %s"
                                % (codon, cur_record.id))


print(codonCount)
totalCount = {}
ratioCount = {}
#Get Totals
for key in SynonymousCodons:
    codonList = list(SynonymousCodons[key])
    totalCount[key] = 0
    #Get Totals
    for codon in codonList:
        totalCount[key] += codonCount.get(codon)
#Get ratios of each gene
for divisiveKeys in SynonymousCodons:
    divList = list(SynonymousCodons[divisiveKeys])
    totalUsage = totalCount[divisiveKeys]
    for divisiveCodons in divList:
        ratioCount[divisiveCodons] = round(float(codonCount.get(divisiveCodons) / totalUsage), 2)
        outputFile.write(divisiveCodons + " = " + str(ratioCount.get(divisiveCodons)) + "\n")

outputFile.close()
print(totalCount)
print(ratioCount)