'''
좌표 압축
첫째 줄: 1 ≤ N ≤ 1,000,000
둘째 줄: 공백 한 칸으로 구분된 X1, X2, ..., XN, -109 ≤ Xi ≤ 109
'''

from sys import stdin, stdout 
input = stdin.readline 
N = int(input())
arr = list(map(int, input().split()))
arr_sort = sorted(set(arr))
answers = []
for element in arr:
    start, end = 0, len(arr_sort)-1
    while start <= end:
        mid = (start+end)//2
        if arr_sort[mid] == element:
            answers.append(str(mid))
            break
        else:
            if arr_sort[mid] < element:
                start = mid+1
            else:
                end = mid-1
stdout.write(" ".join(answers))