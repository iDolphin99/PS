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
    wasOpen = False
    stack = [["{", 1]]
    answer = 0
    for s in string:
        last = stack[-1][1]
        if s in dic.values(): # open
            if s == "(": last *= 2 
            else: last *= 3 
            stack.append([s, last])
            wasOpen = True
        elif s in dic.keys(): # close   
            if stack[-1][0]=="{" or stack[-1][0] != dic.get(s): 
                return 0
            if wasOpen:
                answer += last
            stack.pop()
            wasOpen = False    
            
    return answer if len(stack)==1 else 0

if __name__ == "__main__":
    print(solution())