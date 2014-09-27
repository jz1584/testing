import random

for i in range(10):
	a=random.randint(0,1)
	if a==1:
		step=1

	elif a==0:
		step=-1
		
	else:	
		print " error"
	print i, a, step


