#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Copyright 2021 EMBL-European Bioinformatics Institute
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import requests, sys, json, os
import argparse


def fetch_endpoint(server, request, content_type):

    r = requests.get(server+request, headers={ "Accept" : content_type})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text



def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description="Parses command.")
    parser.add_argument("-i", "--input", help="Your input file with ensembl stable ids.")
    parser.add_argument("-o", "--output", help="Your fasta output file with ensembl stable ids and seqs.")
    parser.add_argument("-e", "--example", help="No input need. I will run a test.")
    options = parser.parse_args()
    
    server = "http://rest.ensembl.org/"
    
    example = options.example
    if example: 
        gene = "ENSG00000157764"
        ext_get_seq = "/sequence/id/" + gene + "?";

        get_seq = fetch_endpoint(server, ext_get_seq, "text/x-fasta")

        # print the gene name, ID and sequence
        # print(get_seq)

    else: 
        with open(options.output, 'w+') as fw:    
            with open(options.input, 'r') as f:
                for line in f:
                    if not line.strip():
                        print('empty line')
                    else: 
                        gene = line.split("\t")[0]
                        gene = gene.rstrip()
                        ext_get_seq = "/sequence/id/" + gene + "?";
                        get_seq = fetch_endpoint(server, ext_get_seq, "text/x-fasta")
                        print(get_seq, end='\n', file=fw) 



if __name__ == "__main__":
    main()

