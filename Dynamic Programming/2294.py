'''
동전 2
첫째 줄: N, K (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
둘째 줄~N째 줄: 동전의 가치 A (1 ≤ A ≤ 100,000)
가치가 같은 동전이 여러 개 주어질 수 있음 
동전 사용이 불가능한 경우 -1 출력
'''

from sys import stdin

def solution():
    input = stdin.readline
    N, K = map(int, input().rsplit())
    coins = [int(input().rstrip()) for _ in range(N)]
    
    dp = [10001] * 100001
    dp[0] = 0
    for coin in coins:
        for i in range(coin, K+1):
            if dp[i] > 0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return -1 if dp[K]==10001 else dp[K]

if __name__ == "__main__":
    print(solution())

    
    
    

