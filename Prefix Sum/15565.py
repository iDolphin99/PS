'''
귀여운 라이언
첫째 줄: N과 K가 주어진다. (1 ≤ K ≤ N ≤ 106)
둘째 줄: N개의 인형 정보 (1 or 2)
'''
from sys import stdin

def solution():
    input = stdin.readline
    N, K = map(int, input().rsplit())
    toylist = list(map(int, input().rsplit()))
    print(toylist)
    
    
    
    return -1

if __name__ == "__main__":
    print(solution())