'''
랜선 자르기 
첫째 줄: 이미 가지고 있는 랜선의 개수 K (1<=K<=10,000)
둘째 줄: 필요한 랜선의 개수 N (1<=N<=1,000,000), 항상 K<=N
셋째 줄 ~ K줄: 이미 가지고 있는 랜선의 길이 (2^31-1보다 작거나 같은 자연수)
'''

from sys import stdin 

if __name__=='__main__':
    input = stdin.readline
    K, N = map(int, input().rsplit())
    kList = sorted([int(input()) for _ in range(K)])
    
    st, en = 1, 2**31-1 
    while st < en:
        mid = (st+en+1)//2
        count = sum([k//mid for k in kList])
        flag = True if count==N else False 
        if flag:
            st = mid
        else:
            if count < N:
                en = mid-1
            else:
                st = mid
    print(st)