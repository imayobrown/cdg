'''
Functions/methods utilized to generate documentation
'''

import types
import os
import argparse
from argparse import ArgumentParser, _SubParsersAction
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

def _extract_arguments(parser):
    print parser

def _extract_subcommands(parser):
    '''
    Extract subcommands if there are any.
    Returns a dictionary of subcommands mapped to parser object

    :param parser: Parser extracted from imported module
    :type parser:class: argparse.ArgumentParser

    :rtype class: Dict
    '''

    for action in parser._actions:
        if isinstance(action, _SubParsersAction):
            print 'Subactions: '
            print action._get_subactions()
            print
            for subparser_name, subparser in action.choices.iteritems():
                print subparser_name, subparser
                print subparser._actions
                print subparser.format_help()


def _extract_usage(parser):
    '''
    Extract usage information from parser

    :param parser: Parser to extract usage from
    :type parser:class: argparse.ArgumentParser

    :rtype String
    '''
    return

def _extract_description(parser):
    '''
    Extract description from parser/subcommand
    '''
    return

def _extract_arguments(parser):
    '''
    Extract arguments and their descriptions from the parser/subcommand
    '''
    return

def generate_docs(prog, parser):
    parser = _import_parser_object(prog, parser)
    _extract_subcommands(parser)
    # print(parser._actions[-1].choices['a'])
