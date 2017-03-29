#!/usr/bin/env python
#-*- coding:utf-8 -*-

##---------------------------------------------------------------------------------------------

## This script is used to deal with the reference genome
##
## Usages:
##      python *.py reference_genome.fa
##
## NB: based on last-759
## this script will creat one directory name reference.
## Dependencies: Biopython, LAST
##               
##---------------------------------------------------------------------------------------------
import sys
from Bio import SeqIO
import os

target=sys.argv[1]
t_abspath=os.path.abspath(target)
t_fullname=os.path.basename(target)
t_name=os.path.splitext(t_fullname)[0]

os.system('mkdir -p reference/Nib_t reference/tba')

def deal_target():
    tf1=open(target,'r')
    tf2=open('./reference/t1.fa','w')
    tf22=open('./reference/tba/%s.fa'%(t_name),'w')
    for seq_record in SeqIO.parse(tf1,'fasta'):
	id=str(seq_record.id)
        seq=str(seq_record.seq)
        length=str(len(seq))
        tf2.write('>'+ t_name + '.'+ id +'\n'+ seq +'\n')
        tf22.write('>'+ t_name + ':'+ id + ':' + '1' + ':' + '+' + ':' + length + '\n'+ seq +'\n')
    tf1.close()
    tf2.close()
    tf22.close()	

def main():
    deal_target()
    lastdb()
    trans()

if __name__=='__main__': 
    main()
