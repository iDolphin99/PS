'''
생태학
입력에는 최대 10,000개 종, 최대 1,000,000 그루
주어진 각 종의 이름을 사전순으로 출력하고, 
그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력
'''
from sys import stdin
from collections import defaultdict
input = stdin.readline
treeDict = defaultdict(int)
treeSum = 0
while True:
    tree = input().rstrip()
    if len(tree):
        treeDict[tree] += 1
        treeSum += 1
    else:
        treeDict = sorted(treeDict.items())
        break 
for tree, cnt in treeDict:
    print(tree, "%.4f" %(cnt/treeSum*100))
