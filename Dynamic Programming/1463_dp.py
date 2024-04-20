'''
1로 만들기 
첫째 줄: 정수 N (1보다 크거나 같고, 10^6보다 작거나 같음)
1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.
'''

from sys import stdin 

if __name__ == "__main__":
    N = int(stdin.readline())
    memo = [0] * (N+1)
    for i in range(2, N+1):
        memo[i] = memo[i-1] + 1 
        if i % 3 == 0:
            memo[i] = min(memo[i], memo[i//3] + 1)
        if i % 2 == 0:
            memo[i] = min(memo[i], memo[i//2] + 1)
    print(memo[N])