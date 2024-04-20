'''
1로 만들기 
첫째 줄: 정수 N (1보다 크거나 같고, 10^6보다 작거나 같음)
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
'''

from sys import stdin 
from collections import deque
if __name__ == "__main__":
    N = int(stdin.readline())
    visited = [0] * (N+1)
    deq = deque([N])
    while deq:
        node = deq.popleft()
        if node == 1:
            print(visited[node])
            break
        else:
            cur = visited[node]
            nextList = []
            if visited[node-1] == 0:
                nextList.append(node-1)
            if node%3 == 0 and visited[node//3] == 0:
                nextList.append(node//3)
            if node%2 == 0 and visited[node//2] == 0:
                nextList.append(node//2)
            for nextNode in nextList:
                visited[nextNode] = cur+1
                deq.append(nextNode)
                        
             
        