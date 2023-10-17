'''
덱
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
'''
from collections import deque 
from sys import stdin
deq = deque()
for i in range(int(stdin.readline())):
    op, *n = stdin.readline().split()
    if op == "push_front" : deque.appendleft(deq, *n)
    elif op == "push_back": deque.append(deq, *n)
    elif op == "pop_front": print(deque.popleft(deq)) if len(deq) else print("-1")
    elif op == "pop_back" : print(deque.pop(deq)) if len(deq) else print("-1")
    elif op == "size"     : print(len(deq))
    elif op == "empty"    : print("0") if len(deq) else print("1")
    elif op == "front"    : print(deq[0]) if len(deq) else print("-1")
    elif op == "back"     : print(deq[-1]) if len(deq) else print("-1")