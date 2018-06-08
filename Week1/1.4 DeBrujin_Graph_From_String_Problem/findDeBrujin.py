import sys, argparse

#------------------------------------------------------------------------------
# Name : getDeBrujinGraph()
# Function : Given DNA string, it will first get sequence of kmers, then
#            divide each kmers into prefix and suffix. Then, this algorithm
#            combine those with the same prefixes together.
# Parameters/Flags :
#       (int) kval - length of k.
#       (str) dna - string of DNA.
# Return Value :
#       (dict) debrujinDict - representation of debrujin graph from the string.
#------------------------------------------------------------------------------
def getDeBrujinGraph( kval, dna ) :
    kmers = list()
    debrujinDict = dict()

    # Step 1 : break it into sequence of k-mers.
    [kmers.append( dna[i:i+kval] ) for i in range( len(dna)-kval+1 )]

    # Step 2 : create dictionary with only unique keys (prefixes).
    for kmer in kmers : debrujinDict.setdefault( kmer[:-1], [] )

    # Step 3 : Fill in the correlated suffixes to the dictionary.
    for kmer in kmers :
        pre = kmer[:-1]
        suf = kmer[1:]

        debrujinDict[pre].append(suf)

    return debrujinDict

#------------------------------------------------------------------------------
# Name : parse_args()
# Function : Parses the arguments with given flags when running the program.
# Parameters/Flags :
#       Input file.
#
# Return Value :
#       parser.parse_args() - Returning 'ArgumentParser' object with info.
#------------------------------------------------------------------------------
def parse_args( args ) :
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
    args = parse_args( sys.argv[1:] )

    with args.file as file :
        contents = file.read().splitlines()
        k = int( contents[0] )
        dna = contents[1]

    debrujin = getDeBrujinGraph( k, dna )

    if 'o' in args :
        with args.o as outfile :
            for k, v in debrujin.items() :
                outfile.write( k + ' -> ' + ','.join(v) + '\n' )

            outfile.close()

if __name__ == '__main__' :
    main()
