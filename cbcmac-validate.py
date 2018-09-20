#!/usr/bin/env python3
#validate a tag for a given file

from Crypto.Cipher import AES
from Crypto import Random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k','--keyfile',required = True)
parser.add_argument('-m','--messagefile',required = True)
parser.add_argument('-t','--tagfile',required = True)
args = parser.parse_args()

key = args.keyfile
message = args.messagefile
tag_in = args.tagfile

if key is None or message is None or tag_in is None:
        print("Incorrect usage\n")
        exit(1)
