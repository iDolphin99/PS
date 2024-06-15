'''
강의실 배정 
첫째 줄: N(1 ≤ N ≤ 200,000)
이후 N개 줄: Si, Ti(0 ≤ Si < Ti ≤ 10^9)
'''
from sys import stdin 
import heapq
input = stdin.readline
start, end = [], []
for _ in range(int(input())):
    st, en = map(int, input().rsplit())
    if len(end) == 0:
        heapq.heappush(end, en)
        heapq.heappush(start, st)
    else:
        if end[0] <= st:
            heapq.heappop(end)
            heapq.heappush(end, en)
        elif start[0] >= en:
            heapq.heappop(start)
            heapq.heappush(start, st)
        else:
            heapq.heappush(start, st)
            heapq.heappush(end, en)
print(len(start))

'''
start, end = [], []
for _ in range(int(input())):
    st, en = map(int, input().rsplit())
    if len(end) == 0:
        heapq.heappush(start, st)
        heapq.heappush(end, en)
    else:
        for i in range(len(end)):
            if end[i][0] >= en:
                heapq.heappushpop(start[i], st)
                heapq.heappushpop(end[i], en)


'''
