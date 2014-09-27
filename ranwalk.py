import random
import matplotlib.pyplot as plt
position=0
walk=[position]
steps=1000

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



plt.plot(walk)
plt.ylabel("walk direction")
plt.xlabel("walking steps")
plt.show()



