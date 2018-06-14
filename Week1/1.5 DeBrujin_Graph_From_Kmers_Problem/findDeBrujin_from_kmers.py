import sys, argparse




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
                description = 'It will debrujin graph from the given list of '
                            + 'kmers.')

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
        kmers = file.read().splitlines()

    


if __name__ == '__main__' :
    main()
