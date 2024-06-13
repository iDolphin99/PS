'''
K번째 수 
첫째 줄: 배열의 크기 N (10^5보다 작거나 같은 자연수)
둘째 줄: k (min(10^9, N^2)보다 작거나 같은 자연수)
'''
from sys import stdin
from collections import defaultdict
input = stdin.readline
N, K = int(input().rstrip()), int(input().rstrip())

boundary = defaultdict()
boundary[1] = 1
kkk = 1
for i in range(2, N+1):
    kkk += 2*(N-i+1) + 1
    boundary[i] = kkk
print(boundary)

st, en, k = 1, N, 1

check = 0#
while st < en:
    mid = (st+en+1)//2
    
    k = 1
    for i in range(2, mid+1):
        k += 2*(N-i+1) + 1 
    
    check += 1# 
    print(check, "회차: ", st, en, mid, k)#    
    
    if k > K:
        en = mid-1
    else:
        st = mid
        
print(st, en+1, k)#
        
while k > K:
    k-=1
    print(k, ": ", st*N)
    k-=1
    print(k, ": ", st*N)
    N-=1