'''
수 찾기 
첫째 줄: N(1 ≤ N ≤ 100,000)
둘째 줄: N개의 정수 A[1], A[2], …, A[N]
셋째 줄: M(1 ≤ M ≤ 100,000)
넷째 줄: M개의 수(모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다)
'''
from sys import stdin
input = stdin.readline 
N = int(input())
Narr = sorted(list(map(int, input().split())))
M = int(input())
Marr = list(map(int, input().split()))
for m in Marr:
    start, end, answer = 0, N-1, 0
    while end >= start:
        mid = (start+end)//2
        if Narr[mid] == m:
            answer = 1
            break
        else:   
            if Narr[mid] > m:
                end = mid - 1
            else:
                start = mid + 1  
    print(answer)
    
    
'''
    while end - start != 1:
        mid = (start+end)//2
        if Narr[mid] == m:
            answer = 1
            break
        else:   
            if Narr[mid] > m:
                end = mid
            else:
                start = mid 
    if Narr[start] == m or Narr[end] == m:
        answer = 1 
'''
