#DNA ToolKit file
import collections
from Structure import * 


#Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmseq = dna_seq.upper()
    for nuc in tmseq:
        if nuc not in Nucleotides:
            return False
    return tmseq

def countNucFrequency(tmseq):
#   tmFreDic = {"A": 0, "C": 0, "G": 0, "T": 0}
#     for nuc in tmseq:
#           tmFreDic[nuc] += 1
#    return tmFreDic 
    return dict(collections.Counter(tmseq))

def transcription(tmseq):
    return tmseq.replace("T", "U")

def reverse_complement(tmseq):
    return ''.join([DNA_Reversecomplement[nuc] for nuc in tmseq])[::-1]