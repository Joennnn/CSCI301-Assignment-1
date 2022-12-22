#!/usr/bin/env python3
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

# Decrypting key.bin
file_in = open('key.bin', 'rb')
private_key = RSA.import_key(open('ransomprvkey.pem').read())
enc_data = file_in.read(private_key.size_in_bytes())
cipher_rsa = PKCS1_OAEP.new(private_key)
# Obtaining key from encryption
data = cipher_rsa.decrypt(enc_data)
key = data.decode('utf-8')
file_in.close()

# Storing decrypted key (key.bin) in key.txt
with open('key.txt', 'w') as newfile:
	newfile.write(key)
	
print("You have successfully obtained the key to decrypt your files")
