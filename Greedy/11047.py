'''
동전 0
첫째 줄: N, K (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄~N째 줄: 동전의 가치 Ai (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
'''
from sys import stdin 

if __name__ == '__main__':
    input = stdin.readline
    N, K = map(int, input().rsplit())
    coins = [int(input()) for i in range(N)]
    answer = 0 
    for j in range(N, 0, -1):
        answer += K//coins[j-1]
        K %= coins[j-1]
        if K==0: break 
    print(answer)
    