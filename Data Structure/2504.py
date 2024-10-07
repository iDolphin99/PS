'''
괄호의 값 
() : 2 
[] : 3
(X) : Xx2
[X] : Xx3 
'''

from sys import stdin 

def solution():
    string = stdin.readline().rstrip()
    
    dic = {")": "(", "]": "["}
    stack = []
    answer = 0
    for s in string:
        if s in dic.values():
            stack.append(s)
        elif s in dic.keys():
            last = stack.pop()
            if last != dic.get(s):
                break 
            else:
                answer += 1
    
    return answer

if __name__ == "__main__":
    print(solution())