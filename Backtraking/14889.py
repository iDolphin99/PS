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
answer = 1e9

for starts in combinations(range(N), N//2):
    links = [i for i in range(N) if i not in starts]
    start = list(permutations(starts, 2))
    link = list(permutations(links, 2))
    start_sum, link_sum = 0, 0
    for s, l in zip(start, link):
        start_sum += S[s[0]][s[1]]
        link_sum += S[l[0]][l[1]]
    if abs(start_sum-link_sum) < answer: answer = abs(start_sum-link_sum)
print(answer)

'''
combination = list(combinations(range(N), N//2))
for starts in combination:
    start = list(permutations(starts, 2))
    start_sum = 0
    for s in start:
        start_sum += S[s[0]][s[1]]
    link_sum = total_sum - start_sum
    print(link_sum, start_sum)
    if abs(start_sum - link_sum) < answer: 
        answer = abs(start_sum - link_sum)
        # print(answer)
print(total_sum)
print(answer)

'''