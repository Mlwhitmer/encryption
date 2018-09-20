from Crypto.Cipher import AES
from Crypto import Random
import sys, argparse
import binascii

# key = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff';
# cipher = AES.new(key, AES.MODE_ECB);
# msg = cipher.encrypt();
# print(msg);

def ctr_d(keyFile, input, output):

	inf = open(keyFile, "r")
	fKey = inf.read().strip()

	with open(input, 'rb') as inputFile:
		msg = inputFile.read()


	result = bytearray.fromhex(fKey)

	# print(result)

	cipher = AES.new(str(result), AES.MODE_ECB)

	counter = 0


##############################################################################
cmd = argparse.ArgumentParser(
    )

cmd.add_argument("-k", "--key",  help="specifies a file storing a valid AES key as a hex encoded string", type=str, required=True, metavar="IN")
cmd.add_argument("-i", "--input", help="specifies the path of the file that is being operated on", type=str, required=True, metavar="IN")
cmd.add_argument("-o", "--output",  help=", specifies the path of the file where the resulting output is stored", type=str, required=True, metavar="IN")
args = cmd.parse_args()

iv = Random.get_random_bytes(16)
# print(iv)
# print " ".join(hex(ord(n)) for n in iv)

ctr_d(args.key, args.input, args.output)


