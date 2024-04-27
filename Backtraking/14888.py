'''
연산자 끼워넣기 
첫째 줄: 수의 개수 N(2<=N<=11) 
둘째 줄: A1, A2, ..., An(1<=Ai<=100)
셋째 줄: +, -, x, % (도합 N-1개)
주어진 수의 순서를 바꾸면 안 된다.
연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 
또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.
'''
from sys import stdin
input = stdin.readline
N = input()
nums = list(map(int, input().split())) 
cals = list(map(int, input().split()))
maxValue, minValue = -1e9, 1e9

def backTracking(depth, plus, minus, multiply, divide, result):
    global maxValue, minValue
    
    if depth == len(nums)-1: # 종료 조건 
        maxValue = max(maxValue, result)
        minValue = min(minValue, result)
        print("return")
        return
    
    if plus > 0:
        print("Plus: Backtracking with depth: ", depth, " / ", plus-1,minus,multiply,divide, "result: ", result+nums[depth+1])
        backTracking(depth+1, plus-1, minus, multiply, divide, result+nums[depth+1])
    if minus > 0:
        print("Minus: Backtracking with depth: ", depth, " / ", plus,minus-1,multiply,divide, "result: ", result-nums[depth+1])
        backTracking(depth+1, plus, minus-1, multiply, divide, result-nums[depth+1])
    if multiply > 0:
        print("Multiply: Backtracking with depth: ", depth, " / ", plus,minus,multiply-1,divide, "result: ", result*nums[depth+1])
        backTracking(depth+1, plus, minus, multiply-1, divide, result*nums[depth+1])
    if divide > 0:
        print("Divide: Backtracking with depth: ", depth, " / ", plus,minus,multiply,divide-1, "result: ", result//nums[depth+1])  
        if result < 0:
            backTracking(depth+1, plus, minus, multiply, divide-1, -(abs(result)//nums[depth+1]))
        else: backTracking(depth+1, plus, minus, multiply, divide-1, result//nums[depth+1])
    
backTracking(0, cals[0], cals[1], cals[2], cals[3], nums[0])
print(maxValue, minValue)


''' Failed Code
    for i in range(index, len(visited)): 
        if visited[index] == -1:
            for j in range(len(cals)): # 0 1 2 3 
                if cals[j] != 0:
                    visited[depth] = cals_visited[i]
                    cals[j] -= 1
                    print("changed: ", visited)
                    break
                    #result = nums[i] + nums[i+1] # dictionary 써서 연산 
            print("backtracking", depth+1, i+1)
            backTracking(depth+1, result, i+1)
            cals[visited[i]] += 1
            visited[depth] = -1
            print("unchanged: ", visited)
        else:
            print("pass if")
'''