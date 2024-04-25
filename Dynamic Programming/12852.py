'''
1로 만들기 2
- X가 3으로 나누어 떨어지면, 3으로 나눈다.
- X가 2로 나누어 떨어지면, 2로 나눈다.
- 1을 뺀다.
첫째 줄: 연산을 하는 횟수의 최솟값
둘째 줄: N을 1로 만드는 방법에 포함되어 있는 수를 공백 단위로 출력, 아무거나 ok 
'''

from sys import stdin 
if __name__ == "__main__":
    input = stdin.readline 
    N = int(input())
    dp = [0] * (N+1)    # 1-indexed 
    graph = [0] * (N+1)
    for i in range(2, N+1):
        nxtNode = [i-1]
        if i%3==0: nxtNode.append(i//3)
        if i%2==0: nxtNode.append(i//2)
                         
        dp[i] = dp[i-1]+1
        graph[i] = i-1
            
        for nxt in nxtNode:
            if dp[i] >= dp[nxt]+1:
                dp[i] = dp[nxt]+1
                graph[i] = nxt
    
    print(dp[N])
    print(N, end=' ')
    while N!=1:
        print(graph[N], end=' ')
        N = graph[N]
            
    
''' failed code >> 경로 최솟값보다 경로 노드가 더 많이 나옴
    input = stdin.readline 
    N = int(input())
    dp = [0] * (N+1) # 1-indexed 
    graph = [1]
    for i in range(2, N+1): # 
        dp[i] = dp[i-1]+1
        if i%3 == 0: 
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2 == 0: 
            dp[i] = min(dp[i], dp[i//2]+1)
        if dp[i] >= len(graph):
            graph.append(i)
        else:
            graph[dp[i]] = i
    print(dp[N])
    print(*(sorted(graph, reverse=True)))
    print(dp)
    print(len(graph))
'''
    