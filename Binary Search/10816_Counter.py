'''
숫자 카드 2 
첫째 줄: 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)
둘째 줄: 숫자 카드에 적혀있는 정수(-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다)
셋째 줄: M(1 ≤ M ≤ 500,000)
넷째 줄: 구해야 할 M개의 정수(-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다)
'''

from sys import stdin, stdout
from collections import Counter
input = stdin.readline
N = int(input())
nArr = sorted(list(map(int, input().split())))
M = int(input())
mArr = list(map(int, input().split()))
cntArr = dict(Counter(nArr))
answers = []
for m in mArr:
    answers.append(str(cntArr.get(m, 0)))
stdout.write(" ".join(answers))
