import os
import sys
import glob

#Get Bacteria File 1st input is bacteria name
inputs = sys.argv[1:]
bacteriaFileName = inputs[0] + ".txt"
bacteriaFile = open(bacteriaFileName, "r")
bacteriaContent = bacteriaFile.readlines()
bacteriaDict = {}

for x in bacteriaContent:
    row = x.split('=')
    codon = row[0].strip()
    number = row[1].strip()
    bacteriaDict[codon] = number

outputFile = open(os.getcwd() + "\\Correlation.txt", "w")


for phageFiles in glob.glob(os.path.join(os.getcwd(), '*.txt')):
    fileName = os.path.basename(phageFiles)
    fileName = os.path.splitext(fileName)[0]
    if fileName is not bacteriaFileName:
        cPhageFile = open(phageFiles, "r")
        correlationDict = {}
        phageContent = cPhageFile.readlines()
        phageDict = {}
        for phages in phageContent:
            row = phages.split('=')
            print(row)
            phageCodon = row[0].strip()
            phageNumber = row[1].strip()
            print(phageCodon)
            print(phageNumber)
            phageDict[phageCodon] = phageNumber
        print(phageDict)
        for codons in bacteriaDict:
            #print(phageDict[codons])
            codonValues = list(bacteriaDict[codons])
            correlationDict[codons] = codonValues
            #print(correlationDict)