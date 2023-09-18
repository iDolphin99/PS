'''
A+B - 9
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
'''
from sys import stdin, stdout
stdout.write(str(sum(map(int, stdin.readline().split()))))