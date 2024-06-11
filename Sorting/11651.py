'''
좌표 정렬하기 2 
y 좌표가 증가하는 순으로, 같다면 x 좌표가 증가하는 순으로 정렬
첫째 줄: N (1 ≤ N ≤ 100,000)
둘째 줄 ~ N째 줄: (-100,000 ≤ xi, yi ≤ 100,000), 위치가 같은 점 X 
'''
from sys import stdin
input = stdin.readline

def solution():
    xy = [input().rstrip() for _ in range(int(input()))]
    xy.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])), reverse=False)
    print('\n'.join(xy))

if __name__=="__main__":
    solution()