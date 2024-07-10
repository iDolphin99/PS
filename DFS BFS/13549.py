'''
숨바꼭질 3
첫째 줄: N, K (0 ≤ N, K ≤ 100,000), 정수
- 걷기: x-1, x+1, 1초 
- 순간이동: 2*x, 0초
'''
from sys import stdin
from collections import deque 
N, K = map(int, stdin.readline().rsplit())
visited = [0]*100001
visited[N] = 1

deq = deque([N])
while deq:
    current = deq.popleft()
    if current == K:
        print(visited[K]-1)
        break
    
    visitList = [2*current, current-1, current+1]  
    for v in visitList: 
        if 0 <= v <= 100000 and visited[v] == 0:
            deq.append(v)
            if v == current*2: 
                visited[v] = visited[current] 
            else :
                if visited[v] == 0: 
                    visited[v] = visited[current]+1
