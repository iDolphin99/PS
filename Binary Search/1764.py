'''
듣보잡
첫째 줄: 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M (N, M <= 500,000)
둘째 줄 ~ N째 줄: 듣도 못한 사람의 이름 
N+2째 줄부터: 보도 못한 사람의 이름이 순서대로
이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하
'''
from sys import stdin, stdout 
input = stdin.readline
print = stdout.write
N, M = map(int, input().split())
nArr = sorted([input().rstrip() for _ in range(N)])
mArr = sorted([input().rstrip() for _ in range(M)])
answers = []
for m in mArr:
    start, end = 0, len(nArr)-1
    while start <= end:
        mid = (start+end)//2
        if nArr[mid] == m:
            answers.append(m)
            break
        else:
            if nArr[mid] < m:
                start = mid + 1 
            else: 
                end = mid - 1
print(str(len(answers))+'\n')
print("\n".join(answers))