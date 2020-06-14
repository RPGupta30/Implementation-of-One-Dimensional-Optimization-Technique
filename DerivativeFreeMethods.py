#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Implementing Derivative Free Methods'''
'''Dichotomous search Algorithm'''
# Default values epsilon=0.01, function = -2x^2 - 2x, initial interval of uncertainity = [-3,6] 
# and final length of uncertainity interval(l=0.2)
# If we will not enter anything,the program will consider the above default values.

def DichotomousSearch(k=0, epsilon=0.01, l=0.2):
    
    try:
        x = []
        for i in range(2):
            z = float(input('Enter the first and second value in interval of uncertainity'))
            x.append(z)
    except:
        print('No interval taken, default value is assigned for interval of uncertainity i.e. x ')
        x = [-3,6]
    
    try:
        epsilon = float(input('Enter the value of epsilon'))
    except:
        print('No interval taken, default value is assigned for epsilon')
        pass
    
    
    def func(y):
        f = -(y**2) - 2*y
        return f
    
    a_k=x[0]
    b_k=x[1]
    
    p = {'k':k, 'epsilon':epsilon, 'l':l, 'a_k':a_k, 'b_k':b_k }

    while (p['b_k'] - p['a_k'])> p['l']:
        
        lambd_k = (p['b_k'] + p['a_k'])*0.5 - p['epsilon']
        mu_k = (p['b_k'] + p['a_k'])*0.5 + p['epsilon']
        
        f1 = func(lambd_k)
        f2 = func(mu_k)

        if f1>=f2:
            p['b_k'] = mu_k
        else:
            p['a_k'] = lambd_k
                   
        k = k +1
      
    local_minima = (p['a_k'] + p['b_k'])/2
    minimum_value = func(local_minima)
    optimized_values = {'local_minima':local_minima, 'minimum_value':minimum_value, 'Number of iterations taken':k}

    return optimized_values
            
local_minima = DichotomousSearch()
print('Dichotomous Search method: ',local_minima)


# In[ ]:


'''Implementing Derivative Free Methods'''
'''Fibbonacci Search Algorithm'''
# Default values epsilon=0.01, function = x^2 + 54/x, initial interval of uncertainity = [0,5] 
# and final length of uncertainity interval(L=0.2)  

# Function for nth Fibonacci number where fn = [1,1,2,3,5,8,13,....] i.e. zeroth fibonacci number taken is 1, 
# 1st fibonacci number = 1, 2nd fibonacci number = 2, and so on. 
# If we will not enter anything,the program will consider the above default values.

def FibonacciNumber(n): 
    if n<0:
        print("Incorrect input")    
    elif n==0:
        return 1
    elif n==1: 
        return 1 
    elif n==2:
        return 2
    else: 
        return FibonacciNumber(n-1)+FibonacciNumber(n-2)
    
def FibonacciSearch(k=2, n=3, l=0.2):
    try:
        x = []
        for i in range(2):
            z = float(input('Enter the first and second value in interval of uncertainity'))
            x.append(z)
    except:
        print('No interval taken, default value is assigned for interval of uncertainity')
        x = [0,5]
    
    
    def func(y):
        f = y**2 + 54/y
        return f
    
    a_k=x[0]
    b_k=x[1]
    L = x[1] - x[0]
    
    
    p = {'k':k, 'a_k':a_k, 'b_k':b_k }

    while (k-1)!=n:
        
        num = n-k +1
        den = n+1
        
        num = FibonacciNumber(num)
        den = FibonacciNumber(den)
    
        L_star = (num/den)*L
        
        lambd_k = p['a_k'] + L_star 
        mu_k = p['b_k'] - L_star
        
        f1 = func(lambd_k)
        f2 = func(mu_k)

        if f1>=f2:
            p['a_k'] = lambd_k
        else:
            p['b_k'] = mu_k
                   
        k = k + 1
  
    local_minima = []
    local_minima.append(p['a_k'])
    local_minima.append(p['b_k'])
    optimized_values = {'local_minima lies between':local_minima, 'Number of iterations taken':k-2}
    
    return optimized_values
            
local_minima = FibonacciSearch(k=2, n=3, l=0.2)
print('Fibonacci Search method: ',local_minima)


# In[ ]:





# In[ ]:




