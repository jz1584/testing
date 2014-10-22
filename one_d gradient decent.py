from sympy import * 
"""
This function is to approximate the min of a function
by using simple 1-D Gradient Descent 
Just trying to write the math algorithm in  in python
"""
x=Symbol('x')
y=Symbol('y')
def f(x):
    a=x**2+2*x+ 1
    return a 

def g(x):
    return 2*x+2
y=x**2+2*x+ 1



def Grad_decent(init_x,alpha):
    " this function will return approximately the min value of function"
    
    if abs(g(init_x)) >0.0000000001:
        init_x-=alpha*g(init_x)
        print  init_x
        return Grad_decent(init_x,alpha)  
    else:
        print init_x
        a=f(init_x)
        print a
    
Grad_decent(-100,.07)





