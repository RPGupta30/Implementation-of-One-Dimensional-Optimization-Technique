#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Implementing Derivative Based Methods'''
'''Bisection Method'''
# Default values function = x**2 - 2*x +1, initial interval of uncertainity = [0,2], epsilon=0.01 
# If we will not enter anything,the program will consider the above default values.
 
import sympy as sym
import math
import numpy as np

def Derivativefunc(x_value=4):
    x = sym.Symbol('x')
    f = x**2-2*x+1
    df = sym.diff(f)
    df = df.doit().subs({x:x_value})
    f = f.doit().subs({x:x_value})    
    return f,df
    
def BisectionMethod(epsilon=0.01):
    
    try:
        x = []
        for i in range(2):
            z = float(input('Enter the first and second value in interval of uncertainity'))
            x.append(z)
    except:
        print('No interval taken, default value is assigned for interval of uncertainity')
        x = [0,3]
    
    a_k=x[0]
    b_k=x[1]
    k = 1
    
    n = np.log((b_k-a_k)/epsilon)/np.log(2)
    n = math.ceil(n)

    p = {'k':k, 'a_k':a_k, 'b_k':b_k }

    
    while k<=n:
        
        c = (p['a_k']+p['b_k'])/2
        f, dfc = Derivativefunc(x_value = c)
        
        
        if dfc==0:
            local_minima = c
            minimum_value,df = Derivativefunc(x_value = c)
            optimized_values = {'local_minima':local_minima, 'minimum_value':minimum_value}
            return optimized_values
        
        elif dfc>0:
            p['b_k'] = c
        
        else:
            p['a_k'] = c
        
        k = k+1
        
    local_minima = c
    minimum_value, dff = Derivativefunc(x_value = c)
    optimized_values = {'local_minima':local_minima, 'minimum_value':minimum_value, 'Number of iterations taken':k-1}      
    return optimized_values

    
local_minima = BisectionMethod(epsilon=0.01)
print('Bisection search method: ',local_minima)


# In[ ]:


'''Newton Method'''

# Default values function = x**2 - 2*x +1, x0 = 1.5
# If we will not enter anything,the program will consider the above default values.


def function(x):
    return x**2-2*x +1 

def derivative(x):
    return 2*x-2 


def NewtonSearch(function, derivative, x0=1.5, epsilon=0.0000001, number_of_max_iterations=100000):

    x1 = 0
    if abs(x0-x1)<= epsilon and abs((x0-x1)/x0)<= epsilon:
        return x0

    k = 1
    while k <= number_of_max_iterations:

        x1 = x0 - (function(x0)/derivative(x0))

        if abs(x0-x1)<= epsilon and abs((x0-x1)/x0)<= epsilon:

            return x1

        x0 = x1
        k = k + 1

        # Stops the method if it hits the number of maximum iterations
        if k > number_of_max_iterations:

            print("ERROR: Exceeded max number of iterations")
            
    return x1 


local_minima = NewtonSearch(function, derivative)
minimum_value = function(local_minima)
optimal_values = {'local_minima':local_minima, 'minimum_value':minimum_value}
print('Bisection search method: ',optimal_values)


# In[ ]:





# In[ ]:




