# Uses python3
import sys

def gcd_naive(a, b):
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

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
