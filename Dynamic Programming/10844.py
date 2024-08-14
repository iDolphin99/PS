'''
쉬운 계단수
N은 1보다 크거나 같고, 100보다 작거나 같은 자연수
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력
'''

from sys import stdin

def solution():
    N = int(stdin.readline())
    dp = [[1 for _ in range(10)] for __ in range(N+1)]
    dp[1][0] = 0
    mod = 1000000000
    
    ans = 9
    for i in range(2, N+1):
        for j in range(10):
            if j==0:
                dp[i][j]=dp[i-1][1]
            elif j==9:
                dp[i][j]=dp[i-1][8]
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
        ans = sum(dp[i])%mod

    return ans

if __name__ == "__main__":
    print(solution())