import sys, argparse

def findOverlapGraph( kmers ) :
    kmerDict = dict()

    # create empty dictionary of kmers
    for kmer in kmers : kmerDict.setdefault( kmer, [] )

    # populate the dictionary
    for i in range( len(kmers) ) :
        suffix = kmers[i][1:]

        for j in range( len(kmers) ) :
            prefix = kmers[j][:-1]

            if prefix == suffix : kmerDict[ kmers[i] ].append( kmers[j] )

    return kmerDict

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

    graphDict = findOverlapGraph( kmers )

    if 'o' in args :
        with args.o as outfile :
            for k, v in graphDict.items() :
                if v :
                    outfile.write( k + ' -> ' + ','.join(v) + '\n' )
                else : continue

            #outfile.write()


if __name__ == '__main__' :
    main()
