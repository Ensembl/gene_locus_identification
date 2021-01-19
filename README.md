# Gene Locus Identification

https://www.ebi.ac.uk/seqdb/confluence/display/ENSGBD/Gene+Locus+Identification




Example commands to run: 


# data:
export GENOMES_DIR=/hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/genomes/
export DATA_DIR_IN=/nfs/production/panda/ensembl/kbillis/machine_learning_projects/Gene_Locus_Identification/code/gene_locus_identification/data/
export ENSCODE=/nfs/production/panda/ensembl/kbillis/enscode_2020_08/enscode/

# get genomes:
wget ftp://ftp.ensembl.org/pub/release-102/fasta/pan_troglodytes/dna/Pan_troglodytes.Pan_tro_3.0.dna.toplevel.fa.gz
#or:


# Done that (uncomment if nesecary):
perl $ENSCODE/ensembl-analysis/scripts/sequence_dump.pl $(mysql-ens-mirror-1 details -script_db) -dbname pan_troglodytes_core_101_3 -toplevel -onefile -filename $GENOMES_DIR/chimpanzee_softmasked.fa -mask -softmask -mask_repeat dust -mask_repeat repeatmask_repbase_primates -coord_system_name Pan_tro_3.0

perl $ENSCODE/ensembl-analysis/scripts/sequence_dump.pl $(mysql-ens-mirror-1 details -script_db) -dbname oryctolagus_cuniculus_core_103_2 -toplevel -onefile -filename $GENOMES_DIR/rabbit_softmasked.fa -mask -softmask -mask_repeat dust -mask_repeat repeatmask_repbase_primates -coord_system_name OryCun2.0


# genomes will be:
ls -l /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/genomes/

# get seq data:
python /nfs/production/panda/ensembl/kbillis/machine_learning_projects/Gene_Locus_Identification/code/gene_locus_identification/gene_locus_identification/fetch_gene_seq.py   -i /nfs/production/panda/ensembl/kbillis/machine_learning_projects/Gene_Locus_Identification/code/gene_locus_identification/data/human_orthologues.csv   -o /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/kbillis/test1/human_genes.fa

# index blast db:
convert2blastmask -in $GENOMES_DIR/chimpanzee_softmasked.fa  -parse_seqids -masking_algorithm repeatmasker -masking_options "repeatmasker, default" -outfmt maskinfo_asn1_bin -out $GENOMES_DIR/chimpanzee_softmasked.fa.asnb
makeblastdb -in $GENOMES_DIR/chimpanzee_softmasked.fa  -dbtype nucl -parse_seqids -mask_data $GENOMES_DIR/chimpanzee_softmasked.fa.asnb

convert2blastmask -in $GENOMES_DIR/rabbit_softmasked.fa  -parse_seqids -masking_algorithm repeatmasker -masking_options "repeatmasker, default" -outfmt maskinfo_asn1_bin -out $GENOMES_DIR/rabbit_softmasked.fa.asnb
makeblastdb -in $GENOMES_DIR/rabbit_softmasked.fa  -dbtype nucl -parse_seqids -mask_data $GENOMES_DIR/rabbit_softmasked.fa.asnb


# blast command:
blastn -db $GENOMES_DIR/chimpanzee_softmasked.fa   -query /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/kbillis/test1/human_genes.fa  -out /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/kbillis/test1/humanGenes_to_chimpanzeeGenome_blastn.out -outfmt 6

blastn -db $GENOMES_DIR/rabbit_softmasked.fa   -query /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/kbillis/test1/human_genes.fa  -out /hps/nobackup2/production/ensembl/genebuild/production/gene-locus-identification/kbillis/test1/humanGenes_to_rabbitGenome_blastn.out -outfmt 6

