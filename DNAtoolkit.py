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

def gc_count(tmseq):
    return round((tmseq.count('C') + tmseq.count('G')) / len(tmseq) * 100)

def gc_content_subsec(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subsec = seq[i:i+k]
        gc_val = gc_count(subsec)
        res.append(gc_val)
    return res

def translate_Seq(tmseq , init_pos=0):
    return ''.join(DNA_Codons[tmseq[pos:pos + 3]] for pos in range(init_pos, len(tmseq) - 2, 3))

def codon_usage(tmseq, aminoacid):
    tmlist = []
    for i in range(0, len(tmseq) -2, 3):
        if DNA_Codons[tmseq[i:i+3]] ==aminoacid:
            tmlist.append(tmseq[i:i+3])

    freqdict = dict(collections.Counter(tmlist))
    Totalwight = sum(freqdict.values())
    for tmseq in freqdict:
        freqdict[tmseq] = round(freqdict[tmseq]/Totalwight, 2)
    return freqdict

def gen_reading_frames(tmseq):
    #generate 6 reading frames of a DNA sequence, including reverse complement
    frames = []
    frames.append(translate_Seq(tmseq, 0)) #press Alt+Shift+down to copy the line and edit the init_pos for each reading frame.
    frames.append(translate_Seq(tmseq, 1))
    frames.append(translate_Seq(tmseq, 2))
    frames.append(translate_Seq(reverse_complement(tmseq), 0))
    frames.append(translate_Seq(reverse_complement(tmseq), 1))
    frames.append(translate_Seq(reverse_complement(tmseq), 2))
    return frames
