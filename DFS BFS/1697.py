'''
Catch That Cow
Walking: FJ can move from any point X to the points X-1 or X+1 in a single minute
Teleporting: FJ can move from any point X to the point 2*X in a single minute.
print("level: ", level, ", deque: ", deq, ", child: ", child)   
'''
from sys import stdin 
from collections import deque
input = stdin.readline
N, K = map(int, input().split())

def bfs():
    visited = [0]*100001
    visited[N] = 1
    deq = deque([N])
    while deq: 
        node = deq.popleft()
        if K == node : 
            return print(visited[node]-1) # visited[N]=1로 시작해버려서 -1을 해줘야 함 
        child = [node-1, node+1, node*2] 
        for c in child: 
            if 0 <= c <= 100000 : # important constraint
                if visited[c]==0: # 아직 방문하지 않았다면
                    visited[c] = visited[node] + 1 # 따로 경로의 수를 변수로 둘 필요 없음 
                    deq.append(c)
    
bfs()
