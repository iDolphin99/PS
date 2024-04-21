'''
1, 2, 3 더하기 
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성
첫째 줄: test case T
둘째 줄: 정수 n은 양수이며 11보다 작음 
'''

from sys import stdin

if __name__ == "__main__":
    input = stdin.readline
    initVal = {1: 1, 2: 2, 3: 4}
    for i in range(int(input())):
        N = int(input())
        if N in initVal:
            print(initVal.get(N))
        else: 
            for i in range(4, N+1):
                initVal[i] = initVal.get(i-1) + initVal.get(i-2) + initVal.get(i-3)
            print(initVal[N])