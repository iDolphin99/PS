'''
2xN 타일링
첫째 줄: n (1 ≤ n ≤ 1,000)
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력
'''

from sys import stdin
if __name__ == "__main__":
    input = stdin.readline
    N = int(input())
    dp = {1: 1, 2: 2}
    if N >=3:
        for i in range(3, N+1):
            dp[i] = (dp.get(i-1) + dp.get(i-2))%10007
    print(dp.get(N))