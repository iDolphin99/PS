'''
01타일 
첫째 줄: 1 ≤ N ≤ 1,000,000
'''
from sys import stdin 

def solution():
    N = int(stdin.readline())
    dp = [0, 1, 2]
    
    if N <= 2:
        return dp[N]
    
    for i in range(3, N+1):
        dp.append((dp[i-2] + dp[i-1]) % 15746)
    
    return dp[N]

if __name__ == "__main__":
    print(solution())