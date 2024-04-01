'''
숫자 카드 2 
첫째 줄: 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)
둘째 줄: 숫자 카드에 적혀있는 정수(-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다)
셋째 줄: M(1 ≤ M ≤ 500,000)
넷째 줄: 구해야 할 M개의 정수(-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다)
'''

from sys import stdin, stdout
input = stdin.readline
N = int(input())
nArr = sorted(list(map(int, input().split())))
M = int(input())
mArr = list(map(int, input().split()))
answers = []

def upper_idx(target):
    start, end = 0, N
    while start < end:
        mid = (start+end)//2
        if nArr[mid] > target:
            end = mid 
        else:
            start = mid+1
    if start == N-1: start += 1
    return start
def lower_idx(target):
    start, end = 0, N
    while start < end:
        mid = (start+end)//2
        if nArr[mid] >= target:
            end = mid 
        else:
            start = mid+1 
    return start

for m in mArr:
    answers.append(str(upper_idx(m) - lower_idx(m)))
stdout.write(" ".join(answers))
        