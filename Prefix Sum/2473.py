'''
세 용액 
첫째 줄: 용액의 수 N (N은 3 이상 5,000 이하의 정수)
둘째 줄: 용액의 특성값을 나타내는 N개의 정수 (-1,000,000,000 이상 1,000,000,000 이하)
'''
from sys import stdin 

def solution():
    input = stdin.readline
    N = int(input())
    nlist = list(map(int, input().rsplit()))
    nlist.sort()
    
    answer = [4e9]
    for i in range(N-2):
        fix = nlist[i]
        st, en = i+1, N-1
        while st < en:
            threeSum = nlist[st] + nlist[en] + fix
            if abs(threeSum) < abs(sum(answer)):
                answer = [nlist[st], nlist[en], fix]
            if threeSum >= 0:
                en -= 1
            else:
                st += 1
            
    return print(*sorted(answer))

if __name__ =="__main__":
    solution()