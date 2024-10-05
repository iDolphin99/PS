'''
LCS
문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자
ACAYKP
CAPCAK
'''

from sys import stdin 

def solution():
    input = stdin.readline
    
    str1 = list(input().rstrip())
    str2 = list(input().rstrip())
    
    dp = [[0 for _ in range(len(str1)+1)] for __ in range(len(str2)+1)]
    
    for i in range(len(str1)):
        s1 = str1[i]
        for j in range(len(str2)):
            s2 = str2[j]
            if s1 == s2:
                dp[j+1][i+1] = dp[j][i]+1
            else:
                dp[j+1][i+1] = max(dp[j][i+1], dp[j+1][i])
    
    return dp[len(str2)][len(str1)]

if __name__ == "__main__":
    print(solution())