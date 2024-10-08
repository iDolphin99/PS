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
    num = 1
    isOpen = False
    stack = []
    answer = 0
    for s in string:
        if s in dic.values(): # open
            if s == "(": num *= 2 
            else: num *= 3 
            stack.append([s, num])
            isOpen = True
        elif s in dic.keys(): # close
            if len(stack)==0 or stack[-1][0] != dic.get(s): 
                break 
            last = stack.pop()
            if isOpen:
                answer += last[1]
            num = stack[-1][1]
            isOpen = False
        print(stack, answer)
            
            
    return answer

if __name__ == "__main__":
    print(solution())