import os
import sys
import glob

#Get Bacteria File 1st input is bacteria name
inputs = sys.argv[1:]
bacteriaFileName = inputs[0] + ".txt"
bacteriaFile = open(bacteriaFileName, "r")
bacteriaContent = list(bacteriaFile.readlines())
outputFile = open(os.getcwd() + "\\Correlation.txt", "w")


for phageFiles in glob.glob(os.path.join(os.getcwd(), '*.txt')):
    fileName = os.path.basename(phageFiles)
    fileName = os.path.splitext(fileName)[0]
    if fileName is not bacteriaFileName:
        cPhageFile = open(phageFiles, "r")
        correlationDict = {}
        phageContent = list(cPhageFile.readlines())
        print(bacteriaContent)
        print(phageContent)
        for codons in bacteriaFile:
            bacteriaNumber = bacteriaFile[codons]
            phageNumber = phageContent[codons]
            correlationDict[codons] = [bacteriaNumber, phageNumber]
