#!/usr/bin/env python3
# encrypting files using cbc mode 

from Crypto.Cipher import AES
from Crypto import Random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k','--keyfile',required = True)
parser.add_argument('-i','--inputfile',required = True)
parser.add_argument('-o','--outputfile',required = True)
args = parser.parse_args()


input = args.inputfile
key = args.keyfile
output = args.outputfile

if input is None or key is None or output is None:
	print("Incorrect usage\n")
	exit(1)

iv = bytearray(Random.get_random_bytes(16))
print(iv)
in = open(keyfile,"rb")
fKey = in.read().strip()
in.close()

out = open(outputfile,"wb+")
out.write(iv)



