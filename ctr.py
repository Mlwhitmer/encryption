from Crypto.Cipher import AES
from Crypto import Random
import sys, argparse


# key = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff';
# cipher = AES.new(key, AES.MODE_ECB);
# msg = cipher.encrypt();
# print(msg);

cmd = argparse.ArgumentParser(
    )

cmd.add_argument("-k", "--key",  help="specifies a file storing a valid AES key as a hex encoded string", type=str, required=True, metavar="IN")
cmd.add_argument("-i", "--input", help="specifies the path of the file that is being operated on", type=str, required=True, metavar="IN")
cmd.add_argument("-o", "--output",  help=", specifies the path of the file where the resulting output is stored", type=str, required=True, metavar="IN")
args = cmd.parse_args()

iv = Random.get_random_bytes(16)



def ctr_e(key, iv, input, output): 

	with open(input, 'r') as inputFile:
		msg = inputfile.read()
