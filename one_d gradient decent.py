import matplotlib.pyplot as plt
import sys
import numpy as np

"""
This function is to approximate the min of a function
by using simple 1-D Gradient Descent 
Just trying to write the math algorithm in  in python
"""
def f(x):
    a=x**4+2*x+ 1
    return a 

def derivative_f(x):
    return 4*x**3+2
x_value=[]

def Grad_decent(init_x,step):
    " this function will return approximately the min value of function"
    
    if abs(derivative_f(init_x)) >0.00001:
        init_x-=step*derivative_f(init_x)
        print  init_x
        x_value.append(init_x)
        return Grad_decent(init_x,step)  
    else:
        #x_round=round(init_x,2)
        #x_value.append(x_round)
        a=f(init_x)
        print "the Mini of f(x) is %d" % a
    
Grad_decent(6,0.01)

"""
plotting result
"""


plt.plot(x_value)
plt.ylabel("x_value")
plt.xlabel("steps")

plt.show()
"""
x_list=[i for i in np.arange(-5,5,0.01)]
print x_list 
y_list=[]
for i in x_list:
    y_list.append(f(i))

plt.plot(x_list,y_list)
plt.show()
"""

