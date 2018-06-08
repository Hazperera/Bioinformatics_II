import sys, argparse

#------------------------------------------------------------------------------
# Name : findOverlapGraph()
# Function : Iterates over list of kmers to find overlap graph.
# Parameters :
#       (list) kmers - list of kmers.
#
# Return Value :
#       (dict) kmerDict - representation of overlap graph.
#------------------------------------------------------------------------------
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
#       Input file.
#
# Return Value :
#       parser.parse_args() - Returning 'ArgumentParser' object with info.
#------------------------------------------------------------------------------
def parse_args(args) :
    parser = argparse.ArgumentParser(
                usage = '%(prog)s <input_file> [-o] <output_file>',
                description = 'It will provide an overlap graph from '
                            + 'given list of kmers.')
    # Optional Arguments (Flags)
    parser.add_argument('--output', '-o', dest = 'o', required = False,
                        nargs = '?', type = argparse.FileType('w'),
                        default = argparse.SUPPRESS,
                        help = 'Write out to a file.')

    # Positional Arguments (User input parameters)
    parser.add_argument('file', type = argparse.FileType('r'),
                                help = 'File contaning list of kmers.')

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

            # format answer
            for k, v in graphDict.items() :
                if v :
                    outfile.write( k + ' -> ' + ','.join(v) + '\n' )
                else : continue

            outfile.close()


if __name__ == '__main__' :
    main()
