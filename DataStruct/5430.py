'''
AC 
첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
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
        if len(deq)==0:
            error = True
            break 
        else:
            if p=='R':
                if reverse: reverse = False 
                else : reverse = True
            elif p=='D' :
                if reverse: deq.pop()
                else : deq.popleft()
    
    if error: print("error")
    else: 
        if reverse : deq.reverse()
        print("["+",".join(deq)+"]")
    #     print(deq.reverse() if reverse else deq)
    # # deqLast = int(input())-1
    # deqStart = 0
    # deq = list(map(int, input().rstrip()[1:-1].split(",")))
    # for p in pList:
    #     if p=='R': deqLast, deqStart = deqStart, deqLast
    #     elif p=='D': 
    #         if deqStart > deqLast: deqStart -= 1
    #         else : deqStart += 1
    # result = deq[deqStart:deqLast+1:-1] if deqStart > deqLast else deq[deqStart:deqLast+1]
    # print("error") if result==[] else print(result) 
    # print(deqStart, deqLast)   