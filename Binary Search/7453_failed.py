'''
합이 0인 네 정수 
첫째 줄: 배열의 크기 n (1 ≤ n ≤ 4000)
둘째 줄 ~ N째 줄: A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어짐, 정수의 절대값 최대 2^28
'''

# Binary Search 응용 
from sys import stdin 
input = stdin.readline 

# 입력 받기 
N = int(input())
arr = [[0]*N for _ in range(4)]
for i in range(N):
    elements = list(map(int, input().rsplit()))
    for j, ele in enumerate(elements):
        arr[j][i] = ele

# 두 집합 만들기 
# 01 23 / 02 13 / 03 12
answers = set()
combination = [((0,1), (2,3)), ((0,2), (1,3)), ((0,3), (1,2))]
for aa, bb in combination: # 3회 
    arrA, arrB = [], []
    for i in range(N):
        for j in range(N):
            arrA.append((arr[aa[0]][i], arr[aa[1]][j]))
            arrB.append((arr[bb[0]][i], arr[bb[1]][j]))
    arrA = sorted(arrA, key=lambda x:(x[0]+x[1]))
    
    for target in arrB:
        st, ed = 0, len(arrA)-1
        while st <= ed:
            mid = (st+ed)//2
            if sum(arrA[mid]) == -sum(target):
                ans = sorted((arrA[mid] + target))
                answers.add(tuple(ans))
                break 
            else:
                if sum(arrA[mid]) > -sum(target):
                    ed = mid-1 
                elif sum(arrA[mid]) < -sum(target):
                    st = mid+1
print(len(answers))


