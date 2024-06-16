'''
강의실 배정 
첫째 줄: N(1 ≤ N ≤ 200,000)
이후 N개 줄: Si, Ti(0 ≤ Si < Ti ≤ 10^9)
'''
from sys import stdin 
import heapq
input = stdin.readline
times = sorted([list(map(int, input().rsplit())) for _ in range(int(input()))])
start, end = [], []
for st, en in times:
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

