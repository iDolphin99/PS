'''
수 정렬하기 5
N개의 수가 주어졌을 때, 이를 비내림차순으로 정렬하는 프로그램을 작성하시오.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
- 첫째 줄: N(1 ≤ N ≤ 1,000,000)
- 둘째 줄~N개의 줄: 절댓값이 1,000,000보다 작거나 같은 정수이며, 같은 수가 여러 번 중복될 수도 있다.
'''

from sys import stdin, stdout 
input = stdin.readline
print = stdout.write
N = int(input())
nList = sorted([int(input()) for _ in range (N)])
for n in nList:
    print(str(n) + "\n")