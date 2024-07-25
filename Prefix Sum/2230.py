'''
수 고르기 
첫째 줄: N, M 
둘째 줄~N째 줄: A[1], A[2], ... , A[N]
'''

from sys import stdin 

def solution():
    input = stdin.readline 
    N, M = map(int, input().rsplit())
    nlist = [int(input().rstrip()) for _ in range(N)]
    nlist.sort()
    
    answer = 2e9
    st, en = 0, N-1
    while en >= 0 and en >= st:
        gap = nlist[en]-nlist[st]
        if gap >= M:
            st += 1 
            answer = min(answer, gap)
            if answer == M: return M
        else:
            en -= 1
            st = 0
    return answer

if __name__ == "__main__":
    print(solution())