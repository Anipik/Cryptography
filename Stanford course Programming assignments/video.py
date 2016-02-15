from Crypto.Hash import SHA256
import sys
import os

digest_size = 1024
filename = sys.argv[1]




f=open(filename,'rb')
sz= os.path.getsize(filename)

sz=sz-955;
f.seek(sz);
chunk = f.read(955);
h = SHA256.new(chunk);



for pos in range(sz-1024, -1024, -digest_size):
	print pos
	f.seek(pos)
	chunk=f.read(digest_size)
	k=chunk+h.digest()
	
	
	h = SHA256.new(k)
	
	
#54cccdb119cd73746e109c90974b20907b5ef787844bd107fe1c45df038a86ea



print h.hexdigest();

f.close()
# print h1
# f=open(filename,'rb')

# i=0;
# while True:
# 	chunk = f.read(digest_size)
# 	i=0;
# 	print i;
# 	if len(chunk) != 1024:
# 		print len(chunk)
# 		break

# 	h = SHA256.new(chunk)
# 	h1= h.hexdigest()
# 	break;
# f.close()
# # print h1
# #size=i*digest_size + len(chunk)

# print h1