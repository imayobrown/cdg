'''
Functions/methods utilized to generate documentation
'''

import types
import os
from argparse import ArgumentParser
from importlib import import_module

# TODO: Maybe support importing by file path. Currently throws exception
def _import_parser_object(module, parser_name):
    '''
    Given module name and variable/function name within module get parser object.
    If function given, that function should return an argparse object.

    :param module: Fully qualified import path of the module where the function/variable can be found
    :type module: String

    :param parser_name: Name of the function that returns parser object or name of parser object itself (needs to be available in global scope)
    :type parser_name: String

    :rtype class: argparse.ArgumentParser
    '''

    imported_module = import_module(module)
    imported_parser_name = getattr(imported_module, parser_name)

    if isinstance(imported_parser_name, types.FunctionType):
        imported_parser = imported_parser_name()
    else:
        imported_parser = imported_parser_name

    if not isinstance(imported_parser, ArgumentParser):
        raise Exception('Passed parser name does not yeild an instance of ArgumentParser. Type received: %s' % str(imported_parser))

    return imported_parser

def _get_parser_help_message(parser):
    '''
    Get help message from passed parser

    :param parser: Instance of parser to extract help message from
    :type paraser:class: argparse.ArgumentParser

    :rtype String
    '''

    help_message = parser.format_help()
    return help_message

def _extract_subcommands():
    return

def _extract_arguments():
    '''
    Get arguments for command and
    '''
    return

def _extract_

def generate_docs(prog, parser):
    parser = _import_parser_object(prog, parser)
    help_message = _get_parser_help_message(parser)
    print(help_message)
