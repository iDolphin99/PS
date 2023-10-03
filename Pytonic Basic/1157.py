'''
단어 공부
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
'''
import sys
from collections import Counter
words = sys.stdin.readline().upper()
cnt = Counter(words).most_common(2)
print(cnt[0][0] if cnt[1][0]=='\n' or cnt[0][1]!=cnt[1][1] else '?')
