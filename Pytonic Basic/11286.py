'''
절댓값 힙
첫째 줄에 연산의 개수 N(1≤N≤100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 만약 x가 0이 아니라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 입력되는 정수는 -231보다 크고, 231보다 작다.
'''
from sys import stdin, stdout 
import heapq
input = stdin.readline
print = stdout.write
heappos, heapneg = [], []
for i in range(int(input())):
    n = int(input())
    if n == 0 : 
        if len(heapneg):   
            if len(heappos) : print(str(heapq.heappop(heapneg) * -1)+"\n")  if heappos[0] >= heapneg[0] else print(str(heapq.heappop(heappos))+"\n")
            else : print(str(heapq.heappop(heapneg) * -1)+"\n")
        elif len(heappos): print(str(heapq.heappop(heappos)) + "\n")
        else :             print("0\n")
    else : 
        heapq.heappush(heappos, n) if n>0 else heapq.heappush(heapneg, -n)