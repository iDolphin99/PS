'''
쇠막대기
한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어짐
- 괄호 문자의 개수는 최대 100,000
'''

from sys import stdin

def solution():
    iron = stdin.readline().rstrip()
    
    stack = []
    answer = 0
    for i, peice in enumerate(iron):
        if peice=="(":
            stack.append(i)
        else:
            if iron[i-1] == "(": 
                answer += len(stack)-1
            else:    
                answer += 1
            stack.pop()
    
    return answer

if __name__ == "__main__":
    print(solution())