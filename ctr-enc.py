#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto import Random
import sys, argparse
import struct

cmd = argparse.ArgumentParser(
    )

cmd.add_argument("-k", "--keyfile",  help="specifies a file storing a valid AES key as a hex encoded string", type=str, required=True, metavar="IN")
cmd.add_argument("-i", "--inputfile", help="specifies the path of the file that is being operated on", type=str, required=True, metavar="IN")
cmd.add_argument("-o", "--outputfile",  help=", specifies the path of the file where the resulting output is stored", type=str, required=True, metavar="IN")
args = cmd.parse_args()

input = args.inputfile
key = args.keyfile
output = args.outputfile

if input is None or key is None or output is None:
	print("Incorrect usage\n")
	exit(1)

iv = Random.get_random_bytes(16)

#reading in the key
inK = open(key, "r")
fKey = inK.read().strip()
inK.close()

with open(input, 'r') as inputFile:
	msg = inputFile.read()

#block cipher
Fk = AES.new(str(bytearray.fromhex(fKey)), AES.MODE_ECB)

#writing out IV to encrypted file
out = open(output, "wb+")
out.write(iv)

int.from_bytes(iv, byteorder='big')

#TODO need to get iv counters and xor try for encryption locally first