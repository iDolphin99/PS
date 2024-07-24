'''
회전 초밥
첫째 줄
- 회전 초밥 벨트에 놓인 접시의 수 N
- 초밥의 가짓수 d
- 연속해서 먹는 접시의 수 k
- 쿠폰 번호 c가 각각 하나의 빈 칸을 사이에 두고 주어짐
- 단, 2 ≤ N ≤ 30,000, 2 ≤ d ≤ 3,000, 2 ≤ k ≤ 3,000 (k ≤ N), 1 ≤ c ≤ d
둘째 줄~N개의 줄 
- 초밥의 종류를 나타내는 1 이상 d 이하의 정수가 각 줄마다 하나씩 
'''

from sys import stdin

def solution():
    input = stdin.readline
    N, D, K, C = map(int, input().rsplit())
    sushi = [int(input().rstrip()) for _ in range (N)]
    sushi += sushi[:K-1]

    answer = 1
    for i in range(N): 
        plate = sushi[i:i+K]
        plate += [C]
        cnt = len(set(plate))
        answer = max(answer, cnt)
        if answer == K+1: 
            return K+1
    return answer

if __name__ == "__main__":
    print(solution())