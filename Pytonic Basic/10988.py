'''
팰린드롬인지 확인하기 
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.
'''
import sys 
s = sys.stdin.readline().rstrip()
print(1 if s[::] == s[::-1] else 0)