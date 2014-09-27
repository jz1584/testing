from ranwalk import *
import matplotlib.pyplot as plt

#plotting 2 lines 
def plot(trails,size):
	data=[]
	for i in range(trails):
    		data.append(rwalk(size))


	for i in data:
		plt.plot(i)
	plt.ylabel("walk direction")
	plt.xlabel("walking steps")
	plt.show()


plot(10,1000)

