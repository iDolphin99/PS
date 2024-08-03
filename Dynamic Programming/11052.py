'''
카드 구매하기
첫째 줄: 구매하려고 하는 카드의 개수 N (1 ≤ N ≤ 1,000)
둘째 줄: Pi가 P1부터 PN까지 순서대로 (1 ≤ Pi ≤ 10,000)
'''

from sys import stdin 

def solution():
    input = stdin.readline
    N = int(input().rstrip())
    cards = list(map(int, input().rsplit()))
    
    dp = [0] * N
    dp[0] = cards[0]
    
    for i in range(1, N):
        dp[i] = cards[i]
        for j in range(i):
            tmp = dp[j] + dp[i-j-1]
            if tmp > dp[i]: 
                dp[i] = tmp    
    
    return dp[N-1]

if __name__ == "__main__":
    print(solution())