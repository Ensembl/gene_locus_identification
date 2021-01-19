import ensembl_rest
# this script is using ensembl_rest package
# information about this package are in: https://ensemblrest.readthedocs.io/en/latest/


# read file with list

# read blast file


def fetch_genes_in_region(region):
    species = "human"
    
    region = "13:31786617-31872809"
    # https://rest.ensembl.org/documentation/info/overlap_region
    parameters = {
        "feature": "gene",
    }
    genes = ensembl_rest.overlap_region(
        species=species,
        region=region,
        params=parameters,
    )
    print(genes)
    
    for gene in genes:
        gene_id = gene["gene_id"]
        start = gene["start"]
        end = gene["end"]
        print(f"{gene_id}: {start} - {end}")




def main():
    """
    main function
    """
    
    print("DONE")



if __name__ == "__main__":
    main()
    
