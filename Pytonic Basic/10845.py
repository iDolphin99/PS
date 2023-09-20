'''
큐
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from sys import stdin,stdout
from collections import deque 
deq = deque()
for _ in range(int(stdin.readline())):
    op, *num = map(str, stdin.readline().split())
    if   op=="push" : deq.append(int(*num))
    elif op=="pop"  : stdout.write("-1\n" if len(deq)==0 else '%d\n' % deq.popleft())
    elif op=="size" : stdout.write("%d\n" % len(deq))
    elif op=="empty": stdout.write("1\n" if len(deq)==0 else '0\n')
    elif op=="front": stdout.write("-1\n" if len(deq)==0 else '%d\n' % deq[0])
    elif op=="back" : stdout.write("-1\n" if len(deq)==0 else '%d\n' % deq[-1])