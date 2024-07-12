'''
벽 부수고 이동하기 
첫째 줄: N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)
다음 N개의 줄에 M개의 숫자로 맵
(1, 1)과 (N, M)은 항상 0이라고 가정
'''
from sys import stdin 
from collections import deque 
input = stdin.readline

def printgraph(g):
    for i in range(len(g)): 
        print(g[i])
    print("----------------------------------")

def BFS():
    N, M = map(int, input().rsplit())
    graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)] # 1: not broken, 0: broken
    visited[0][0][1] = 1
    
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    deq = deque([(0,0,1)])
    while deq:
        x, y, break_cnt = deq.popleft()
        if (x, y) == (N-1, M-1): 
            return visited[x][y][break_cnt]
        for dx, dy in directions:
            newX, newY = x+dx, y+dy
            if 0 <= newX < N and 0 <= newY < M:
                # 벽이 없다면?
                if graph[newX][newY] == 0 and visited[newX][newY][break_cnt] == 0: 
                    visited[newX][newY][break_cnt] = visited[x][y][break_cnt] + 1 
                    deq.append((newX, newY, break_cnt))
                # 벽이 있다면?
                if graph[newX][newY] == 1 and break_cnt == 1 and visited[newX][newY][0] == 0: 
                    visited[newX][newY][break_cnt-1] = visited[x][y][break_cnt] + 1
                    deq.append((newX, newY, break_cnt-1))    
        # printgraph(visited) # for check
    return -1
    
print(BFS())