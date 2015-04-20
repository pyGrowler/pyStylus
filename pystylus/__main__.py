#
# pystylus/__main__.py
#

import sys
import pystylus
from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser("pystylus")
    parser.add_argument("filenames",
                        nargs='*',
                        type=str,
                        help="Filename(s) which to convert to css"
                        )
    parser.add_argument("--",
                        dest='read_from_stdin',
                        action='store_true',
                        help="Read from STDIN instead of file."
                        )
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)

    if args.filenames:
        print(args.filenames)
    elif args.read_from_stdin:
        print("Reading from stdin...")


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
