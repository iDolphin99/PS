'''
LCS
문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자
'''

from sys import stdin 

def solution():
    input = stdin.readline
    
    str1 = input().rstrip()
    str2 = input().rstrip()
    
    return str1

if __name__ == "__main__":
    print(solution())