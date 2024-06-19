'''
저울
첫째 줄: N (1<=N<=1,000)
둘째 줄: N개의 양의 정수, (1<=각 추의 무게<=1,000,000)
'''
from sys import stdin 
input = stdin.readline
      
def solution():
    N = int(input())
    weights = sorted(list(map(int, input().rsplit())))

    possible, answer = [weights[0]], weights[0]+1
    if answer != 2: 
        print(1)
    else:
        for i in range(1, N):
            possible.append(weights[i])
            if weights[i] <= answer: 
                possible.append(sum(weights[:i+1]))
                answer = max(possible)+1
            else:
                break
            # print("updated possible Ws: ", possible)
            # print("updated answer: ", answer)  
        print(answer)
    
if __name__ == "__main__":
    solution()