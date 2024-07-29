'''
소수의 연속합
첫째 줄: 자연수 N (1 ≤ N ≤ 4,000,000)
'''
from sys import stdin 

def solution():
    N = int(stdin.readline())
    
    primeNums = [] 
    sieve = [False, False] + [True]*(N-1)
    for i in range(2, N+1):
        if sieve[i]:
            primeNums.append(i)
            for j in range(2, N//i+1):
                sieve[i*j] = False
    primeNums.append(0)
    
    answer = 0
    st, en = 0, 1
    numSum = primeNums[st]
    while st < en < len(primeNums): 
        if numSum < N:
            numSum += primeNums[en]
            en += 1 
        else:
            if numSum == N: 
                answer += 1 
            numSum -= primeNums[st]
            st += 1 
    
    return answer

if __name__ == "__main__":
    print(solution())