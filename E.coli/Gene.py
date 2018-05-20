from Bio import SeqIO

for genome in SeqIO.parse('EcoliGenome.gb','genbank'):
    for gene in genome.features:
        if(gene.type =="CDS"):
            if 'gene' in gene.qualifiers:
            	start=gene.location.start.position
                end=gene.location.end.position
                print gene, start, end