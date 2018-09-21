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

#Get iv, this will be our first xor value
xor_value = bytearray(Random.get_random_bytes(16))

#reading in the key
inp = open(key,"r")
fKey = inp.read().strip()
inp.close()

#block cipher in AES ECB Mode
Fk = AES.new(bytearray.fromhex(fKey), AES.MODE_ECB)

#writing out IV to encrypted file
out = open(output,"wb+")
out.write(xor_value)

#This boolean is used to determine if we need to add a whole block of padding since last bit must always equal padding size
padding_added = False

inM = open(input,"rb")
while True:
	m_block = bytearray(inM.read(16))

	if len(m_block) != 0:
		if len(m_block) != 16:
			pad_size = 16 - len(m_block)
			#Append the padding size to the end of the last block
			for i in range(0, pad_size):
				m_block += bytes([pad_size])

			xor_block = [None] * 16

			# XOR the xor_value with the m_block
			for i in range(0, 16):
				xor_block[i] = xor_value[i] ^ m_block[i]

			# Get the encryped xor_block
			encryped_block = Fk.encrypt(bytearray(xor_block))

			# write
			out.write(encryped_block)

			padding_added = True;

		else:
			xor_block = [None] * 16

			#XOR the xor_value with the m_block
			for i in range(0, 16):
				xor_block[i] = xor_value[i] ^ m_block[i]

			# Get the encryped xor_block
			encryped_block = Fk.encrypt(bytearray(xor_block))

			#Set new xor_value for later xoring
			xor_value = encryped_block

			#write
			out.write(encryped_block)
	else:
		break

#Add a whole 16 byte block of padding
if not padding_added:
	m_block = bytearray()

	for i in range(0, 16):
		m_block += bytes([16])

	xor_block = [None] * 16

	# XOR the xor_value with the m_block
	for i in range(0, 16):
		xor_block[i] = xor_value[i] ^ m_block[i]

	# Get the encryped xor_block
	encryped_block = Fk.encrypt(bytearray(xor_block))

	# write
	out.write(encryped_block)

	padding_added = True

out.close()
