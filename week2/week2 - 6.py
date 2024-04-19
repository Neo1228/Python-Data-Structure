num = 11
isprime = True
for now in range(2, num//2+1):
    if num%now == 0:
        isprime = False

if isprime: print(num)