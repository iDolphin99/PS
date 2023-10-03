'''
국영수
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
국어 감소 -> 영어 증가 -> 수학 감소 -> 이름 사전순 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
'''
import sys
input = sys.stdin.readline
scores=[]
for _ in range(int(input())):
    scores.append(list(input().split()))
scores.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), str(x[0]))) 
print('\n'.join([s[0] for s in scores]))