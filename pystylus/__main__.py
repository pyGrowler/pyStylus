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
    parser.add_argument("-P", "--pretty",
                        action='store_true',
                        help="Print the output css in a pretty way."
                        )
    return parser.parse_args(args)


def main(args):
    args = parse_args(args)

    if args.filenames:
        with open(args.filenames) as file:
            input = file.read()
    else:
        input = sys.stdin.read()

    node = pystylus.StylusParser().parse(input)[0]
    print(node)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
