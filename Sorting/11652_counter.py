'''
카드 
첫째 줄: N (1 ≤ N ≤ 100,000)
둘째 줄~N째 줄: 숫자 카드에 적혀 있는 정수, -262보다 크거나 같고, 262보다 작거나 같음
'''
from sys import stdin
from collections import Counter
input = stdin.readline
cards = [int(input()) for _ in range(int(input()))]
cnt = sorted(Counter(cards).most_common(), key=lambda x:x[0])
cnt = sorted(cnt, key=lambda x:x[1], reverse=True)
print(cnt[0][0])