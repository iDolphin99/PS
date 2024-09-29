'''
균형잡힌 세상 
- 각 문자열은 마지막 글자를 제외하고 영문 알파벳, 공백, 소괄호("( )"), 대괄호("[ ]")로 이루어져 있으며, 온점(".")으로 끝남
- 길이는 100글자보다 작거나 같음
- 입력의 종료조건으로 맨 마지막에 온점 하나(".")가 들어옴
'''

from sys import stdin

def solution():
    input = stdin.readline
    pairs = {"]": "[", ")": "("}
    
    while True:
        string = input().rstrip()
        flag = True
        stack = []
        if len(string) == 1:
            break
        else:
            for s in string:
                if s in pairs.values():
                    stack.append(s)
                elif s in pairs.keys():
                    if len(stack) == 0 or stack.pop() != pairs[s]:
                        flag = False
                if flag == False:
                    break
            print("yes") if flag and len(stack) == 0 else print("no")
     
    return 0

if __name__ == "__main__":
    solution()