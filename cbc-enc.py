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

#reading in the key
in = open(keyfile,"rb")
fKey = in.read().strip()
in.close()

#block cipher 
Fk = AES.new(bytearray.fromhex(fKey),AES.MODE_ECB)

#writing out IV to encrypted file
out = open(outputfile,"wb+")
out.write(iv)

pad_neeeded = False;
bool = True

in = open(inputfile,"rb")
while True:
	m_block = bytearray(in.read(16))
	if len(m_block) != 16:
		pad_needed = True;
		pads = 16 - len(m_block)
	if bool:
		for i in range(0,16):
			xor_block = iv[i] ^ m_block[i]
		c_block = Fk.encrypt(bytearray(xor_block))
		out.write(c_block)
		bool = False;
		prev_m_iv = bytearray(c_block)
	else:
		for i in range(0,16):
			xor_block = prev_m_iv[i] ^ m_block[i]
		c_block = Fk.encrypt(bytearray(xor_block))
		out.write(c_block)
		prev_m_iv = bytearray(c_block)

if pad_needed:
	m_block = bytearray(pads)
	for i in range(0,len(pads)):
		xor_block = m_block[i] ^ prev_m_iv[i]
	c_block = Fk.encrypt(bytearray(xor_block))
	out.write(c_block)

out.close()
