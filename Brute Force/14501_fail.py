'''
퇴사
첫째 줄 1 <= N <= 15
둘째 줄부터 N개의 줄에 T, P가 공백을 구분으로 주어지며, 1일부터 N일까지 순서대로 주어짐
둘째 줄 1 <= T <= 5 
둘째 줄 1 <= P <= 1,000
'''
from sys import stdin 
import numpy as np
input = stdin.readline
N = int(input())
arr = [[0] * N for _ in range(2)] 
for i in range(N):
    t, p = map(int, input().rsplit())
    arr[0][i], arr[1][i] = t, p

def rec(day, pay, remain):
    if day == N:
        answer = max(answer, pay)
        return 
    if remain <= 0:
        print()