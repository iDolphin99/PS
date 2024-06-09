'''
중앙값 구하기 
첫째 줄: 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)
각 테스트 케이스 첫째 줄: 수열의 크기 M(1 ≤ M ≤ 9999, M은 홀수)
그 다음줄부터 수열의 원소가 차례대로 주어짐 (원소는 한 줄에 10개씩 나누어져있고, 32비트 부호있는 정수)
'''
from sys import stdin
import heapq
input = stdin.readline

def solution():
    for _ in range(int(input())): # 1,000
        M = int(input())
        _list = []
        cnt = M//10 if M%10==0 else M//10+1
        for _ in range(cnt): # 1,000
            _list += list(map(int, input().rsplit()))
        
        answer = []
        for i in range(len(_list)):
            if i%2==0: # enter
                heap = _list[:i+1]
                heapq.heapify(heap)
                for j in range(len(answer)):
                    heapq.heappop(heap)
                answer.append(heap[0])

        print(len(answer))
        if len(answer) < 11:
            print(*answer)
        else:
            for j in range(0, len(answer), 10):
                print(*answer[j:j+10])

if __name__ == "__main__":
    solution()
    
    
    
'''
        # answer, heap = [], []
        # for __ in range(M//10+1):
        #     _list = list(map(int, input().rsplit()))
        #     for i, e in enumerate(_list):
        #         heap.append(e)
        #         if i%2==0:
        #             heap = sorted(heap)
        #             print(heap)
        #             if len(heap) > 3:
        #                 heap = heap[1:-1]
        #             answer.append(heap[len(heap)//2])
        #     print("heap: ", heap)
'''