'''
퇴사
첫째 줄 1 <= N <= 15
둘째 줄부터 N개의 줄에 T, P가 공백을 구분으로 주어지며, 1일부터 N일까지 순서대로 주어짐
둘째 줄 1 <= T <= 5 
둘째 줄 1 <= P <= 1,000
'''
from sys import stdin 
def recursive(day, remain, money): # 1, N, 0
    global answer
    if day==N: # 1일부터 N일까지 전부 순회하면 종료 (Brute Force)
        answer = max(answer, money)
        return
    if remain <= 0 and tList[day]+day <= N: 
        recursive(day, tList[day], money+pList[day]) # 경우의 수 분기점 
    recursive(day+1, remain-1, money) # 1일부터 N일까지 순회하기 위한 재귀
    

input = stdin.readline
N = int(input())
tList, pList, answer = [], [], 0
for i in range(N):
    t, p = map(int, input().rsplit())
    tList.append(t)
    pList.append(p)
for i in range(N):
    recursive(i, 0, 0)
print(answer)

