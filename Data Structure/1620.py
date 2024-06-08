'''
나는야 포켓몬 마스터 이다솜 
첫째 줄: 포켓몬 개수 N, 맞춰야 하는 문제 개수 M (1 <= N,M <= 100.000)
둘째 줄~N개의 줄: 1번부터 N번에 해당하는 포켓몬 이름(2~20) 
N째 줄~M개의 줄 : 알파벳 > 포켓몬 번호, 숫자 > 포켓몬 문자 
'''
from sys import stdin
input = stdin.readline
N, M, = map(int, input().rsplit())
numList = [input().rstrip() for _ in range(N)]
nameDict = {k:v for v, k in enumerate(numList, 1)}
for _ in range(M):
    key = input().rstrip()
    if key.isdigit() : print(numList[int(key)-1])
    else: print(nameDict.get(key))