'''
미로 탐색 
IN: 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
OUT: 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''
from sys import stdin 
from collections import deque
input = stdin.readline

N, M = map(int, input().split())
graph = [[0]*(M+2)]
for _ in range(N):
    graph.append([0] + list(map(int, input().rstrip())) + [0])
graph.append([0]*(M+2))

def bfs() :
    deq = deque([(1, 1)])
    level = 1
    while deq:
        dLen = len(deq)
        for i in range(dLen):
            x, y = deq.popleft() 
            if x == N and y == M : return print(level)
            graph[x][y] = graph[x][y] + 1
            if graph[x+1][y] == 1 and [x+1, y] not in deq: deq.append([x+1, y])
            if graph[x-1][y] == 1 and [x-1, y] not in deq: deq.append([x-1, y])
            if graph[x][y+1] == 1 and [x, y+1] not in deq: deq.append([x, y+1])
            if graph[x][y-1] == 1  and [x, y-1] not in deq: deq.append([x, y-1])
        level = level+1

bfs()  