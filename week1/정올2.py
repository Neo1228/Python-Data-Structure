import sys
sys.stdin = open('input2.txt', 'r')

howmany= int(input())

sum = 0
start = 1
while start <= howmany:
    sum += start
    start += 1

print(sum)