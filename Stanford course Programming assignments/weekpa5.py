import numpy
import gmpy2
from collections import defaultdict


p=13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171


g=11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568

h=3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333

B=numpy.powmod(2,20,p)

# hash_table=[None] * (B+1)
hash_table=defaultdict(int)
i=0;

for i in range(0,B+1):
	print i
	l= numpy.powmod(g,i,p)
	l=gmpy2.invert(l,p)
	z=(h*l)%p
	# print l;
	hash_table[z]=i;
	# print z
	# print hash_table[i] 

m=numpy.powmod(g,B,p)

# for i in range(0,B+1):
# 	print i
#  	l= numpy.powmod(m,i,p)
#  	if l in hash_table:
#    		x0=i
#     	x1=hash_table[l]
#     	break
    
#      else:
#     	continue

for i in range(0,B+1):
	print i;
	l=numpy.powmod(m,i,p)
	if l in hash_table:
		x0=i
		x1 = hash_table[l]
		break
	else:
		continue


x= (x0*B + x1)%p

print x