'''
평범한 배낭 
첫째 줄: 물품의 수 N(1 ≤ N ≤ 100), 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
둘째 줄~N째 줄: 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)
'''

from sys import stdin 

def solution():
    input = stdin.readline
    N, K = map(int, input().rsplit())
    bags = [list(map(int, input().rsplit())) for _ in range(N)]
    
    dp = [[0 for _ in range(N+1)] for __ in range (K+1)]
    for i in range(1, N+1):
        wi, vi = bags[i-1]
        for j in range(1, K+1):
            if j >= wi:
                dp[j][i] = max(dp[j][i-1], dp[j-wi][i-1]+vi)
            else:
                dp[j][i] = dp[j][i-1]
        print(dp)
    
    return dp[K][N] 

if __name__ == "__main__":
    print(solution())