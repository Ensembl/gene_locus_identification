# First tests

We want to look at a first round of genes from the human genome and see how they map to two other species.

## Choice of species

### Human
This is the species with the best genome annotation as it as been manually curated.

### Chimpanzee
Chimpanzee is a close relative to human, we expect that the human genes will almost perfectly match.

### Rabbit
Rabbit is more distant to human but it is a mammal so we would still expect high scores in the alignments.

## Retrieving the data
We will use the Ensembl compara database for release 101 to fetch 10 one to one orthologues for each Human-* pair.
We only select high confidence genes.

### Human-Chimpanzee
```mysql
SELECT CONCAT("http://ensembl.org/", gdb.name, "/Gene/Summary?db=core;g=", gm.stable_id) AS URL, gm.stable_id, gm.biotype_group, gm.display_label, hm.perc_cov, hm.perc_id, hm.perc_pos FROM method_link ml LEFT JOIN method_link_species_set mlss ON ml.method_link_id = mlss.method_link_id LEFT JOIN homology h ON mlss.method_link_species_set_id = h.method_link_species_set_id LEFT JOIN species_set ss ON mlss.species_set_id = ss.species_set_id LEFT JOIN genome_db gd ON ss.genome_db_id = gd.genome_db_id
LEFT JOIN homology_member hm ON h.homology_id = hm.homology_id LEFT JOIN gene_member gm ON hm.gene_member_id = gm.gene_member_id LEFT JOIN genome_db gdb ON gdb.genome_db_id = gm.genome_db_id WHERE ml.type = "ENSEMBL_ORTHOLOGUES" AND h.description = "ortholog_one2one" AND gd.assembly = "GRCh38" AND h.is_high_confidence = 1 AND mlss.name = "Hsap-Ptro orthologues" LIMIT 20;
```
| URL                                                                          | stable_id          | biotype_group | display_label | perc_cov | perc_id | perc_pos |
|------------------------------------------------------------------------------|--------------------|---------------|---------------|----------|---------|----------|
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000000771 | ENSPTRG00000000771 | coding        | ACOT11        |      100 | 98.8468 |  99.1763 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000162390       | ENSG00000162390    | coding        | ACOT11        |      100 | 98.8468 |  99.1763 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000013732 | ENSPTRG00000013732 | coding        | NKAIN4        |      100 | 96.6346 |  98.0769 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000101198       | ENSG00000101198    | coding        | NKAIN4        |      100 | 96.6346 |  98.0769 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000001756 | ENSPTRG00000001756 | coding        | RGS16         |      100 | 99.0099 |  99.0099 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000143333       | ENSG00000143333    | coding        | RGS16         |      100 | 99.0099 |  99.0099 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000051859 | ENSPTRG00000051859 | coding        | RGS8          |      100 | 99.4949 |      100 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000135824       | ENSG00000135824    | coding        | RGS8          |      100 | 99.4949 |      100 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000014572 | ENSPTRG00000014572 | coding        | ARL8B         |      100 |     100 |      100 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000134108       | ENSG00000134108    | coding        | ARL8B         |      100 |     100 |      100 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000012869 | ENSPTRG00000012869 | coding        | MAP2          |      100 | 99.4527 |  99.5621 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000078018       | ENSG00000078018    | coding        | MAP2          |      100 | 99.4527 |  99.5621 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000004305 | ENSPTRG00000004305 | coding        | RBM7          |      100 | 99.6255 |  99.6255 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000076053       | ENSG00000076053    | coding        | RBM7          |      100 | 99.6255 |  99.6255 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000013786 | ENSPTRG00000013786 | coding        | RBM11         |      100 | 99.6441 |      100 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000185272       | ENSG00000185272    | coding        | RBM11         |      100 | 99.6441 |      100 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000007653 | ENSPTRG00000007653 | coding        | ATP6V0C       |      100 | 99.3548 |  99.3548 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000185883       | ENSG00000185883    | coding        | ATP6V0C       |      100 | 99.3548 |  99.3548 |
| http://ensembl.org/pan_troglodytes/Gene/Summary?db=core;g=ENSPTRG00000043064 | ENSPTRG00000043064 | coding        | RAB8B         |      100 |     100 |      100 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000166128       | ENSG00000166128    | coding        | RAB8B         |      100 |     100 |      100 |

