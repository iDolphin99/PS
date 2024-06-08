'''
문자열 집합 
첫째 줄: N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)
둘째 줄~N째 줄: 집합 S에 포함되어 있는 문자열 
N째 줄 ~M째 줄: 검사해야 하는 문자열 
'''
from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
nSet = {input().rstrip() for _ in range(N)}
answer = 0
for _ in range(M):
    key = input().rstrip()
    if key in nSet:
        answer += 1
print(answer)