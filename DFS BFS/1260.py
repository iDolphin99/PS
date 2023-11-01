'''
DFS와 BFS
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''
from sys import stdin 
from collections import deque
input = stdin.readline

N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    matrix[n1][n2] = 1 
    matrix[n2][n1] = 1

visited1 = [0] * (N+1) 
visited2 = [0] * (N+1) 

def dfs(V):
    visited1[V] = 1 
    print(V, end=" ")
    for i in range(1, N+1):
        if visited1[i] != 1 and matrix[V][i] == 1 :
            dfs(i)   
def bfs(V):
    deq = deque([V])
    visited2[V] = 1 
    while deq:
        n = deque.popleft(deq)
        for i in range(1, N+1):
            if visited2[i] != 1 and matrix[n][i] == 1 : 
                visited2[i] = 1
                deq.append(i)
        print(n, end=" ")

dfs(V)
print()
bfs(V)
    