### Human-Rabbit
```mysql
SELECT CONCAT("http://ensembl.org/", gdb.name, "/Gene/Summary?db=core;g=", gm.stable_id) AS URL, gm.stable_id, gm.biotype_group, gm.display_label, hm.perc_cov, hm.perc_id, hm.perc_pos FROM method_link ml LEFT JOIN method_link_species_set mlss ON ml.method_link_id = mlss.method_link_id LEFT JOIN homology h ON mlss.method_link_species_set_id = h.method_link_species_set_id LEFT JOIN species_set ss ON mlss.species_set_id = ss.species_set_id LEFT JOIN genome_db gd ON ss.genome_db_id = gd.genome_db_id
LEFT JOIN homology_member hm ON h.homology_id = hm.homology_id LEFT JOIN gene_member gm ON hm.gene_member_id = gm.gene_member_id LEFT JOIN genome_db gdb ON gdb.genome_db_id = gm.genome_db_id WHERE ml.type = "ENSEMBL_ORTHOLOGUES" AND h.description = "ortholog_one2one" AND gd.assembly = "GRCh38" AND h.is_high_confidence = 1 AND mlss.name = "Hsap-Ocun orthologues" LIMIT 20;
```
| URL                                                                                | stable_id          | biotype_group | display_label | perc_cov | perc_id | perc_pos |
|------------------------------------------------------------------------------------|--------------------|---------------|---------------|----------|---------|----------|
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000008092 | ENSOCUG00000008092 | coding        | ACOT11        |  98.6555 | 87.2269 |  90.9244 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000162390             | ENSG00000162390    | coding        | ACOT11        |  96.7051 | 85.5025 |  89.1269 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000024520 | ENSOCUG00000024520 | coding        | RGS8          |  87.3684 | 62.6316 |  68.4211 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000135824             | ENSG00000135824    | coding        | RGS8          |  83.8384 |  60.101 |  65.6566 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000005163 | ENSOCUG00000005163 | coding        | MAP2          |  95.0026 |  83.342 |  87.7668 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000078018             | ENSG00000078018    | coding        | MAP2          |  99.8905 |   87.63 |  92.2824 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000007121 | ENSOCUG00000007121 | coding        | ATP6V0C       |  58.4906 | 51.3208 |  55.0943 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000185883             | ENSG00000185883    | coding        | ATP6V0C       |      100 | 87.7419 |  94.1936 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000010005 | ENSOCUG00000010005 | coding        | RAB8B         |  77.2388 | 76.4925 |  76.8657 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000166128             | ENSG00000166128    | coding        | RAB8B         |      100 | 99.0338 |  99.5169 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000027851 | ENSOCUG00000027851 | coding        | PARG          |  96.2488 | 84.9951 |  89.3386 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000227345             | ENSG00000227345    | coding        | PARG          |  99.8975 | 88.2172 |  92.7254 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000016953 | ENSOCUG00000016953 | coding        | RNF14         |      100 | 94.9367 |  97.4684 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000013561             | ENSG00000013561    | coding        | RNF14         |      100 | 94.9367 |  97.4684 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000008174 | ENSOCUG00000008174 | coding        | STAMBPL1      |  92.9638 | 89.1258 |   91.258 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000138134             | ENSG00000138134    | coding        | STAMBPL1      |      100 | 95.8716 |  98.1651 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000006863 | ENSOCUG00000006863 | coding        | SERPINB8      |      100 | 79.1444 |  90.9091 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000166401             | ENSG00000166401    | coding        | SERPINB8      |      100 | 79.1444 |  90.9091 |
| http://ensembl.org/oryctolagus_cuniculus/Gene/Summary?db=core;g=ENSOCUG00000006684 | ENSOCUG00000006684 | coding        | SRSF3         |      100 |     100 |      100 |
| http://ensembl.org/homo_sapiens/Gene/Summary?db=core;g=ENSG00000112081             | ENSG00000112081    | coding        | SRSF3         |      100 |     100 |      100 |

