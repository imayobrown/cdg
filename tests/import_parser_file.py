#!/usr/bin/env python

'''
Support file for import parser test
'''

from argparse import ArgumentParser

parser = ArgumentParser(prog='test_prog', description='test_prog description')

parser_with_subcommands = ArgumentParser(prog='test_prog_subcommands')
subparsers = parser_with_subcommands.add_subparsers(help='sub-command help')

parser_a = subparsers.add_parser('a', help='a help')
parser_a.add_argument('--x', help='x argument help')

parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('y', help='y argument help')

def get_parser():
    parser = ArgumentParser(prog='test_prog')
    return parser

def get_parser_with_subcommands():
    parser = ArgumentParser(prog='test_prog_subcommands')
    subparser = parser.add_subparsers()

    parser_a = subparser.add_parser('a', help='a help')
    parser_a.add_argument('--x', help='x argument help')

    parser_b = subparser.add_parser('b', help='b help')
    parser_b.add_argument('y', help='y argument help')

    return parser
