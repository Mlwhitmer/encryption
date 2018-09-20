#!/usr/bin/env python3
# decrypting files using cbc mode

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

in = open(keyfile, "rb")
fKey = in.read().strip()
in.close()

Fk = AES.new(bytearray.fromhex(fKey), AES.MODE_ECB)

in = open(inputfile,"rb")
iv = in.read(16)

out = open(outputfile,"wb+")

while True:
	c_block = bytearray(in.read(16))
	fk_out = Fk.decrypt(c_block)
	m_block = [None] * len(c_block)
	for i in range(0,16):
		m_block[i] = fk_out[i] ^ iv[i]
	out.write(m_block)
	iv = c_block

out.close()
in.close()
