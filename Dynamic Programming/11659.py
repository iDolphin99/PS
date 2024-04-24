'''
구간 합 합치기 4 
첫째 줄: 수의 개수 N, 합을 구해야 하는 횟수 M, 1 ≤ N ≤ 100,000, 1 ≤ M ≤ 100,000
둘째 줄: N개의 수 
셋째 줄~M째 줄: 합을 구해야 하는 구간 i, j (1 ≤ i ≤ j ≤ N)
'''

from sys import stdin 
if __name__ == "__main__":
    input = stdin.readline
    N, M = map(int, input().rsplit())
    nList = list(map(int, input().rsplit()))
    dp = [0]
    for n in nList:
        dp.append(n+dp[-1])
    for k in range(M):
        i, j = map(int, input().rsplit())
        print(dp[j]-dp[i-1])
    

