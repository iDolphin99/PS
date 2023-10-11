'''
최대 힙
첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 자연수는 231보다 작다.
'''
from sys import stdin, stdout
import heapq
heap = []
input = stdin.readline
print = stdout.write
for i in range(int(input())):
    n = int(input()) * -1
    if n==0 :
        print("0 \n") if len(heap) == 0 else print(str(heapq.heappop(heap) * -1) + '\n')
    else: heapq.heappush(heap, n) 