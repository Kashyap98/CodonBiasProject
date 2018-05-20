from Bio import SeqIO
from CodonBiasProject import CodonUsage
from Bio.SeqUtils import CodonUsage as CU

#Not automated yet.
testCodonUsage = CodonUsage.CodonAdaptationIndex()
fastaFile = open("A2363.fasta")
records = list(SeqIO.parse(fastaFile, "fasta"))

#WIP I don't really know what is going on here.
testCodonUsage.__init__()
testCodonUsage.generate_index("A2363.fasta")
#testCodonUsage.set_cai_index(newIndex)
test = testCodonUsage.cai_for_gene(str(records[0].seq))
print(testCodonUsage.print_index())
print(test)

