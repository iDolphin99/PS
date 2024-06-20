'''
연결 요소의 개수 
첫째 줄: 정점의 개수 N, 간선의 개수 M (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄~M개의 줄: 간선의 양 끝점 u, v 
'''
from sys import stdin 
from collections import deque
input = stdin.readline
N, M = map(int, input().rsplit())
graph = [[] * (N) for _ in range(N)]
for __ in range(M):
    u, v = map(int, input().rsplit())
    graph[u-1] += [v]
    graph[v-1] += [u]
print(graph)
    

  
    