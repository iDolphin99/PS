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
grounds = []
for i in range(N):
    grounds += list(map(int, input().rsplit()))
maxH, minH, answer, glevel = max(grounds), min(grounds), int(1e9), 0

for h in range(maxH, minH-1, -1):
    take, use = 0, 0
    for g in grounds: 
        if g > h: take += g-h # 제거
        else:     use += h-g  # 쌓기
    if use > take + B:
        continue
    
    count = take * 2 + use
    if count < answer:
        answer = count 
        glevel = h

print(answer, glevel)
            

''' Failed Code '''
# for h in range(maxH, minH-1, -1):
#     cnt, b = 0, B
#     for g in grounds: # 65 64 63 62 61 60
#         if g > h: # 제거하기
#             cnt += (g-h)*2
#             b += (g-h)
#         else:     # 쌓기
#             cnt += (h-g) 
#             b -= (h-g)
#     if b >= 0:
#         answers.append((cnt, h))
# print(*min(answers))