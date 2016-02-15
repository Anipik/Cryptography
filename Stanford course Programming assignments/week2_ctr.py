from Crypto.Cipher import AES
import os
import binascii

key="36f18357be4dbd77f050515c73fcf9f2"
iv="770b80259ec33beb2561358a9f2dc618"

# iv="69dda8455c7dd4254bf353b773304eee"

# print l=int(key,16)
# print secret=int(iv,16)
# key = bin
# secret=bin((int)key)
# key=bin((int)secret) 
secret= binascii.unhexlify(iv)
key =binascii.unhexlify(key)

# os.urandom(32)
# secret1 = os.urandom(32)
# print key
# print binascii.hexlify(secret1)
# print secret1
# cipher_block=binascii.unhexlify("5f51eeca32eabedd9afa9329")
cipher = AES.new(key)
last_block=cipher.encrypt(secret)
print str(binascii.hexlify(last_block))
#c=0x333e8da11289d7adf29fe107#8e8370b4
# m=0x5f51eeca32eabedd9afa9329#00000000
# s=c^m
c=0x2e456cb1bd3a681f0811f4a2207095b4
m=0x0e311bde9d4e01726d3184c344510000
s=c^m
print hex(s)
#770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451
#crypto = AES.new(key, AES.MODE_CTR, counter=lambda: secret)
#encrypted = crypto.encrypt("aaaaaaaaaaaaaaaa")
# binascii.hexlify(encrypted)
#encrypted=binascii.unhexlify("e46218c0a53cbeca695ae45faa8952aa")
#encrypted=binascii.unhexlify("5f51eeca32eabedd9afa9329")

#print crypto.decrypt(encrypted)

# 69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329