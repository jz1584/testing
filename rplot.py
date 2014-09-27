import random
import matplotlib.pyplot as plt

#plotting 2 lines 
def plot(walk1,walk2):
	plt.plot(walk1)
	plt.plot(walk2)
       
	plt.ylabel("walk direction")
	plt.xlabel("walking steps")
	plt.show()



