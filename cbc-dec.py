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

#reading in the key
inp = open(key,"r")
fKey = inp.read().strip()
inp.close()

#block cipher in AES ECB Mode
Fk = AES.new(bytearray.fromhex(fKey), AES.MODE_ECB)

message_blocks = []

inM = open(input,"rb")

#Get iv from input, this will be our first xor value
xor_value = bytearray(inM.read(16))

while True:
	m_block = bytearray(inM.read(16))

	if len(m_block) != 0:

		# Get the decrypted message block
		decrypted_block = Fk.decrypt(m_block)

		message_block = [None] * 16

		#XOR to unXOR the message
		for i in range(0, 16):
			message_block[i] = xor_value[i] ^ decrypted_block[i]

		xor_value = m_block

		#Append the message block to the large list of message blocks
		message_blocks.append(bytearray(message_block))
	else:
		break

out = open(output, "wb+")

count = 0
final_message_block = bytearray()

#Write decrypted message to output file
for m in message_blocks:
	if count == (len(message_blocks) - 1):
		final_message_block_string = m.decode("utf-8")[:-message_blocks[len(message_blocks) - 1][len(message_blocks[len(message_blocks) - 1]) - 1]]

		out.write(bytearray(final_message_block_string, 'utf8'))

	else:
		out.write(m)
		count += 1

out.close()
