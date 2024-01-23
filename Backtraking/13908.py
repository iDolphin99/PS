'''
비밀번호
1) 첫째 줄: 비밀번호 길이 1 <= N <= 7
2) 첫째 줄: 선견지명 비밀먼호 수 0 <= M <= N
3) 둘째 줄: M개의 서로 다른 숫자(0~9), M이 0일 경우 둘째 줄 X 
'''
from sys import stdin
N, M = map(int, stdin.readline().rsplit())
if M != 0:
    mList = list(stdin.readline().rsplit())
else:
    mList = []

possible, answer = 10**N, 10**N 
for i in range(possible):
    text = str(i).zfill(N)
    if mList != []:
        for m in mList:
            if m not in text:
                answer -= 1
                break

print(answer)
