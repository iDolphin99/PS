'''
스타트와 링크
4 <= N <= 20 (N은 짝수)
Sii = 0 
1 < = Sij <= 100 
'''
from sys import stdin
input = stdin.readline
N = int(input())
S = [[0] * N] * N
for i in range(N): S[i] = list(map(int, input().rsplit()))
visited = [False for _ in range(N)] # 방문 리스트 
answer = int(1e9)                   # 최소값을 저장할 변수

def backTracking(depth, index):
    global answer # 전역 변수를 사용할 것이라는 것을 명시해야 함
    
    if depth == N//2: # 팀원을 다 채운 후에 불러진 backTracking 함수에서 능력치 비교 후 return 
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:         # (T, T)일 때 
                    start += S[i][j]
                if not visited[i] and not visited[j]: # 그냥 else 처리 해버리면 (T, F)/(F, T)/(F, F)인 모든 상황이 잡혀버림 
                    link += S[i][j]
        answer = min(answer, abs(start - link))       # 값의 차이를 비교해야 하니까 abs는 필수
        return 
    
    for i in range(index, N):   # backtracking 순회 부분
        if not visited[i]:      # 순회하지 않은 선수는 True를 주어 방문 
            visited[i] = True
            backTracking(depth+1, i+1)
            visited[i] = False  # 순회 끝, 해당 선수는 다시 False

backTracking(0, 0)
print(answer)