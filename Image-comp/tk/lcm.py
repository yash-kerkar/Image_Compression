# Uses python3
import sys

def lcm_naive(a, b):
    return (a*b)/gcd(a,b)

def gcd(a, b):
    if(a > b):
        if(a % b == 0):
            return b
    else:
        if(b % a == 0):
            return a
        else:
            a ,b = b, a
    while(True):
        if(a == 0):
            return b
        elif(b == 0):
            return a
        else:
            a,b = b,a % b

#if __name__ == '__main__':
 #   input = sys.stdin.read()
inp = input()
a, b = map(int, inp.split())
print(int(lcm_naive(a, b)))

