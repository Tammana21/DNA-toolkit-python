#DNA Toolset/code testing file
from DNAtoolkit import *
from Utility import colored
import random 

rndDNAStr =''.join([random.choice(Nucleotides)
                    for nu in range(50)])
DNAStr = validateSeq(rndDNAStr)
print(f'\n Sequence: {colored(DNAStr)}\n')
print(f'[1] + sequence length: {len(DNAStr)}\n')
print(colored( f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(f"[4] DNA String + Reverse complement:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")