# python3
import sys


def compute_min_refills(d, m, stops):
    # write your code here
    i = 0 
    res = 0
    stops.append(d)
    stops.insert(0,0)
    n = len(stops)
    while(d > 0):
        j = i + 1
        found = 0
        while((stops[j] - stops[i])<=m):
            found = 1
            if((j + 1) == n):
                j += 1
                break
            j += 1
        if(found == 0):
            res = 0
            break
        else:
            j -= 1
            d -= stops[j] - stops[i]
            i = j
            res += 1

    return res - 1

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
