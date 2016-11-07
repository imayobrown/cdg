#!/usr/bin/env python

'''
Generate documentation for cli. Needs to be able to handle a variety
of different ways that cli is implemented. Goal is to be able to handle
any type of command line executable but will begin development with assumption
that executable was written in python using argparse.

Possible Scenarios:

1. Usage of argparse ArgumentParser
2. Usage of optparse OptionParser
3. Unknown method/custom method (complicated because it will involve a lot of regex)
'''

from argparse import ArgumentParser
from cdg.generate_docs import generate_docs

def get_parser():
    '''
    Get the parser object
    '''

    parser = ArgumentParser(prog='cdg',
		description='Command Line Documentation Generator')
    parser.add_argument('prog', type=str,
                        help='The executable that implements the cli.')
    parser.add_argument('parser', type=str,
                        help='The function in the executable that returns the ArgumentParser object or, if directly exposed, the variable name that holds the ArgumentParser object')

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    generate_docs(args.prog, args.parser)

if __name__ == '__main__':
    main()
