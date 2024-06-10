'''
나이순 정렬 
회원들은 나이가 증가하는 순, 나이가 같으면 먼저 가입한 순으로 
첫째 줄: 1 ≤ N ≤ 100,000
둘째 줄~ : 각 회원의 나이와 이름을 공백으로 구분해서 (1 <= 나이 <= 200)
'''
from sys import stdin
input = stdin.readline

def solution(): 
    customers = []
    for _ in range(int(input())):
        age, name = input().rsplit()
        customers.append((int(age), name))
    customers.sort(key=lambda x: x[0])
    for cus in customers: print(*cus)

if __name__ == "__main__":
    solution()    
