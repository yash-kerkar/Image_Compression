# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    p = pisanoPeriod(m)
    rem = n%p
    return fibonacci(rem) % m

def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current = current, (previous + current) % m 
          
        # A Pisano Period starts with 01 
        if (previous == 0 and current == 1): 
            return i + 1

def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0,1]
        for i in range(2,n+1):
            fib.append(fib[i-1] + fib[i-2])         
        return fib[n]   

#if __name__ == '__main__':
#   input = sys.stdin.read();
inp = input()
n, m = map(int, inp.split())
print(get_fibonacci_huge_naive(n, m))
