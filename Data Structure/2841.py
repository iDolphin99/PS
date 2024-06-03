'''
외계인의 기타 연주 
첫째 줄: 음의 수 N, 한 줄에 있는 프렛 수 P (1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)
둘째 줄~N개 줄: 줄의 번호, 줄에서 눌러야 하는 프렛 번호 
줄의 번호는 N보다 작거나 같은 자연수이고, 프렛의 번호도 P보다 작거나 같은 자연수
'''

from collections import deque
from sys import stdin
input = stdin.readline
N, F = map(int, input().split())
guitar = [deque([0]) for _ in range(F)]
answer = 0

for _ in range(N):
    isAppend = True
    string, fret = map(int, input().split())
    while isAppend:
        if len(guitar[string]) == 0:
            guitar[string].append(fret)
            answer += 1
            isAppend = False
        else:
            if guitar[string][-1] < fret: 
                guitar[string].append(fret)
                answer += 1
                isAppend = False
            elif guitar[string][-1] > fret: 
                guitar[string].pop()
                answer += 1
            else:
                isAppend = False
    
print(answer)


''' Another Answer (Shorter)
for _ in range(N):
    string, fret = map(int, input().split())
    while guitar[string][-1] > fret: 
        guitar[string].pop()
        answer += 1
    if guitar[string][-1] != fret:
        guitar[string].append(fret)
        answer += 1
'''