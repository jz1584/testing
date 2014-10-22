"""Author: Jianming Zhou
    Date: 10/21/2014
"""
import matplotlib.pyplot as plt
import sys
import numpy as np

"""
This function is to approximate the min of a function
by using simple 1-D Gradient Descent method
first time to write the math algorithm in python :)
Nice combination of mathematics & programming
"""
def f(x):
    a=x**4+2*x+ 1
    return a 
"""
#show the graph of original function 
x_list=[i for i in np.arange(-5,5,0.01)]
y_list=[]
for i in x_list:
    y_list.append(f(i))
plt.plot(x_list,y_list)
plt.show()
"""

def derivative_f(x):#differentiate the original function
    return 4*x**3+2

x_value=[]#make a list of x value
y_value=[]#create a list of y value


"""
The method of choosing alpha (step-size):
For sufficiently small alpha, the function should decrease on every iteration
but if alpha is too small, gradient descent can be slow to converge
we can always try alpha value 0.001, 0.01,0.1,1
"""
def Grad_decent(init_x,alpha):
    " this function will return approximately the min value of function"
    
    if abs(derivative_f(init_x)) >0.00001:#the derivative of fuction at min point the should be near zero
        init_x-=alpha*derivative_f(init_x)
        print  init_x
        x_value.append(init_x) # append all the x stepped values in to x_value
        y_value.append(f(init_x))
        return Grad_decent(init_x,alpha)  
    else:
        #x_round=round(init_x,2)
        #x_value.append(x_round)
        a=f(init_x) #return the y value of the final step
        print "the Mini of f(x) is %d" % a
    
Grad_decent(-10,0.003) #testing the Grad_decent method, & it works

"""
plotting testing result to check if function converge:
visualize the trend of y_value upon the 
movement of x_value 
"""
plt.plot(y_value)
plt.ylabel("y_value")
plt.xlabel("steps")

plt.show()




