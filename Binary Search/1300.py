'''
K번째 수 
첫째 줄: 배열의 크기 N (10^5보다 작거나 같은 자연수)
둘째 줄: k (min(10^9, N^2)보다 작거나 같은 자연수)
'''
from sys import stdin
input = stdin.readline
N, K = int(input().rstrip()), int(input().rstrip())

st, en, answer = 1, N**2, 0
while st <= en:
    mid = (st+en)//2
    
    k = 0
    for i in range(1, N+1):
        k += min(mid//i, N)       
    
    if k >= K:
        answer = mid
        en = mid-1
    else:
        st = mid+1
        
print(answer)