#!/usr/bin/env python3
import os
import sys
import glob
import string
import random

letters = string.ascii_letters
with open('key.txt', 'r') as keyFile:
	for line in keyFile:
		cipherKey = line;
	
def decryptMessage(cipher, key, letters):
    keyMap = dict(zip(key, letters))
    return ''.join(keyMap.get(c, c) for c in cipher)

# Splitting .enc files into variables
encFiles = glob.glob("*.enc")

# Opening each .enc files in folder
for dataFile in encFiles:
	extension = os.path.splitext(dataFile)[0]
	fileExtension = '.txt'
	newFile = extension + fileExtension
	# Opening in readonly mode
	with open(dataFile, 'r') as encfile, open(newFile, 'w') as newfile:
		for line in encfile:
			# Encrypting the file using substitution cipher
			plain_txt = decryptMessage(line, cipherKey, letters)
			newfile.write(plain_txt)
			
			try:
				# Deleting .txt file
				os.unlink(encfile.name)
			except OSError:
				pass 

		# End of file
		if 'str' in line:
			break
			
print("Your files have been decrypted")
