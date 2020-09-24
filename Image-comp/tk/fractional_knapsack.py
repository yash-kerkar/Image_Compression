# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    # write your code here
    res = 0
    ratio = [i / j for i, j in zip(values, weights)]
    for _ in range(len(values)):
        if(capacity == 0):
            break
        else:
            ix = ratio.index(max(ratio))
            if(capacity - weights[ix] >= 0):
                res += weights[ix] * ratio[ix] 
                capacity -= weights[ix]
            else:
                res += capacity*ratio[ix]
                capacity = 0
            ratio.pop(ix)
            weights.pop(ix)


    return res


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
