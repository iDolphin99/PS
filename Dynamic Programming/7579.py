'''
앱
첫째 줄: 정수 N과 M
둘째 줄: 활성화 되어 있는 앱 A1, ..., AN이 사용 중인 메모리의 바이트 수인 m1, ..., mN
셋째 줄: 각 앱을 비활성화 했을 경우의 비용 c1, ..., cN
1 ≤ N ≤ 100, 1 ≤ M ≤ 10,000,000
1 ≤ m1, ..., mN ≤ 10,000,000
0 ≤ c1, ..., cN ≤ 100
M ≤ m1 + m2 + ... + mN
'''

from sys import stdin

def solution():
    input = stdin.readline
    
    N, M = map(int, input().rsplit())
    memory = [0] + list(map(int, input().rsplit()))
    cost = [0] + list(map(int, input().rsplit()))

    minCost = sum(cost)    
    dp = [[0 for _ in range(minCost)] for __ in range(N+1)]
    for i in range(1, N+1):
        mi, ci = memory[i], cost[i]
        for j in range(minCost):
            if ci > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-ci]+mi)
            if dp[i][j] >= M:
                minCost = min(minCost, j) 
        
    return minCost

if __name__ == "__main__":
    print(solution())