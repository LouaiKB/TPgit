"""

    Author: louai kb

"""

# !usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from Bio import SeqIO

def create_parser():
    """
    function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', type=str, required=True)
    parser.add_argument('-seq', '--ids', type=str, required=True)
    return parser

def main():
    """
    function
    """
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    fasta = []

    for i in SeqIO.parse(args['inputfile'], 'fasta'):
        fasta.append(i)

    ids = args['ids'].split(',')

    for i in ids:
        for j in fasta:
            if i == j.id:
                print('>' + j.id + '\n' + j.seq)

if __name__ == '__main__':
    main()
