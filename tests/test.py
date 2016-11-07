#!/usr/bin/env python

'''
Tests for the cdg
'''

import unittest
from argparse import ArgumentParser
import cdg.generate_docs as generate_docs


class TestImportParser(unittest.TestCase):
    '''
    Tests for importing parser function
    '''

    def test_bare_parser_import(self):
        parser = generate_docs._import_parser_object('tests.import_parser_file', 'parser')
        self.assertIsInstance(parser, ArgumentParser)

    def test_generated_parser_import(self):
        parser = generate_docs._import_parser_object('tests.import_parser_file', 'get_parser')
        self.assertIsInstance(parser, ArgumentParser)

    def test_get_help_message_bare(self):
        '''
        Imports bare parser from import_parser_file.py and checks that the help message matches the expected one
        '''
        parser = generate_docs._import_parser_object('tests.import_parser_file', 'parser')
        help_message = generate_docs._get_parser_help_message(parser)
        self.assertEquals(help_message, 'usage: test_prog [-h]\n\noptional arguments:\n  -h, --help  show this help message and exit\n')

    def test_get_help_message_generated(self):
        '''
        Imports parser generated from function from import_parser_file.py and checks that the help message matches the expected one
        '''
        parser = generate_docs._import_parser_object('tests.import_parser_file', 'get_parser')
        help_message = generate_docs._get_parser_help_message(parser)
        self.assertEquals(help_message, 'usage: test_prog [-h]\n\noptional arguments:\n  -h, --help  show this help message and exit\n')

class TestParserWithSubparsers(unittest.TestCase):
    '''
    Test parser with subparser
    '''


if __name__ == '__main__':
    unittest.main()
