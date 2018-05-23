
from Bio import SeqIO
gb_file = "EcoliGenome.gb"
for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    # now do something with the record
    print "Name %s, %i features" % (gb_record.name, len(gb_record.features))
    print repr(gb_record.seq)
    #print(gb_record.seq)
    gb_feature = gb_record.features
    print gb_feature

#for genome in SeqIO.parse('EcoliGenome.gb','genbank'):
        #print(seq_record.id)
        
        #for gene in genome.features:
            #if gene.type != "CDS":
            	#continue
        #if 'gene' in gene.qualifiers:
            #print(gene)
            #continue
            #gene_seq = gene.extract(genome.seq)
            #print (genome.description, gene_seq)
        #geneSeq= gene.extract(genome.seq)
        #print(geneSeq)

        #for 'gene_synonym' in gene.qualifiers
        #print(gene_synonym)
        #for key = 'gene_synonym' in qualifiers
        #print (gene_synonym)



        
        



       