import sys, argparse

#------------------------------------------------------------------------------
# Name : composition
# Function : Finds all kmers within the sequence.
# Parameters :
#       (int) k        - length of kmer
#       (str) sequence - sequence of DNA.
#
# Return Value :
#       list of kmers.
#------------------------------------------------------------------------------
def composition( k, sequence ) :
    kmersList = list()

    for i in range( len(sequence)-k+1 ) :
        kmersList.append( sequence[i:i+k] )

    return kmersList

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
    #Optional Arguments (Flags)
    parser.add_argument('--output', '-o', dest = 'o', required = False,
                        nargs = '?', type = argparse.FileType('w'),
                        default = argparse.SUPPRESS,
                        help = 'Write out to a file.')

    #Positional Arguments (User input parameters)
    parser.add_argument('file', type = argparse.FileType('r'),
                                help = 'File contaning value k and a sequence.')

    return parser.parse_args()

#------------------------------------------------------------------------------
# Name : main()
# Description : Where the program starts.
#------------------------------------------------------------------------------
def main() :
    args = parse_args(sys.argv[1:])

    # Define variables
    k = 0
    sequence = ""

    # Read the input file
    with args.file as f :
        contents = f.read().splitlines()
        k = int( contents[0] )
        sequence = contents[1].strip()

    # Call the actual algorithm
    kmers = composition( k, sequence )

    # Printing out result to the console or to a file.
    if 'o' in args :
        with args.o as outfile :
            [ outfile.write( kmer + '\n' ) for kmer in kmers ]
            outfile.close()
    else :
        [ print( kmer ) for kmer in kmers ]

if __name__ == '__main__' :
    main()
