'''
최소 힙
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
1. 배열에 자연수 x를 넣는다.
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''
import heapq
from sys import stdin, stdout
heap = []
for _ in range(int(stdin.readline())):
    value = int(stdin.readline())
    if value==0:
        stdout.write(str(heapq.heappop(heap)) + '\n') if len(heap) != 0 else stdout.write(str(0) + '\n')
    else: heapq.heappush(heap, value)
    