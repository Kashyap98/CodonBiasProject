import os
import sys
import glob
from scipy import stats as corr

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

#outputFile = open(os.getcwd() + "\\Correlation.txt", "w")


for phageFiles in glob.glob(os.path.join(os.getcwd(), '*.txt')):

    phageDict = {}
    bacteriaArray = []
    phageArray = []
    cPhageFile = open(phageFiles, "r")
    correlationDict = {}
    phageContent = cPhageFile.readlines()

    for y in phageContent:
        row = y.split('=')
        phageCodon = row[0].strip()
        phageNumber = row[1].strip()
        phageDict[phageCodon] = phageNumber

    for codons in bacteriaDict:
        bacteriaArray.append(float(bacteriaDict.get(codons)))
        phageArray.append(float(phageDict.get(codons)))

    correlation = corr.pearsonr(bacteriaArray, phageArray)

    print(correlation)

