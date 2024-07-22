'''
두 용액
첫째 줄: 전체 용액의 수 N (2이상 100,000 이하)
-1,000,000,000 이상 1,000,000,000 이하
N개의 용액들의 특성값은 모두 다르고, 
산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.
'''
from sys import stdin
input = stdin.readline

def solution():
    N = int(input())
    nlist = sorted(list(map(int, input().rsplit())))
    
    answer = [nlist[0], nlist[-1]]
    prev = nlist[0] + nlist[-1]
    st, en = 1, N-1
    while st < N and en > -1 and len(nlist) > 2:
        curr = nlist[st] + nlist[en]
        print(nlist[st], nlist[en], curr, prev)
        if abs(prev) > abs(curr) and nlist[st] != nlist[en]:
            prev = curr
            answer = [nlist[st], nlist[en]] 
        if curr <= 0:
            st += 1
        else: 
            en -= 1

    return print(*sorted(answer))
    
if __name__ == "__main__":
    solution()