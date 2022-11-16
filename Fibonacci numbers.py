# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 02:43:23 2022

@author: Jon

Fibonacci numbers is a sequence of numbers starting with 1, 1,
 and the next number in the sequence is the sum of the previous two.
   So the sequence looks like 1,2,2,3,5,8,...

F[n] = F[n-1} + F[N-2]

1. Write a function 'make_Fibonacci' that returns the first N Fibonacci numbers.
  Put the function in a module named fibonacci  (that's just a file named fibonacci.py).
 In the module, put a test block, so that if the file were run as a program,
 the first 20 Fibonacci numbers print to the screen. 

2.  Johannes Kepler (yes, that Johannes Kepler)
 claimed that the ratio of consecutive Fibonacci numbers converges to the
 'golden ratio Links to an external site..'   

Golden Ratio:      F[N+1]/F[N] -> (read, 'gets close to  as N increases' )  (1+sqrt(5))/2

Extend your module by defining a function 'converging_ratios' that takes an
 array or list F that contains Fibonacci numbers as input and
 tests to see if Kepler's claim seems correct.    
 Put a call to the function in the test block and run the function.

3.  'Rate of convergence' is a mathematical concept that shows up in math and engineering.
   if e[N] is the difference between the ratio you compute 
   and the golden ratio F[N+1]/F[N} - golden ratio =  e[N} = C*e[N}**q, C is some constant,
 then q is the rate of convergence   The computation for q is

q = np.log(e[N+1]/e{N]) / np.log(e[N]/e[N-1])

Extend your module by including a function 'computre_rates' that  takes a sequence F,
 and computes the corresponding values for q and prints the last 5 values.
 You do not need any value for C,    The convergence rates should get close to 1 and N gets large.
"""
import numpy as np

def fibonacci(n):
    if n < 3:
        print(f"n not large enough {int(n)}")
        return(None)
    F = [1,1]
    for i  in range(2,n):
        F.append(F[i-1]+F[i-2])
        
    return F

def converging_ratios(n):
    
    if n < 3:
        print(f"n not large enough {int(n)}")
        return(None)
    F = fibonacci(n)
    
    for i  in range(2,n):
        F.append(F[i+1]/F[i])
        
    return F

def computre_rates(N):
    if N < 3:
        print(f"n not large enough {int(N)}")
        return(None)
    F = fibonacci(N)
    
    for i  in range(2,N):
        F.append(np.log((N+1)/(N)) / np.log((N)/(N-1)))
        
        return F

if __name__ == '__main__':
    print('===fibonacci===')

    print(f"{fibonacci(10)}")
    
    print('===Golden Ratio===')

    print((1+np.sqrt(5))/2)
    
    print('===converging_ratios===')

    print(f"{converging_ratios(10)}")
    
    print('===computre_rates===')
    
    print(f"{computre_rates(10)}")
    
    print('++++++++++++++++++++++++++')

    print(f"{computre_rates(100)}")

    