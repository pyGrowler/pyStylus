#
# pystylus/__main__.py
#

import sys
import pystylus
from argparse import ArgumentParser


def parse_args(args):
    parser = ArgumentParser("pystylus")
    return parser.parse_args(args)

def main(args):
    args = parse_args(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
