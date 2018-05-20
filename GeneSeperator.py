from Bio import SeqIO
import os
#DIRECTIONS: Place in the same folder as the genbank file, change the new directory name to new genome name, change the file being opened

#Create directory and initialize lists
os.makedirs("C:\\Users\Kashyap\Desktop\CodonBiasExploit\CodonBiasProject\TestFolder\k12")
nameList = []
seqList = []
#Get Genbank Data, seperate the name and seq and add to lists
for genes in SeqIO.parse(open("k12Genome.gb","r"), "genbank"):
    for features in genes.features:
        if features.type == "CDS":
            name = features.qualifiers['gene'][0]
            seq = features.extract(genes.seq)
            nameList.append(name)
            seqList.append(seq)

print(len(nameList))
#Go through lists and write new fasta files for each gene
for i in range(len(nameList)):
    fastaFile = open(os.getcwd() + "/k12/" +nameList[i]+ ".fasta", "w")
    fastaFile.write(">" + nameList[i] + "\n" + str(seqList[i]) + "\n")
    fastaFile.close()
