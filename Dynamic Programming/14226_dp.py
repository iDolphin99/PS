'''
이모티콘
첫째 줄:  S (2 ≤ S ≤ 1000)
'''

from sys import stdin

def solution():
    S = int(stdin.readline())
    
    dp = [[0 for _ in range(S)] for __ in range(S)]
    dp[0][0] = 1

    for i in range(1, S):
        minCnt = float("inf")
        for j in range(i):
            dp[i][j] = dp[i-j-1][j] + 1
            minCnt = min(minCnt, dp[i][j])
        dp[i][i] = minCnt + 1
        for k in range(i, 0, -1):
            dp[k-1][i] = dp[k][i] + 1
    
    return min(dp[S-1])

if __name__ == "__main__":
    print(solution())