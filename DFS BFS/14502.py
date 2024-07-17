'''
연구소
첫째 줄: 세로 크기 N과 가로 크기 M (3 ≤ N, M ≤ 8)
둘째 줄~N개 줄: 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치
빈 칸의 개수는 3개 이상 
'''
import copy
from sys import stdin
from collections import deque 
input = stdin.readline

def printGraph(g):
    for i in range(len(g)):
        print(g[i])
    print()

def BFS(graph):
    nullCnt = len(emptyPos)
    graph_tmp = copy.deepcopy(graph)
     
    deq = deque(virusPos)
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    while deq:
        curX, curY = deq.pop()
        for dx, dy in directions:
            nxtX, nxtY = curX+dx, curY+dy
            if 0<=nxtX<N and 0<=nxtY<M:
                if graph_tmp[nxtX][nxtY]==0:
                    graph_tmp[nxtX][nxtY] = 2
                    deq.append((nxtX, nxtY))
                    nullCnt -= 1
    #print("answer of BFS: ", nullCnt)
    #printGraph(graph_tmp)

    return nullCnt
    
    
def BackTracking(three, answer): 
    if three==3:
        answer = max(answer, BFS(graph))
        return answer
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 3 # new wall
                answer = BackTracking(three+1, answer) # return
                graph[i][j] = 0 # destroy the new wall 

    return answer 
    
    
if __name__ == "__main__":
    N, M = map(int, input().rsplit())
    graph = [list(map(int, input().rsplit())) for _ in range(N)]   
    printGraph(graph)
    
    virusPos, emptyPos = [], []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2: virusPos.append((i, j))
            if graph[i][j] == 0: emptyPos.append((i, j))
    
    print("Answer: ", BackTracking(0, 0)-3)