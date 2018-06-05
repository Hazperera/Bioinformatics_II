import sys, argparse

#------------------------------------------------------------------------------
# Name : startingKmer()
# Description : This function aims to find the kmer that initiates the path.
#               Initial kmer is found by finding which kmer's prefix doesn't
#               have an overlap.
# Parameters/Flags :
#       (list) kmers - list of kmers.
# Return Value :
#       (str) kmer - starting kmer.
#------------------------------------------------------------------------------
def startingKmer( kmers ) :
    prefixes = list()
    suffixes = list()
    starter = ""

    for kmer in kmers :
        prefix = kmer[:-1]
        suffix = kmer[1:]

        prefixes.append( prefix )
        suffixes.append( suffix )

    for suff in suffixes :
        if suff in prefixes :
            prefixes.remove(suff)

    for kmer in kmers :
        if ''.join(prefixes) in kmer :
            starter = kmer

    return starter

#------------------------------------------------------------------------------
# Name : genomePath()
# Description : This function aims to reconstruct the kmers into a single
#               DNA string, or so called finding the genome path.
# Parameters/Flags :
#       (str) starter - initial kmer for the path.
#       (list) kmers - list of kmers.
# Return Value :
#       (str) path - fully reconstructed DNA sequence from kmers.
#------------------------------------------------------------------------------
def genomePath( starter, kmers ) :
    limit = len(starter) + len(kmers) - 1
    path = starter
    kmers.remove(starter)

    # Dictionary that holds pair of prefix and suffix
    presufDict = dict()

    # Populate the Dictionary
    for kmer in kmers :
        prefix = kmer[:-1]
        suffix = kmer[1:]

        presufDict[ prefix ] = suffix

    # Predefine suffix
    suff = path[ 1 : ]

    while len(path) < limit :
        if suff in presufDict :
            path += presufDict[suff][-1]
            suff = presufDict[suff]

    return path

#------------------------------------------------------------------------------
# Name : parse_args()
# Function : Parses the arguments with given flags when running the program.
# Parameters/Flags :
#       Input file example :
#           5
#           CAATCCAAC
#
# Return Value :
#       parser.parse_args() - Returning 'ArgumentParser' object with info.
#------------------------------------------------------------------------------
def parse_args(args) :
    parser = argparse.ArgumentParser(
                usage = '%(prog)s <input_file> [-o] <output_file>',
                description = 'It will provide all possible k-mers from a '
                            + 'given sequence')
    # Optional Arguments (Flags)
    parser.add_argument('--output', '-o', dest = 'o', required = False,
                        nargs = '?', type = argparse.FileType('w'),
                        default = argparse.SUPPRESS,
                        help = 'Write out to a file.')

    # Positional Arguments (User input parameters)
    parser.add_argument('file', type = argparse.FileType('r'),
                                help = 'File contaning value k and a sequence.')

    return parser.parse_args()

#------------------------------------------------------------------------------
# Name : main()
# Description : Where the program starts.
#------------------------------------------------------------------------------
def main() :
    args = parse_args(sys.argv[1:])

    with args.file as file :
        kmers = file.read().splitlines()

    # Find which kmer is the start of the path.
    starter = startingKmer( kmers )

    # Reconstruct the path.
    path = genomePath( starter, kmers )

    # Write out to a file or on the console.
    if 'o' in args :
        with args.o as outfile :
            outfile.write( path )
            outfile.close()
    else : print( path )

if __name__ == '__main__' :
    main()
