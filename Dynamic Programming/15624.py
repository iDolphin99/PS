'''
피보나치 수 7
n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력
첫째 줄: n (n은 1,000,000보다 작거나 같은 자연수 또는 0이다)
'''

from sys import stdin 

if __name__ == "__main__":
    N = int(stdin.readline())
    memo = [0] * (N+1)
    if N>=1:
        memo[1]=1
    for i in range(2, N+1):
        memo[i] = (memo[i-1]+memo[i-2])%1000000007
    print(memo[N])
