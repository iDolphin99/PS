'''
귀여운 라이언
첫째 줄: N과 K가 주어진다. (1 ≤ K ≤ N ≤ 106)
둘째 줄: N개의 인형 정보 (1 or 2)
'''
from collections import deque
from sys import stdin

def solution():
    input = stdin.readline
    N, K = map(int, input().rsplit())
    toys = list(map(int, input().rsplit()))

    answer = 1e6
    ryan = deque([])
    st, en, cnt = 0, 0, 0
    while en < N:
        if toys[en] == 1: 
            ryan.append(en)
            cnt += 1
        if cnt == K:
            st = ryan.popleft()
            answer = min(answer, en-st+1)
            if answer == K:
                return K
            cnt = K-1
        en+=1
    
    return answer if answer != 1e6 else -1

if __name__ == "__main__":
    print(solution())