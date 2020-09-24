# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    coins = [10,5,1]
    for i in coins:
        if(m == 0):
            break
        elif(m % i == 0):
            count += m/i
            m = m % i
        elif(m / i > 0):
            count += int(m/i)
            m = m % i

    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(int(get_change(m)))

