'''
스타트와 링크
4 <= N <= 20 (N은 짝수)
Sii = 0 
1 < = Sij <= 100 
'''
from sys import stdin
from itertools import combinations, permutations
input = stdin.readline
N = int(input())
S = [[0] * N] * N
for i in range(N):
    S[i] = list(map(int, input().rsplit()))

answer = int(1e9)
combination = list(combinations(range(N), N//2))
for starts in combination:
    links = [i for i in range(N) if i not in starts]
    start = list(permutations(starts, 2))
    link = list(permutations(links, 2))
    sum1, sum2 = 0, 0
    for s, l in zip(start, link):
        sum1 += S[s[0]][s[1]]
        sum2 += S[l[0]][l[1]]
    if abs(sum1-sum2) < answer: answer = abs(sum1-sum2)
print(answer)