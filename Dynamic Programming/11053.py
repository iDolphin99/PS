'''
가장 긴 증가하는 부분 수열 
첫째 줄: 수열 A의 크기 N (1 ≤ N ≤ 1,000)
둘째 줄: 수열 A를 이루고 있는 Ai (1 ≤ Ai ≤ 1,000)
'''

from sys import stdin 

def solution():
    input = stdin.readline 
    N = int(input())
    nlist = list(map(int, input().rsplit()))
    
    dp = [1]
    for i in range(N-2, -1, -1):
        # print(nlist[i:])
        dpNow = 1
        for j in range(i+1, N):
            if nlist[j] > nlist[i]:
                dpNow = max(dp[N-j-1]+1, dpNow)
        dp.append(dpNow)
        # print(dp[::-1])

    return max(dp)

if __name__ == "__main__":
    print(solution())