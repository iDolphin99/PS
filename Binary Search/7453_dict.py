'''
합이 0인 네 정수 
첫째 줄: 배열의 크기 n (1 ≤ n ≤ 4000)
둘째 줄 ~ N째 줄: A, B, C, D에 포함되는 정수가 공백으로 구분되어져서 주어짐, 정수의 절대값 최대 2^28
'''

from sys import stdin 
input = stdin.readline 

if __name__ == '__main__':
    N = int(input())
    arr = [[0]*N for _ in range(4)]
    for i in range(N):
        elements = list(map(int, input().rsplit()))
        for j, ele in enumerate(elements):
            arr[j][i] = ele
    
    # make A+B dictionary 
    ab_dict = {}
    for i in range(N):
        for j in range(N):
            ab = (arr[0][i] + arr[1][j])
            if not ab in ab_dict:
                ab_dict[ab] = 1 
            else:
                ab_dict[ab] += 1 

    answer = 0
    for i in range(N):
        for j in range(N):
            cd = -(arr[2][i]+arr[3][j])
            answer += ab_dict.get(cd, 0)
    print(answer)