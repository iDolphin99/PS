'''
카드 
첫째 줄: N (1 ≤ N ≤ 100,000)
둘째 줄~N째 줄: 숫자 카드에 적혀 있는 정수, -262보다 크거나 같고, 262보다 작거나 같음
- Counter 라이브러리를 사용하지 않고 풀어보기!
'''
from sys import stdin
input = stdin.readline
cards = sorted([int(input()) for _ in range(int(input()))])
idx, maxCnt, cnt = 0, 1, 1
for i in range(1, len(cards)):
    if cards[i] == cards[i-1]:
        cnt += 1 
    else:
        if cnt > maxCnt:
            maxCnt = cnt
            idx = i-1
        cnt = 1
if cnt > maxCnt:
    idx = len(cards)-1
print(cards[idx])
    