from sympy import * 
"""
This function is to approximate the min of a function
by using simple 1-D Gradient Descent 
Just trying to write the math algorithm in  in python
"""
x=Symbol('x')
y=Symbol('y')
y=x**4 + 1



def Grad_decent(init_x, f, alpha):
    " this function will return approximately the min value of function"
    derivative=diff(f,x)
    #print derivative.subs(x,init_x)
    
    if derivative.subs(x,init_x) >0.01:
        init_x-=alpha*derivative.subs(x,init_x)
        print  init_x
        return Grad_decent(init_x,f,alpha)  
    else:
        return f.subs(x,init_x)
    
print Grad_decent(4,y,0.01)





