from Bio import SeqIO
import os
import sys
import shutil
import glob
#DIRECTIONS: Place in the same folder as the genbank file, change the new directory name to new genome name, change the file being opened

inputs = sys.argv[1:]

for genbankFiles in glob.glob(os.path.join(os.getcwd(), '*.gb')):
    nameList = []
    seqList = []
    currentFile = open(genbankFiles, "r")
    print(currentFile)
    fileName = os.path.basename(genbankFiles)
    fileName = os.path.splitext(fileName)[0]
    print(fileName)
    os.makedirs(os.getcwd() + "\\" + fileName + "\\")
    os.makedirs(os.getcwd() + "\\" + fileName + "\\matched")
    shutil.copy(str(inputs[0]) + ".nhr", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy(str(inputs[0]) + ".nin", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy(str(inputs[0]) + ".nsq", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy("BacteriaBias.py", os.getcwd() + "\\" + fileName + "\\matched\\")
    shutil.copy("LocalBlast.py", os.getcwd() + "\\" + fileName + "\\")

    #Get Genbank Data, seperate the name and seq and add to lists
    for genes in SeqIO.parse(currentFile, "genbank"):
        for features in genes.features:
            if features.type == "CDS":
                name = features.qualifiers['locus_tag'][0]
                seq = features.extract(genes.seq)
                nameList.append(name)
                seqList.append(seq)
        print(len(nameList))

        #Go through lists and write new fasta files for each gene
        for i in range(len(nameList)):
            fastaFile = open(os.getcwd() + "\\" + fileName + "\\" + nameList[i] + ".fasta", "w")
            fastaFile.write(">" + nameList[i] + "\n" + str(seqList[i]) + "\n")
            fastaFile.close()
