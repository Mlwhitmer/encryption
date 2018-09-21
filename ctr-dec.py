from Crypto.Cipher import AES
from Crypto import Random
import argparse
import threading


def encrypt(block_number, iv_counter, msg_block):
	ivFk = Fk.encrypt(iv_counter)
	
	xor_block = [None] * len(msg_block)
	
	for i in range(0, len(msg_block)):
		xor_block[i] = bytearray(ivFk)[i] ^ msg_block[i]
	
	decryption_blocks[block_number] = bytearray(xor_block)
	
	return


cmd = argparse.ArgumentParser()

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

#reading in the key
inK = open(key, "r")
fKey = inK.read().strip()
inK.close()

#block cipher
Fk = AES.new(bytearray.fromhex(fKey), AES.MODE_ECB)

#Get IV to decrypted file
inM = open(input, "rb")
#First 16 bytes will always be our iv
iv = bytearray(inM.read(16))

#convert iv to int so we can increment
iv_count = int.from_bytes(iv, byteorder='big')
#initial iv count
iv_count += 1

iv_counters = []
blocks = []

#Read in message and divide into 16 byte chunks if possible else that is fine this is ctr
while True:
	m_block = bytearray(inM.read(16))

	if len(m_block) != 0:
		blocks.append(m_block)
		iv_counters.append(iv_count)
		iv_count += 1
	else:
		break

decryption_blocks = [None] * len(iv_counters)


#thread encryption and run in parallel
threads = []
for i in range(len(iv_counters)):
	t = threading.Thread(target=encrypt(i, iv, blocks[i]))
	threads.append(t)
	t.start()

#Open write file stream
out = open(output, "wb+")

for i in decryption_blocks:
	out.write(i)

out.close()
