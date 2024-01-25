'''
모든 순열 
1 <= N <= 8
'''
from itertools import permutations
from sys import stdin, stdout
N = int(stdin.readline())
answers = list(permutations([i for i in range(1, N+1)], N)) 
for answer in answers:
    stdout.write(str(answer)[1:-1].replace(",", "") + "\n")
