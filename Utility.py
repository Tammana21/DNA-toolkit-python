def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }
    tmStr= ""
    for nuc in seq:
        if nuc in bcolors:
             tmStr += bcolors[nuc] + nuc
        else:
            tmStr += bcolors['reset'] + nuc
    return tmStr + '\033[0;0m'
