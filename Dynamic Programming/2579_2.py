'''
계단 오르기 
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.
첫째 줄: 계단의 개수 (N<=300,자연수)
둘째 줄~N째 줄: 계단 점수 (M<=10,000 자연수)
-> 2차원 배열이 아닌 관점을 바꿔서 1차원 배열로 점화식 설계 후 코딩
'''

from sys import stdin
if __name__ == "__main__":
    input = stdin.readline
    N = int(input())
    stairs = [int(input()) for _ in range(N)]
    if N<=2:
        print(sum(stairs))
    else: 
        dp = {1: stairs[0], 2: stairs[1], 3: stairs[2]}
        for i in range(4, N):
            dp[i] = min(dp.get(i-2), dp.get(i-3)) + stairs[i-1]
        print(sum(stairs) - min(dp.get(N-1), dp.get(N-2)))