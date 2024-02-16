'''
연결단지 붙이기 
연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다. 
'''
from sys import stdin,stdout
input = stdin.readline
print = stdout.write
N = int(input())
visited = [list(map(int, input().rstrip())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
groups = []

def DFS(x, y):
    global count
    visited[x][y] = 0
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X >= N or Y < 0 or Y >= N:
            continue
        else: 
            if visited[X][Y] == 1: 
                count += 1
                # print("dfs with ", X, Y, count)
                DFS(X, Y)
    return count

for i in range(N):
    for j in range(N):
        if visited[i][j] == 1:
            count = 1
            groups.append(DFS(i, j))

groups.sort()
print(str(len(groups))+'\n')
print(str(groups)[1:-1].replace(', ', '\n'))
