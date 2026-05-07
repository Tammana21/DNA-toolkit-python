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
print(f"3' {colored(reverse_complement(DNAStr)[::-1])} 5' [complement]")
print(f"5' {colored(reverse_complement(DNAStr))} 3' [Rev. Complement]\n")

print(f' [5] + GC content: {gc_count(DNAStr)}%\n')
print(f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr , k=5)}\n')
print(f'[7] + Amino Acid Sequence: {translate_Seq(DNAStr)}\n')
print(f'[8] + Codon Usage for amino acid "L" (Leucine): {codon_usage(DNAStr, "L")}\n')
print(f'[9] + reading frames: ')
for frames in gen_reading_frames(DNAStr):
    print((list((frames))))
