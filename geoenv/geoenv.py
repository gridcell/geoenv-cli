#!/usr/bin/env python

import argparse

from .commands import core
from .rich_argparse import RichHelpFormatter


def main():
    core.main_parser.formatter_class = RichHelpFormatter
    args = core.main_parser.parse_args()
    if hasattr(args, "handler"):
        core.setup()
        args.handler(args)
        return
    core.main_parser.print_help()
