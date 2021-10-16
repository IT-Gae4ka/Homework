import argparse
import logging

parser = argparse.ArgumentParser(description="RSS news parser by Alesia Tsepliakova")
parser.add_argument("source", type=str, help="RSS URL")
parser.add_argument("--version", action='version', version='Version 1.0', help = "Print version info")
parser.add_argument("--json", action = "store_true", help = "Print result as JSON in stdout")
parser.add_argument("--limit", type=int, default = -1, help= "Limit news topics if this parameter provided")
parser.add_argument('-v', '--verbose', action="store_const", dest="loglevel", const=logging.INFO, help="Outputs verbose status messages")

args = parser.parse_args()    
logging.basicConfig(level=args.loglevel)

logger = logging.getLogger()


