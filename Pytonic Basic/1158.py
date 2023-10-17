'''
요세푸스 
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
'''
from collections import deque
from sys import stdin
n, k = map(int, stdin.readline().split())
deq = deque([n for n in range(1, n+1)])
res = []
for i in range (n):
    deq.rotate(-(k-1))
    res.append(deq.popleft())
print("<" , ", ".join(map(str, res)), ">")