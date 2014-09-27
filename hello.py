import random
position=0
walk=[position]
steps=100

for i in range(steps):
	a=random.randint(0,1)
	if a==1:
		step=1

	elif a==0:
		step=-1
		
	else:	
		print " error"
	position+=step
	walk.append(position)

print walk


