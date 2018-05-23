from Bio import SeqIO
import os
import sys
#DIRECTIONS: Place in the same folder as the genbank file, change the new directory name to new genome name, change the file being opened

inputs = sys.argv[1:]
#Create directory and initialize lists
os.makedirs(os.getcwd() + "\\" + str(inputs[0]))
os.makedirs(os.getcwd() + "\\" + str(inputs[0]) + "\\matched")
nameList = []
seqList = []

#Move files into appropriate directories
os.rename(os.getcwd() + "\\LocalBlast.py" ,
          os.getcwd() + "\\" + str(inputs[0]) + "\\LocalBlast.py")
os.rename(os.getcwd() + "\\BiasGenerator.py" ,
          os.getcwd() + "\\" + str(inputs[0]) + "\\matched\\BiasGenerator.py")
os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nhr" ,
          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nhr")
os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nin" ,
          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nin")
os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nsq" ,
          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nsq")

#Get Genbank Data, seperate the name and seq and add to lists
for genes in SeqIO.parse(open(str(inputs[0]) + ".gb","r"), "genbank"):
    for features in genes.features:
        if features.type == "CDS":
            name = features.qualifiers['locus_tag'][0]
            seq = features.extract(genes.seq)
            nameList.append(name)
            seqList.append(seq)

print(len(nameList))
#Go through lists and write new fasta files for each gene
for i in range(len(nameList)):
    fastaFile = open(os.getcwd() + "\\" + str(inputs[0]) + "\\" + nameList[i] + ".fasta", "w")
    fastaFile.write(">" + nameList[i] + "\n" + str(seqList[i]) + "\n")
    fastaFile.close()


#os.system(os.getcwd() + "\\" + str(inputs[0]) + "\\LocalBlast.py")