'''
수리공 항승
첫째 줄: 물이 새는 곳의 개수 N과 테이프의 길이 L
N과 L은 1,000보다 작거나 같은 자연수 
둘째 줄: 물이 새는 곳의 위치
물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수
'''
from sys import stdin
input = stdin.readline

def solution():
    N, L = map(int, input().rsplit())
    alist = sorted(list(map(int, input().rsplit())))    
    answer, distance = 1, 0
    for i in range(1, N):
        distance -= (alist[i-1]-alist[i])
        if distance >= L:
            answer += 1 
            distance = 0    
    print(answer)

if __name__ == "__main__":
    solution()