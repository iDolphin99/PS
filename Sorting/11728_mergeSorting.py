'''
배열 합치기 
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.
'''
from sys import stdin 
input = stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer, a, b = [], 0, 0

while True:
    if a==N:
        answer += B[b:]
        break 
    if b==M:
        answer += A[a:]
        break
    if A[a] <= B[b]:
        answer.append(A[a])
        a += 1
    else:
        answer.append(B[b])
        b += 1
print(*answer)        