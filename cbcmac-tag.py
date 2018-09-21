#!/usr/bin/env python3
#building a tag for a given file

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
tag_out = args.tagfile
	
if key is None or message is None or tag_out is None:
	print("Incorrect usage\n")
	exit(1)

#reading in the key 
in_stream = open(key, "r")
fKey = in_stream.read().strip()
in_stream.close()

#block cipher in AES ECB mode
Fk = AES.new(bytes.fromhex(fKey),AES.MODE_ECB)

#get in the message size 
in_S = open(message, "rb")
message_file = in_S.read().strip()
message_size = len(message_file)
in_S.close()

encrypted_block = Fk.encrypt(message_size.to_bytes(16,byteorder = 'big'))

#reading in the file to generate a tag
in_file = open(message,"rb")
while True:
	message_in = bytearray(in_file.read(16))
	
	if(len(message_in)) != 0:
		#checking if padding is needed before encrypting
		if len(message_in) != 16:
			padding = 16 - len(message_in)
			for i in range(0,padding):
				message_in += bytes([padding])
		
		#XORing the message block and previous encrypted block
		xor_block = [None] * 16
		for i in range(0,16):
			xor_block[i] = message_in[i] ^ encrypted_block[i]
		
		encrypted_block = Fk.encrypt(bytearray(xor_block))		
	else:
		break

in_file.close()

#writing the tag to tag file
out_stream = open(tag_out, "wb+")
out_stream.write(encrypted_block)
out_stream.close()

