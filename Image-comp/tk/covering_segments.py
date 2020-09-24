# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        found = 0
        for i in range(0,len(points),2):
            if(s.start <= points[i]):
                points.insert(i,s.start)
                points.insert(i+1,s.end)
                found = 1
                break
        if(found == 0):
            points.append(s.start)
            points.append(s.end)

    groups = [points[0:2]]
    res = [groups[0][1]]
    for i in range(2,len(points),2):
        found = 0
        for j in range(len(groups)):
            if((points[i] <= groups[j][1] and points[i] >= groups[j][0]) or (points[i+1]>=groups[j][0] and points[i+1]<=groups[j][1] )):
                groups[j][0] = max(points[i],groups[j][0])
                groups[j][1] = min(points[i+1],groups[j][1])
                found = 1
                res[j] = groups[j][1]
                break
        if(found == 0):
            groups.append(points[i:i+2])
            res.append(points[i+1])

    return res
    

if __name__ == '__main__':
    input = sys.stdin.read()
    #inp = input()
    #n, *data = map(int, inp.split())
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
