'''
ATM 
첫째 줄: 사람의 수 N(1 ≤ N ≤ 1,000)
둘째 줄: 각 사람이 돈을 인출하는 데 필요한 시간 Pi(1 ≤ Pi ≤ 1,000)
'''
from sys import stdin
input = stdin.readline
N = int(input().rstrip())
times = sorted(list(map(int, input().rsplit())))
answer = 0
for i, t in enumerate(times):
    answer += t*(N-i)
print(answer)