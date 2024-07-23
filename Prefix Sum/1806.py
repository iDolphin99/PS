'''
부분합
첫째 줄: N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
둘째 줄: 수열, 각 원소는 공백으로 구분, 10,000이하의 자연수
'''
from sys import stdin 

def solution():
    input = stdin.readline
    N, S = map(int, input().rsplit())
    nList = list(map(int, input().rsplit()))
    
    if S == 0:
        return 1
    
    prefix = [0]
    for i in range(N):
        prefix.append(nList[i]+prefix[i])
    
    st, en = 0, 1
    answer = []
    while st <= en <= N: 
        if st == 0:
            preSum = prefix[en] + prefix[st]
        else:
            preSum = prefix[en] - prefix[st]
        if preSum < S:
            en += 1 
        else:
            if len(answer) and en-st < answer[0]-answer[1] or len(answer)==0:
                answer = [en, st]
            st += 1 
    
    return answer[0]-answer[1] if len(answer) else 0

if __name__ == "__main__":
    print(solution())