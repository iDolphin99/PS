'''
이진수 덧셈 
두 이진수가 주어졌을 때, 그 합을 이진수로 출력하는 프로그램을 작성하시오.
'''

from sys import stdin, stdout
input = stdin.readline
for _ in range(int(input().rstrip())):
    A, B = input().split()
    stdout.write(str(bin(int(A,2)+int(B,2))[2:])+'\n')