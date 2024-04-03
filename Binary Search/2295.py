'''
세 수의 합 
첫째 줄: N(5 ≤ N ≤ 1,000)
둘째 줄 ~ N+1줄: U의 원소가 하나씩, 집합이므로 같은 수 없음, 200,000,000보다 작거나 같은 자연수
'''

from sys import stdin
input = stdin.readline
arr = sorted([int(input()) for _ in range(int(input()))]) 
arr2 = []
for i in range(len(arr)):
    for j in range(i, len(arr)):
        arr2.append(arr[i]+arr[j])
arr2.sort()
answer = 0

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i+1):
        start, end = 0, len(arr2)-1 
        while start <= end:
            mid = (start+end)//2
            if arr2[mid] == arr[i]-arr[j]:
                answer = max(answer, arr[i])
                break
            else:
                if arr2[mid] < arr[i]-arr[j]:
                    start = mid + 1 
                elif arr2[mid] > arr[i]-arr[j]:
                    end = mid -1
print(answer)
