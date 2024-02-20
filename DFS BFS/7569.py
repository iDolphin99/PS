'''
토마토(with h)
하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 
둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다. 
정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
'''
from sys import stdin
from collections import deque
input = stdin.readline
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
deq = deque([])

def BFS():
    tomato = M * N * H
    days = 1
    for i in range(H): # 1,000,000
        for j in range(N):
            for k in range(M):
                if graph[i][j][k] == 1: 
                    deq.append([i, j, k])    # z x y
                    tomato -= 1
                if graph[i][j][k] == -1:
                    tomato -= 1
    while deq:
        z, x, y = deq.popleft() # i, j, k -> H, N, M -> z, x, y
        for dx, dy, dz in d:
            Z, X, Y = z+dz, x+dx, y+dy
            if 0<=X<N and 0<=Y<M and 0<=Z<H and graph[Z][X][Y]==0:
                graph[Z][X][Y] = graph[z][x][y] + 1
                deq.append([Z, X, Y])
                tomato -= 1
                days = max(days, graph[Z][X][Y])
    return tomato, days

tomato, days = BFS()

if tomato != 0:
    print("-1")
else:
    print(days-1)
