import argparse
import logging
from datetime import datetime


def create_parser():
    """Creates parser. Takes arguments:
    source, version, json, limit, verbose"""
    parser = argparse.ArgumentParser(description="RSS news parser")
    parser.add_argument("source", nargs='?', default=None, type=str,
                        help="RSS URL")
    parser.add_argument("--version", action='version',
                        version='Version 1.0', help="Print version info")
    parser.add_argument("--json", action="store_true",
                        help="Print result as JSON in stdout")
    parser.add_argument("--limit", type=int, default=None,
                        help="Limit news topics if this parameter provided")
    parser.add_argument("-v", "--verbose", action="store_const",
                        dest="loglevel", const=logging.INFO,
                        help="Outputs verbose status messages")
    return parser


args = create_parser().parse_args()
logging.basicConfig(level=args.loglevel)
logger = logging.getLogger()
