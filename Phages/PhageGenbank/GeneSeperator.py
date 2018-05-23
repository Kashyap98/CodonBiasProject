from Bio import SeqIO
import os
import sys
import shutil
import glob
#DIRECTIONS: Place in the same folder as the genbank file, change the new directory name to new genome name, change the file being opened

inputs = sys.argv[1:]
#Create directory and initialize lists
#os.makedirs(os.getcwd() + "\\" + str(inputs[0]))

#os.rename(os.getcwd() + "\\BiasGenerator.py" ,
#          os.getcwd() + "\\" + str(inputs[0]) + "\\matched\\BiasGenerator.py")
#os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nhr" ,
#          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nhr")
#os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nin" ,
#          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nin")
#os.rename(os.getcwd() + "\\" + str(inputs[1]) + ".nsq" ,
#          os.getcwd() + "\\" + str(inputs[0]) + "\\" + str(inputs[1]) + ".nsq")

for genbankFiles in glob.glob(os.path.join(os.getcwd(), '*.gb')):
    nameList = []
    seqList = []
    currentFile = open(genbankFiles, "r")
    print(currentFile)
    fileName = os.path.basename(genbankFiles)
    fileName = os.path.splitext(fileName)[0]
    print(fileName)
    os.makedirs(os.getcwd() + "\\" + fileName + "\\")
    shutil.copy(str(inputs[0]) + ".nhr", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy(str(inputs[0]) + ".nin", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy(str(inputs[0]) + ".nsq", os.getcwd() + "\\" + fileName + "\\")
    shutil.copy("BiasGenerator.py", os.getcwd() + "\\" + fileName + "\\")

    #Get Genbank Data, seperate the name and seq and add to lists
    for genes in SeqIO.parse(currentFile, "genbank"):
        for features in genes.features:
            if features.type == "CDS":
                #if features.qualifiers['gene'][0] is not None:
                if ['gene'][0] in features.qualifiers:
                    name = features.qualifiers['gene'][0]
                elif ['locus_tag'][0] in features.qualifiers:
                    name = features.qualifiers['locus_tag'][0]
                else:
                    name = "error"

                seq = features.extract(genes.seq)
                nameList.append(name)
                seqList.append(seq)
        print(len(nameList))

        #Go through lists and write new fasta files for each gene
        for i in range(len(nameList)):
            fastaFile = open(os.getcwd() + "\\" + fileName + "\\" + nameList[i] + ".fasta", "w")
            fastaFile.write(">" + nameList[i] + "\n" + str(seqList[i]) + "\n")
            fastaFile.close()
