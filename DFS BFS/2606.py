'''
바이러스
첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
'''
from sys import stdin 
from collections import deque
input = stdin.readline
V = int(input())
vList = [[] for _ in range(1, V+1)] # index number = vertex - 1
for i in range (int(input())):
    v, e = map(int, input().split())
    vList[v-1] += [e]
    vList[e-1] += [v]

def bfs(startV): # 이유: dfs는 가장 깊은 곳 까지 순회하면 탐색을 종료하니까? -> dfs도 가능
    visited = []
    deq = deque([startV])
    while deq: 
        currentV = deq.popleft()
        if currentV not in visited:
            visited.append(currentV)
            for v in vList[currentV-1]:
                if v not in visited:
                    deq.append(v)
    return len(visited)-1

print(bfs(1))

    
    