## Data
For each species there is three files in the data directory
### \<species\>_orthologues.lst
This is the list of gene stable and the name associated with the gene, the delimiter is "\t"

### \<species\>_five_prime.lst
This is the list of genes which are on the five prime end of the orthologue considering the forward strand. If the gene is on the reverse strand, it will be the biogical three prime end. The advantage of doing this is that the five prime end gene is always on the left on the orthologue when looking in Ensembl.

The list is ordered based on <species>_orthologues.lst

### \<species\>_three_prime.lst
This is the list of genes which are on the three prime end of the orthologue considering the forward strand. If the gene is on the reverse strand, it will be the biogical five prime end. The advantage of doing this is that the three prime end gene is always on the right on the orthologue when looking in Ensembl.

The list is ordered based on <species>_orthologues.lst

### Notes
In some cases the name will not have been assigned but the supporting evidence matches the human gene. So the stable id is present but no name is added.
When the line is empty, it means the gene was not found in the area. However the other files can have a entry for this gene "group"
SRFS3 is problematic in chimpanzee because the 3' gene is LAP3 which is a pseudogene in human. CDKN1A is just after LAP3.

## Retrieving the genome sequence

### Chimpanzee
```bash
perl $ENSCODE/ensembl-analysis/scripts/sequence_dump.pl $(mysql-ens-mirror-1 details -script_db) -dbname pan_troglodytes_core_101_3 -toplevel -onefile -filename <mypath>/chimpanzee_softmasked.fa -mask -softmask -mask_repeat dust -mask_repeat repeatmask_repbase_primates -coord_system_name Pan_tro_3.0
```

### Rabbit
```bash
perl $ENSCODE/ensembl-analysis/scripts/sequence_dump.pl $(mysql-ens-mirror-1 details -script_db) -dbname oryctolagus_cuniculus_core_101_2 -toplevel -onefile -filename <mypath>/rabbit_softmasked.fa -mask -softmask -mask_repeat dust -mask_repeat repeatmask -coord_system_name OryCun2.0
```

## Running BLAST on a sequence

### Using ensembl.org
It is possible to run BLAST on ensembl.org and has the advantage of being able to see the hits on the genome. It is possible to tweak the options but it is limited.

### On the cluster
It should be easy to run BLAST on the cluster and to tweak parameters
1. Index the genome file
This would only be done once for each genome
```bash
bsub -M2000 -R"select[mem>2000] rusage[mem=2000]" -oo <mypath>/blast.log -eo <mypath>/blast.err convert2blastmask -in <mypath>/chimpanzee_softmasked.fa -parse_seqids -masking_algorithm repeatmasker -masking_options "repeatmasker, default" -outfmt maskinfo_asn1_bin -out <mypath>/chimpanzee_softmasked.fa.asnb
bsub -M2000 -R"select[mem>2000] rusage[mem=2000]" -oo <mypath>/blast.log -eo <mypath>/blast.err makeblastdb -in <mypath>/chimpanzee_softmasked.fa -dbtype nucl -parse_seqids -mask_data <mypath>/chimpanzee_softmasked.fa.asnb -title "chimpanzee" 
```
2. Run a blast command
```bash
bsub -M2000 -n 4 -R"select[mem>2000] rusage[mem=2000] span[hosts=1]" -oo <mypath>/blast.log -eo <mypath>/blast.err tblastn -db <mypath>/chimpanzee_softmasked.fa -query <mypath>/<protein>.fa -num_threads 4 -db_soft_mask repeatmasker
```
