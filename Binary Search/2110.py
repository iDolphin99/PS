'''
공유기 설치 
첫째 줄: 집의 개수 N (2 ≤ N ≤ 200,000), 공유기의 개수 C (2 ≤ C ≤ N)
둘째 줄~N째 줄: 집의 좌표 xi (0 ≤ xi ≤ 1,000,000,000)
'''
from sys import stdin
input = stdin.readline

def solution():
    N, C = map(int, input().rsplit())
    houses = sorted([int(input()) for _ in range(N)])
    distances = [houses[i]-houses[i-1] for i in range(1, N)]
    st, en = min(distances), houses[N-1]-houses[0]

    while st < en:
        mid = (st+en+1)//2 
        if st == mid: break  
        count, lengthSum = 1, 0
        for j in range(N-1):
            lengthSum += distances[j]
            if lengthSum >= mid:
                count += 1
                lengthSum = 0
        if count < C:
            en = mid-1
        else:
            st = mid
    print(st)

if __name__ == "__main__":
    solution()