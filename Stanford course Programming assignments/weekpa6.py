import numpy
import gmpy2
import math
from collections import defaultdict

from gmpy2 import mpz
gmpy2.get_context().precision=100000


N = 179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
N=179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581
#N=648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877
A=gmpy2.ceil(gmpy2.sqrt(gmpy2.mpz(N)))
B=numpy.powmod(2,20,N)
for i in range(0,B+1):
	#print i
	
#x=mpz(A*A) -N 
	A=mpz(A)
	
	z=mpz(A)*mpz(A)
#print mpz(z)+1
	y=mpz(z)-mpz(N)
	x=gmpy2.sqrt(gmpy2.mpz(y))
	p=mpz(A)-mpz(x)
	q=mpz(A)+mpz(x)
	#print p
	#print mpz(p)
	if mpz(mpz(p)*mpz(q)) == mpz(N):
		break
	
#x=mpz(gmpy2.square(A))-N
y=22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540
k=mpz((mpz(p)-1))*mpz((mpz(q)-1))
e=65537
i=0
m=3
#print mpz(p)
l=mpz(p)-1
#print mpz(l)
t=mpz(q)-1
#print mpz(q)
#print mpz(t)
print mpz(mpz(l)*mpz(t))
print mpz(k)
d=gmpy2.invert(e,mpz(k))
print mpz(mpz(d)*mpz(e))%k

# while m != 0:
# 	m=mpz((mpz(i*mpz(k)+1)))%e
# 	l=mpz((mpz(i*mpz(k)+1)))/e
# 	i=i+1

# m=mpz((mpz(mpz(l*mpz(k))+1)))%e
#k=mpz(k)%N

x=numpy.powmod(y,d,N)

print hex(x)	
#print x
# p=A+x
# q=A-x
# print p
# print q