'''
저울
첫째 줄: N (1<=N<=1,000)
둘째 줄: N개의 양의 정수, (1<=각 추의 무게<=1,000,000)
'''
from sys import stdin 
input = stdin.readline
N = int(input())
weights = sorted(list(map(int, input().rsplit())))
print(weights)

previous = [weights[0]]
for i in range(1, N):
    current = []
    current.append(weights[i])
    for p in previous:
        if isinstance(p, int):
            p = [p, weights[i]]
        else:
            p.append(weights[i])
        current.append(p)
    previous.append(current)
print(previous)