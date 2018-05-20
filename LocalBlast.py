from Bio.Blast.Applications import NcbiblastnCommandline
import os
import glob

#DIRECTIONS: File must be placed with db files and fasta files to be blasted, Change directory to be made, change movemnt directory

#Make a new directory to move the matched genomes too
os.makedirs("C:\\Users\Kashyap\Desktop\CodonBiasExploit\CodonBiasProject\TestFolder\k12\matched")
for file in glob.glob(os.path.join(os.getcwd(), '*.fasta')):
    name = os.path.basename(file)
    blastn = NcbiblastnCommandline(query=name, db='housekeeping', outfmt='"10 bitscore"')
    result = list(blastn())
    bitscore = result[0]
    #Change bitscore into an int
    if(bitscore == ''):
        bitscore = 0
    else:
        bitscore = int(bitscore)

    #Move the fasta file if bitscore > 50, currently does not move files but prints file name and score.
    if(bitscore > 50):
        os.rename("C:\\Users\Kashyap\Desktop\CodonBiasExploit\CodonBiasProject\TestFolder\k12\\", "C:\\Users\Kashyap\Desktop\CodonBiasExploit\CodonBiasProject\TestFolder\k12\matched\\")
        print(bitscore)
        print(name)