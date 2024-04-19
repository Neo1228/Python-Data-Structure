import sys
sys.stdin = open('input.txt', 'r')

NUM1, NUM2, NUM3 = map(int, input().split())
min1 = NUM1 if NUM1 < NUM2 else NUM2
min2 = min1 if min1 < NUM3 else NUM3
print(min2)