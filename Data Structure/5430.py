'''
AC 
- 첫째 줄: 테스트 케이스 개수 1 <= T <= 100 
- 테스트 케이스 첫째 줄: 수행 함수 1 <= p <= 100,000
- 테스트 케이스 둘째 줄: 배열에 들어있는 수의 개수 0 ≤ n ≤ 100,000
- 테스트 케이스 셋째 줄: 배열에 들어있는 정수 [x1,...,xn], 1 ≤ xi ≤ 100
- p의 길이 합과 n의 합 < 700,000
''' 
from sys import stdin
from collections import deque 
input = stdin.readline
for _ in range(int(input())):
    pList = input().rstrip()
    deqLen = int(input())
    deq = deque(input().rstrip()[1:-1].split(","))
    if deqLen == 0:
        deq = deque([])
    reverse, error = False, False
    
    for p in pList:
        if p=='R':
            if reverse: reverse = False 
            else : reverse = True
        elif p=='D' :
            if len(deq)==0:
                error = True
                break 
            if reverse: deq.pop()
            else : deq.popleft()
    
    if error: print("error")
    else: 
        if reverse : deq.reverse()
        print("["+",".join(deq)+"]")