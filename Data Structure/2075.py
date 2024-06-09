'''
N번째 큰 수 
첫째 줄: N(1 ≤ N ≤ 1,500)
둘째 줄~N째 줄:-10억보다 크거나 같고 10억보다 작거나 같은 정수 
'''
from sys import stdin
import heapq
input = stdin.readline
N = int(input())
heap = []
for _ in range(N):
    heap += list(map(int, input().rsplit()))
    heapq.heapify(heap)
    while len(heap) > N:
        heapq.heappop(heap)
print(heap[0])