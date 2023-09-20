'''
GCD합
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
'''

from sys import stdin, stdout 
from math import gcd
from itertools import combinations  
input = stdin.readline
for _ in range(int(input().rstrip())):
    total = 0
    num, *arr = map(int, input().split())
    for _, pair in enumerate(list(combinations(arr, 2))):
        total += gcd(*pair)
    stdout.write(str(total) + '\n')