# CodonBiasProject
FYRE 2018 Codon Bias Project

*Steps to extract bacteria codon bias:*

1. Copy all contents of MasterBacteria (BacteriaBias, BacteriaGenes, LocalBlast, and all 3 housekeeping files) into
the same folder as the genbank(full) for desired bacteria genomes.

2. In the command prompt. Type 'cd ' and go into the directory in which you have the bacteria genbank files and the 
contents of MasterBacteria. This can be done easily by clicking on the folder in the file explorer and copying the
directory and pasting it after 'cd'.

3. In the command prompt. Type 'python BacteriaGenes.py [name of database (housekeeping, in this case)]'

4. In the command prompt. Type 'cd [name of bacteria]'

5. In the command prompt. Type 'python LocalBlast.py'

6. In the command prompt. Type 'cd [matched]'

7. In the command prompt. Type 'python BacteriaBias.py' 

8. Rename 'output.txt' to '[bacteria name].txt'


*Steps to extract phage codon bias:*

1. Copy all contents of MasterPhage (PhageBias, PhageGenes, Correlation) into the same folder as all genbank(full) 
for desired phage genomes.

2. In the command prompt. Type 'cd ' and go into the directory in which you have the phage genbank files and the 
contents of MasterPhage. This can be done easily by clicking on the folder in the file explorer and copying the
directory and pasting it after 'cd'.

3. In the command prompt. Type 'python PhageBias.py' (This runs the script to attain the codon bias of the phage)

4. [phage name]output.txt is the bias for each of the phages. These files are found in the correlation folder.
This is done to make finding the correlation easier.

_________________________________________________________________________________________________________________
*Steps to attain correlation:*

1. Find the bias file for the bacteria in which you want to find a correlation to for the phages. Place this file in 
the same correlation folder as the desired phages.

2. In the command prompt. Type 'cd ' and go into the directory in which you have the correlation files. This can be
done easily by clicking on the folder in the file explorer and copying the directory and pasting it after 'cd'. 

3. Ensure the correlation files for the phages and the bacteria are in the correlation folder.

4. In the command prompt. type 'python Correlation.py [bacteria name]'

5. The output file is Correlation.txt and will have the name of each phage and the first number after is correlation
in decimal form. 

Sequence of files BACTERIA:
Splitter.py
BacteriaGenes.py
LocalBlast.py
BacteriaBias.py

Sequence of files PHAGE:
Splitter.py
PhageGenes.py
PhageBias.py

Much of the code is shared between files with similar names, the difference is only the name because it is simpler for
the end user. 

##//TODO//##
Automate LocalBlast.py so it only has to be run once.
Automate BacteriaBias.py so that it is like PhageBias.py

##Libraries##
Ensure you have Python 3 correctly installed, and Blast+ (Blastn) from the Installation Guide.
In addition, Biopython and Scipy were also used.
