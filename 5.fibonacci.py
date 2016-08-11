import sys

def fibonacci(n):
    if n<=0: return [1]
    elif n==1: return [1,1]
    else: 
      fib = fibonacci(n-1)
      fib += [fib[-1]+fib[-2]]
      return fib
    
print fibonacci(int(sys.argv[1]))