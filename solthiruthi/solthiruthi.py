## -*- coding: utf-8 -*-
## (C) 2015 Muthiah Annamalai,
##
from __future__ import print_function

import sys
import argparse
import tamil

# from pprint import pprint

PYTHON3 = sys.version[0] == "3"


class Solthiruthi:
    @staticmethod
    def get_CLI_options(do_parse=True, DEBUG=False):
        # Ref: ArgParse doc - https://docs.python.org/dev/library/argparse.html
        # parse and get CLI options. Set do_parse = False for testing
        parser = argparse.ArgumentParser()
        parser.add_argument("-files", default="", nargs="*")
        parser.add_argument(
            "-dialects",
            default=[u"std"],
            nargs="*",
            choices=(u"std", u"ceylon", u"kovai", u"nellai", u"chennai"),
        )
        parser.add_argument(
            "-Dictionary",
            default=[u"std"],
            nargs="*",
            choices=(u"std", u"wikipedia", u"madurai"),
        )
        parser.add_argument(
            "-nalt",
            default=10,
            type=int,
            help=u"number of alternative suggestions for wrong type",
        )
        parser.add_argument(
            "-debug", default=False, help="enable debugging information on screen"
        )
        parser.add_argument(
            "-stdin",
            default=False,
            const=True,
            nargs="?",
            help="read input from the standard input",
        )
        parser.add_argument(
            "-auto",
            default=False,
            const=True,
            nargs="?",
            help="write output as suitable for testing",
        )
        parser.add_argument(
            "-help", default=False, const=True, nargs="?", help="show help and exit"
        )
        if do_parse:
            args = parser.parse_args()
        else:
            args = None

        if DEBUG:
            print(u"files = %s" % u"|".join(args.files))
            print(u"help = %s" % str(args.help))
            print(u"dialects = %s" % u"|".join(args.dialects))
            print(u"Dictionary = %s" % u"|".join(args.Dictionary))
            print(u"nalt = %d" % args.nalt)
            print(u"IN = %s" % str(args.stdin))
        return args, parser


if __name__ == u"__main__":
    args, parser = Solthiruthi.get_CLI_options(DEBUG=False)
    if (len(args.files) == 0 and not args.stdin) or args.help:
        parser.print_help()
        sys.exit(-1)
