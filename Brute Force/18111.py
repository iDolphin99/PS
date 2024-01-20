'''
마인크래프트 
M x N의 집터에서 제거(2초), 쌓기(1초)작업을 통해 빠른 시간 안에 땅 평탄화를 이루어야 함 
1 ≤ M, N ≤ 500
0 ≤ B ≤ 6.4 × 107
(i, j)땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
'''
from sys import stdin 
input = stdin.readline
N, M, B = map(int, input().rsplit())
arr = []
for i in range(N):
    arr += list(map(int, input().rsplit()))
arr = sorted(arr)
maxH, minH, answers = max(arr), min(arr), []
    
for h in range(maxH, minH-1, -1):
    cnt, b = 0, B
    for e in arr: # 65 64 63 62 61 60
        if e > h: # 제거하기
            cnt += (e-h)*2
            b += (e-h)
        cnt += (h-e) # 쌓기 
        b -= (h-e)
        
        
    if b >= 0:
        answers.append((cnt, h))

print(*min(answers))