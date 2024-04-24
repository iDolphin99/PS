'''
RGB거리 
1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
첫째 줄: N(2 ≤ N ≤ 1,000)
둘째 줄~N째 줄: 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄씩 제공
'''

from sys import stdin
if __name__ == "__main__":
    input = stdin.readline 
    N = int(input())
    rgb = [list(map(int, input().rsplit())) for _ in range(N)]
    r = {0: rgb[0][0]}
    g = {0: rgb[0][1]}
    b = {0: rgb[0][2]}
    for i in range(1, N):
        r[i] = min(g.get(i-1), b.get(i-1)) + rgb[i][0]
        g[i] = min(r.get(i-1), b.get(i-1)) + rgb[i][1]
        b[i] = min(r.get(i-1), g.get(i-1)) + rgb[i][2]
    print(min(r.get(N-1), g.get(N-1), b.get(N-1)))