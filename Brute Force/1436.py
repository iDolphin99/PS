'''
영화감독 숌
첫째 줄: N <= 10,000
'''
from sys import stdin 
N = int(stdin.readline())
for i in range(666, 6660000):
    if "666" in str(i): 
        N-=1
    if N==0: 
        print(i)
        break
     