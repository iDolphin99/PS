'''
단어 수학
첫째 줄: 단어의 개수 N(1 ≤ N ≤ 10)
둘째 줄~N째 줄: 단어가 한 줄에 하나씩, 모든 단어에 포함된 알파벳은 최대 10개, 최대 길이 8
'''
from sys import stdin 
from collections import defaultdict
input = stdin.readline
words = defaultdict(int)
for _ in range(int(input())):
    wlist = reversed(input().rstrip())
    for i, w in enumerate(wlist):
        words[w] += 10**i
words = sorted(words.items(), key=lambda x: x[1], reverse=True)

answer, cnt = 0, 9
for k, v in words:
    answer += cnt*v
    cnt -= 1
print(answer)


