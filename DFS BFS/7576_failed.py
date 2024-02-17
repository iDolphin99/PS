'''
토마토
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 
둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
'''

from sys import stdin 
input = stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tmt = sum(row.count(0) for row in graph)
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def BFS(x, y):
    global tmt
    for dx, dy in d:
        X, Y = x+dx, y+dy 
        if 0 <= X < N and 0 <= Y < M and graph[X][Y] == 0:
            graph[X][Y] = graph[x][y]+1
            tmt = tmt - 1

days = 1
while tmt > 0:
    if days > max(map(max, graph)) : 
        days = 0
        break
    for i in range(N):
        if graph[i].count(0) == 0:
            continue 
        else:    
            for j in range(M):
                if graph[i][j] == days: 
                    BFS(i, j)
    days += 1
    for row in graph:
        print(row)
    print("===========", days,"============")

print(days-1)